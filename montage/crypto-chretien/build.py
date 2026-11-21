"""Short « Faut-il investir dans les cryptomonnaies quand on est chrétien ? » (Proverbes 28.20) — style 02, 9:16, ~77.1 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Faut-il investir dans les cryptomonnaies quand on est chrétien ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=77.1, cols=COLS, rows=ROWS, theme=THEME)
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
sticker(S1, "piece-montagnes-russes", 20, 650, 620, 0.0, rot=-2, instant=True)
sticker(S1, "baton-calcule-perte", 560, 900, 420, 74.0, rot=3)
headline(S1, 300, ["Cryptos :", "oui ou [non] ?"], 0.0, kicker="Quand on est chrétien", hl_t=1.2, size=104)
bigword("Trois questions", 4.8, 1.0, y=1260, size=96)
hit(5.2, 0.9)

# --- S2 · la Bible n'en parle pas
cam(8.8, S2)
headline(S2, 280, ["La Bible n'en", "[parle] pas"], 8.9, kicker="D'abord, soyons honnêtes", hl_t=W("parle", 8.8), size=100)
sticker(S2, "baton-pense", 60, 650, 320, 9.2, rot=-2)
tag(S2, 70, 1160, "Ni condamnées", W("condamne", 8.8), "", 40)
tag(S2, 70, 1250, "Ni recommandées", W("recommande", 8.8), "acc", 40)

# --- S3 · sagesse, patience, hâte
cam(15.3, S3)
headline(S3, 280, ["Sagesse,", "patience, [hâte]"], 15.4, kicker="Ce dont elle parle", hl_t=W("enrichir", 15.3), size=100)
sticker(S3, "balance-patience-hate", 40, 650, 520, 15.7, rot=-2)
tag(S3, 70, 1220, "Sagesse", W("sagesse", 15.3), "", 38)
tag(S3, 70, 1300, "Patience", W("patience", 15.3), "", 38)
tag(S3, 70, 1380, "S'enrichir vite", W("vite", 15.3), "acc", 38)

# --- S4 · le verset (Proverbes 28.20) : séquence « Parole »
cam(20.8, S4)
headline(S4, 280, ["Se [hâter]", "de s'enrichir"], 20.9, kicker="Livre des Proverbes", hl_t=W("hâte", 23.7), size=104)
verse = "«&nbsp;L'homme " + m(0, "fidèle") + " est comblé de bénédictions, mais celui qui " + m(1, "se hâte de s'enrichir") + " ne reste pas impuni.&nbsp;»"
verse_block(S4, "Proverbes 28.20", 22.1, verse, 23.7, [W("fidèle", 23.7), W("hâte", 23.7)], size=56, ref_label="PROVERBES 28.20")
sticker(S4, "livre-croix-ouvert", 60, 1060, 340, 21.3, rot=-3)
sticker(S4, "croix-verte", 600, 1080, 190, 28.0, rot=4)
hit(29.3, 1.0)

# --- S5 · le danger, c'est la hâte
cam(29.8, S5)
headline(S5, 280, ["Le danger :", "la [hâte]"], 29.9, kicker="Pas la technologie", hl_t=W("hâte", 29.8), size=110)
sticker(S5, "baton-ecran-graphique", 40, 650, 420, 30.2, rot=-2)
hit(W("hâte", 29.8), 0.9)

# --- S6 · monter vite, chuter vite
cam(32.9, S6)
headline(S6, 280, ["Ça monte vite,", "ça [chute] vite"], 33.0, kicker="Un fait à connaître", hl_t=W("chuter", 32.9), size=88)
sticker(S6, "piece-montagnes-russes", 40, 650, 560, 33.3, rot=-2)
tag(S6, 70, 1190, "Les arnaques sont nombreuses", W("arnaques", 32.9), "", 34)
tag(S6, 70, 1280, "Tout perdre est possible", W("perdre", 32.9), "acc", 38)
hit(W("perdre", 32.9), 0.8)

# --- S7 · trois questions
cam(40.9, S7)
headline(S7, 280, ["Trois", "[questions]"], 41.0, kicker="Avant d'investir", hl_t=41.5, size=110)
counter(S7, 70, 640, 0, 3, 41.5, 0.8, " questions", 140)
sticker(S7, "baton-calcule-perte", 560, 820, 360, 41.3, rot=3)

# --- S8 · question 1
cam(42.6, S8)
headline(S8, 280, ["Est-ce que je", "[comprends] ?"], 42.7, kicker="Question 1", hl_t=W("comprends", 42.6), size=96)
sticker(S8, "baton-loupe-boite", 40, 650, 440, 43.0, rot=-2)
bigword("Question 1", 42.8, 0.9, y=1180, size=110)
tag(S8, 70, 1300, "Pas expliqué simplement : j'y touche pas", W("expliquer", 42.6), "acc", 30)

# --- S9 · question 2
cam(47.8, S9)
headline(S9, 280, ["Perdre cette", "[somme] ?"], 47.9, kicker="Question 2", hl_t=W("somme", 47.8), size=104)
sticker(S9, "coffre-urgence", 40, 650, 330, 48.2, rot=-2)
bigword("Question 2", 48.0, 0.9, y=1180, size=110)
tag(S9, 70, 1300, "Jamais le loyer, ni ton urgence", W("loyer", 47.8), "acc", 34)

# --- S10 · question 3
cam(56.1, S10)
headline(S10, 280, ["Patience ou", "[peur] ?"], 56.2, kicker="Question 3", hl_t=W("peur", 56.1), size=110)
sticker(S10, "balance-patience-hate", 40, 650, 520, 56.4, rot=-2)
bigword("Question 3", 56.2, 0.9, y=1180, size=110)
tag(S10, 70, 1300, "Peur de rater l'occasion", W("rater", 56.1), "acc", 36)

# --- S11 · mets de l'ordre
cam(59.9, S11)
headline(S11, 280, ["Mets de", "l'[ordre]"], 60.0, kicker="Avant tout cela", hl_t=W("ordre", 59.9), size=110)
sticker(S11, "baton-ecrit-liste", 40, 650, 440, 60.3, rot=-2)
tag(S11, 70, 1190, "Dettes", W("dettes", 59.9), "", 38)
tag(S11, 70, 1270, "Réserve de sécurité", W("réserve", 59.9), "", 38)
tag(S11, 70, 1350, "Générosité", W("générosité", 59.9), "acc", 38)

# --- S12 · jamais dans la précipitation
cam(64.6, S12)
headline(S12, 280, ["Jamais dans la", "[précipitation]"], 64.7, kicker="Ni oui, ni non", hl_t=W("précipitation", 64.6), size=88)
sticker(S12, "baton-calcule-perte", 40, 650, 500, 65.0, rot=-2)
tag(S12, 70, 1220, "Ni « investis », ni « n'investis pas »", W("investir", 64.6), "", 32)
hit(W("précipitation", 64.6), 0.8)

# --- S13 · question aux spectateurs
cam(70.3, S13)
headline(S13, 300, ["Quelle question", "te fait [réfléchir] ?"], 70.4, kicker="À ton tour", hl_t=W("réfléchir", 70.3), size=84)
sticker(S13, "baton-pense", 700, 880, 210, 70.7, rot=3)
cta = put(S13, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 70.3) - 0.4, 14)
sfx("click", W("commentaire", 70.3) - 0.4, 0.8)
tag(S13, 70, 900, "Abonne-toi", W("abonne", 70.3), "acc", 48)

# --- fin en boucle
cam(73.9, S1)
bigword("La hâte", W("hâte", 73.9), 1.0, y=1260, size=110)
hit(W("hâte", 73.9), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 8.8), ("02", "Verset", 8.8, 29.8), ("03", "Questions", 29.8, 70.3), ("04", "Action", 70.3, DUR)],
    suppress=[(23.6, 29.7)],
)
