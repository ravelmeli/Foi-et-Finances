"""Short « Pourquoi la cupidité détruit la paix intérieure » (Proverbes 15.27) — style 02, 9:16, ~81.9 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Pourquoi la cupidité détruit la paix intérieure", "lang": "fr"}
COLS, ROWS = 3, 16
s.setup(here=HERE, duration=81.9, cols=COLS, rows=ROWS, theme=THEME)
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



S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16 = S[:16]

# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-encore-sacs", 30, 640, 540, 0.0, rot=-2, instant=True)
headline(S1, 300, ["Plus on en veut,", "moins on est en [paix]"], 0.0, kicker="Pourquoi ?", hl_t=2.0, size=80)
tag(S1, 70, 1300, "Ambition… ou cupidité ?", 3.0, "acc", 38)
bigword("Encore plus ?", 2.2, 0.8, y=1170, size=110)
hit(2.4, 0.9)

# --- S2 · le verset (Proverbes 15.27) : séquence « Parole »
cam(5.7, S2)
headline(S2, 280, ["Trouble", "sa [maison]"], 5.8, kicker="Livre des Proverbes", hl_t=11.2, size=110)
verse = ("«&nbsp;Celui qui est avide de gain " + m(0, "trouble sa maison") + ", mais celui qui hait les présents vivra.&nbsp;»")
verse_block(S2, "Proverbes 15.27", 7.2, verse, 9.3, [W("trouble", 9.3)], size=58, ref_label="PROVERBES 15.27")
sticker(S2, "maison-orage-pieces", 60, 1060, 320, 6.4, rot=-2)
hit(14.2, 1.0)

# --- S3 · la paix du cœur et de la famille
cam(14.4, S3)
headline(S3, 280, ["La paix du cœur,", "de la [famille]"], 14.5, kicker="Plus qu'un portefeuille", hl_t=18.2, size=80)
sticker(S3, "maison-orage-pieces", 40, 650, 440, 15.0, rot=-2)
sticker(S3, "coeur-receptacle", 620, 740, 300, 17.5, rot=3)
hit(18.6, 0.7)

# --- S4 · jamais « assez »
cam(21.0, S4)
headline(S4, 280, ["Jamais", "« [assez] »"], 21.1, kicker="La cupidité, c'est", hl_t=22.6, size=110)
sticker(S4, "baton-encore-sacs", 40, 650, 460, 21.5, rot=-2)
tag(S4, 70, 1130, "Toujours plus", 23.0, "acc", 42)
bigword("Encore", 24.2, 0.8, y=1260, size=110)
hit(24.6, 0.7)

# --- S5 · trois façons
cam(25.6, S5)
headline(S5, 280, ["Trois", "[façons]"], 25.7, kicker="Elle détruit la paix", hl_t=26.4, size=110)
counter(S5, 70, 640, 0, 3, 26.8, 0.8, " façons", 140)
sticker(S5, "baton-sur-coffre", 640, 800, 240, 27.0, rot=3)
hit(27.6, 0.7)

# --- S6 · 1 : elle t'empêche de profiter
cam(28.1, S6)
headline(S6, 280, ["Elle t'empêche", "de [profiter]"], 28.2, kicker="Façon 1", hl_t=29.5, size=84)
sticker(S6, "baton-encore-sacs", 40, 650, 440, 28.6, rot=-2)
tag(S6, 70, 1130, "Ce qui manque", 30.0, "", 40)
tag(S6, 70, 1220, "jamais ce que tu as", 31.2, "acc", 36)
hit(32.4, 0.7)

# --- S7 · 2 : elle t'éloigne des tiens
cam(32.7, S7)
headline(S7, 280, ["Elle t'éloigne", "des [tiens]"], 32.8, kicker="Façon 2", hl_t=34.0, size=96)
sticker(S7, "famille-sortie", 40, 650, 520, 33.2, rot=-2)
tag(S7, 70, 1130, "Du temps", 34.8, "", 38)
tag(S7, 70, 1220, "Des repas", 35.8, "", 38)
tag(S7, 70, 1310, "Des conversations", 36.8, "acc", 36)
hit(39.0, 0.7)

# --- S8 · 3 : elle t'angoisse
cam(39.9, S8)
headline(S8, 280, ["Elle", "t'[angoisse]"], 40.0, kicker="Façon 3", hl_t=40.8, size=110)
sticker(S8, "baton-sur-coffre", 40, 650, 360, 40.4, rot=-2)
tag(S8, 70, 1220, "Plus tu as, plus tu as peur", 41.6, "acc", 32)
hit(42.8, 0.7)

# --- S9 · le test ambition / cupidité
cam(43.3, S9)
headline(S9, 280, ["Ambition", "ou [cupidité] ?"], 43.4, kicker="Le test", hl_t=44.2, size=104)
sticker(S9, "cible-spirale", 40, 650, 560, 44.6, rot=-2)
tag(S9, 70, 1050, "L'ambition sert un but", 46.0, "", 34)
tag(S9, 70, 1140, "La cupidité dit : encore", 49.0, "acc", 34)
hit(51.5, 0.9)

# --- S10 · trois remèdes
cam(52.2, S10)
headline(S10, 280, ["Trois", "[remèdes]"], 52.3, kicker="Pour retrouver la paix", hl_t=53.0, size=110)
counter(S10, 70, 640, 0, 3, 53.0, 0.8, " remèdes", 140)
sticker(S10, "colombe", 600, 820, 300, 52.6, rot=3)

# --- S11 · remède 1 : fixe ton assez
cam(54.1, S11)
headline(S11, 280, ["Fixe ton", "[assez]"], 54.2, kicker="Remède 1", hl_t=54.8, size=110)
sticker(S11, "bol-assez-coche", 40, 650, 520, 54.5, rot=-2)

# --- S12 : remède 2 : remercie
cam(56.2, S12)
headline(S12, 280, ["Remercie", "chaque [jour]"], 56.3, kicker="Remède 2", hl_t=57.0, size=104)
sticker(S12, "baton-content", 60, 650, 300, 56.6, rot=-2)
sticker(S12, "soleil-nuage", 620, 720, 300, 58.0, rot=3)

# --- S13 : remède 3 : donne
cam(59.6, S13)
headline(S13, 280, ["Donne,", "[main ouverte]"], 59.7, kicker="Remède 3", hl_t=61.0, size=96)
sticker(S13, "poing-main-ouverte", 40, 660, 560, 60.4, rot=-2)
tag(S13, 70, 1060, "Poing fermé", 61.4, "", 38)
tag(S13, 70, 1150, "Main ouverte", 62.4, "acc", 40)
hit(63.0, 0.7)

# --- S14 : ne te condamne pas
cam(63.0, S14)
headline(S14, 280, ["Ne te", "condamne [pas]"], 63.1, kicker="Si tu te reconnais", hl_t=64.0, size=104)
sticker(S14, "baton-serein", 60, 650, 300, 63.5, rot=-2)
sticker(S14, "colombe", 620, 720, 300, 66.0, rot=3)
tag(S14, 70, 1130, "On commence petit", 66.5, "acc", 40)
hit(67.4, 0.7)

# --- S15 : cette semaine
cam(67.7, S15)
headline(S15, 280, ["Écris le chiffre", "qui te [suffit]"], 67.8, kicker="Cette semaine", hl_t=69.0, size=88)
sticker(S15, "baton-ecrit-liste", 60, 650, 360, 68.2, rot=-2)
sticker(S15, "enveloppe-don", 620, 730, 280, 70.0, rot=3)
tag(S15, 70, 1150, "Puis décide d'un don", 70.5, "acc", 38)
hit(71.2, 0.7)

# --- S16 : question aux spectateurs
cam(71.9, S16)
headline(S16, 300, ["Ta tentation du", "« [encore plus] » ?"], 72.0, kicker="À ton tour", hl_t=72.8, size=84)
sticker(S16, "baton-serein", 700, 880, 210, 72.4, rot=3)
cta = put(S16, 70, 760, CTA, "cta")
blur_in(cta, 75.2, 14)
sfx("click", 75.2, 0.8)
tag(S16, 70, 900, "Abonne-toi", 76.0, "acc", 48)

# --- fin en boucle
cam(76.9, S1)
bigword("Pas le plus", 78.2, 0.8, y=1170, size=110)
bigword("C'est l'assez", 79.4, 1.0, y=1170, size=110)
hit(79.6, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 5.7), ("02", "Verset", 5.7, 21.0), ("03", "Pourquoi", 21.0, 52.2), ("04", "Remèdes", 52.2, DUR)],
    suppress=[(9.25, 14.45)],
)
