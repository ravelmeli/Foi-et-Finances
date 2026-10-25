"""Short « 3 erreurs financières que les couples chrétiens doivent éviter » (Amos 3.3) — style 02, 9:16, ~71 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - 3 erreurs financieres couples", "lang": "fr"}
s.setup(here=HERE, duration=71.0, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8 = (0, 2), (1, 2)

# --- S1 · 0 – 9.4 · accroche : le couple dos à dos est à l'écran dès la 1re image
cam(0, S1)
sticker(S1, "couple-dos-a-dos", 60, 600, 330, 0.0, rot=-3, instant=True)
sticker(S1, "bulles-dialogue", 500, 700, 440, T("parlent") - 0.1, rot=4)
headline(S1, 300, ["Parler d'argent", "en [couple]"], 0.0, kicker="Couples chrétiens · Argent", hl_t=T("parlent"), size=100)
tag(S1, 470, 1240, "3 erreurs à éviter", T("trois") - 0.1, "acc", 44)
hit(T("trois"), 0.9)

# --- S2 · 9.4 – 20.9 · erreur n°1 : les secrets d'argent
cam(9.4, S2)
headline(S2, 280, ["Garder des [secrets]", "d'argent"], T("première") - 0.3, kicker="Erreur n°1", hl_t=T("secrets"), size=88)
sticker(S2, "sac-cache", 60, 600, 250, T("dépense") - 0.1, rot=-4)
label_box(S2, 60, 990, "Dépense<br>cachée", None, T("dépense") + 0.2)
sticker(S2, "enveloppe-scellee", 380, 650, 280, T("dette") - 0.1, rot=3)
label_box(S2, 380, 990, "Dette<br>non avouée", None, T("dette") + 0.2)
sticker(S2, "carte-bancaire", 700, 650, 280, T("compte") - 0.1, rot=-3)
label_box(S2, 700, 990, "Compte<br>ignoré", None, T("compte") + 0.2)
tag(S2, 70, 1250, "Une question de confiance", T("question", 1) - 0.1, "acc", 40)
hit(T("confiance"), 1.0)

# --- S3 · 20.9 – 26.0 · le verset (Amos 3.3) ; sous-titres coupés pendant la citation
cam(20.9, S3)
headline(S3, 280, ["Marcher", "[ensemble]"], T("amos") - 0.2, kicker="La Parole", hl_t=T("ensemble"), size=110)
tag(S3, 70, 590, "Amos 3.3", T("amos") + 0.1, "acc", 52)
verse = '« Deux hommes marchent-ils <em class="hl h1"><span>ensemble</span><i></i></em>, sans en être convenus&nbsp;? »'
v = put(S3, 70, 710, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("deux") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("ensemble"))
sticker(S3, "couple-main-dans-la-main", 390, 960, 300, T("ensemble") + 0.2, rot=3)
ref(S3, 70, 1000, "AMOS 3.3 · LSG 1910", T("verset") + 0.3)
hit(T("convenus"), 1.0)

# --- S4 · 26.0 – 37.5 · erreur n°2 : pas de budget commun
cam(26.0, S4)
headline(S4, 280, ["Pas de [budget]", "commun"], T("deuxième") - 0.2, kicker="Erreur n°2", hl_t=T("budget"), size=100)
sticker(S4, "deux-portefeuilles", 60, 620, 460, T("chacun") - 0.1, rot=-2)
label_box(S4, 60, 850, "Chacun", "de son côté", T("chacun") + 0.3)
b1 = put(S4, 90, 960, "<small>Ce qui</small>entre", "box out", "font-size:52px")
b2 = put(S4, 610, 960, "<small>Ce qui</small>sort", "box out", "font-size:52px")
blur_in(b1, T("entre") - 0.3, 12)
blur_in(b2, T("sort") - 0.3, 12)
sfx("click", T("entre") - 0.3, 0.6)
sticker(S4, "carnet-budget", 60, 1170, 220, T("asseyez-vous") - 0.1, rot=-3)
sticker(S4, "calculatrice", 320, 1180, 160, T("asseyez-vous") + 0.2, rot=3)
tag(S4, 480, 1260, "Une fois par mois", T("mois") - 0.2, "acc", 36)
hit(T("sort"), 0.9)

# --- S5 · 37.5 – 48.1 · erreur n°3 : décider seul des grandes dépenses
cam(37.5, S5)
headline(S5, 280, ["Décider [seul]"], T("troisième") - 0.2, kicker="Erreur n°3", hl_t=T("seul"), size=110)
sticker(S5, "cle-maison", 50, 620, 240, T("achat") - 0.1, rot=-4)
label_box(S5, 50, 920, "Un achat<br>important", None, T("achat") + 0.2)
sticker(S5, "contrat-stylo", 390, 610, 250, T("prêt") - 0.1, rot=3)
label_box(S5, 390, 920, "Un prêt", None, T("prêt") + 0.2)
sticker(S5, "cartons-demenagement", 730, 610, 230, T("déménagement") - 0.1, rot=-3)
label_box(S5, 730, 920, "Un<br>déménagement", None, T("déménagement") + 0.2)
sticker(S5, "elle-surprise-portrait", 60, 1040, 240, T("découvre") - 0.1, rot=-2)
tag(S5, 340, 1200, "La blessure s'installe", T("blessure") - 0.2, "acc", 38)
hit(T("blessure"), 0.9)

# --- S6 · 48.1 – 57.2 · la règle simple (schéma de décision) + l'aide d'un conseiller
cam(48.1, S6)
headline(S6, 280, ["Une [règle] simple"], T("règle") - 0.5, kicker="À mettre en place", hl_t=T("règle"), size=96)
f1 = put(S6, 290, 620, "Montant fixé<br>ensemble", "box")
blur_in(f1, T("montant") - 0.3, 14)
f2 = put(S6, 230, 860, "On en parle<br>avant de payer", "box q")
blur_in(f2, T("parle") - 0.2, 14)
f3 = put(S6, 290, 1100, "Puis on paie", "box")
blur_in(f3, T("payer") - 0.1, 14)
sx6, sy6 = st(*S6)
arrows = uid()
html.append(f'<svg class="node lead arrows" id="{arrows}" style="left:{sx6}px;top:{sy6}px" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path class="a0" d="M540 748 L540 852" stroke-dasharray="110"/>'
            f'<path class="a1" d="M540 990 L540 1092" stroke-dasharray="110"/></svg>')
tween(f"#{arrows} .a0", "strokeDashoffset: 110", 'strokeDashoffset: 0, duration: 0.3', T("parle") - 0.4)
tween(f"#{arrows} .a1", "strokeDashoffset: 110", 'strokeDashoffset: 0, duration: 0.3', T("payer") - 0.3)
tag(S6, 70, 1300, "Un conseiller ou un pasteur peut aider", T("conseiller") - 0.4, "", 34)
hit(T("payer"), 0.8)

# --- S7 · 57.2 – 61.1 · le silence divise, pas l'argent
cam(57.2, S7)
headline(S7, 300, ["Parler d'argent", "ne divise pas", "un couple"], T("parler") - 0.2, kicker="La vérité", size=92)
tag(S7, 70, 700, "C'est le silence qui divise", T("silence") - 0.4, "acc", 44)
sticker(S7, "couple-souriant-portrait", 240, 800, 600, T("silence") + 0.2, rot=-2)
hit(T("silence"), 1.0)

# --- S8 · 61.1 – 67.5 · mode sombre : la question aux spectateurs
cam(61.0, S8)
dark_mode(60.95)
headline(S8, 430, ["Quelle [erreur]", "est la plus", "difficile pour", "votre couple ?"], T("quelle") - 0.2, kicker="À votre tour", hl_t=T("erreur", 3), size=92, dark=True)
sticker(S8, "bulles-dialogue", 640, 1130, 300, T("dites-le") - 0.1, rot=3)
cta = put(S8, 70, 1000, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(67.5, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 9.4), ("02", "Secrets", 9.4, 26.0), ("03", "Budget", 26.0, 37.5), ("04", "Décisions", 37.5, DUR)],
    suppress=[(23.0, 26.0), (68.0, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("cle-maison", 40, 1180, 300, -6), ("couple-souriant-portrait", 700, 1040, 330, 4)]},
    endcard_t=68.1,
)
