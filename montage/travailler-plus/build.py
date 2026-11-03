"""Short « Pourquoi travailler plus ne suffit pas toujours pour s'enrichir » (Psaume 127.1) — style 02, 9:16, ~73 s.
Acquis des Shorts et longues : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte (la raison n°4) refermée, fin qui revient sur la première image. Temps lus dans transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Travailler plus ne suffit pas", "lang": "fr"}
COLS, ROWS = 3, 6
s.setup(here=HERE, duration=73.4, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S = ST[:17]
(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17) = S


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "baton-heures-sup", 30, 640, 520, 0.0, rot=-2, instant=True)
sticker(S1, "portefeuille-troue", 680, 700, 270, 1.8, rot=3)
headline(S1, 300, ["Plus de travail…", "[pas] plus riche ?"], 0.0, kicker="Tu travailles de plus en plus", hl_t=2.7, size=96)
bigword("Pas riche ?", 2.9, 0.8, y=1270, size=120)
hit(3.0, 0.9)

# --- S2 · boucle ouverte : la raison n°4
cam(3.3, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 3.4, kicker="La raison n°4", hl_t=4.4, size=104)
q = put(S2, 230, 640, "<small>Raison</small>4 ?", "box out", "width:620px;font-size:120px")
blur_in(q, 5.6, 12)
tag(S2, 70, 960, "Celle qu'on oublie le plus", 6.3, "acc", 36)
sticker(S2, "baton-pense", 680, 800, 230, 4.6, rot=3)
hit(5.6, 0.8)

# --- S3 · le verset (Psaume 127.1) : séquence « Parole » ; sous-titres coupés pendant la citation
cam(7.6, S3)
headline(S3, 280, ["Travailler", "en [vain] ?"], 7.7, kicker="Psaume 127", hl_t=13.1, size=104)
tag(S3, 70, 600, "Psaume 127.1", 9.5, "acc", 52)
sfx("spark", 9.5, 1.6)
verse = ("«&nbsp;Si l'Éternel " + m(0, "ne bâtit la maison") + ", ceux qui la bâtissent " + m(1, "travaillent en vain") + ".&nbsp;»")
v = put(S3, 70, 710, f'<div class="h" style="font-size:58px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, 10.0, 20)
tween(f"#{v} .m0 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 11.0)
tween(f"#{v} .m1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 12.7)
sticker(S3, "chantier-plan", 60, 1030, 400, 7.9, rot=-2)
sticker(S3, "livre-croix-ouvert", 580, 1110, 330, 9.8, rot=3)
ref(S3, 70, 1420, "PSAUME 127.1 · LSG 1910", 9.9)
hit(13.4, 1.0)

# --- S4 · ce verset ne dit pas de travailler moins
cam(14.3, S4)
headline(S4, 280, ["Le travail", "est [honoré]"], 14.4, kicker="Attention", hl_t=17.4, size=104)
sticker(S4, "baton-travaille", 60, 640, 330, 14.9, rot=-2)
sticker(S4, "livre-croix-ouvert", 520, 700, 380, 17.0, rot=3)
tag(S4, 70, 1130, "Pas moins de travail", 15.8, "acc", 42)
hit(16.4, 0.7)

# --- S5 · l'effort seul ne suffit pas : il lui faut une direction
cam(18.5, S5)
headline(S5, 280, ["L'effort", "ne suffit [pas]"], 18.6, kicker="Il lui faut", hl_t=20.3, size=104)
sticker(S5, "baton-carte-boussole", 60, 640, 330, 19.4, rot=-2)
sticker(S5, "tapis-roulant-pieces", 540, 720, 380, 20.0, rot=3)
tag(S5, 70, 1160, "Une direction", 21.3, "acc", 52)
hit(21.5, 0.8)

# --- S6 · quatre raisons
cam(22.5, S6)
headline(S6, 280, ["Quatre", "[raisons]"], 22.6, kicker="Travailler plus ne suffit pas", hl_t=23.4, size=110)
counter(S6, 70, 640, 0, 4, 23.0, 0.8, " raisons", 150)
sticker(S6, "baton-tapis-roulant", 560, 840, 330, 24.4, rot=2)
hit(25.4, 0.7)

# --- S7 · raison 1 : les dépenses suivent le salaire
cam(25.8, S7)
headline(S7, 280, ["Dépenses", "= [salaire]"], 25.9, kicker="Raison 1", hl_t=28.2, size=104)
sticker(S7, "enveloppe-salaire", 60, 650, 340, 26.6, rot=-3)
sticker(S7, "pile-factures", 560, 700, 340, 28.8, rot=3)
tag(S7, 70, 1060, "Aussi vite que ton salaire", 27.7, "", 36)
tag(S7, 70, 1150, "Il ne reste rien", 30.8, "acc", 42)
hit(31.1, 0.8)

# --- S8 · raison 2 : pas de plan
cam(31.4, S8)
headline(S8, 280, ["Pas de", "[plan]"], 31.5, kicker="Raison 2", hl_t=32.8, size=110)
sticker(S8, "seau-perce", 60, 650, 300, 33.0, rot=-3)
sticker(S8, "portefeuille-troue", 620, 700, 300, 34.4, rot=3)
tag(S8, 70, 1200, "Mille petits trous", 35.3, "acc", 42)
hit(35.6, 0.8)

# --- S9 · raison 3 : toujours la même chose
cam(35.8, S9)
headline(S9, 280, ["Toujours la", "même [chose]"], 35.9, kicker="Raison 3", hl_t=37.8, size=104)
sticker(S9, "tapis-roulant-pieces", 60, 660, 420, 36.6, rot=-2)
sticker(S9, "calendrier-mois", 620, 700, 300, 38.0, rot=3)
tag(S9, 70, 1100, "Sans nouvelle compétence", 38.7, "", 38)
tag(S9, 70, 1190, "Ton revenu stagne", 39.9, "acc", 42)
hit(40.1, 0.7)

# --- S10 · raison 4 : tu ne sais plus pourquoi (referme la boucle ouverte)
cam(40.4, S10)
headline(S10, 280, ["Pour[quoi]", "tu travailles ?"], 40.5, kicker="Raison 4 · celle qu'on oublie", hl_t=42.0, size=96)
sticker(S10, "baton-soucieux", 60, 640, 260, 41.2, rot=-2)
sticker(S10, "baton-sablier", 600, 700, 280, 44.2, rot=3)
tag(S10, 70, 1130, "Sans but : jamais assez", 43.2, "acc", 38)
bigword("Pourquoi ?", 42.0, 0.9, y=1270, size=110)
hit(42.4, 0.9)

# --- S11 · alors, que faire ?
cam(45.9, S11)
headline(S11, 280, ["Alors,", "que [faire] ?"], 46.0, kicker="Trois remèdes", hl_t=46.9, size=110)
sticker(S11, "baton-pense", 60, 660, 260, 46.3, rot=-2)
sticker(S11, "colombe", 600, 720, 300, 47.0, rot=3)

# --- S12 · remède 1 : un but pour chaque euro
cam(47.5, S12)
headline(S12, 280, ["Un but pour", "chaque [euro]"], 47.6, kicker="Remède 1", hl_t=49.4, size=100)
sticker(S12, "enveloppes-budget", 60, 650, 340, 48.3, rot=-3)
sticker(S12, "baton-budget", 600, 640, 330, 49.0, rot=3)
tag(S12, 70, 1200, "Avant qu'il n'arrive", 50.2, "acc", 38)
hit(50.4, 0.7)

# --- S13 · remède 2 : un plan simple
cam(50.8, S13)
headline(S13, 280, ["Un plan", "[simple]"], 50.9, kicker="Remède 2", hl_t=52.3, size=110)
sticker(S13, "baton-carte-boussole", 60, 650, 340, 51.6, rot=-2)
sticker(S13, "calendrier-mois", 620, 700, 280, 53.2, rot=3)
counter(S13, 70, 1200, 0, 20, 53.0, 0.9, " min", 110)
hit(53.8, 0.7)

# --- S14 · remède 3 : une compétence
cam(54.4, S14)
headline(S14, 280, ["Une [compétence]", "en plus"], 54.5, kicker="Remède 3", hl_t=56.0, size=96)
sticker(S14, "echelle-competences", 60, 640, 330, 55.4, rot=-2)
sticker(S14, "graphique-hausse", 620, 700, 330, 57.0, rot=3)
tag(S14, 70, 1190, "Ta valeur augmente", 57.0, "acc", 40)
hit(57.3, 0.7)

# --- S15 · confier son travail à Dieu
cam(57.6, S15)
headline(S15, 280, ["Confie ton", "[travail]"], 57.7, kicker="Chaque matin", hl_t=59.3, size=104)
sticker(S15, "baton-matin-priere", 40, 640, 520, 58.0, rot=-2)
sfx("spark", 59.6, 1.2)
tag(S15, 70, 1160, "Avant de commencer", 60.1, "acc", 42)
hit(60.3, 0.8)

# --- S16 · dur, c'est bien ; avec sagesse, c'est mieux
cam(61.2, S16)
headline(S16, 280, ["Travailler dur,", "c'est [bien]"], 61.3, kicker="Mais", hl_t=62.2, size=104)
sticker(S16, "baton-content", 60, 640, 300, 61.6, rot=-2)
sticker(S16, "soleil-nuage", 620, 700, 320, 63.8, rot=3)
tag(S16, 70, 1180, "Avec sagesse, c'est mieux", 62.9, "acc", 40)
hit(64.1, 0.8)

# --- S17 · question aux spectateurs
cam(64.4, S17)
headline(S17, 300, ["Où perds-tu", "[de l'argent] ?"], 64.5, kicker="À ton tour", hl_t=66.4, size=104)
sticker(S17, "baton-serein", 700, 880, 210, 65.0, rot=3)
cta = put(S17, 70, 760, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 67.6, 14)
sfx("click", 67.6, 0.8)
tag(S17, 70, 900, "Abonne-toi", 68.2, "acc", 48)

# --- fin en boucle : retour sur l'image d'ouverture
cam(68.7, S1)
bigword("La direction", 71.5, 0.9, y=1270, size=110)
hit(71.9, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 7.6), ("02", "Verset", 7.6, 22.5), ("03", "Raisons", 22.5, 45.9), ("04", "Remèdes", 45.9, DUR)],
    suppress=[(9.95, 14.0)],
)
