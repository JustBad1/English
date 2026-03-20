import tkinter as tk
from tkinter import font as tkfont
import random
import sys

# ─────────────────────────────────────────────────────────────
#  QUESTION BANK  (word in CAPS is what gets identified)
# ─────────────────────────────────────────────────────────────
QUESTIONS = [
    # NOUNS
    {"q": "What part of speech is the bold word?\n\n\"The DOG barked all night.\"",           "a": "Noun",         "opts": ["Noun", "Verb", "Adjective", "Pronoun"]},
    {"q": "What part of speech is the bold word?\n\n\"She put the book on the TABLE.\"",      "a": "Noun",         "opts": ["Noun", "Preposition", "Adverb", "Conjunction"]},
    {"q": "What part of speech is the bold word?\n\n\"HAPPINESS is the best medicine.\"",     "a": "Noun",         "opts": ["Noun", "Adjective", "Verb", "Adverb"]},
    {"q": "What part of speech is the bold word?\n\n\"The CITY was quiet at dawn.\"",         "a": "Noun",         "opts": ["Noun", "Adjective", "Article", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"His COURAGE inspired everyone.\"",      "a": "Noun",         "opts": ["Noun", "Adverb", "Verb", "Adjective"]},

    # ADJECTIVES
    {"q": "What part of speech is the bold word?\n\n\"She wore a BEAUTIFUL dress.\"",         "a": "Adjective",    "opts": ["Adjective", "Adverb", "Noun", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"The COLD wind made him shiver.\"",      "a": "Adjective",    "opts": ["Adjective", "Noun", "Adverb", "Preposition"]},
    {"q": "What part of speech is the bold word?\n\n\"He gave a BRIEF explanation.\"",        "a": "Adjective",    "opts": ["Adjective", "Verb", "Adverb", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"It was a PERFECT day for a walk.\"",   "a": "Adjective",    "opts": ["Adjective", "Adverb", "Conjunction", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"The ANGRY customer complained.\"",      "a": "Adjective",    "opts": ["Adjective", "Noun", "Verb", "Adverb"]},

    # VERBS
    {"q": "What part of speech is the bold word?\n\n\"She RUNS every morning.\"",             "a": "Verb",         "opts": ["Verb", "Noun", "Adverb", "Adjective"]},
    {"q": "What part of speech is the bold word?\n\n\"He TAUGHT English for ten years.\"",   "a": "Verb",         "opts": ["Verb", "Noun", "Adjective", "Preposition"]},
    {"q": "What part of speech is the bold word?\n\n\"They BUILT a new bridge.\"",            "a": "Verb",         "opts": ["Verb", "Adjective", "Adverb", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"She SMILED at the camera.\"",          "a": "Verb",         "opts": ["Verb", "Noun", "Adjective", "Preposition"]},
    {"q": "What part of speech is the bold word?\n\n\"The sun SETS in the west.\"",          "a": "Verb",         "opts": ["Verb", "Noun", "Adverb", "Adjective"]},

    # ADVERBS
    {"q": "What part of speech is the bold word?\n\n\"He spoke SOFTLY to the child.\"",      "a": "Adverb",       "opts": ["Adverb", "Adjective", "Noun", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"She arrived EARLY for the meeting.\"", "a": "Adverb",       "opts": ["Adverb", "Adjective", "Preposition", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"The car moved VERY slowly.\"",         "a": "Adverb",       "opts": ["Adverb", "Adjective", "Verb", "Conjunction"]},
    {"q": "What part of speech is the bold word?\n\n\"He ALMOST missed his flight.\"",       "a": "Adverb",       "opts": ["Adverb", "Adjective", "Verb", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"They ALWAYS eat dinner together.\"",   "a": "Adverb",       "opts": ["Adverb", "Verb", "Adjective", "Noun"]},

    # PHRASAL VERBS
    {"q": "What part of speech is the bold phrase?\n\n\"Please TURN OFF the lights.\"",      "a": "Phrasal Verb", "opts": ["Phrasal Verb", "Verb", "Preposition", "Adverb"]},
    {"q": "What part of speech is the bold phrase?\n\n\"She needs to GIVE UP smoking.\"",    "a": "Phrasal Verb", "opts": ["Phrasal Verb", "Verb", "Adjective", "Conjunction"]},
    {"q": "What part of speech is the bold phrase?\n\n\"He decided to LOOK INTO the case.\"","a": "Phrasal Verb", "opts": ["Phrasal Verb", "Verb", "Noun", "Preposition"]},
    {"q": "What part of speech is the bold phrase?\n\n\"She BROKE DOWN in tears.\"",         "a": "Phrasal Verb", "opts": ["Phrasal Verb", "Adverb", "Verb", "Preposition"]},
    {"q": "What part of speech is the bold phrase?\n\n\"Can you PICK UP the children?\"",    "a": "Phrasal Verb", "opts": ["Phrasal Verb", "Verb", "Preposition", "Noun"]},

    # ARTICLES
    {"q": "What part of speech is the bold word?\n\n\"She ate AN apple for breakfast.\"",    "a": "Article",      "opts": ["Article", "Adjective", "Pronoun", "Conjunction"]},
    {"q": "What part of speech is the bold word?\n\n\"THE cat sat on the mat.\"",            "a": "Article",      "opts": ["Article", "Adjective", "Pronoun", "Preposition"]},
    {"q": "What part of speech is the bold word?\n\n\"He bought A new car yesterday.\"",     "a": "Article",      "opts": ["Article", "Adjective", "Adverb", "Preposition"]},
    {"q": "What part of speech is the bold word?\n\n\"She is THE best student in class.\"",  "a": "Article",      "opts": ["Article", "Adjective", "Adverb", "Pronoun"]},
    {"q": "What part of speech is the bold word?\n\n\"I need AN umbrella today.\"",          "a": "Article",      "opts": ["Article", "Adjective", "Pronoun", "Noun"]},

    # CONJUNCTIONS
    {"q": "What part of speech is the bold word?\n\n\"I like tea BUT not coffee.\"",         "a": "Conjunction",  "opts": ["Conjunction", "Preposition", "Adverb", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"She studied hard SO she passed.\"",    "a": "Conjunction",  "opts": ["Conjunction", "Adverb", "Preposition", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"He was tired AND hungry.\"",           "a": "Conjunction",  "opts": ["Conjunction", "Preposition", "Adverb", "Noun"]},
    {"q": "What part of speech is the bold word?\n\n\"She left BECAUSE she was bored.\"",   "a": "Conjunction",  "opts": ["Conjunction", "Preposition", "Adverb", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"You can have cake OR pie.\"",          "a": "Conjunction",  "opts": ["Conjunction", "Preposition", "Adverb", "Pronoun"]},

    # PREPOSITIONS
    {"q": "What part of speech is the bold word?\n\n\"The keys are ON the table.\"",         "a": "Preposition",  "opts": ["Preposition", "Adverb", "Conjunction", "Adjective"]},
    {"q": "What part of speech is the bold word?\n\n\"She walked THROUGH the park.\"",       "a": "Preposition",  "opts": ["Preposition", "Adverb", "Conjunction", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"He hid BEHIND the door.\"",            "a": "Preposition",  "opts": ["Preposition", "Adverb", "Adjective", "Conjunction"]},
    {"q": "What part of speech is the bold word?\n\n\"The cat jumped OVER the fence.\"",     "a": "Preposition",  "opts": ["Preposition", "Adverb", "Verb", "Conjunction"]},
    {"q": "What part of speech is the bold word?\n\n\"We met AT the coffee shop.\"",         "a": "Preposition",  "opts": ["Preposition", "Adverb", "Conjunction", "Article"]},

    # PRONOUNS
    {"q": "What part of speech is the bold word?\n\n\"SHE finished the report early.\"",     "a": "Pronoun",      "opts": ["Pronoun", "Noun", "Adjective", "Adverb"]},
    {"q": "What part of speech is the bold word?\n\n\"Can you help ME with this?\"",         "a": "Pronoun",      "opts": ["Pronoun", "Noun", "Adjective", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"THEY decided to leave early.\"",       "a": "Pronoun",      "opts": ["Pronoun", "Noun", "Adjective", "Verb"]},
    {"q": "What part of speech is the bold word?\n\n\"This bag is MINE.\"",                  "a": "Pronoun",      "opts": ["Pronoun", "Noun", "Adjective", "Adverb"]},
    {"q": "What part of speech is the bold word?\n\n\"WHO told you that?\"",                 "a": "Pronoun",      "opts": ["Pronoun", "Noun", "Conjunction", "Adverb"]},
]

# ─────────────────────────────────────────────────────────────
#  COLOUR PALETTE
# ─────────────────────────────────────────────────────────────
BG        = "#1e1e2e"
CARD      = "#2a2a3e"
ACCENT    = "#7c3aed"
CORRECT   = "#22c55e"
WRONG     = "#ef4444"
SKIP_COL  = "#6b7280"
TEXT      = "#f1f5f9"
SUBTEXT   = "#94a3b8"
BTN_TXT   = "#ffffff"

PART_COLORS = {
    "Noun":         "#3b82f6",
    "Adjective":    "#f59e0b",
    "Verb":         "#10b981",
    "Adverb":       "#8b5cf6",
    "Phrasal Verb": "#ec4899",
    "Article":      "#06b6d4",
    "Conjunction":  "#f97316",
    "Preposition":  "#84cc16",
    "Pronoun":      "#a855f7",
}


class GrammarQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grammar Wake-Up Quiz")
        self.configure(bg=BG)
        self.resizable(False, False)

        # Center window
        w, h = 600, 460
        self.geometry(f"{w}x{h}+{(self.winfo_screenwidth()-w)//2}+{(self.winfo_screenheight()-h)//2}")
        self.attributes("-topmost", True)

        self._question = random.choice(QUESTIONS)
        self._opts = self._question["opts"][:]
        random.shuffle(self._opts)
        self._answered = False

        self._build_ui()

    # ── UI construction ──────────────────────────────────────
    def _build_ui(self):
        title_f = tkfont.Font(family="Segoe UI", size=11, weight="bold")
        q_f     = tkfont.Font(family="Segoe UI", size=13)
        opt_f   = tkfont.Font(family="Segoe UI", size=11)
        tag_f   = tkfont.Font(family="Segoe UI", size=9, weight="bold")

        # Header bar
        hdr = tk.Frame(self, bg=ACCENT, height=8)
        hdr.pack(fill="x")

        # Tag label (part-of-speech category hint hidden until answer)
        self._tag_lbl = tk.Label(self, text="Parts of Speech Quiz",
                                 font=title_f, bg=BG, fg=SUBTEXT)
        self._tag_lbl.pack(pady=(18, 4))

        # Question card
        card = tk.Frame(self, bg=CARD, bd=0, relief="flat",
                        padx=20, pady=16)
        card.pack(fill="x", padx=30)

        self._q_lbl = tk.Label(card, text=self._question["q"],
                               font=q_f, bg=CARD, fg=TEXT,
                               wraplength=520, justify="center")
        self._q_lbl.pack()

        # Options grid
        opt_frame = tk.Frame(self, bg=BG)
        opt_frame.pack(pady=18, padx=30, fill="x")

        self._btns = []
        labels = ["A", "B", "C", "D"]
        for i, opt in enumerate(self._opts):
            row, col = divmod(i, 2)
            btn = tk.Button(
                opt_frame,
                text=f"  {labels[i]}.  {opt}",
                font=opt_f,
                bg=CARD, fg=TEXT,
                activebackground=ACCENT, activeforeground=BTN_TXT,
                relief="flat", bd=0,
                padx=12, pady=10,
                cursor="hand2",
                anchor="w",
                command=lambda o=opt: self._check(o),
            )
            btn.grid(row=row, column=col, padx=6, pady=5, sticky="ew")
            self._btns.append(btn)
        opt_frame.columnconfigure(0, weight=1)
        opt_frame.columnconfigure(1, weight=1)

        # Feedback label (hidden until answered)
        self._fb_lbl = tk.Label(self, text="", font=opt_f,
                                bg=BG, fg=CORRECT)
        self._fb_lbl.pack(pady=(0, 4))

        # Bottom bar: skip + close
        bar = tk.Frame(self, bg=BG)
        bar.pack(side="bottom", fill="x", padx=30, pady=14)

        self._skip_btn = tk.Button(
            bar, text="Skip  →",
            font=tkfont.Font(family="Segoe UI", size=10),
            bg=SKIP_COL, fg=BTN_TXT,
            activebackground="#9ca3af", activeforeground=BTN_TXT,
            relief="flat", bd=0, padx=14, pady=6,
            cursor="hand2",
            command=self._skip,
        )
        self._skip_btn.pack(side="left")

        self._close_btn = tk.Button(
            bar, text="Close  ✕",
            font=tkfont.Font(family="Segoe UI", size=10),
            bg=CARD, fg=SUBTEXT,
            activebackground=WRONG, activeforeground=BTN_TXT,
            relief="flat", bd=0, padx=14, pady=6,
            cursor="hand2",
            command=self.destroy,
        )
        self._close_btn.pack(side="right")

    # ── Logic ────────────────────────────────────────────────
    def _check(self, chosen):
        if self._answered:
            return
        self._answered = True
        correct = self._question["a"]
        color = PART_COLORS.get(correct, ACCENT)

        for btn in self._btns:
            opt = btn.cget("text").split(".", 1)[1].strip()
            if opt == correct:
                btn.config(bg=CORRECT, fg=BTN_TXT)
            elif opt == chosen:
                btn.config(bg=WRONG, fg=BTN_TXT)
            else:
                btn.config(state="disabled", fg=SUBTEXT)

        if chosen == correct:
            self._fb_lbl.config(
                text=f"✓  Correct!  '{correct}' — well done.",
                fg=CORRECT)
        else:
            self._fb_lbl.config(
                text=f"✗  Not quite. The answer is: {correct}",
                fg=WRONG)

        self._tag_lbl.config(
            text=f"Category: {correct}",
            fg=color)
        self._skip_btn.config(text="Next  →", command=self._new_question)

    def _skip(self):
        self._new_question()

    def _new_question(self):
        # Replace current question with a fresh random one (different from current)
        others = [q for q in QUESTIONS if q is not self._question]
        self._question = random.choice(others)
        self._opts = self._question["opts"][:]
        random.shuffle(self._opts)
        self._answered = False

        # Reset UI
        self._q_lbl.config(text=self._question["q"])
        self._tag_lbl.config(text="Parts of Speech Quiz", fg=SUBTEXT)
        self._fb_lbl.config(text="")
        self._skip_btn.config(text="Skip  →", command=self._skip)

        labels = ["A", "B", "C", "D"]
        for i, (btn, opt) in enumerate(zip(self._btns, self._opts)):
            btn.config(
                text=f"  {labels[i]}.  {opt}",
                bg=CARD, fg=TEXT, state="normal",
                command=lambda o=opt: self._check(o),
            )


if __name__ == "__main__":
    app = GrammarQuiz()
    app.mainloop()
