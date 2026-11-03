"""Short « La parabole des talents expliquée avec ton argent » (Matthieu 25.21) — style 02, 9:16, ~92 s.
Acquis des Shorts et longues : mots géants, compteurs, séquence « verset » identique (sous-titres coupés, espaces insécables),
boucle ouverte (« il n'a pas perdu un euro et pourtant il a tout perdu ») refermée, fin qui revient sur la première image.
Le maître est toujours dessiné de dos (aucun visage de Dieu ou de Jésus). Temps lus dans transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - La parabole des talents", "lang": "fr"}
COLS, ROWS = 3, 6
s.setup(here=HERE, duration=91.9, cols=COLS, rows=ROWS, theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18 = ST


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


# --- S1 · accroche (aussi l'image de fin : la vidéo boucle)
cam(0, S1)
sticker(S1, "maitre-confie", 30, 640, 560, 0.0, rot=-2, instant=True)
sticker(S1, "trois-sacs", 650, 780, 260, 2.8, rot=3)
headline(S1, 300, ["Trois serviteurs,", "ton [argent]"], 0.0, kicker="Un maître part en voyage", hl_t=2.3, size=96)
bigword("Un test ?", 5.2, 0.9, y=1250, size=120)
hit(5.3, 0.9)

# --- S2 · boucle ouverte : celui qui n'a rien perdu
cam(7.7, S2)
headline(S2, 280, ["Reste jusqu'au", "[bout]"], 7.8, kicker="L'un des trois", hl_t=8.5, size=104)
q = put(S2, 190, 640, "<small>Euros perdus</small>0", "box out", "width:700px;font-size:130px")
blur_in(q, 10.2, 12)
sticker(S2, "baton-pense", 680, 860, 230, 8.8, rot=3)
tag(S2, 70, 1000, "Pourtant, il a tout perdu", 11.0, "acc", 36)
hit(11.8, 0.8)

# --- S3 · la parabole (Matthieu 25)
cam(12.2, S3)
headline(S3, 280, ["La parabole", "des [talents]"], 12.3, kicker="Évangile de Matthieu", hl_t=13.5, size=104)
sticker(S3, "maitre-confie", 40, 640, 540, 12.8, rot=-2)
sticker(S3, "livre-croix-ouvert", 620, 780, 320, 14.4, rot=3)
tag(S3, 70, 1170, "Matthieu 25", 14.8, "acc", 46)
hit(15.4, 0.7)

# --- S4 · cinq, deux, un talent
cam(16.0, S4)
headline(S4, 280, ["Cinq, deux,", "[un] talent"], 16.1, kicker="Selon les capacités", hl_t=19.2, size=100)
sticker(S4, "trois-sacs", 50, 640, 620, 16.4, rot=-2)
tag(S4, 70, 1180, "5 talents", 17.3, "", 40)
tag(S4, 70, 1270, "2 talents", 18.4, "", 40)
tag(S4, 70, 1360, "1 talent", 19.5, "acc", 40)
hit(19.4, 0.7)

# --- S5 · fructifier ou enterrer
cam(22.0, S5)
headline(S5, 280, ["Fructifier", "ou [enterrer]"], 22.1, kicker="Deux choix", hl_t=26.4, size=96)
sticker(S5, "arbre-pieces", 40, 640, 330, 23.2, rot=-2)
sticker(S5, "baton-creuse", 460, 700, 450, 25.0, rot=3)
tag(S5, 70, 1100, "Faire fructifier", 23.4, "acc", 38)
tag(S5, 70, 1190, "Par peur : il enterre", 25.8, "", 38)
hit(26.4, 0.9)

# --- S6 · le retour du maître
cam(27.6, S6)
headline(S6, 280, ["Le [retour]", "du maître"], 27.7, kicker="Il parle aux fidèles", hl_t=28.5, size=104)
sticker(S6, "maitre-felicite", 60, 640, 540, 28.4, rot=-2)
hit(30.0, 0.8)

# --- S7 · le verset (Matthieu 25.21) : séquence « Parole » ; sous-titres coupés pendant la citation
cam(30.4, S7)
headline(S7, 280, ["Bon et", "[fidèle]"], 30.5, kicker="Matthieu 25", hl_t=32.2, size=104)
tag(S7, 70, 600, "Matthieu 25.21", 30.6, "acc", 52)
sfx("spark", 30.6, 1.6)
verse = ("«&nbsp;C'est bien, bon et fidèle serviteur&nbsp;; tu as été " + m(0, "fidèle en peu de chose") + ", je te confierai beaucoup&nbsp;; "
         + m(1, "entre dans la joie de ton maître") + ".&nbsp;»")
v = put(S7, 70, 710, f'<div class="h" style="font-size:50px;font-weight:700;line-height:1.22">{verse}</div>', "headline", f"width:{W - 2 * 70 - 60}px")
blur_in(v, 30.5, 20)
tween(f"#{v} .m0 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 34.2)
tween(f"#{v} .m1 i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', 37.2)
sticker(S7, "livre-croix-ouvert", 60, 1130, 320, 31.0, rot=-3)
sticker(S7, "croix-verte", 700, 1120, 170, 36.0, rot=4)
ref(S7, 70, 1420, "MATTHIEU 25.21 · LSG 1910", 31.2)
hit(38.6, 1.0)

# --- S8 · attention : d'abord ce que Dieu confie, l'argent en fait partie
cam(40.5, S8)
headline(S8, 280, ["Dieu nous", "[confie]"], 40.6, kicker="Attention", hl_t=43.4, size=110)
sticker(S8, "coeur-receptacle", 60, 640, 330, 43.0, rot=-3)
sticker(S8, "piedestal-pieces", 560, 700, 330, 44.2, rot=3)
tag(S8, 70, 1100, "L'argent en fait partie", 44.3, "acc", 38)
hit(45.9, 0.8)

# --- S9 · leçon 1 : ton argent t'est confié
cam(46.4, S9)
headline(S9, 280, ["Ton argent", "t'est [confié]"], 46.5, kicker="Leçon 1", hl_t=49.4, size=100)
sticker(S9, "baton-budget", 60, 640, 330, 47.3, rot=-2)
sticker(S9, "enveloppe-don", 620, 720, 280, 47.9, rot=3)
tag(S9, 70, 1200, "Il ne t'appartient pas vraiment", 48.2, "acc", 34)
hit(49.6, 0.8)

# --- S10 · leçon 2 : fidèle dans le peu
cam(49.9, S10)
headline(S10, 280, ["Fidèle dans", "le [peu]"], 50.0, kicker="Leçon 2", hl_t=52.2, size=104)
sticker(S10, "piles-croissantes", 50, 660, 420, 51.0, rot=-2)
sticker(S10, "bocal-plein", 620, 700, 300, 52.4, rot=3)
tag(S10, 70, 1120, "Avant le beaucoup", 52.5, "acc", 42)
hit(53.2, 0.8)

# --- S11 · leçon 3 : la peur est une erreur
cam(53.6, S11)
headline(S11, 280, ["La [peur]", "est une erreur"], 53.7, kicker="Leçon 3", hl_t=55.4, size=104)
sticker(S11, "baton-soucieux", 60, 640, 260, 54.4, rot=-2)
sticker(S11, "pot-enterre", 560, 760, 380, 56.4, rot=3)
tag(S11, 70, 1180, "Rien volé, rien perdu", 58.4, "", 36)
tag(S11, 70, 1270, "Il a seulement enterré", 59.4, "acc", 40)
hit(60.3, 0.8)

# --- S12 · fructifier ne veut pas dire spéculer
cam(61.1, S12)
headline(S12, 280, ["Fructifier,", "pas [spéculer]"], 61.2, kicker="Attention", hl_t=62.7, size=100)
sticker(S12, "arbre-pieces", 60, 650, 330, 61.8, rot=-2)
sticker(S12, "baton-serein", 620, 680, 270, 64.1, rot=3)
tag(S12, 70, 1100, "Gérer avec sagesse", 64.2, "acc", 42)
hit(65.0, 0.8)

# --- S13 · épargner, apprendre, donner
cam(65.3, S13)
headline(S13, 280, ["Épargner,", "apprendre, [donner]"], 65.4, kicker="Gérer avec sagesse", hl_t=67.5, size=84)
sticker(S13, "baton-epargne", 40, 640, 270, 65.8, rot=-2)
sticker(S13, "baton-lit-livre", 380, 660, 240, 66.7, rot=2)
sticker(S13, "baton-donne", 680, 700, 250, 67.5, rot=3)
hit(67.7, 0.8)

# --- S14 · cette semaine, une seule chose
cam(68.0, S14)
headline(S14, 280, ["Une seule", "[chose]"], 68.1, kicker="Cette semaine", hl_t=70.0, size=110)
sticker(S14, "baton-pense", 60, 660, 260, 68.6, rot=-2)
sticker(S14, "calendrier-mois", 620, 720, 300, 69.4, rot=3)
hit(70.1, 0.8)

# --- S15 · écris ce que tu possèdes
cam(70.5, S15)
headline(S15, 280, ["Écris ce que", "tu [possèdes]"], 70.6, kicker="Action 1", hl_t=71.7, size=92)
sticker(S15, "baton-ecrit-liste", 60, 640, 420, 71.0, rot=-2)
sticker(S15, "enveloppes-budget", 600, 720, 300, 72.0, rot=3)
hit(73.1, 0.8)

# --- S16 · choisis une action
cam(73.6, S16)
headline(S16, 280, ["Choisis une", "[action]"], 73.7, kicker="Action 2", hl_t=74.0, size=104)
tag(S16, 70, 660, "Épargner 20 €", 74.1, "acc", 40)
tag(S16, 70, 750, "Apprendre une compétence", 75.3, "", 36)
tag(S16, 70, 840, "Donner", 76.5, "", 40)
counter(S16, 70, 980, 0, 20, 74.5, 0.8, " €", 120)
sticker(S16, "piles-croissantes", 560, 900, 380, 74.2, rot=3)
hit(76.8, 0.8)

# --- S17 · le troisième serviteur n'a pas perdu d'argent (referme la boucle ouverte)
cam(77.0, S17)
headline(S17, 280, ["Pas perdu", "d'[argent]"], 77.1, kicker="Le troisième serviteur", hl_t=79.0, size=100)
sticker(S17, "pot-enterre", 60, 700, 420, 77.4, rot=-2)
tag(S17, 70, 1080, "Il a perdu l'occasion", 80.1, "", 38)
tag(S17, 70, 1170, "et la confiance", 81.2, "acc", 42)
hit(81.4, 0.9)

# --- S18 · question aux spectateurs
cam(82.0, S18)
headline(S18, 300, ["Quel [talent]", "arrêter d'enterrer ?"], 82.1, kicker="À ton tour", hl_t=82.7, size=92)
sticker(S18, "baton-serein", 700, 880, 210, 83.0, rot=3)
cta = put(S18, 70, 760, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 85.2, 14)
sfx("click", 85.2, 0.8)
tag(S18, 70, 900, "Abonne-toi", 86.0, "acc", 48)

# --- fin en boucle : retour sur l'image d'ouverture
cam(86.6, S1)
bigword("Il t'est confié", 89.7, 0.9, y=1250, size=100)
hit(90.2, 0.9)

# ================================================================ assemble
build(
    chapters=[("01", "Question", 0, 12.2), ("02", "Parabole", 12.2, 30.4), ("03", "Verset", 30.4, 46.4), ("04", "Leçons", 46.4, 68.0), ("05", "Action", 68.0, DUR)],
    suppress=[(30.45, 38.95)],
)
