"""Short « Pourquoi ton salaire disparaît si rapidement » (Proverbes 27.23) — style 02, 9:16, ~73 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Pourquoi ton salaire disparait", "lang": "fr"}
s.setup(here=HERE, duration=73.5, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8, S9 = (0, 2), (1, 2), (2, 2)
S10 = (2, 3)

# --- S1 · 0 – 6.0 · accroche : compte plein, déjà presque vide
cam(0, S1)
sticker(S1, "perso-surpris-pied", 60, 600, 330, 0.0, rot=-2, instant=True)
sticker(S1, "telephone-abonnements", 560, 650, 260, T("vide") - 0.1, rot=3)
headline(S1, 300, ["Où part ton", "[salaire] ?"], 0.0, kicker="Plein au début, vide déjà ?", hl_t=T("vide"), size=104)
tag(S1, 400, 1180, "Pas toujours trop peu", T("toujours") - 0.1, "acc", 34)
hit(T("vide"), 0.8)

# --- S2 · 6.0 – 11.8 · trois raisons ; raison 1 : tu ne sais pas où va ton argent
cam(6.0, S2)
headline(S2, 280, ["Trois [raisons]", "très courantes"], T("voici") - 0.2, kicker="À connaître", hl_t=T("raisons"), size=100)
boxes(S2, 50, 640, ["1", "2", "3"], T("trois") + 0.1, step=300, small="Raison", cls="day wide")
tag(S2, 70, 900, "Tu ne sais pas où va ton argent", T("première") - 0.1, "acc", 40)
sticker(S2, "perso-fatigue-portrait", 600, 1000, 300, T("première") + 0.3, rot=3)
hit(T("première"), 0.7)

# --- S3 · 11.8 – 19.0 · le verset (Pr 27.23) ; sous-titres coupés pendant la citation
cam(11.8, S3)
headline(S3, 280, ["Connaître", "ton [troupeau]"], T("bible") - 0.2, kicker="La Parole", hl_t=T("troupeaux"), size=104)
tag(S3, 70, 600, "Proverbes 27.23", T("bible") + 0.3, "acc", 52)
verse = ('« Connais bien l\'état de tes <em class="hl h1"><span>brebis</span><i></i></em>, '
         'donne tes soins à tes <em class="hl h2"><span>troupeaux</span><i></i></em>. »')
v = put(S3, 70, 710, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("connais") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("brebis"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("troupeaux"))
sticker(S3, "page-bible-enluminee", 70, 1000, 220, T("connais") + 0.4, rot=-3)
sticker(S3, "troupeau", 400, 1060, 400, T("troupeaux") + 0.1, rot=3)
ref(S3, 70, 1420, "PROVERBES 27.23 · LSG 1910", T("verset") + 0.4)
hit(T("troupeaux"), 1.0)

# --- S4 · 19.0 – 24.0 · un berger sait compter ses brebis
cam(18.9, S4)
headline(S4, 280, ["Un berger", "[compte] ses brebis"], T("berger") - 0.5, kicker="Une image", hl_t=T("compter"), size=90)
sticker(S4, "brebis", 60, 650, 380, T("brebis", 1) - 0.2, rot=-3)
sticker(S4, "perso-compte-pied", 620, 620, 260, T("sais-tu") - 0.2, rot=3)
tag(S4, 70, 1100, "Où partent tes dépenses ?", T("partent") - 0.3, "acc", 38)
hit(T("sais-tu"), 0.7)

# --- S5 · 24.0 – 36.3 · raison 2 : les petites fuites
cam(24.0, S5)
headline(S5, 280, ["Les petites", "[fuites]"], T("deuxième") - 0.2, kicker="Raison n°2", hl_t=T("fuites"), size=110)
sticker(S5, "telephone-abonnements", 50, 640, 200, T("abonnement") - 0.1, rot=-3)
label_box(S5, 50, 1000, "Abonnement<br>oublié", None, T("abonnement") + 0.2)
sticker(S5, "robinet-goutte", 300, 650, 230, T("achat") - 0.1, rot=3)
label_box(S5, 300, 1000, "Achat sur un<br>coup de tête", None, T("achat") + 0.2)
sticker(S5, "seau-perce", 620, 620, 260, T("livraison") - 0.1, rot=-3)
label_box(S5, 620, 1040, "Livraison<br>de trop", None, T("livraison") + 0.2)
tag(S5, 70, 1160, "Elles vident le réservoir", T("réservoir") - 0.4, "acc", 36)
hit(T("réservoir"), 0.9)

# --- S6 · 36.3 – 41.7 · raison 3 : épargner ce qui reste
cam(36.3, S6)
headline(S6, 280, ["Épargner", "ce qui [reste]"], T("troisième") - 0.2, kicker="Raison n°3", hl_t=T("reste"), size=104)
sticker(S6, "enveloppe-salaire", 60, 660, 440, T("épargnes") - 0.1, rot=-3)
tag(S6, 70, 1100, "Il ne reste presque rien", T("reste", 1) - 0.3, "acc", 40)
hit(T("rien"), 0.8)

# --- S7 · 41.7 – 47.5 · fais l'inverse : d'abord toi (schéma)
cam(41.7, S7)
headline(S7, 280, ["Fais", "[l'inverse]"], T("alors") - 0.2, kicker="D'abord toi", hl_t=T("linverse"), size=110)
f1 = put(S7, 290, 620, "Dès que ton<br>salaire arrive", "box")
blur_in(f1, T("dès") - 0.1, 14)
f2 = put(S7, 230, 860, "Mets de côté<br>un petit montant", "box q")
blur_in(f2, T("mets") - 0.2, 14)
f3 = put(S7, 290, 1100, "Avant toute<br>dépense", "box")
blur_in(f3, T("avant") - 0.1, 14)
sx7, sy7 = st(*S7)
arrows = uid()
html.append(f'<svg class="node lead arrows" id="{arrows}" style="left:{sx7}px;top:{sy7}px" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path class="a0" d="M540 748 L540 852" stroke-dasharray="110"/>'
            f'<path class="a1" d="M540 990 L540 1092" stroke-dasharray="110"/></svg>')
tween(f"#{arrows} .a0", "strokeDashoffset: 110", 'strokeDashoffset: 0, duration: 0.3', T("dès") + 0.3)
tween(f"#{arrows} .a1", "strokeDashoffset: 110", 'strokeDashoffset: 0, duration: 0.3', T("avant") - 0.2)
hit(T("avant"), 0.8)

# --- S8 · 47.5 – 56.7 · l'exercice de la semaine
cam(47.5, S8)
headline(S8, 280, ["Cette semaine,", "trois [gestes]"], T("cette") - 0.2, kicker="Exercice", hl_t=T("fuite", 1), size=96)
boxes(S8, 50, 620, ["1", "2", "3"], T("regarde") - 0.3, step=300, small="Étape", cls="day wide")
label_box(S8, 60, 800, "Regarde tes<br>trois relevés", None, T("relevés") - 0.2)
label_box(S8, 360, 800, "Repère une<br>fuite, ferme-la", None, T("repère") - 0.1)
label_box(S8, 660, 800, "Choisis un<br>petit montant", None, T("choisis") - 0.1)
sticker(S8, "perso-robinet-pied", 400, 920, 300, T("ferme-la") - 0.3, rot=-2)
hit(T("ferme-la"), 0.8)

# --- S9 · 56.7 – 63.5 · régularité ; un berger fidèle prend soin de son troupeau
cam(56.7, S9)
headline(S9, 280, ["Pas le montant :", "la [régularité]"], T("ce", 2) - 0.2, kicker="Ce qui compte", hl_t=T("régularité"), size=92)
sticker(S9, "troupeau", 60, 640, 460, T("berger", 1) - 0.1, rot=-3)
sticker(S9, "perso-enveloppe-pied", 640, 620, 250, T("régularité") - 0.3, rot=3)
tag(S9, 70, 1120, "Même avec peu", T("peu", 1) - 0.3, "acc", 44)
hit(T("troupeau"), 0.8)

# --- S10 · 63.5 – 69.9 · mode sombre : la question aux spectateurs
cam(63.5, S10)
dark_mode(63.45)
headline(S10, 430, ["Quelle [fuite]", "vas-tu fermer", "en premier ?"], T("quelle") - 0.2, kicker="À ton tour", hl_t=T("fuite", 2), size=96, dark=True)
sticker(S10, "robinet-goutte", 680, 1000, 220, T("fermer") - 0.1, rot=3)
cta = put(S10, 70, 900, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(69.9, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 11.8), ("02", "Verset", 11.8, 24.0), ("03", "Fuites", 24.0, 47.5), ("04", "Action", 47.5, DUR)],
    suppress=[(12.6, 18.9), (70.4, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("troupeau", 40, 1190, 420, -4), ("perso-serein-portrait", 760, 1050, 260, 5)]},
    endcard_t=70.5,
)
