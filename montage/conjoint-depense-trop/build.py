"""Short « Que faire quand son conjoint dépense trop ? » (Proverbes 15.1) — style 02, 9:16, ~81.4 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Que faire quand son conjoint dépense trop ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=81.4, cols=COLS, rows=ROWS, theme=THEME)
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
sticker(S1, "couple-sacs-tension", 10, 650, 640, 0.0, rot=-2, instant=True)
sticker(S1, "couple-meme-cote", 480, 930, 520, 78.0, rot=3)
headline(S1, 300, ["Ton conjoint", "[dépense] trop"], 0.0, kicker="Comment réagir ?", hl_t=1.2, size=104)
bigword("Une phrase simple", 4.1, 1.0, y=1260, size=88)
hit(4.5, 0.9)

# --- S2 · l'attaque ferme l'oreille
cam(8.2, S2)
headline(S2, 280, ["L'attaque", "[ferme] l'oreille"], 8.3, kicker="Quand la colère monte", hl_t=W("ferme", 8.2), size=92)
sticker(S2, "couple-sacs-tension", 40, 650, 560, 8.5, rot=-2)
tag(S2, 70, 1230, "L'argent s'évapore", W("évapore", 8.2), "acc", 38)

# --- S3 · le verset (Proverbes 15.1) : séquence « Parole »
cam(13.5, S3)
headline(S3, 280, ["Une [réponse]", "douce"], 13.6, kicker="Livre des Proverbes", hl_t=W("douce", 16.2), size=110)
verse = "«&nbsp;" + m(0, "Une réponse douce") + " calme la fureur, mais " + m(1, "une parole dure") + " excite la colère.&nbsp;»"
verse_block(S3, "Proverbes 15.1", 14.9, verse, 16.2, [W("réponse", 16.1), W("parole", 16.2)], size=56, ref_label="PROVERBES 15.1")
sticker(S3, "baton-parole-douce", 60, 1010, 260, 14.0, rot=-3)
sticker(S3, "croix-verte", 600, 1030, 190, 19.0, rot=4)
hit(20.6, 1.0)

# --- S4 · étape 1
cam(21.1, S4)
headline(S4, 280, ["Étape 1 :", "le bon [moment]"], 21.2, kicker="Pas en pleine dispute", hl_t=W("moment", 21.1), size=96)
sticker(S4, "couple-table-calme", 40, 650, 540, 21.4, rot=-2)
tag(S4, 70, 1190, "Pas devant les enfants", W("enfants", 21.1), "", 36)
tag(S4, 70, 1270, "Pas juste après une facture", W("facture", 21.1), "acc", 34)

# --- S5 · étape 2
cam(27.3, S5)
headline(S5, 280, ["Étape 2 :", "les [faits]"], 27.4, kicker="Pas le caractère", hl_t=W("faits", 27.3), size=104)
sticker(S5, "baton-parole-douce", 40, 650, 340, 27.6, rot=-2)
tag(S5, 70, 1170, "Pas « tu es irresponsable »", W("irresponsable", 27.3), "", 32)
tag(S5, 70, 1250, "Mais « on a dépensé plus que prévu »", W("prévu", 27.3), "acc", 30)

# --- S6 · étape 3
cam(34.5, S6)
headline(S6, 280, ["Étape 3 :", "[comprendre]"], 34.6, kicker="Avant de juger", hl_t=W("comprendre", 34.5), size=104)
sticker(S6, "baton-pense", 60, 650, 300, 34.8, rot=-2)
tag(S6, 70, 1170, "Le stress", W("stress", 34.5), "", 32)
tag(S6, 70, 1240, "Un manque", W("manque", 34.5), "", 32)
tag(S6, 70, 1310, "Une habitude", W("habitude", 34.5), "", 32)
tag(S6, 70, 1380, "Une façon de se consoler", W("consoler", 34.5), "acc", 32)

# --- S7 · étape 4
cam(42.6, S7)
headline(S7, 280, ["Étape 4 :", "un [cadre]"], 42.7, kicker="Ensemble", hl_t=W("cadre", 42.6), size=110)
sticker(S7, "enveloppes-plaisir", 40, 650, 460, 42.9, rot=-2)
tag(S7, 70, 1020, "Un budget partagé", W("budget", 42.6), "", 36)
tag(S7, 70, 1100, "Une somme « plaisir » pour chacun", W("plaisir", 42.6), "", 32)
tag(S7, 70, 1180, "Un seuil : on se parle avant", W("seuil", 42.6), "acc", 32)

# --- S8 · la phrase
cam(52.7, S8)
headline(S8, 280, ["Une [équipe]", "face à l'argent"], 52.8, kicker="La phrase qui change tout", hl_t=W("équipe", 52.7), size=92)
sticker(S8, "couple-meme-cote", 40, 650, 560, 53.0, rot=-2)
tag(S8, 70, 1210, "« Je veux qu'on soit une équipe »", W("veux", 52.7), "acc", 30)

# --- S9 · nous contre le problème
cam(56.9, S9)
headline(S9, 280, ["Nous contre", "le [problème]"], 57.0, kicker="Pas toi contre moi", hl_t=W("problème", 56.9), size=96)
sticker(S9, "couple-meme-cote", 40, 650, 560, 57.2, rot=-2)
hit(W("problème", 56.9), 0.9)

# --- S10 · dépenses incontrôlables
cam(60.1, S10)
headline(S10, 280, ["Dépenses", "[incontrôlables]"], 60.2, kicker="Attention", hl_t=W("incontrôlables", 60.1), size=84)
sticker(S10, "couple-conseiller", 40, 650, 560, 60.4, rot=-2)
tag(S10, 70, 1210, "Cachées, répétées", W("cachées", 60.1), "", 34)
tag(S10, 70, 1290, "Dettes qui s'accumulent", W("dettes", 60.1), "", 34)
tag(S10, 70, 1370, "Un conseiller peut aider", W("conseiller", 60.1), "acc", 34)

# --- S11 · en danger : parle
cam(69.1, S11)
headline(S11, 280, ["Contrôlé, menacé ?", "[Parle]"], 69.2, kicker="Si tu te sens en danger", hl_t=W("parle", 69.1), size=84)
sticker(S11, "baton-conseillers", 40, 650, 520, 69.4, rot=-2)
tag(S11, 70, 1190, "Une personne de confiance", W("confiance", 69.1), "", 32)
tag(S11, 70, 1270, "Ou un professionnel", W("professionnel", 69.1), "acc", 32)

# --- S12 · question aux spectateurs
cam(74.5, S12)
headline(S12, 300, ["Comment gères-tu", "ce [sujet] ?"], 74.6, kicker="À ton tour", hl_t=W("sujet", 74.5), size=92)
sticker(S12, "baton-pense", 700, 880, 210, 74.9, rot=3)
cta = put(S12, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 74.5) - 0.4, 14)
sfx("click", W("commentaire", 74.5) - 0.4, 0.8)
tag(S12, 70, 900, "Abonne-toi", W("abonne", 74.5), "acc", 48)

# --- fin en boucle
cam(78.0, S1)
bigword("Réponse douce", W("réponse", 78.0), 1.0, y=1260, size=100)
hit(W("douce", 78.0), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 13.5), ("02", "Verset", 13.5, 21.1), ("03", "Étapes", 21.1, 74.5), ("04", "Action", 74.5, DUR)],
    suppress=[(16.1, 21.0)],
)
