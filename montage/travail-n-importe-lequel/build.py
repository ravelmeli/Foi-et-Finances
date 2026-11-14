"""Short « Faut-il accepter n'importe quel travail pour gagner plus ? » (Actes 5.29) — style 02, 9:16, ~77.1 s.
Lot de 4 Shorts. Acquis : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte refermée, fin qui revient sur la première image. Temps lus dans transcript.json (voix fournie).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Faut-il accepter n'importe quel travail pour gagner plus ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=77.1, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S = ST
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot contenant `prefix`, après l'instant `after`."""
    k = 0
    for w in _TR:
        if w["start"] >= after and _norm(prefix) in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    raise KeyError(prefix)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


CTA = '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire'


def verse_block(stn, ref_txt, t_ref, verse_html, t_text, marks, size=54, ref_y=1420, ref_label=None):
    verse_html = verse_html.replace(" »", "&nbsp;»").replace("« ", "«&nbsp;").replace(" ;", "&nbsp;;").replace(" :", "&nbsp;:")
    tag(stn, 70, 600, ref_txt, t_ref, "acc", 52)
    sfx("spark", t_ref, 1.6)
    v = put(stn, 70, 710, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.22">{verse_html}</div>', "headline", f"width:{W_PX}px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    ref(stn, 70, ref_y, (ref_label or ref_txt.upper()) + " · LSG 1910", t_text + 0.3)


W_PX = 1080 - 2 * 70 - 60



S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15 = S[:15]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-refuse-offre", 30, 650, 560, 0.0, rot=-2, instant=True)
sticker(S1, "baton-dort-paix", 560, 880, 400, 70.5, rot=3)
headline(S1, 300, ["N'importe quel", "[travail] ?"], 0.0, kicker="Il paie mieux…", hl_t=1.0, size=100)
bigword("Une seule question", 1.8, 1.0, y=1260, size=92)
hit(2.2, 0.9)

# --- S2 · la dignité du travail
cam(4.3, S2)
headline(S2, 280, ["Tout travail", "[honnête]"], 4.4, kicker="La Bible honore le travail", hl_t=5.2, size=104)
sticker(S2, "baton-tablier-fier", 40, 650, 440, 4.8, rot=-2)
hit(7.0, 0.7)

# --- S3 · pas de sot métier
cam(8.8, S3)
headline(S3, 280, ["Des tentes,", "un [établi]"], 8.9, kicker="Pas de sot métier", hl_t=9.6, size=104)
sticker(S3, "baton-travaille", 60, 650, 340, 9.4, rot=-2)
sticker(S3, "mallette-travail", 620, 720, 280, 11.0, rot=3)
tag(S3, 70, 1100, "Des métiers modestes", 10.5, "acc", 36)
hit(11.8, 0.7)

# --- S4 · pas par orgueil
cam(11.9, S4)
headline(S4, 280, ["Pas par", "[orgueil]"], 12.0, kicker="Refuser un travail", hl_t=13.6, size=110)
sticker(S4, "baton-tablier-fier", 40, 650, 420, 12.4, rot=-2)
tag(S4, 70, 1100, "« En dessous de toi »", 14.6, "", 36)
tag(S4, 70, 1190, "Pas un principe biblique", 16.0, "acc", 32)
hit(16.8, 0.7)

# --- S5 · la limite (Actes 5.29) : séquence « Parole » ; sous-titres coupés
cam(17.0, S5)
headline(S5, 280, ["Obéir à", "[Dieu]"], 17.1, kicker="Livre des Actes", hl_t=22.4, size=110)
verse = "«&nbsp;Il faut " + m(0, "obéir à Dieu") + " plutôt qu'aux hommes.&nbsp;»"
verse_block(S5, "Actes 5.29", 19.8, verse, 21.6, [W("obéir", 21.5)], size=64, ref_label="ACTES 5.29")
sticker(S5, "livre-croix-ouvert", 60, 1040, 360, 17.5, rot=-3)
sticker(S5, "croix-verte", 580, 1040, 190, 22.5, rot=4)
hit(24.0, 1.0)

# --- S6 · appliqué au travail : la réponse est non
cam(24.3, S6)
headline(S6, 280, ["Tromper, voler,", "faire du [tort]"], 24.4, kicker="Appliqué au travail", hl_t=27.5, size=84)
sticker(S6, "baton-refuse-offre", 40, 650, 520, 24.8, rot=-2)
tag(S6, 70, 1180, "La réponse est non", 29.5, "acc", 42)
tag(S6, 70, 1270, "Même s'il paie plus", 30.8, "", 36)
hit(31.8, 0.8)

# --- S7 · cinq questions
cam(32.3, S7)
headline(S7, 280, ["Cinq", "[questions]"], 32.4, kicker="Pour décider", hl_t=33.0, size=110)
counter(S7, 70, 640, 0, 5, 33.3, 0.8, " questions", 140)
sticker(S7, "liste-cinq-cases", 600, 820, 300, 33.0, rot=3)
hit(34.2, 0.7)

# --- S8 · question 1 : honnête ?
cam(34.7, S8)
headline(S8, 280, ["Est-ce", "[honnête] ?"], 34.8, kicker="Question 1", hl_t=35.2, size=110)
sticker(S8, "baton-pense", 60, 650, 240, 35.0, rot=-2)

# --- S9 · question 2 : la décisive
cam(36.6, S9)
headline(S9, 280, ["Du [mal]", "à faire ?"], 36.7, kicker="Question 2 · la décisive", hl_t=37.4, size=104)
sticker(S9, "baton-refuse-offre", 40, 650, 460, 37.0, rot=-2)
bigword("Question 2", 36.9, 0.9, y=1130, size=110)
hit(40.5, 0.8)

# --- S10 : questions 3, 4, 5
cam(41.5, S10)
headline(S10, 280, ["Famille,", "santé, [durée]"], 41.6, kicker="Questions 3, 4 et 5", hl_t=45.5, size=92)
sticker(S10, "balance-famille-argent", 40, 650, 460, 41.8, rot=-2)
sticker(S10, "baton-marche-etape", 560, 720, 360, 45.6, rot=3)
tag(S10, 70, 1120, "Ma famille", 42.0, "", 38)
tag(S10, 70, 1210, "Ma santé", 43.6, "", 38)
tag(S10, 70, 1300, "Temporaire ou durable ?", 45.7, "acc", 34)
hit(47.0, 0.7)

# --- S11 : une bonne étape
cam(47.4, S11)
headline(S11, 280, ["Une bonne", "[étape]"], 47.5, kicker="Modeste, honnête, temporaire", hl_t=49.0, size=104)
sticker(S11, "baton-marche-etape", 40, 650, 480, 48.0, rot=-2)
tag(S11, 70, 1180, "Travail honnête = dignité", 50.0, "acc", 34)
hit(51.0, 0.7)

# --- S12 : ça coûte trop cher
cam(51.5, S12)
headline(S12, 280, ["Trop", "[cher]"], 51.6, kicker="Un salaire qui t'éloigne", hl_t=56.0, size=120)
sticker(S12, "balance-famille-argent", 40, 650, 520, 52.0, rot=-2)
tag(S12, 70, 1160, "Ta famille", 53.4, "", 38)
tag(S12, 70, 1250, "Ta santé", 54.6, "", 38)
tag(S12, 70, 1340, "Ta conscience", 55.6, "acc", 38)
hit(56.8, 0.8)

# --- S13 : ton salaire n'est pas ta valeur
cam(57.4, S13)
headline(S13, 280, ["Ton salaire", "n'est pas ta [valeur]"], 57.5, kicker="Rappelle-toi", hl_t=58.6, size=80)
sticker(S13, "baton-serein", 60, 650, 300, 58.0, rot=-2)
sticker(S13, "croix-verte", 620, 700, 220, 59.0, rot=4)
hit(59.2, 0.7)

# --- S14 : cette semaine
cam(59.4, S14)
headline(S14, 280, ["Cinq questions,", "une [feuille]"], 59.5, kicker="Si tu hésites", hl_t=61.0, size=92)
sticker(S14, "liste-cinq-cases", 60, 650, 400, 60.0, rot=-2)
tag(S14, 70, 1180, "Parles-en à quelqu'un de sage", 63.8, "acc", 32)
hit(65.0, 0.7)

# --- S15 : question aux spectateurs
cam(66.9, S15)
headline(S15, 300, ["Quel critère", "te [manquait] ?"], 67.0, kicker="À ton tour", hl_t=67.6, size=96)
sticker(S15, "baton-serein", 700, 880, 210, 67.4, rot=3)
cta = put(S15, 70, 760, CTA, "cta")
blur_in(cta, 68.9, 14)
sfx("click", 68.9, 0.8)
tag(S15, 70, 900, "Abonne-toi", 69.6, "acc", 48)

# --- fin en boucle
cam(70.2, S1)
bigword("La dignité", 72.8, 0.9, y=1260, size=110)
bigword("Ta conscience", 74.6, 1.0, y=1260, size=110)
hit(74.8, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 4.3), ("02", "Principe", 4.3, 24.3), ("03", "Critères", 24.3, 57.4), ("04", "Action", 57.4, DUR)],
    suppress=[(21.55, 24.25)],
)
