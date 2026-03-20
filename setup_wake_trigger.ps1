# ============================================================
#  Grammar Quiz - Wake-from-sleep Task Scheduler Setup
#  Run this script as Administrator (right-click > Run as Admin)
# ============================================================

$TaskName = "GrammarQuizOnWake"
$ExePath  = "$PSScriptRoot\dist\grammar_quiz.exe"

# Verify the exe exists
if (-not (Test-Path $ExePath)) {
    Write-Host "ERROR: Could not find $ExePath" -ForegroundColor Red
    Write-Host "Please run build_windows.bat first, then try again."
    Read-Host "Press Enter to exit"
    exit 1
}

# Remove any previous version of the task
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Removed old task." -ForegroundColor Yellow
}

# Action: launch the quiz exe
$Action = New-ScheduledTaskAction -Execute $ExePath

# Trigger 1: On workstation unlock (covers password-protected sleep wake-up)
$TriggerUnlock = New-ScheduledTaskTrigger -AtLogOn

# Trigger 2: Event-based wake from sleep
#   Event log: Microsoft-Windows-Power-Troubleshooter/Operational, Event ID 1
$CIMTriggerClass = Get-CimClass -ClassName "MSFT_TaskEventTrigger" `
                                -Namespace "Root/Microsoft/Windows/TaskScheduler"
$TriggerWake = New-CimInstance -CimClass $CIMTriggerClass -ClientOnly
$TriggerWake.Enabled = $true
$TriggerWake.Subscription = @"
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Power-Troubleshooter/Operational">
    <Select Path="Microsoft-Windows-Power-Troubleshooter/Operational">
      *[System[EventID=1]]
    </Select>
  </Query>
</QueryList>
"@

# Settings: allow running on battery, run only if logged on
$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 5)

# Principal: run as current user, only when logged on
$Principal = New-ScheduledTaskPrincipal `
    -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) `
    -LogonType Interactive `
    -RunLevel Limited

# Register the task with both triggers
$Task = New-ScheduledTask `
    -Action    $Action `
    -Trigger   @($TriggerUnlock, $TriggerWake) `
    -Settings  $Settings `
    -Principal $Principal

Register-ScheduledTask -TaskName $TaskName -InputObject $Task -Force | Out-Null

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  SUCCESS! Task '$TaskName' registered." -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "The Grammar Quiz will pop up every time you"
Write-Host "wake your laptop from sleep or unlock it."
Write-Host ""
Write-Host "To remove: open Task Scheduler and delete '$TaskName'"
Write-Host "       or: Unregister-ScheduledTask -TaskName '$TaskName'"
Write-Host ""
Read-Host "Press Enter to exit"
