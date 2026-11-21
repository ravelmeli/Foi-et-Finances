"""Short « Compte séparé ou compte commun : quelle sagesse ? » (Ecclésiaste 4.9) — style 02, 9:16, ~76.6 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Compte séparé ou compte commun : quelle sagesse ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=76.6, cols=COLS, rows=ROWS, theme=THEME)
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
sticker(S1, "couple-un-compte", 20, 650, 560, 0.0, rot=-2, instant=True)
sticker(S1, "couple-chemin-ensemble", 480, 920, 520, 72.8, rot=3)
headline(S1, 300, ["Compte [commun]", "ou séparé ?"], 0.0, kicker="Pour un couple", hl_t=1.2, size=100)
bigword("Une question simple", 4.5, 1.0, y=1260, size=88)
hit(4.9, 0.9)

# --- S2 · aucune règle
cam(7.4, S2)
headline(S2, 280, ["Aucune [règle]", "sur les comptes"], 7.5, kicker="D'abord", hl_t=W("aucune", 7.4), size=100)
sticker(S2, "couple-budget", 40, 650, 460, 7.8, rot=-2)
tag(S2, 70, 1180, "Pas de nombre de comptes imposé", W("nombre", 7.4), "acc", 34)

# --- S3 · l'unité
cam(11.5, S3)
headline(S3, 280, ["L'[unité]"], 11.6, kicker="Elle parle d'autre chose", hl_t=W("unité", 11.5), size=130)
sticker(S3, "couple-chemin-ensemble", 40, 650, 560, 11.9, rot=-2)
tag(S3, 70, 1200, "« Les deux deviennent une seule chair »", W("chair", 11.5), "acc", 30)

# --- S4 · le verset (Ecclésiaste 4.9) : séquence « Parole »
cam(17.3, S4)
headline(S4, 280, ["Mieux à", "[deux]"], 17.4, kicker="Livre de l'Ecclésiaste", hl_t=W("valent", 20.0), size=110)
verse = "«&nbsp;" + m(0, "Deux valent mieux qu'un") + ", parce qu'ils retirent " + m(1, "un bon salaire") + " de leur travail.&nbsp;»"
verse_block(S4, "Ecclésiaste 4.9", 18.6, verse, 20.0, [W("valent", 20.0), W("salaire", 20.0)], size=56, ref_label="ECCLÉSIASTE 4.9")
sticker(S4, "livre-croix-ouvert", 60, 1000, 340, 17.8, rot=-3)
sticker(S4, "croix-verte", 600, 1020, 190, 21.5, rot=4)
hit(23.0, 1.0)

# --- S5 · avancer ensemble
cam(23.4, S5)
headline(S5, 280, ["Avancer", "[ensemble]"], 23.5, kicker="Ce qui compte", hl_t=W("ensemble", 23.4), size=110)
sticker(S5, "couple-chemin-ensemble", 40, 650, 540, 23.8, rot=-2)
tag(S5, 70, 1190, "Pas le nombre de comptes", W("nombre", 23.4), "acc", 38)

# --- S6 · trois formules
cam(27.5, S6)
headline(S6, 280, ["Trois", "[formules]"], 27.6, kicker="Voici", hl_t=28.0, size=120)
counter(S6, 70, 640, 0, 3, 28.0, 0.8, " formules", 140)
sticker(S6, "couple-deux-poches", 500, 840, 460, 28.2, rot=3)

# --- S7 · formule 1
cam(29.9, S7)
headline(S7, 280, ["Tout en", "[commun]"], 30.0, kicker="Formule 1", hl_t=W("commun", 29.9), size=110)
sticker(S7, "couple-un-compte", 40, 650, 480, 30.2, rot=-2)
tag(S7, 70, 1170, "Simple, transparent", W("transparent", 29.9), "", 38)
tag(S7, 70, 1260, "Favorise l'unité", W("unité", 29.9), "acc", 38)

# --- S8 · formule 2
cam(34.7, S8)
headline(S8, 280, ["Commun +", "[personnel]"], 34.8, kicker="Formule 2", hl_t=W("personnel", 34.7), size=100)
sticker(S8, "couple-deux-poches", 40, 650, 540, 35.0, rot=-2)
tag(S8, 70, 1190, "Un compte pour le foyer", W("foyer", 34.7), "", 36)
tag(S8, 70, 1270, "Un petit compte pour chacun", W("chacun", 34.7), "", 36)
tag(S8, 70, 1350, "Un bon équilibre", W("équilibre", 34.7), "acc", 36)

# --- S9 · formule 3
cam(41.4, S9)
headline(S9, 280, ["Comptes", "[séparés]"], 41.5, kicker="Formule 3", hl_t=W("séparés", 41.4), size=110)
sticker(S9, "couple-deux-comptes", 40, 650, 560, 41.7, rot=-2)
tag(S9, 70, 1190, "Contribution aux dépenses communes", W("contribution", 41.4), "", 30)
tag(S9, 70, 1270, "À condition d'être transparent", W("transparent", 41.4), "acc", 30)

# --- S10 · deux dangers
cam(47.1, S10)
headline(S10, 280, ["Deux", "[dangers]"], 47.2, kicker="Attention", hl_t=W("dangereuses", 47.1), size=120)
sticker(S10, "couple-secret-cache", 40, 650, 440, 47.4, rot=-2)
tag(S10, 70, 1160, "Le secret", W("secret", 47.1), "", 42)
tag(S10, 70, 1250, "Le contrôle", W("contrôle", 47.1), "acc", 42)
hit(W("contrôle", 47.1), 0.8)

# --- S11 · le secret
cam(50.8, S11)
headline(S11, 280, ["Le secret :", "la confiance se [fissure]"], 50.9, kicker="Dépenses ou dettes cachées", hl_t=W("fissure", 50.8), size=78)
sticker(S11, "couple-secret-cache", 40, 650, 460, 51.1, rot=-2)

# --- S12 · le contrôle
tC = W("contrôle", 50.8)
cam(tC - 0.4, S12)
headline(S12, 280, ["Le contrôle :", "pas de [liberté]"], tC - 0.3, kicker="Si l'un contrôle tout", hl_t=W("liberté", 50.8), size=84)
sticker(S12, "couple-controle-wallet", 40, 650, 560, tC, rot=-2)
tag(S12, 70, 1210, "Ce n'est pas de l'unité", W("unité", 50.8), "acc", 38)

# --- S13 · la question qui tranche
cam(58.0, S13)
headline(S13, 280, ["Plus [unis]", "ou plus distants ?"], 58.1, kicker="La question qui tranche", hl_t=W("unis", 58.0), size=92)
sticker(S13, "couple-chemin-ensemble", 40, 650, 520, 58.3, rot=-2)
hit(W("unis", 58.0), 0.9)

# --- S14 · choisir ensemble
cam(63.5, S14)
headline(S14, 280, ["Choisissez", "[ensemble]"], 63.6, kicker="En prière", hl_t=W("prière", 63.5), size=104)
sticker(S14, "couple-lit-bible", 40, 650, 460, 63.8, rot=-2)
tag(S14, 70, 1170, "Vos objectifs", W("objectifs", 63.5), "", 38)
tag(S14, 70, 1250, "Vos habitudes", W("habitudes", 63.5), "", 38)
tag(S14, 70, 1330, "Vos peurs", W("peurs", 63.5), "acc", 38)

# --- S15 · question aux spectateurs
cam(68.8, S15)
headline(S15, 300, ["Quelle formule", "vous [convient] ?"], 68.9, kicker="À ton tour", hl_t=W("convient", 68.8), size=92)
sticker(S15, "baton-pense", 700, 880, 210, 69.2, rot=3)
cta = put(S15, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 68.8) - 0.4, 14)
sfx("click", W("commentaire", 68.8) - 0.4, 0.8)
tag(S15, 70, 900, "Abonne-toi", W("abonne", 68.8), "acc", 48)

# --- fin en boucle
cam(72.7, S1)
bigword("La confiance", W("confiance", 72.7), 1.0, y=1260, size=100)
hit(W("confiance", 72.7), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 17.3), ("02", "Formules", 17.3, 47.1), ("03", "Dangers", 47.1, 68.8), ("04", "Action", 68.8, DUR)],
    suppress=[(19.9, 23.3)],
)
