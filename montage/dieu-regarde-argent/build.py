"""Short « Pourquoi Dieu regarde aussi la manière dont tu utilises ton argent » (Matthieu 6.21) — style 02, 9:16, ~85 s.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
Les temps sont calés sur transcript.json (mots de la voix off) via T("mot").
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Dieu regarde ton argent", "lang": "fr"}
s.setup(here=HERE, duration=85.2, cols=3, rows=5, theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# ================================================================ STORY
S1, S2, S3 = (0, 0), (1, 0), (2, 0)
S4, S5, S6 = (2, 1), (1, 1), (0, 1)
S7, S8 = (0, 2), (1, 2)

# --- S1 · 0 – 9.5 · foi et argent séparés ? (personnage, Bible, coffre dès la 1re image)
cam(0, S1)
sticker(S1, "perso-releve-pied", 50, 600, 330, 0.0, rot=-3, instant=True)
sticker(S1, "bible-ouverte", 490, 640, 460, T("foi") - 0.1, rot=3)
sticker(S1, "coffre-pieces", 530, 1060, 330, T("l'argent") - 0.1, rot=-4)
headline(S1, 300, ["Foi et argent :", "[séparés] ?"], 0.0, kicker="Foi · Argent", hl_t=T("deux"), size=100)
hit(T("deux"), 0.7)

# --- S2 · 9.5 – 17.6 · pas le montant : les priorités
cam(9.5, S2)
headline(S2, 280, ["Pas une question", "de [montant]"], T("ce", 1) - 0.2, kicker="Les priorités", hl_t=T("montant"), size=92)
bar_to_scale(S2, 80, 1230, 420, T("montant") - 0.4, width=150, acc=False)
bar_to_scale(S2, 290, 1230, 260, T("montant") - 0.2, width=150, acc=False)
bar_to_scale(S2, 500, 1230, 150, T("montant"), width=150, acc=False)
bar_to_scale(S2, 710, 1230, 330, T("priorité") - 0.2, width=150, acc=True)
tag(S2, 70, 1280, "Tes priorités", T("priorité") + 0.1, "acc", 44)
ref(S2, 70, 1370, "ILLUSTRATION · SANS CHIFFRES RÉELS", T("priorité") + 0.4)
hit(T("argent", 1), 0.8)

# --- S3 · 17.6 – 25.3 · le verset (Mt 6.21) ; sous-titres coupés pendant la citation
cam(17.6, S3)
headline(S3, 280, ["Ton [trésor],", "ton cœur"], T("jésus") - 0.2, kicker="La Parole", hl_t=T("trésor"), size=110)
tag(S3, 70, 600, "Matthieu 6.21", T("matthieu") + 0.1, "acc", 52)
verse = ('« Car là où est ton <em class="hl h1"><span>trésor</span><i></i></em>, '
         'là aussi sera ton <em class="hl h2"><span>cœur</span><i></i></em>. »')
v = put(S3, 70, 710, f'<div class="h" style="font-size:60px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, T("car") - 0.1, 20)
tween(f"#{v} .h1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("trésor"))
tween(f"#{v} .h2 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', T("cœur"))
sticker(S3, "bible-ouverte", 50, 1010, 420, T("matthieu") + 0.5, rot=-3)
sticker(S3, "coffre-pieces", 700, 1030, 240, T("trésor") + 0.1, rot=4)
sticker(S3, "coeur", 500, 1040, 190, T("cœur") + 0.1, rot=-5)
ref(S3, 70, 1420, "MATTHIEU 6.21 · LSG 1910", T("verset") + 0.4)
hit(T("cœur"), 1.0)

# --- S4 · 25.3 – 37.9 · Dieu ne surveille pas pour punir : l'argent suit le cœur
cam(25.2, S4)
headline(S4, 280, ["Pas pour te [punir]"], T("verset", 1) - 0.2, kicker="Ce que le verset dit", hl_t=T("punir"), size=92)
sticker(S4, "coeur", 70, 640, 330, T("réalité") - 0.1, rot=-3)
sticker(S4, "coffre-pieces", 600, 660, 330, T("argent", 2) - 0.1, rot=3)
tag(S4, 70, 1050, "Ton argent suit ton cœur", T("suit") - 0.2, "acc", 36)
tag(S4, 70, 1140, "Ton cœur suit ton argent", T("suit", 1) - 0.2, "", 36)
sticker(S4, "perso-soulage-portrait", 650, 1000, 300, T("piéger") - 0.3, rot=2)
hit(T("taime"), 0.9)

# --- S5 · 37.9 – 52.5 · gérant, pas propriétaire
cam(37.9, S5)
headline(S5, 280, ["Tu es [gérant],", "pas propriétaire"], T("mais") - 0.2, kicker="Une vérité qui change tout", hl_t=T("gérant"), size=92)
sticker(S5, "balance-marchand", 50, 640, 470, T("possèdes") - 0.1, rot=-2)
sticker(S5, "perso-portefeuille-pied", 700, 600, 260, T("gères") - 0.3, rot=3)
tag(S5, 70, 1290, "À quoi cet argent est-il destiné ?", T("demande") - 0.3, "acc", 36)
hit(T("gères"), 0.9)

# --- S6 · 52.5 – 69.3 · l'exercice : trois dépenses, un seul ajustement
cam(52.5, S6)
headline(S6, 280, ["Un petit [exercice]"], T("alors") - 0.2, kicker="Cette semaine", hl_t=T("exercice"), size=92)
boxes(S6, 50, 620, ["1", "2", "3"], T("dépenses") - 0.3, step=300, small="Dépense", cls="day wide")
f2 = put(S6, 230, 840, "Cela reflète-t-il<br>mes priorités ?", "box q")
blur_in(f2, T("reflète") - 0.3, 14)
sx6, sy6 = st(*S6)
arrows = uid()
html.append(f'<svg class="node lead arrows" id="{arrows}" style="left:{sx6}px;top:{sy6}px" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path class="a1" d="M380 994 L240 1142" stroke-dasharray="220"/>'
            f'<path class="a2" d="M700 994 L840 1142" stroke-dasharray="220"/></svg>')
tween(f"#{arrows} .a1, #{arrows} .a2", "strokeDashoffset: 220", 'strokeDashoffset: 0, duration: 0.4, stagger: 0.15', T("réponse") - 0.3)
ok = put(S6, 90, 1150, "<small>Oui</small>Je garde", "box out", "font-size:42px")
no = put(S6, 690, 1150, "<small>Non</small>J'ajuste", "box out", "font-size:42px")
blur_in(ok, T("réponse") + 0.1, 12)
blur_in(no, T("non") - 0.2, 12)
sfx("click", T("non") - 0.2, 0.6)
tag(S6, 70, 1330, "Un seul ajustement", T("choisis") - 0.1, "acc", 38)
hit(T("ajustement"), 0.8)

# --- S7 · 69.3 – 73.6 · un cœur qui apprend
cam(69.3, S7)
headline(S7, 300, ["Un cœur qui", "[apprend]"], T("dieu", 3) - 0.2, kicker="Pas parfait", hl_t=T("apprend"), size=110)
sticker(S7, "perso-serein-pied", 600, 560, 290, T("parfait") - 0.2, rot=2)
sticker(S7, "coeur", 90, 900, 330, T("cœur", 4) - 0.2, rot=-4)
hit(T("apprend"), 0.9)

# --- S8 · 73.6 – 81.6 · mode sombre : la question aux spectateurs
cam(73.6, S8)
dark_mode(73.55)
headline(S8, 430, ["Quelles [dépenses]", "révèlent", "tes priorités ?"], T("toi", 1) - 0.5, kicker="À ton tour", hl_t=T("dépenses", 1), size=96, dark=True)
sticker(S8, "coeur", 640, 1090, 280, T("priorités") - 0.1, rot=4)
cta = put(S8, 70, 920, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, T("commentaire") - 0.5, 14)
sfx("click", T("commentaire") - 0.5, 0.8)

# --- fin · vue d'ensemble puis carte de fin
cam(81.6, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 17.6), ("02", "Verset", 17.6, 37.9), ("03", "Gérant", 37.9, 52.5), ("04", "Action", 52.5, DUR)],
    suppress=[(19.9, 25.3), (82.0, DUR)],     # verset affiché en grand, puis carte de fin : pas de sous-titres
    endcard={"kicker": "Abonne-toi", "title": "Foi et<br />[Finances]", "button": "S'abonner",
             "stickers": [("bible-ouverte", 40, 1190, 400, -5), ("coeur", 760, 1070, 230, 5)]},
    endcard_t=82.2,
)
