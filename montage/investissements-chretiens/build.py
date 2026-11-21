"""Short « Peut-on faire confiance à tous les investissements chrétiens ? » (1 Thessaloniciens 5.21) — style 02, 9:16, ~70.3 s.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Peut-on faire confiance à tous les investissements chrétiens ?", "lang": "fr"}
COLS, ROWS = 3, 15
s.setup(here=HERE, duration=70.3, cols=COLS, rows=ROWS, theme=THEME)
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
sticker(S1, "panneau-croix-brillant", 20, 650, 600, 0.0, rot=-2, instant=True)
sticker(S1, "baton-recule-prudent", 560, 920, 380, 66.0, rot=3)
headline(S1, 300, ["Placement", "« [chrétien] » ?"], 0.0, kicker="Confiance aveugle ?", hl_t=1.0, size=100)
bigword("Un signal d'alerte", 4.3, 1.0, y=1260, size=88)
hit(4.7, 0.9)

# --- S2 · un mot n'est pas une garantie
cam(7.6, S2)
headline(S2, 280, ["Un mot", "n'est pas une [garantie]"], 7.7, kicker="La réponse est non", hl_t=W("garantie", 7.6), size=84)
sticker(S2, "panneau-croix-brillant", 40, 650, 520, 8.0, rot=-2)
hit(W("garantie", 7.6), 0.9)

# --- S3 · arnaques qui visent les croyants
cam(11.5, S3)
headline(S3, 280, ["Des arnaques", "qui visent les [croyants]"], 11.6, kicker="Attention", hl_t=W("croyants", 11.5), size=78)
sticker(S3, "loup-peau-mouton", 40, 650, 560, 11.9, rot=-2)
tag(S3, 70, 1190, "La foi, des versets, des prières", W("versets", 11.5), "", 32)
tag(S3, 70, 1270, "…pour inspirer confiance", W("confiance", 11.5), "acc", 34)

# --- S4 · le verset (1 Thessaloniciens 5.21) : séquence « Parole »
cam(18.8, S4)
headline(S4, 280, ["[Examiner]", "toutes choses"], 18.9, kicker="Première lettre aux Thessaloniciens", hl_t=W("examinez", 21.5), size=104)
verse = "«&nbsp;" + m(0, "Examinez toutes choses") + " ; " + m(1, "retenez ce qui est bon") + "&#8288;.&nbsp;»"
verse_block(S4, "1 Thessaloniciens 5.21", 20.2, verse, 21.6, [W("examinez", 21.5), W("retenez", 21.5)], size=64, ref_label="1 THESSALONICIENS 5.21")
sticker(S4, "baton-loupe-documents", 60, 1000, 320, 19.3, rot=-3)
sticker(S4, "croix-verte", 600, 1020, 190, 23.0, rot=4)
hit(23.4, 1.0)

# --- S5 · signaux d'alerte
cam(23.8, S5)
headline(S5, 280, ["Cinq signaux", "d'[alerte]"], 23.9, kicker="Voici", hl_t=W("alerte", 23.8), size=104)
counter(S5, 70, 640, 0, 5, 24.2, 0.8, " signaux", 140)
sticker(S5, "drapeau-rouge-garanti", 560, 820, 360, 24.0, rot=3)

# --- S6 · signal 1
cam(25.7, S6)
headline(S6, 280, ["Rendement", "[garanti]"], 25.8, kicker="Signal 1", hl_t=W("garanti", 25.7), size=110)
sticker(S6, "drapeau-rouge-garanti", 40, 650, 460, 26.0, rot=-2)
tag(S6, 70, 1170, "Ou « sans risque »", W("risque", 25.7), "acc", 40)

# --- S7 · signal 2
cam(29.0, S7)
headline(S7, 280, ["La [pression]", "pour décider vite"], 29.1, kicker="Signal 2", hl_t=W("pression", 29.0), size=88)
sticker(S7, "horloge-urgence", 40, 650, 420, 29.3, rot=-2)

# --- S8 · signal 3
cam(31.3, S8)
headline(S8, 280, ["Le [secret]"], 31.4, kicker="Signal 3", hl_t=W("secret", 31.3), size=130)
sticker(S8, "baton-soucieux", 60, 650, 320, 31.6, rot=-2)
tag(S8, 70, 1160, "Refus d'expliquer", W("refus", 31.3), "acc", 40)

# --- S9 · signal 4
cam(34.5, S9)
headline(S9, 280, ["Foi + argent", "[mélangés]"], 34.6, kicker="Signal 4", hl_t=W("mélange", 34.5), size=96)
sticker(S9, "loup-peau-mouton", 40, 650, 560, 34.8, rot=-2)
tag(S9, 70, 1190, "« Dieu veut que tu sois riche »", W("riche", 34.5), "", 32)
tag(S9, 70, 1270, "« Douter, c'est manquer de foi »", W("douter", 34.5), "acc", 32)

# --- S10 · signal 5
cam(40.2, S10)
headline(S10, 280, ["Recruter", "tes [proches]"], 40.3, kicker="Signal 5", hl_t=W("recruter", 40.2), size=104)
sticker(S10, "baton-ami", 60, 650, 320, 40.5, rot=-2)
tag(S10, 70, 1160, "Pour que ça marche", W("marche", 40.2), "acc", 40)

# --- S11 · un seul signal : recule
cam(43.0, S11)
headline(S11, 280, ["Un seul signal :", "[recule]"], 43.1, kicker="Si tu en vois", hl_t=W("recule", 43.0), size=96)
sticker(S11, "baton-recule-prudent", 40, 650, 440, 43.3, rot=-2)
hit(W("recule", 43.0), 0.9)

# --- S12 · trois questions
cam(45.7, S12)
headline(S12, 280, ["Trois", "[questions]"], 45.8, kicker="Ensuite", hl_t=W("questions", 45.7), size=110)
counter(S12, 70, 640, 0, 3, 46.2, 0.8, " questions", 140)
sticker(S12, "baton-loupe-documents", 600, 800, 300, 46.0, rot=3)
tag(S12, 70, 900, "Qui propose ? Vérifiable ?", W("propose", 45.7), "", 34)
tag(S12, 70, 990, "Où va mon argent ? Documents clairs ?", W("documents", 45.7), "", 30)
tag(S12, 70, 1080, "Combien puis-je perdre ?", W("perdre", 45.7), "acc", 34)

# --- S13 · un professionnel indépendant
cam(55.3, S13)
headline(S13, 280, ["Un [professionnel]", "indépendant"], 55.4, kicker="Et demande l'avis d'un", hl_t=W("professionnel", 55.3), size=84)
sticker(S13, "baton-conseiller-pro", 40, 650, 560, 55.6, rot=-2)
tag(S13, 70, 1200, "Il ne gagne rien si tu dis oui", W("gagne", 55.3), "acc", 34)

# --- S14 · le signal numéro un
cam(59.9, S14)
headline(S14, 280, ["Si on te reproche", "tes [questions]"], 60.0, kicker="Le signal numéro un", hl_t=W("reproche", 59.9), size=80)
sticker(S14, "drapeau-rouge-garanti", 40, 650, 440, 60.2, rot=-2)
tag(S14, 70, 1180, "Un bon projet résiste aux questions", W("résiste", 59.9), "acc", 32)
hit(W("reproche", 59.9), 0.9)

# --- S15 · question aux spectateurs
cam(64.8, S15)
headline(S15, 300, ["Quel signal", "est le plus [fréquent] ?"], 64.9, kicker="À ton tour", hl_t=W("fréquent", 64.8), size=84)
sticker(S15, "baton-pense", 700, 880, 210, 65.2, rot=3)
cta = put(S15, 70, 760, CTA, "cta")
blur_in(cta, W("commentaire", 64.8) - 0.4, 14)
sfx("click", W("commentaire", 64.8) - 0.4, 0.8)
tag(S15, 70, 900, "Abonne-toi", W("abonne", 64.8), "acc", 48)

# --- fin en boucle
cam(68.4, S1)
bigword("Examine", W("examine", 67.9), 1.0, y=1260, size=120)
hit(W("examine", 67.9), 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 7.6), ("02", "Verset", 7.6, 23.8), ("03", "Signaux", 23.8, 64.8), ("04", "Action", 64.8, DUR)],
    suppress=[(21.5, 23.7)],
)
