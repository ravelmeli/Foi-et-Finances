"""Vidéo longue « 7 versets bibliques qui vont transformer vos finances » — style 02 en 16:9, ~9 min 30.
7 versets, 7 séquences « Parole » identiques, abonnement au milieu, exemple (David et Claire), récapitulatif, carte de fin.

Les temps écrits ci-dessous sont ceux de la voix avant le retrait d'une phrase lue deux fois par la synthèse vocale
(2,48 s à 46,9 s) : la fonction t() les recale sur transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - 7 versets bibliques qui vont transformer vos finances", "lang": "fr"}
COLS, ROWS = 9, 8
s.setup(here=HERE, duration=571.5, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]


def t(x):
    """Temps avant correction → temps réel (une phrase dupliquée de 2,48 s a été retirée à 46,9 s)."""
    return round(x - 2.48, 2) if x > 49.0 else x


def nxt(x):
    stn = ST[_n[0]]
    _n[0] += 1
    cam(t(x), stn)
    return stn


def title(stn, lines, x, kicker, hl=None, size=80):
    size = min(size, 78 if len(lines) > 1 else 96)
    return headline(stn, 172, lines, t(x), kicker=kicker, hl_t=t(hl) if hl is not None else None, size=size, x=80)


def stk(stn, name, px, py, w, x, rot=-2):
    return sticker(stn, name, px, py, w, t(x), rot=rot)


def tg(stn, y, text, x, cls="", size=40):
    return tag(stn, 80, y, text, t(x), cls, size)


def bw(text, x, dur=0.9, size=110):
    bigword(text, t(x), dur, y=640, size=size)


def hx(x, k=0.8):
    hit(t(x), k)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


def parole(x_cam, ref_txt, x_ref, verse_html, x_text, marks, size=48):
    """Séquence « Parole », identique pour chaque verset."""
    stn = nxt(x_cam)
    title(stn, ["La [Parole]"], x_cam + 0.1, "Ce que dit la Bible", hl=x_ref, size=84)
    tag(stn, 80, 350, ref_txt, t(x_ref), "acc", 46)
    sfx("spark", t(x_ref), 1.6)
    v = put(stn, 80, 450, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.25">{verse_html}</div>', "headline", "width:880px")
    blur_in(v, t(x_text) - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', t(mt))
    sticker(stn, "pupitre-parole", 1080, 260, 420, t(x_ref) + 0.2, rot=2)
    sticker(stn, "livre-croix-ouvert", 1500, 520, 330, t(x_text) + 0.4, rot=-3)
    ref(stn, 80, 830, ref_txt.upper() + " · LSG 1910", t(x_ref) + 0.4)
    return stn


def verset_n(n, x):
    bw(f"Verset {n}", x, 0.9)


# ================================================================ 01 · Introduction
S = nxt(0.0)
sticker(S, "livre-croix-ouvert", 1050, 300, 380, 0.0, rot=-3, instant=True)
sticker(S, "baton-lit-livre", 1480, 240, 300, 0.0, rot=2, instant=True)
title(S, ["7 versets qui changent", "ta façon de voir l'[argent]"], 0.0, "Et si…", hl=3.4)
bw("7 versets", 1.2, 1.0, 130)
hx(3.6)

S = nxt(4.3)
title(S, ["Pas une formule", "[magique]"], 4.4, "Mais le cœur", hl=6.2)
stk(S, "coeur-receptacle", 1100, 300, 360, 7.4, rot=-3)
stk(S, "boite-argent-facile", 1520, 360, 260, 5.0, rot=4)
tg(S, 480, "D'abord ton cœur, puis ton compte", 8.4, "acc", 38)

S = nxt(10.3)
title(S, ["Lire la Bible…", "et [manquer] d'argent"], 10.4, "Beaucoup de chrétiens", hl=13.8)
stk(S, "baton-lit-livre", 1050, 260, 300, 10.6)
stk(S, "baton-soucieux", 1480, 260, 300, 12.8, rot=3)
tg(S, 450, "Fins de mois serrées", 15.6, "", 38)
tg(S, 540, "Dettes qui s'accumulent", 16.8, "", 38)
tg(S, 630, "Inquiétude qui revient", 18.4, "acc", 38)

S = nxt(20.9)
title(S, ["La Bible parle", "[beaucoup] d'argent"], 21.0, "Au contraire", hl=23.8)
stk(S, "pupitre-parole", 1100, 260, 380, 21.4, rot=-2)
tg(S, 450, "Mais personne ne nous a appris", 25.8, "", 38)
tg(S, 540, "à relier ces versets à notre budget", 27.4, "acc", 38)

S = nxt(32.2)
title(S, ["Versets", "[bibliques]"], 32.3, "Aujourd'hui", hl=34.0)
counter(S, 80, 430, 0, 7, t(33.6), 1.0, " versets", 170)
stk(S, "baton-pense", 1450, 240, 300, 33.0)
tg(S, 680, "Ce qu'il dit vraiment + comment l'appliquer", 36.8, "", 34)

S = nxt(41.5)
title(S, ["Le dernier est le plus", "[difficile]"], 41.6, "Mais le plus paisible", hl=43.6)
stk(S, "colombe", 1250, 300, 360, 44.2, rot=4)
hx(43.8, 0.7)

# ================================================================ 02 · Versets 1 à 3
S = nxt(46.8)
title(S, ["La question des", "[priorités]"], 46.9, "Verset 1", hl=49.0)
stk(S, "baton-pense", 1150, 240, 300, 47.2)
stk(S, "croix-verte", 1500, 300, 240, 48.0, rot=4)
verset_n(1, 47.0)
hx(49.2)

parole(51.9, "Matthieu 6.33", 52.0,
       f"« Cherchez {m(0, 'premièrement')} le royaume et la justice de Dieu ; et {m(1, 'toutes ces choses')} vous seront données par-dessus. »",
       53.6, [55.0, 59.2], size=52)
hx(61.6, 0.6)

S = nxt(61.8)
title(S, ["« Toutes ces choses » :", "tes [besoins]"], 61.9, "Remarque bien", hl=69.6)
stk(S, "panier-besoins", 1050, 300, 330, 62.4, rot=-3)
stk(S, "maison-simple", 1460, 320, 320, 64.6, rot=3)
tg(S, 480, "Pas une promesse de richesse", 70.6, "acc", 38)
bw("Tes besoins", 69.8, 0.9)

S = nxt(73.0)
title(S, ["Dieu d'abord,", "l'argent à sa [place]"], 73.1, "Le message", hl=76.4)
stk(S, "pupitre-parole", 1000, 280, 360, 73.6, rot=-2)
stk(S, "piedestal-pieces", 1450, 360, 280, 75.2, rot=3)
hx(76.6, 0.8)

S = nxt(78.0)
title(S, ["Qu'est-ce qui vient", "en [premier] ?"], 78.1, "Quand ton salaire arrive", hl=80.0)
stk(S, "baton-jaloux", 1100, 260, 380, 83.0)
tg(S, 450, "Les envies, les crédits, les achats…", 84.0, "", 36)
tg(S, 545, "… et Dieu reçoit ce qui reste", 88.0, "acc", 36)
stk(S, "pile-factures", 1480, 400, 280, 85.0, rot=4)

S = nxt(92.0)
title(S, ["Inverser", "l'[ordre]"], 92.1, "Chercher premièrement", hl=94.4)
tg(S, 430, "Prière", 96.4, "", 38)
tg(S, 515, "Ta famille, tes besoins", 97.6, "", 38)
tg(S, 600, "Générosité, épargne", 99.0, "acc", 38)
stk(S, "baton-priere", 1350, 260, 300, 95.0)
bw("Regarde ton cœur", 100.6, 1.0, 100)

S = nxt(103.0)
title(S, ["Prie sur ton", "[budget]"], 103.1, "Le premier jour du mois", hl=106.6)
stk(S, "baton-prie-budget", 1150, 300, 460, 103.6)
tg(S, 480, "5 minutes, avant toute dépense", 104.8, "acc", 38)
stk(S, "calendrier-mois", 700, 600, 220, 105.6, rot=4)

S = nxt(109.7)
title(S, ["Voir [clair]"], 109.8, "Demande à Dieu", hl=111.0)
tg(S, 430, "L'essentiel ou le superflu ?", 112.0, "", 38)
tg(S, 530, "Rester fidèle tout le mois", 114.0, "acc", 38)
stk(S, "baton-serein", 1400, 260, 300, 110.4)
stk(S, "soleil-nuage", 1050, 380, 280, 116.4, rot=-3)

S = nxt(120.2)
title(S, ["La sagesse de la", "[planification]"], 120.3, "Verset 2", hl=121.8)
stk(S, "baton-budget", 1250, 260, 480, 120.6)
verset_n(2, 120.4)
hx(122.0)

parole(123.8, "Proverbes 21.5", 123.9,
       f"« Les {m(0, 'projets')} de l'homme diligent ne mènent qu'à l'abondance, mais celui qui agit avec {m(1, 'précipitation')} "
       "n'arrive qu'à la disette. »", 125.5, [125.9, 129.6], size=48)
hx(132.0, 0.6)

S = nxt(132.4)
title(S, ["Réfléchir ou se", "[précipiter]"], 132.5, "Deux attitudes", hl=136.2)
stk(S, "baton-carnet", 1000, 260, 280, 132.8)
stk(S, "baton-jaloux", 1380, 260, 360, 135.2, rot=3)
tg(S, 480, "L'abondance n'est pas une garantie de richesse", 138.4, "", 34)

S = nxt(144.2)
title(S, ["La précipitation", "coûte [cher]"], 144.3, "À l'inverse", hl=145.8)
tg(S, 430, "L'achat sur un coup de tête", 146.9, "", 38)
tg(S, 520, "Le crédit signé trop vite", 148.6, "", 38)
tg(S, 610, "La dépense regrettée", 150.2, "acc", 38)
stk(S, "boite-argent-facile", 1300, 300, 300, 147.4, rot=-3)

S = nxt(152.4)
title(S, ["L'erreur la plus", "[courante]"], 152.5, "Attention", hl=154.8)
stk(S, "baton-soucieux", 1400, 240, 300, 152.8)
tg(S, 450, "« Un budget, c'est pour les riches »", 155.6, "", 38)
tg(S, 550, "C'est quand on a peu qu'un plan compte le plus", 158.2, "acc", 34)
hx(158.4, 0.7)

S = nxt(162.1)
title(S, ["Une heure", "ce [week-end]"], 162.2, "Concrètement", hl=163.4)
stk(S, "baton-ecrit-liste", 1150, 260, 460, 162.6)
tg(S, 450, "Ce qui entre", 164.2, "", 40)
tg(S, 540, "Ce qui sort", 165.8, "", 40)
tg(S, 630, "Loyer, courses, factures, abonnements", 166.9, "acc", 34)

S = nxt(173.6)
title(S, ["Une place pour", "chaque [euro]"], 173.7, "Ensuite", hl=175.6)
stk(S, "enveloppes-budget", 1200, 300, 460, 174.2, rot=-3)
tg(S, 450, "Besoins · factures · épargne · don", 176.9, "", 34)
tg(S, 540, "Et un peu pour les plaisirs", 180.0, "acc", 36)

S = nxt(182.8)
title(S, ["Pas une [punition]"], 182.9, "Le budget", hl=183.4)
tg(S, 420, "Une décision prise dans le calme", 184.3, "acc", 38)
tg(S, 510, "plutôt qu'à la caisse, sous la pression", 186.6, "", 36)
stk(S, "couple-budget", 1250, 280, 460, 184.6)

S = nxt(189.3)
title(S, ["La puissance du", "[peu à peu]"], 189.4, "Verset 3", hl=191.2)
stk(S, "croissance-plante", 1150, 340, 480, 189.8, rot=-2)
verset_n(3, 189.6)
hx(191.4)

parole(192.2, "Proverbes 13.11", 192.3,
       f"« La richesse mal acquise {m(0, 'diminue')}, mais celui qui amasse {m(1, 'peu à peu')} l'augmente. »", 194.0, [195.4, 197.2], size=54)

S = nxt(198.8)
title(S, ["Tout, tout de", "[suite] ?"], 198.9, "Le monde promet", hl=201.6)
stk(S, "boite-argent-facile", 1100, 300, 300, 199.4, rot=-4)
stk(S, "baton-refuse", 1440, 260, 400, 205.5, rot=2)
tg(S, 480, "Devenir riche vite, sans effort", 202.3, "", 38)
tg(S, 570, "La Bible met en garde", 205.5, "acc", 38)

S = nxt(208.0)
title(S, ["Construit", "[patiemment]"], 208.1, "Ce qui tient", hl=215.0)
tg(S, 450, "Gagné trop vite : vite parti", 208.6, "", 38)
tg(S, 540, "Construit peu à peu : ça dure", 213.6, "acc", 38)
stk(S, "baton-arrose", 1250, 260, 460, 213.8)

S = nxt(217.5)
title(S, ["10 €, puis 20,", "puis [50]"], 217.6, "L'épargne", hl=220.6)
stk(S, "piles-croissantes", 1150, 340, 440, 219.2, rot=-2)
tg(S, 520, "Un vrai coussin de sécurité", 223.6, "acc", 38)

S = nxt(226.8)
title(S, ["50 € par mois,", "c'est…"], 226.9, "Imagine")
counter(S, 80, 430, 0, 600, t(228.2), 1.4, " € par an", 150)
stk(S, "machine-laver", 1250, 300, 300, 231.0, rot=-3)
tg(S, 680, "La facture imprévue, sans emprunter", 233.4, "acc", 36)
hx(229.6)

S = nxt(236.1)
title(S, ["[Automatise]"], 236.2, "Le secret", hl=237.0)
stk(S, "baton-epargne", 1350, 260, 380, 236.6)
tg(S, 420, "Un virement vers l'épargne", 238.7, "", 38)
tg(S, 510, "le jour où ton salaire arrive", 240.6, "acc", 38)
coins(S, 1000, 500, t(239.6), n=5, spread=240, size=64)

S = nxt(243.8)
title(S, ["Méfie-toi de", "l'[argent facile]"], 243.9, "Même avec de beaux versets", hl=245.6)
stk(S, "boite-argent-facile", 1050, 300, 320, 244.2, rot=-3)
stk(S, "baton-refuse", 1420, 260, 400, 245.0, rot=2)

S = nxt(248.6)
title(S, ["Si cette vidéo", "t'[aide]…"], 248.7, "Un instant", hl=249.6)
tg(S, 470, "Abonne-toi", 250.4, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", 252.7, "", 36)
stk(S, "croix-verte", 1200, 280, 260, 249.0, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 249.4, rot=2)
bw("Abonne-toi", 250.4, 1.0)

# ================================================================ 03 · Versets 4 et 5
S = nxt(257.4)
title(S, ["La liberté face", "aux [dettes]"], 257.5, "Verset 4", hl=259.6)
stk(S, "pile-factures", 1050, 300, 320, 257.8, rot=3)
stk(S, "chaine-cassee", 1450, 340, 340, 259.4, rot=-3)
verset_n(4, 257.7)
hx(259.8)

parole(260.3, "Romains 13.8", 260.4,
       f"« Ne devez {m(0, 'rien')} à personne, si ce n'est de vous {m(1, 'aimer')} les uns les autres. »", 263.0, [263.6, 265.6], size=58)

S = nxt(266.8)
title(S, ["Pas interdit", "d'[emprunter]"], 266.9, "Ce verset ne dit pas", hl=268.6)
stk(S, "baton-pense", 1400, 240, 300, 267.2)
tg(S, 450, "Ne rien laisser en souffrance", 269.4, "", 38)
tg(S, 540, "Payer ce que l'on doit", 271.6, "", 38)
tg(S, 630, "La seule dette qui dure : l'amour", 276.8, "acc", 38)
stk(S, "coeur-receptacle", 1050, 420, 240, 277.4, rot=-3)

S = nxt(279.3)
title(S, ["Ce que tes dettes", "te [coûtent]"], 279.4, "Vraiment", hl=281.2)
stk(S, "baton-insomnie", 1100, 280, 480, 282.6)
tg(S, 450, "Des intérêts", 281.9, "", 38)
tg(S, 540, "Des nuits blanches", 283.6, "", 38)
tg(S, 630, "Des tensions dans le couple", 285.0, "acc", 38)
stk(S, "couple-dispute", 650, 640, 220, 285.2, rot=3)

S = nxt(289.9)
title(S, ["Une dette", "à la [fois]"], 290.0, "Concrètement", hl=294.6)
stk(S, "baton-ciseaux-carte", 1400, 240, 300, 290.4)
tg(S, 450, "Arrête d'en ajouter", 290.4, "", 38)
tg(S, 540, "Fais la liste", 292.1, "", 38)
tg(S, 630, "Attaque une seule dette", 294.2, "acc", 38)
stk(S, "chaine-cassee", 1000, 520, 280, 296.4, rot=-3)
hx(296.6, 0.8)

S = nxt(299.6)
title(S, ["La plus petite,", "ou la plus [chère]"], 299.7, "Deux méthodes", hl=303.4)
stk(S, "piles-croissantes", 1150, 340, 420, 300.2, rot=-2)
tg(S, 480, "L'important : commencer", 305.8, "", 38)
tg(S, 570, "et ne pas abandonner", 308.4, "acc", 38)

S = nxt(311.1)
title(S, ["Ne reste pas", "[seul]"], 311.2, "Si c'est trop lourd", hl=312.4)
stk(S, "baton-ami", 1250, 260, 460, 311.6)
tg(S, 480, "Un conseiller en budget ou une association", 314.7, "acc", 34)

S = nxt(319.4)
title(S, ["Le sens de ton", "[travail]"], 319.5, "Verset 5", hl=321.4)
stk(S, "baton-travaille", 1250, 260, 460, 319.8)
verset_n(5, 319.6)
hx(321.6)

parole(322.1, "Colossiens 3.23", 322.2,
       f"« Tout ce que vous faites, faites-le {m(0, 'de bon cœur')}, comme {m(1, 'pour le Seigneur')} et non pour des hommes. »",
       323.5, [325.6, 327.8], size=54)

S = nxt(333.3)
title(S, ["Ton salaire commence", "dans ton [travail]"], 333.4, "Même quand c'est difficile", hl=336.2)
stk(S, "mallette-travail", 1100, 320, 300, 333.8, rot=-3)
stk(S, "baton-travaille", 1450, 260, 400, 335.0, rot=2)
tg(S, 480, "Honnête, fiable, le meilleur de toi", 338.0, "acc", 36)

S = nxt(343.9)
title(S, ["La fidélité ouvre", "des [portes]"], 344.0, "Sans t'épuiser", hl=347.8)
tg(S, 430, "Une compétence nouvelle", 349.9, "", 38)
tg(S, 520, "Une promotion", 351.6, "", 38)
tg(S, 610, "La confiance d'un employeur", 352.6, "acc", 38)
stk(S, "graphique-hausse", 1250, 300, 380, 349.0, rot=-2)

S = nxt(354.0)
title(S, ["Ta valeur ≠", "ton [salaire]"], 354.1, "Et cela te protège", hl=357.0)
stk(S, "baton-serein", 1400, 240, 300, 354.4)
tg(S, 480, "Tu cherches du travail ? Ce verset ne te condamne pas", 358.4, "", 32)
tg(S, 570, "Offre à Dieu ce que tu fais aujourd'hui", 363.6, "acc", 34)

# ================================================================ 04 · Versets 6 et 7
S = nxt(370.2)
title(S, ["Le pouvoir de la", "[générosité]"], 370.3, "Verset 6", hl=372.4)
stk(S, "baton-donne", 1250, 260, 520, 370.6)
verset_n(6, 370.5)
hx(372.6)

parole(373.0, "Proverbes 11.25", 373.1,
       f"« L'âme bienfaisante sera {m(0, 'rassasiée')}, et celui qui {m(1, 'arrose')} sera lui-même arrosé. »", 374.9, [376.8, 378.2], size=56)

S = nxt(379.9)
title(S, ["Pas un contrat", "[financier]"], 380.0, "Attention", hl=381.6)
stk(S, "baton-refuse", 1100, 260, 400, 380.4)
tg(S, 450, "« Donne 100 €, tu en recevras 1000 »", 382.8, "", 36)
bw("Non", 384.6, 0.7, 150)
stk(S, "arrosoir", 1500, 360, 300, 386.4, rot=4)

S = nxt(386.1)
title(S, ["Un cœur généreux,", "un cœur [rassasié]"], 386.2, "Un principe de vie", hl=389.4)
stk(S, "baton-arrose", 1250, 260, 460, 386.6)
tg(S, 480, "Libéré de la peur de manquer", 390.7, "", 38)
tg(S, 570, "Jamais vraiment seul dans la sécheresse", 396.6, "acc", 34)

S = nxt(402.0)
title(S, ["Une part pour", "le [don]"], 402.1, "Concrètement", hl=403.6)
stk(S, "enveloppe-don", 1050, 340, 280, 402.4, rot=-4)
stk(S, "couple-don", 1400, 280, 440, 405.7, rot=2)
tg(S, 450, "Ton église", 405.8, "", 38)
tg(S, 540, "Une famille dans le besoin", 407.0, "", 38)
tg(S, 630, "Ton temps", 408.8, "acc", 38)

S = nxt(410.8)
title(S, ["Donne avec", "[joie]"], 410.9, "Jamais sous la pression", hl=412.4)
stk(S, "coeur-receptacle", 1100, 300, 330, 411.4, rot=-3)
tg(S, 480, "Plus on donne, moins l'argent nous tient", 416.1, "acc", 34)
stk(S, "chaine-cassee", 1500, 360, 280, 419.4, rot=4)

S = nxt(422.7)
title(S, ["Le plus difficile", "à [vivre]"], 422.8, "Verset 7", hl=425.6)
stk(S, "baton-pense", 1400, 240, 300, 423.0)
verset_n(7, 423.0)
hx(425.8, 0.9)

parole(426.9, "Hébreux 13.5", 427.0,
       f"« Ne vous livrez pas à l'amour de l'argent ; {m(0, 'contentez-vous')} de ce que vous avez ; car Dieu lui-même a dit : "
       f"{m(1, 'Je ne te délaisserai point')}, et je ne t'abandonnerai point. »", 429.0, [430.8, 434.8], size=46)
hx(440.6, 0.6)

S = nxt(441.5)
title(S, ["La course", "sans [fin]"], 441.6, "On pense souvent", hl=443.6)
stk(S, "baton-jaloux", 1150, 260, 400, 441.8)
tg(S, 450, "Un peu plus… une plus grande maison…", 442.6, "", 34)
tg(S, 545, "Jamais content avec peu, jamais avec plus", 447.4, "acc", 34)

S = nxt(451.5)
title(S, ["Dieu ne t'abandonnera", "[jamais]"], 451.6, "La vraie raison", hl=456.4)
stk(S, "colombe", 1100, 300, 340, 453.4, rot=-3)
stk(S, "baton-priere", 1500, 260, 280, 454.6, rot=2)
tg(S, 480, "La sécurité est en sa présence", 458.0, "acc", 38)
bw("Jamais", 456.6, 0.9, 140)

S = nxt(461.7)
title(S, ["Des projets, oui :", "pas la [condition]"], 461.8, "Le contentement", hl=469.0)
stk(S, "baton-serein", 1400, 240, 300, 462.0)
tg(S, 480, "Cette vérité change tout", 461.8, "", 38)
tg(S, 570, "La paix ne dépend pas de ton compte", 468.4, "acc", 36)

# ================================================================ 05 · Exemple
S = nxt(472.0)
title(S, ["Un exemple :", "David et [Claire]"], 472.1, "Prenons", hl=473.6)
stk(S, "couple-dispute", 1200, 280, 480, 473.1)
tg(S, 480, "Deux salaires… et des disputes", 474.6, "", 38)
tg(S, 570, "Ils se comparaient à leurs amis", 478.0, "acc", 36)

S = nxt(483.5)
title(S, ["Un verset par", "[semaine]"], 483.6, "Un soir", hl=486.0)
stk(S, "couple-lit-bible", 1250, 280, 460, 483.8)

S = nxt(487.8)
title(S, ["Priorités, budget,", "[épargne]"], 487.9, "Ils ont commencé", hl=492.6)
stk(S, "couple-budget", 1000, 280, 420, 488.2)
stk(S, "couple-epargne", 1450, 280, 420, 492.0, rot=2)
tg(S, 480, "Plus de nouveau crédit", 495.1, "", 38)
tg(S, 570, "Le plus petit remboursé d'abord", 496.8, "acc", 36)

S = nxt(498.9)
title(S, ["Ils ont recommencé", "à [donner]"], 499.0, "Avec joie", hl=500.4)
stk(S, "couple-don", 1250, 280, 480, 499.2)

S = nxt(503.4)
title(S, ["Une paix", "[retrouvée]"], 503.5, "Au bout de quelques mois", hl=509.4)
stk(S, "couple-heureux", 1250, 280, 420, 505.7)
tg(S, 480, "Moins de disputes", 506.4, "", 38)
hx(509.6, 0.8)

# ================================================================ 06 · À retenir
S = nxt(510.7)
title(S, ["Pas de [magie]"], 510.8, "Ces 7 versets", hl=513.6)
tg(S, 420, "D'abord ton cœur", 514.2, "", 40)
tg(S, 510, "puis tes habitudes", 515.6, "", 40)
tg(S, 600, "puis tes finances", 517.4, "acc", 40)
stk(S, "croissance-plante", 1200, 340, 460, 514.4, rot=-2)

S = nxt(519.4)
title(S, ["Souviens-[toi]"], 519.5, "Les 7 versets", hl=520.2)
for k, (txt, x) in enumerate([("1 · Cherche Dieu en premier", 520.8), ("2 · Planifie avec diligence", 522.6),
                              ("3 · Construis peu à peu", 524.4), ("4 · Libère-toi des dettes", 526.0),
                              ("5 · Travaille de bon cœur", 527.6), ("6 · Donne avec générosité", 529.4),
                              ("7 · Apprends le contentement", 531.2)]):
    tag(S, 80, 330 + k * 66, txt, t(x), "acc" if k == 6 else "", 28)
stk(S, "livre-croix-ouvert", 1250, 320, 420, 520.0, rot=-3)

S = nxt(533.3)
title(S, ["Un seul verset,", "sur ton [frigo]"], 533.4, "Cette semaine", hl=537.8)
stk(S, "baton-post-it", 1250, 260, 440, 535.2)
tg(S, 480, "Laisse-le travailler en toi", 541.4, "acc", 38)

S = nxt(543.8)
title(S, ["Il ne t'abandonnera", "[jamais]"], 543.9, "Pas parfait", hl=547.2)
stk(S, "baton-priere", 1400, 260, 300, 544.2)
stk(S, "colombe", 1050, 340, 280, 545.6, rot=-3)

S = nxt(548.3)
title(S, ["Quel verset te", "[parle] le plus ?"], 548.4, "Et toi", hl=550.4)
stk(S, "baton-pense", 1450, 240, 300, 548.6)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, t(551.8), 14)
sfx("click", t(551.8), 0.8)
tg(S, 620, "Abonne-toi", 555.2, "acc", 56)

cam(t(558.6), "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, t(46.8)), ("02", "Versets 1-3", t(46.8), t(257.4)), ("03", "Versets 4-5", t(257.4), t(370.2)),
              ("04", "Versets 6-7", t(370.2), t(472.0)), ("05", "Exemple", t(472.0), t(510.7)), ("06", "À retenir", t(510.7), DUR)],
    suppress=[(t(53.4), t(61.8)), (t(125.3), t(132.4)), (t(193.8), t(198.8)), (t(262.8), t(266.8)), (t(323.3), t(333.3)),
              (t(374.7), t(379.9)), (t(428.8), t(441.5)), (t(559.2), DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=t(559.4),
)
