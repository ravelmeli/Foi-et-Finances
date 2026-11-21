"""Short « Pourquoi l'épargne n'est pas un manque de foi » (Genèse 41.36) — style 02, 9:16, ~79.2 s.
Lot de 4 Shorts. Acquis : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte refermée, fin qui revient sur la première image. Temps lus dans transcript.json (voix fournie).

Lancer : python3 build.py   (puis hyperframes check et hyperframes render -q draft)
"""
import difflib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Pourquoi l'épargne n'est pas un manque de foi", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=79.2, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S = ST
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot contenant `prefix`, après l'instant `after` (repli approximatif signalé)."""
    pn = _norm(prefix).rstrip("s")
    k = 0
    for w in _TR:
        if w["start"] >= after and pn in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    cand = [w for w in _TR if after <= w["start"] <= after + 12]
    best = difflib.get_close_matches(_norm(prefix), [_norm(w["text"]) for w in cand], n=1, cutoff=0.55)
    for w in cand:
        if best and _norm(w["text"]) == best[0]:
            print("  ~ repli", prefix, "->", w["text"], w["start"])
            return round(w["start"], 2)
    raise KeyError((prefix, after))


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
sticker(S1, "piggy-parapluie", 20, 650, 600, 0.0, rot=-2, instant=True)
sticker(S1, "baton-espere-ciel", 560, 900, 400, 76.0, rot=3)
headline(S1, 300, ["Épargner :", "[manque] de foi ?"], 0.0, kicker="Une idée reçue", hl_t=1.3, size=96)
bigword("Un test simple", 4.4, 1.0, y=1260, size=96)
hit(4.8, 0.9)

# --- S2 · préparer, c'est douter ?
cam(8.1, S2)
headline(S2, 280, ["Préparer,", "c'est [douter] ?"], 8.2, kicker="Certains pensent", hl_t=W("douter", 8.1), size=100)
sticker(S2, "baton-soucieux", 60, 650, 320, 8.4, rot=-2)
tag(S2, 70, 1180, "La Bible raconte l'inverse", W("inverse", 8.1), "acc", 38)

# --- S3 · le verset (Genèse 41.36) : séquence « Parole »
cam(13.4, S3)
headline(S3, 280, ["Joseph fait", "des [réserves]"], 13.5, kicker="Livre de la Genèse", hl_t=W("réserve", 21.1), size=100)
verse = "«&nbsp;Ces vivres seront " + m(0, "en réserve") + " pour le pays, pour les sept années de famine ; et le pays " + m(1, "ne sera pas détruit") + " par la famine.&nbsp;»"
verse_block(S3, "Genèse 41.36", 15.6, verse, 21.2, [W("réserve", 21.1), W("détruit", 21.1)], size=50, ref_label="GENÈSE 41.36")
sticker(S3, "livre-croix-ouvert", 60, 1090, 320, 14.0, rot=-3)
sticker(S3, "croix-verte", 600, 1100, 190, 26.0, rot=4)
hit(26.9, 1.0)

# --- S4 · Joseph a-t-il manqué de foi ?
cam(27.2, S4)
headline(S4, 280, ["Joseph a-t-il", "manqué de [foi] ?"], 27.3, kicker="Non", hl_t=W("sage", 27.2), size=84)
sticker(S4, "greniers-joseph", 40, 650, 580, 27.5, rot=-2)
tag(S4, 70, 1200, "Il a été sage", W("sage", 27.2), "", 40)
tag(S4, 70, 1280, "Il a sauvé des vies", W("vies", 27.2), "acc", 40)

# --- S5 · épargner, c'est prévoir
cam(31.9, S5)
headline(S5, 280, ["Épargner,", "c'est [prévoir]"], 32.0, kicker="Pas un manque de confiance", hl_t=W("prévoir", 31.9), size=104)
sticker(S5, "piggy-parapluie", 40, 650, 420, 32.2, rot=-2)
tag(S5, 70, 1170, "Ce n'est pas refuser de faire confiance", W("refuser", 31.9), "acc", 30)

# --- S6 · l'autre extrême
cam(35.6, S6)
headline(S6, 280, ["L'autre", "[extrême]"], 35.7, kicker="Attention", hl_t=W("extrême", 35.6), size=110)
sticker(S6, "grenier-trop-plein", 40, 650, 560, 35.9, rot=-2)
tag(S6, 70, 1210, "Amasser, et oublier Dieu", W("oublie", 35.6), "", 34)
tag(S6, 70, 1290, "Et oublier les autres", W("autres", 35.6), "acc", 34)

# --- S7 · où est ton cœur ?
cam(41.4, S7)
headline(S7, 280, ["Où est ton", "[cœur] ?"], 41.5, kicker="Le vrai problème", hl_t=W("cœur", 41.4), size=110)
sticker(S7, "baton-tiraille", 60, 650, 300, 41.7, rot=-2)
tag(S7, 70, 1170, "Pas l'épargne : l'endroit du cœur", W("épargne", 41.4), "acc", 32)

# --- S8 · le test
cam(45.4, S8)
headline(S8, 280, ["Le [test]", "en 3 questions"], 45.5, kicker="Voici", hl_t=45.8, size=100)
counter(S8, 70, 640, 0, 3, 45.9, 0.8, " questions", 140)
sticker(S8, "balance-prudence-peur", 480, 840, 480, 46.0, rot=3)

# --- S9 · question 1
cam(48.0, S9)
headline(S9, 280, ["Prudence", "ou [peur] ?"], 48.1, kicker="Question 1", hl_t=W("peur", 48.0), size=110)
sticker(S9, "balance-prudence-peur", 40, 650, 520, 48.3, rot=-2)
bigword("Question 1", 48.1, 0.9, y=1180, size=110)

# --- S10 · question 2
cam(52.2, S10)
headline(S10, 280, ["Donner et", "[aider] ?"], 52.3, kicker="Question 2", hl_t=W("donner", 52.2), size=110)
sticker(S10, "bocal-donne-main", 40, 650, 500, 52.5, rot=-2)
bigword("Question 2", 52.3, 0.9, y=1180, size=110)
tag(S10, 70, 1300, "Mon épargne m'en empêche-t-elle ?", W("empêche", 52.2), "acc", 32)

# --- S11 · question 3
cam(56.2, S11)
headline(S11, 280, ["Mon espérance", "en [Dieu] ?"], 56.3, kicker="Question 3", hl_t=W("espérance", 56.2), size=100)
sticker(S11, "baton-espere-ciel", 40, 650, 400, 56.5, rot=-2)
bigword("Question 3", 56.3, 0.9, y=1180, size=110)

# --- S12 · une épargne saine
cam(59.7, S12)
headline(S12, 280, ["Une épargne", "[saine]"], 59.8, kicker="Si tes réponses sont…", hl_t=W("saine", 59.7), size=110)
sticker(S12, "piggy-parapluie", 40, 650, 420, 60.0, rot=-2)
tag(S12, 70, 1170, "La prudence", W("prudence", 59.7), "", 38)
tag(S12, 70, 1250, "Je donne", W("donne", 59.7), "", 38)
tag(S12, 70, 1330, "Mon espérance reste en Dieu", W("espérance", 59.7), "acc", 34)

# --- S13 · les trois ensemble
cam(67.4, S13)
headline(S13, 280, ["Épargne, donne,", "[fais confiance]"], 67.5, kicker="Les trois ensemble", hl_t=W("confiance", 67.4), size=84)
sticker(S13, "bocal-donne-main", 40, 650, 500, 67.7, rot=-2)

# --- S14 · question aux spectateurs
cam(72.1, S14)
headline(S14, 300, ["Quelle question", "te [parle] ?"], 72.2, kicker="À ton tour", hl_t=W("parle", 72.1), size=100)
sticker(S14, "baton-pense", 700, 880, 210, 72.5, rot=3)
cta = put(S14, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 72.1) - 0.4, 14)
sfx("click", W("commentaire", 72.1) - 0.4, 0.8)
tag(S14, 70, 900, "Abonne-toi", W("abonne", 72.1), "acc", 48)

# --- fin en boucle
cam(75.6, S1)
bigword("La vivre", W("vivre", 75.6), 1.0, y=1260, size=120)
hit(W("vivre", 75.6), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 13.4), ("02", "Verset", 13.4, 27.2), ("03", "Test", 27.2, 72.1), ("04", "Action", 72.1, DUR)],
    suppress=[(21.1, 27.1)],
)
