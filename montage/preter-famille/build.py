"""Short « Faut-il prêter de l'argent à sa famille ? » (Luc 6.35) — style 02, 9:16, ~86.3 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Faut-il prêter de l'argent à sa famille ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=86.3, cols=COLS, rows=ROWS, theme=THEME)
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
sticker(S1, "baton-frere-demande", 20, 650, 620, 0.0, rot=-2, instant=True)
sticker(S1, "table-famille-paix", 480, 940, 520, 83.0, rot=3)
headline(S1, 300, ["Prêter à ta", "[famille] ?"], 0.0, kicker="Ton frère te demande de l'argent", hl_t=1.0, size=104)
bigword("Une règle simple", 4.0, 1.0, y=1260, size=96)
hit(4.4, 0.9)

# --- S2 · le verset (Luc 6.35) : séquence « Parole »
cam(8.5, S2)
headline(S2, 280, ["Faire du", "[bien]"], 8.6, kicker="Évangile de Luc", hl_t=W("bien", 13.2), size=110)
verse = "«&nbsp;" + m(0, "Faites du bien") + ", et " + m(1, "prêtez sans rien espérer") + "&#8288;.&nbsp;»"
verse_block(S2, "Luc 6.35", 11.2, verse, 13.3, [W("faites", 13.2), W("prêtez", 13.2)], size=64, ref_label="LUC 6.35")
sticker(S2, "livre-croix-ouvert", 60, 1000, 360, 9.0, rot=-3)
sticker(S2, "croix-verte", 600, 1020, 190, 15.0, rot=4)
hit(15.7, 1.0)

# --- S3 · pas sans réfléchir
cam(16.1, S3)
headline(S3, 280, ["Pas sans", "[réfléchir]"], 16.2, kicker="Attention", hl_t=W("réfléchir", 16.1), size=110)
sticker(S3, "baton-pense", 60, 650, 320, 16.5, rot=-2)
tag(S3, 70, 1160, "Aider ta famille : c'est beau", W("beau", 16.1), "", 38)
hit(W("réfléchir", 16.1), 0.8)

# --- S4 · des prêts qui finissent mal
cam(22.2, S4)
headline(S4, 280, ["Souvent, ça", "finit [mal]"], 22.3, kicker="Beaucoup de prêts", hl_t=W("mal", 22.2), size=110)
sticker(S4, "balance-argent-lien", 40, 650, 540, 22.6, rot=-2)
tag(S4, 70, 1190, "L'argent n'est pas rendu", W("rendu", 22.2), "", 36)
tag(S4, 70, 1270, "La gêne s'installe", W("gêne", 22.2), "", 36)
tag(S4, 70, 1350, "La relation en souffre", W("souffre", 22.2), "acc", 36)

# --- S5 · la règle
cam(28.5, S5)
headline(S5, 280, ["La [règle]"], 28.6, kicker="Voici", hl_t=W("règle", 28.5), size=130)
sticker(S5, "baton-ne-jamais-revoir", 40, 650, 480, 28.9, rot=-2)
tag(S5, 70, 1170, "Ne prête que ce que tu peux", W("peux", 28.5), "", 34)
tag(S5, 70, 1250, "te permettre de ne jamais revoir", W("jamais", 28.5), "acc", 34)
hit(W("jamais", 28.5), 0.9)

# --- S6 · si tu ne peux pas perdre cette somme
cam(33.3, S6)
headline(S6, 280, ["Perdre cette somme", "sans [souffrir] ?"], 33.4, kicker="Si tu ne peux pas", hl_t=W("souffrir", 33.3), size=84)
sticker(S6, "baton-soucieux", 60, 650, 320, 33.7, rot=-2)
tag(S6, 70, 1160, "Ne la prête pas", W("prête", 33.3), "acc", 44)

# --- S7 · prêt ou don ?
cam(36.8, S7)
headline(S7, 280, ["Prêt… ou", "[don] ?"], 36.9, kicker="Demande-toi", hl_t=W("don", 36.8), size=120)
sticker(S7, "baton-donne", 40, 650, 420, 37.2, rot=-2)
tag(S7, 70, 1170, "Une petite somme donnée", W("petite", 36.8), "", 34)
tag(S7, 70, 1250, "plutôt qu'une grosse prêtée", W("grosse", 36.8), "acc", 34)

# --- S8 · protège la relation
cam(45.2, S8)
headline(S8, 280, ["Protège la", "[relation]"], 45.3, kicker="Ensuite", hl_t=W("relation", 45.2), size=110)
sticker(S8, "table-famille-paix", 40, 650, 560, 45.5, rot=-2)
hit(W("relation", 45.2), 0.8)

# --- S9 · par écrit
cam(47.0, S9)
headline(S9, 280, ["Mets-le", "par [écrit]"], 47.1, kicker="Les choses claires", hl_t=W("écrit", 47.0), size=110)
sticker(S9, "papier-accord", 40, 650, 420, 47.4, rot=-2)
tag(S9, 70, 1170, "Le montant", W("montant", 47.0), "", 38)
tag(S9, 70, 1250, "Les dates", W("dates", 47.0), "", 38)
tag(S9, 70, 1330, "Du respect, pas de la méfiance", W("respect", 47.0), "acc", 32)

# --- S10 · parle ouvertement
cam(54.7, S10)
headline(S10, 280, ["Parle", "[ouvertement]"], 54.8, kicker="Sans humiliation", hl_t=W("ouvertement", 54.7), size=100)
sticker(S10, "baton-frere-demande", 40, 650, 480, 55.0, rot=-2)

# --- S11 · ne t'endette jamais
cam(57.1, S11)
headline(S11, 280, ["Jamais", "t'[endetter]"], 57.2, kicker="Pour prêter", hl_t=W("endette", 57.1), size=110)
sticker(S11, "baton-fardeau", 60, 650, 320, 57.4, rot=-2)
tag(S11, 70, 1160, "Ni chantage affectif", W("chantage", 57.1), "acc", 38)
hit(W("endette", 57.1), 0.8)

# --- S12 · aider autrement
cam(61.6, S12)
headline(S12, 280, ["Aider", "[autrement]"], 61.7, kicker="Tu peux aussi", hl_t=W("autrement", 61.6), size=110)
sticker(S12, "sac-courses-aide", 40, 650, 440, 61.9, rot=-2)
tag(S12, 70, 1170, "Régler une facture", W("facture", 61.6), "", 36)
tag(S12, 70, 1250, "Faire des courses", W("courses", 61.6), "", 36)
tag(S12, 70, 1330, "Du temps, un conseil", W("temps", 61.6), "acc", 36)

# --- S13 · se relever ou retarder
cam(67.4, S13)
headline(S13, 280, ["Se relever,", "ou [retarder] ?"], 67.5, kicker="La vraie question", hl_t=W("retarder", 67.4), size=100)
sticker(S13, "baton-tiraille", 60, 650, 320, 67.7, rot=-2)
hit(W("retarder", 67.4), 0.9)

# --- S14 · prie, décide avec ton conjoint
cam(73.3, S14)
headline(S14, 280, ["Prie, décide", "avec ton [conjoint]"], 73.4, kicker="Avant de répondre", hl_t=W("conjoint", 73.3), size=88)
sticker(S14, "couple-budget", 40, 650, 460, 73.7, rot=-2)
tag(S14, 70, 1190, "Reste doux, même si tu dis non", W("doux", 73.3), "acc", 34)

# --- S15 · question aux spectateurs
cam(78.3, S15)
headline(S15, 300, ["As-tu déjà", "[prêté] ?"], 78.4, kicker="À ton tour", hl_t=W("prêté", 78.3), size=110)
sticker(S15, "baton-pense", 700, 880, 210, 78.7, rot=3)
cta = put(S15, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 78.3) - 0.4, 14)
sfx("click", W("commentaire", 78.3) - 0.4, 0.8)
tag(S15, 70, 900, "Abonne-toi", W("abonne", 78.3), "acc", 48)

# --- fin en boucle
cam(82.8, S1)
bigword("Sans danger", W("danger", 82.8), 1.0, y=1260, size=110)
hit(W("danger", 82.8), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 8.5), ("02", "Verset", 8.5, 22.2), ("03", "Règle", 22.2, 61.6), ("04", "Action", 61.6, DUR)],
    suppress=[(13.2, 16.0)],
)
