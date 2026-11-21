"""Short « Dieu bénit-il les affaires malhonnêtes ? » (Proverbes 11.1) — style 02, 9:16, ~87.4 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Dieu bénit-il les affaires malhonnêtes ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=87.4, cols=COLS, rows=ROWS, theme=THEME)
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
sticker(S1, "balance-truquee", 20, 650, 620, 0.0, rot=-2, instant=True)
sticker(S1, "baton-conscience-paix", 560, 900, 400, 84.4, rot=3)
headline(S1, 300, ["Dieu bénit-il", "la [tricherie] ?"], 0.0, kicker="Affaires malhonnêtes", hl_t=1.4, size=100)
bigword("Réussir ou être béni ?", 5.3, 1.0, y=1260, size=76)
hit(5.7, 0.9)

# --- S2 · des tricheurs qui réussissent
cam(9.5, S2)
headline(S2, 280, ["Des tricheurs", "qui [réussissent]"], 9.6, kicker="Cela peut troubler", hl_t=W("réussissent", 9.5), size=92)
sticker(S2, "baton-richesse-sans-paix", 40, 650, 520, 9.9, rot=-2)
tag(S2, 70, 1200, "Et même tenter", W("tenter", 9.5), "acc", 40)

# --- S3 · le verset (Proverbes 11.1) : séquence « Parole »
cam(14.3, S3)
headline(S3, 280, ["La balance", "[fausse]"], 14.4, kicker="Livre des Proverbes", hl_t=W("fausse", 18.9), size=110)
verse = "«&nbsp;" + m(0, "La balance fausse") + " est en horreur à l'Éternel, mais " + m(1, "le poids juste") + " lui est agréable.&nbsp;»"
verse_block(S3, "Proverbes 11.1", 16.9, verse, 18.9, [W("balance", 18.9), W("poids", 18.9)], size=54, ref_label="PROVERBES 11.1")
sticker(S3, "livre-croix-ouvert", 60, 1000, 340, 14.8, rot=-3)
sticker(S3, "croix-verte", 600, 1020, 190, 21.0, rot=4)
hit(24.0, 1.0)

# --- S4 · tromper sur le poids
cam(24.5, S4)
headline(S4, 280, ["Tromper sur", "le [poids]"], 24.6, kicker="Aujourd'hui", hl_t=W("poids", 24.5), size=104)
sticker(S4, "baton-prix-caches", 40, 650, 500, 24.9, rot=-2)
tag(S4, 70, 1170, "Fausses factures", W("factures", 24.5), "", 32)
tag(S4, 70, 1240, "Mensonges aux clients", W("mensonges", 24.5), "", 32)
tag(S4, 70, 1310, "Travail au noir", W("noir", 24.5), "", 32)
tag(S4, 70, 1380, "Prix cachés", W("cachés", 24.5), "acc", 32)

# --- S5 · Dieu aime la justice
cam(31.7, S5)
headline(S5, 280, ["Dieu aime", "la [justice]"], 31.8, kicker="Pas un détail", hl_t=W("justice", 31.7), size=110)
sticker(S5, "petit-etal-honnete", 40, 650, 540, 32.0, rot=-2)
tag(S5, 70, 1200, "Deux erreurs à éviter", W("erreurs", 35.0), "acc", 38)
hit(W("justice", 31.7), 0.8)

# --- S6 · erreur 1
cam(36.7, S6)
headline(S6, 280, ["Réussite =", "[bénédiction] ?"], 36.8, kicker="Erreur 1", hl_t=W("bénédiction", 36.7), size=88)
sticker(S6, "baton-richesse-sans-paix", 40, 650, 520, 37.0, rot=-2)
tag(S6, 70, 1200, "Réussir sans être béni : possible", W("entreprise", 36.7), "acc", 30)

# --- S7 · erreur 2
cam(43.4, S7)
headline(S7, 280, ["Honnêteté =", "[richesse] ?"], 43.5, kicker="Erreur 2", hl_t=W("richesse", 43.4), size=88)
sticker(S7, "petit-etal-honnete", 40, 650, 540, 43.7, rot=-2)
tag(S7, 70, 1200, "La Bible ne le promet pas", W("promet", 43.4), "acc", 36)

# --- S8 · être béni
cam(48.7, S8)
headline(S8, 280, ["Être [béni]"], 48.8, kicker="Pas seulement gagner plus", hl_t=W("béni", 48.7), size=130)
sticker(S8, "baton-conscience-paix", 40, 650, 440, 49.0, rot=-2)
tag(S8, 70, 1190, "Conscience tranquille", W("conscience", 48.7), "", 38)
tag(S8, 70, 1270, "Paix", W("paix", 48.7), "", 38)
tag(S8, 70, 1350, "Relations saines", W("relations", 48.7), "acc", 38)

# --- S9 · trois questions
cam(55.1, S9)
headline(S9, 280, ["Trois", "[questions]"], 55.2, kicker="Pour ton activité", hl_t=55.6, size=110)
counter(S9, 70, 640, 0, 3, 55.6, 0.8, " questions", 140)
sticker(S9, "baton-ecrit-liste", 560, 820, 360, 55.4, rot=3)

# --- S10 · question 1
cam(57.8, S10)
headline(S10, 280, ["Mes clients", "savent [tout] ?"], 57.9, kicker="Question 1", hl_t=W("exactement", 57.8), size=100)
sticker(S10, "baton-prix-caches", 40, 650, 480, 58.1, rot=-2)
bigword("Question 1", 57.9, 0.9, y=1180, size=110)

# --- S11 · question 2
cam(61.6, S11)
headline(S11, 280, ["Expliquer", "sans [gêne] ?"], 61.7, kicker="Question 2", hl_t=W("gêne", 61.6), size=104)
sticker(S11, "famille-sortie", 40, 650, 520, 61.9, rot=-2)
bigword("Question 2", 61.7, 0.9, y=1180, size=110)

# --- S12 · question 3
cam(66.0, S12)
headline(S12, 280, ["Profiter de la", "[faiblesse] ?"], 66.1, kicker="Question 3", hl_t=W("faiblesse", 66.0), size=92)
sticker(S12, "baton-soucieux", 60, 650, 320, 66.3, rot=-2)
bigword("Question 3", 66.1, 0.9, y=1180, size=110)

# --- S13 · une porte de sortie
cam(69.4, S13)
headline(S13, 280, ["Une [porte]", "de sortie"], 69.5, kicker="Si tu as déjà triché", hl_t=W("porte", 69.4), size=104)
sticker(S13, "baton-rend-zachee", 40, 650, 540, 69.7, rot=-2)
tag(S13, 70, 1210, "Reconnaître", W("reconnaître", 69.4), "", 36)
tag(S13, 70, 1290, "Corriger", W("corriger", 69.4), "", 36)
tag(S13, 70, 1370, "Réparer, comme Zachée", W("réparer", 69.4), "acc", 36)

# --- S14 · peu et honnête
cam(76.2, S14)
headline(S14, 280, ["Peu et", "[honnête]"], 76.3, kicker="Mieux vaut", hl_t=W("honnête", 76.2), size=120)
sticker(S14, "petit-etal-honnete", 40, 650, 540, 76.5, rot=-2)
hit(W("honnête", 76.2), 0.9)

# --- S15 · question aux spectateurs
cam(79.5, S15)
headline(S15, 300, ["Quelle question", "te [parle] ?"], 79.6, kicker="À ton tour", hl_t=W("parle", 79.5), size=100)
sticker(S15, "baton-pense", 700, 880, 210, 79.9, rot=3)
cta = put(S15, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 79.5) - 0.4, 14)
sfx("click", W("commentaire", 79.5) - 0.4, 0.8)
tag(S15, 70, 900, "Abonne-toi", W("abonne", 79.5), "acc", 48)

# --- fin en boucle
cam(84.0, S1)
bigword("La justice", W("justice", 84.0), 1.0, y=1260, size=110)
hit(W("justice", 84.0), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 14.3), ("02", "Verset", 14.3, 36.7), ("03", "Questions", 36.7, 79.5), ("04", "Action", 79.5, DUR)],
    suppress=[(18.8, 24.4)],
)
