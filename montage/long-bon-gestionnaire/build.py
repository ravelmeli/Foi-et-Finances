"""Vidéo longue « Comment devenir un meilleur gestionnaire de son argent selon la Bible » — style 02 en 16:9, ~7 min.
7 principes, 7 séquences « Parole » identiques, abonnement au milieu, exemple (Sophie), récapitulatif, carte de fin.

Mise en page 16:9 (fiche de style, section 11) : titre en haut à gauche, texte à gauche, illustration à droite,
sous-titres en bas. Les temps sont ceux de transcript.json (voix déjà débarrassée de ses silences).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Devenir un meilleur gestionnaire selon la Bible", "lang": "fr"}
COLS, ROWS = 8, 7
s.setup(here=HERE, duration=426.0, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403  (après setup : W, H, html, T, sticker, headline, cam...)

# Stations en serpentin sur une toile de 8 × 7 écrans 16:9.
ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]


def nxt(t):
    """Station suivante, et la caméra y va à t."""
    stn = ST[_n[0]]
    _n[0] += 1
    cam(t, stn)
    return stn


def title(stn, lines, t, kicker, hl_t=None, size=80):
    # 16:9 : deux lignes de titre au plus 78 px, une ligne au plus 96 px, pour laisser la place aux bandeaux (y ≥ 420).
    size = min(size, 78 if len(lines) > 1 else 96)
    return headline(stn, 172, lines, t, kicker=kicker, hl_t=hl_t, size=size, x=80)


def bw(text, t, dur=0.9, size=110):
    bigword(text, t, dur, y=640, size=size)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


def parole(t_cam, ref_txt, ref_t, verse_html, t_text, marks, size=44):
    """Séquence « Parole », identique pour chaque verset : bandeau vert, verset en grand à gauche, Bible ouverte à droite."""
    stn = nxt(t_cam)
    title(stn, ["La [Parole]"], t_cam + 0.1, "Ce que dit la Bible", hl_t=ref_t, size=84)
    tag(stn, 80, 350, ref_txt, ref_t, "acc", 46)
    sfx("spark", ref_t, 1.6)
    v = put(stn, 80, 450, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.25">{verse_html}</div>', "headline", "width:880px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    sticker(stn, "pupitre-parole", 1080, 260, 420, ref_t + 0.2, rot=2)
    sticker(stn, "livre-croix-ouvert", 1500, 520, 330, t_text + 0.4, rot=-3)
    ref(stn, 80, 830, ref_txt.upper() + " · LSG 1910", ref_t + 0.4)
    return stn


# ================================================================ 01 · Constat
S = nxt(0.0)
sticker(S, "baton-soucieux", 1350, 240, 320, 0.0, rot=-2, instant=True)
sticker(S, "pile-factures", 1000, 420, 330, 0.0, rot=3, instant=True)
title(S, ["Où est passé", "ton [argent] ?"], 0.0, "À la fin du mois", hl_t=4.0, size=96)
bw("Fin du mois", 2.6, 0.9)
hit(4.2, 0.8)

S = nxt(5.6)
title(S, ["Tu aimerais", "mieux [gérer]"], 5.7, "Mais par où commencer ?", hl_t=6.6, size=96)
tag(S, 80, 450, "Mieux gérer", 6.6, "", 42)
tag(S, 80, 545, "Mieux donner", 7.6, "", 42)
tag(S, 80, 640, "Mieux préparer l'avenir", 8.6, "acc", 42)
sticker(S, "baton-pense", 1400, 240, 320, 9.8, rot=-2)

S = nxt(11.4)
title(S, ["Dieu s'intéresse-t-il", "à ton [argent] ?"], 11.5, "Une question", hl_t=17.2, size=84)
sticker(S, "baton-lit-livre", 1050, 260, 320, 11.8, rot=-2)
sticker(S, "pupitre-parole", 1450, 280, 380, 14.6, rot=3)

S = nxt(18.9)
title(S, ["Oui. Pour te", "[libérer]"], 19.0, "La réponse de la Bible", hl_t=22.6, size=100)
sticker(S, "chaine-cassee", 1050, 320, 380, 21.6, rot=-3)
sticker(S, "colombe", 1480, 300, 340, 22.4, rot=4)
tag(S, 80, 480, "Pas pour te juger", 21.6, "", 42)
bw("Oui", 19.6, 0.8, 170)
hit(22.6, 0.8)

S = nxt(24.1)
title(S, ["Pas une question de foi :", "de [sagesse]"], 24.2, "Beaucoup de chrétiens sincères", hl_t=32.0, size=76)
sticker(S, "baton-priere", 1100, 260, 300, 24.6, rot=-2)
sticker(S, "livre-croix-ferme", 1460, 360, 340, 30.2, rot=4)
tag(S, 80, 480, "Une sagesse que personne ne leur a transmise", 32.4, "acc", 36)
hit(32.2, 0.7)

S = nxt(35.5)
title(S, ["Principes", "[bibliques]"], 35.6, "Aujourd'hui", hl_t=41.6, size=96)
counter(S, 80, 430, 0, 7, 41.0, 1.0, " principes", 170)
sticker(S, "baton-pense", 1400, 240, 320, 36.2, rot=-2)
tag(S, 80, 680, "Le dernier : presque tout le monde l'oublie", 45.7, "acc", 36)
hit(42.0, 0.8)

# ================================================================ 02 · Principes 1 à 3
S = nxt(48.5)
title(S, ["Gestionnaire, pas", "[propriétaire]"], 48.6, "Principe 1", hl_t=51.8, size=88)
sticker(S, "baton-cles", 1150, 260, 320, 48.9, rot=-2)
sticker(S, "trousseau-cles", 1550, 360, 260, 51.0, rot=6)
bw("Principe 1", 48.8, 0.9)
hit(51.9, 0.8)

parole(53.6, "Psaume 24.1", 53.8,
       f"« À {m(0, 'l’Éternel')} la terre et ce qu'elle renferme, le monde et ceux qui l'habitent ! »", 55.8, [56.0], size=56)
hit(59.6, 0.6)

S = nxt(60.3)
title(S, ["Tout appartient", "à [Dieu]"], 60.4, "Ton salaire, ta maison…", hl_t=64.6, size=96)
tag(S, 80, 430, "Ton salaire", 60.6, "", 40)
tag(S, 80, 520, "Ta maison", 61.6, "", 40)
tag(S, 80, 610, "Ton temps", 62.4, "", 40)
tag(S, 80, 700, "Tes talents", 63.2, "acc", 40)
sticker(S, "maison-simple", 1100, 300, 330, 61.6, rot=-3)
sticker(S, "panier-besoins", 1500, 380, 300, 62.6, rot=3)

S = nxt(65.6)
title(S, ["Tu es", "[l'intendant]"], 65.7, "Le gérant", hl_t=66.8, size=100)
sticker(S, "baton-pense", 1400, 240, 320, 66.0, rot=-2)
tag(S, 80, 470, "« Qu'est-ce que je veux ? »", 69.4, "", 40)
tag(S, 80, 570, "« Qu'est-ce qui honore Dieu ? »", 72.6, "acc", 40)

S = nxt(77.6)
title(S, ["Les clés d'une", "[maison]"], 77.7, "Une image", hl_t=84.2, size=96)
sticker(S, "trousseau-cles", 1000, 300, 260, 79.0, rot=-6)
sticker(S, "maison-simple", 1350, 320, 380, 82.0, rot=3)
tag(S, 80, 480, "Il ne repeint pas les murs", 85.6, "", 38)
tag(S, 80, 575, "Il prend soin de ce qui ne lui appartient pas", 88.6, "acc", 36)

S = nxt(93.0)
title(S, ["Ta [place]", "face à l'argent"], 93.1, "Exactement", hl_t=95.0, size=96)
sticker(S, "baton-cles", 1400, 240, 320, 93.4, rot=-2)
sticker(S, "croix-verte", 1050, 320, 220, 94.0, rot=-4)

S = nxt(96.5)
title(S, ["Fidèle dans les", "[petites] choses"], 96.6, "Principe 2", hl_t=98.6, size=92)
sticker(S, "baton-carnet", 1400, 240, 300, 96.9, rot=-2)
bw("Principe 2", 96.8, 0.9)
hit(98.7, 0.8)

parole(100.0, "Luc 16.10", 100.2,
       f"« Celui qui est fidèle dans les {m(0, 'moindres choses')} l'est aussi dans les {m(1, 'grandes')}. »", 102.2, [103.6, 105.0], size=58)

S = nxt(105.6)
title(S, ["L'erreur la plus", "[courante]"], 105.7, "Attention", hl_t=109.8, size=96)
sticker(S, "baton-soucieux", 1400, 240, 300, 106.0, rot=-2)
tag(S, 80, 480, "Attendre d'avoir plus", 106.4, "", 42)
tag(S, 80, 580, "La fidélité ne commence pas avec un gros salaire", 111.2, "acc", 34)
hit(110.0, 0.7)

S = nxt(113.7)
title(S, ["Le café, l'abonnement,", "les [10 €]"], 113.8, "Elle commence ici", hl_t=117.0, size=80)
tag(S, 80, 450, "Gérer peu, c'est apprendre à gérer plus", 118.8, "acc", 36)
sticker(S, "feuille-liste", 1150, 300, 300, 114.4, rot=-3)
coins(S, 1500, 520, 116.6, n=5, spread=240, size=70)

S = nxt(122.5)
title(S, ["Note chaque", "[dépense]"], 122.6, "Fais l'essai cette semaine", hl_t=124.6, size=96)
sticker(S, "baton-carnet", 1400, 240, 300, 122.9, rot=-2)
tag(S, 80, 480, "Même un euro", 124.6, "acc", 44)
coins(S, 1000, 520, 127.4, n=6, spread=260, size=64)
hit(130.6, 0.6)

S = nxt(132.7)
title(S, ["Planifie avant", "de [dépenser]"], 132.8, "Principe 3", hl_t=135.2, size=96)
sticker(S, "baton-budget", 1300, 260, 480, 133.1, rot=-2)
bw("Principe 3", 133.0, 0.9)
hit(135.3, 0.8)

parole(136.2, "Luc 14.28", 136.4,
       f"« Car, lequel de vous, s'il veut {m(0, 'bâtir une tour')}, ne s'assied d'abord pour {m(1, 'calculer la dépense')} "
       "et voir s'il a de quoi la terminer ? »", 139.8, [142.0, 144.6], size=48)
hit(148.4, 0.6)

S = nxt(148.8)
title(S, ["Faire un budget,", "c'est [calculer]"], 148.9, "Pas manquer de foi", hl_t=153.6, size=92)
sticker(S, "tour-chantier", 1050, 300, 380, 149.2, rot=-3)
sticker(S, "baton-budget", 1450, 280, 400, 151.6, rot=2)

S = nxt(154.8)
title(S, ["Une mission pour", "chaque [euro]"], 154.9, "Concrètement", hl_t=157.6, size=92)
sticker(S, "enveloppes-budget", 1200, 300, 460, 155.6, rot=-3)
tag(S, 80, 430, "Les besoins", 159.0, "", 40)
tag(S, 80, 520, "Les factures", 159.8, "", 40)
tag(S, 80, 610, "L'épargne", 160.6, "", 40)
tag(S, 80, 700, "Le don", 161.6, "acc", 40)

S = nxt(163.0)
title(S, ["Une [carte],", "pas une prison"], 163.1, "Le budget", hl_t=165.4, size=100)
sticker(S, "baton-chemin", 1150, 280, 500, 163.4, rot=-2)
bw("Une carte", 165.2, 0.9)

S = nxt(166.9)
title(S, ["Si cette vidéo", "t'[aide]…"], 167.0, "Un instant", hl_t=168.0, size=96)
tag(S, 80, 470, "Abonne-toi", 168.6, "acc", 72)
tag(S, 80, 600, "Chaque semaine, un principe biblique simple", 170.6, "", 38)
sticker(S, "croix-verte", 1200, 280, 260, 167.2, rot=-3)
sticker(S, "baton-lit-livre", 1520, 300, 300, 167.6, rot=2)
bw("Abonne-toi", 168.6, 1.0)

# ================================================================ 03 · Principes 4 et 5
S = nxt(174.5)
title(S, ["Prépare", "l'[avenir]"], 174.6, "Principe 4", hl_t=176.6, size=104)
sticker(S, "fourmi-grain", 1050, 340, 300, 175.6, rot=-4)
sticker(S, "baton-epargne", 1420, 260, 360, 176.4, rot=2)
bw("Principe 4", 174.8, 0.9)
hit(176.8, 0.8)

parole(177.6, "Proverbes 6.6-8", 177.8,
       f"« Va vers la {m(0, 'fourmi')}, paresseux ; considère ses voies, et deviens sage. Elle n'a ni chef, ni inspecteur, ni maître ; "
       f"elle {m(1, 'prépare en été')} sa nourriture, elle amasse pendant la moisson de quoi manger. »", 180.4, [180.8, 187.8], size=40)
hit(191.4, 0.6)

S = nxt(191.7)
title(S, ["Épargner n'est pas", "[douter] de Dieu"], 191.8, "La fourmi n'attend pas l'hiver", hl_t=194.8, size=88)
sticker(S, "fourmi-grain", 1050, 340, 280, 192.0, rot=-4)
sticker(S, "baton-priere", 1450, 260, 300, 194.4, rot=2)
tag(S, 80, 520, "C'est la sagesse de sa création", 196.1, "acc", 38)

S = nxt(198.5)
title(S, ["Commence", "[petit]"], 198.6, "Un fonds d'urgence", hl_t=199.2, size=110)
sticker(S, "baton-epargne", 1400, 260, 380, 198.8, rot=-2)
tag(S, 80, 470, "Quelques euros chaque mois", 200.6, "", 40)
tag(S, 80, 570, "La régularité compte plus que le montant", 204.4, "acc", 36)
coins(S, 1000, 480, 201.6, n=5, spread=260, size=64)

S = nxt(206.7)
title(S, ["20 € par mois,", "c'est…"], 206.8, "Imagine", size=96)
counter(S, 80, 430, 0, 240, 208.2, 1.4, " € par an", 150)
sticker(S, "machine-laver", 1200, 300, 330, 210.8, rot=-3)
tag(S, 80, 680, "La paix, plutôt qu'un nouveau crédit", 213.4, "acc", 36)
hit(209.6, 0.8)

S = nxt(216.5)
title(S, ["Libère-toi", "des [dettes]"], 216.6, "Principe 5", hl_t=218.2, size=104)
sticker(S, "pile-factures", 1050, 320, 330, 216.9, rot=3)
sticker(S, "baton-fardeau", 1450, 260, 380, 217.4, rot=-2)
bw("Principe 5", 216.8, 0.9)
hit(218.3, 0.8)

parole(218.8, "Proverbes 22.7", 219.0,
       f"« Le riche domine sur les pauvres, et celui qui emprunte est {m(0, 'l’esclave')} de celui qui prête. »", 220.5, [223.2], size=56)

S = nxt(225.1)
title(S, ["Pas un péché,", "mais moins de [liberté]"], 225.2, "La Bible nous avertit", hl_t=230.0, size=84)
sticker(S, "baton-pense", 1400, 240, 300, 225.6, rot=-2)
tag(S, 80, 520, "Chaque crédit engage ton salaire de demain", 232.4, "acc", 36)

S = nxt(235.5)
title(S, ["Une dette", "à la [fois]"], 235.6, "Concrètement", hl_t=241.6, size=104)
sticker(S, "baton-ciseaux-carte", 1400, 240, 300, 235.8, rot=-2)
tag(S, 80, 430, "N'en ajoute plus", 235.8, "", 38)
tag(S, 80, 520, "Liste celles que tu as", 238.0, "", 38)
tag(S, 80, 610, "Rembourse-les une par une", 240.0, "acc", 38)
tag(S, 80, 720, "Trop lourd ? Un conseiller en budget peut t'aider", 244.1, "", 32)
sticker(S, "chaine-cassee", 1000, 520, 300, 242.0, rot=-3)
hit(242.2, 0.8)

# ================================================================ 04 · Principes 6 et 7
S = nxt(247.8)
title(S, ["Donne avec", "[joie]"], 247.9, "Principe 6", hl_t=249.6, size=110)
sticker(S, "baton-donne", 1250, 260, 520, 248.2, rot=-2)
bw("Principe 6", 248.1, 0.9)
hit(249.7, 0.8)

parole(250.2, "2 Corinthiens 9.7", 250.4,
       f"« Que chacun donne comme il l'a résolu en son cœur, sans tristesse ni contrainte ; car Dieu aime celui qui donne "
       f"{m(0, 'avec joie')}. »", 253.9, [260.4], size=50)
hit(260.6, 0.6)

S = nxt(261.2)
title(S, ["Un outil, pas", "un [maître]"], 261.3, "Un bon gestionnaire n'est pas un avare", hl_t=265.6, size=92)
sticker(S, "piedestal-pieces", 1050, 320, 300, 261.6, rot=-3)
sticker(S, "coeur-receptacle", 1450, 360, 330, 263.6, rot=3)
tag(S, 80, 520, "Ni pour recevoir, ni sous la pression", 266.6, "acc", 38)

S = nxt(270.5)
title(S, ["Donne", "[librement]"], 270.6, "Selon tes moyens", hl_t=271.6, size=110)
sticker(S, "enveloppe-don", 1100, 340, 300, 271.0, rot=-4)
sticker(S, "baton-donne", 1450, 260, 420, 272.6, rot=2)
tag(S, 80, 520, "Une part pour le don dans ton budget", 276.7, "acc", 36)

S = nxt(281.0)
title(S, ["Soutenir, aider,", "[partager]"], 281.1, "Par exemple", hl_t=285.6, size=96)
tag(S, 80, 450, "Ton église", 282.0, "", 40)
tag(S, 80, 540, "Une famille dans le besoin", 283.4, "", 40)
tag(S, 80, 630, "Un repas offert", 285.2, "acc", 40)
sticker(S, "panier-besoins", 1100, 320, 300, 285.2, rot=-3)
sticker(S, "enveloppe-don", 1480, 380, 260, 282.4, rot=4)

S = nxt(287.6)
title(S, ["Même un petit", "[montant]"], 287.7, "Le don n'est pas réservé aux riches", hl_t=291.4, size=100)
sticker(S, "coeur-receptacle", 1250, 300, 400, 290.4, rot=-3)
coins(S, 1300, 300, 291.0, n=4, spread=240, size=64)
hit(293.6, 0.7)

S = nxt(294.9)
title(S, ["Rends des", "[comptes]"], 295.0, "Principe 7 · celui que tout le monde oublie", hl_t=299.2, size=110)
sticker(S, "calendrier-mois", 1250, 300, 380, 296.0, rot=-3)
bw("Principe 7", 297.4, 1.0)
hit(299.3, 0.9)

parole(300.2, "1 Corinthiens 4.2", 300.4,
       f"« Du reste, ce qu'on demande des dispensateurs, c'est que chacun soit trouvé {m(0, 'fidèle')}. »", 303.3, [307.0], size=56)
hit(307.2, 0.6)

S = nxt(307.7)
title(S, ["Fidèle,", "pas [parfait]"], 307.8, "Ce que Dieu demande", hl_t=309.0, size=110)
sticker(S, "baton-serein", 1400, 240, 320, 308.0, rot=-2)
tag(S, 80, 520, "Regarder ses comptes en face", 312.5, "acc", 40)

S = nxt(317.1)
title(S, ["15 minutes", "par [mois]"], 317.2, "Le rendez-vous mensuel", hl_t=318.6, size=104)
sticker(S, "calendrier-mois", 1050, 300, 330, 317.4, rot=-3)
sticker(S, "baton-budget", 1450, 280, 380, 318.4, rot=2)
tag(S, 80, 450, "Qu'est-ce qui est entré ?", 319.9, "", 38)
tag(S, 80, 545, "Qu'est-ce qui est sorti ?", 321.0, "", 38)
tag(S, 80, 640, "Est-ce que cela reflète mes priorités ?", 322.6, "acc", 36)

S = nxt(325.2)
title(S, ["Trois [questions]"], 325.3, "Seul, en couple ou avec quelqu'un", hl_t=329.4, size=104)
sticker(S, "baton-pense", 1400, 240, 300, 325.6, rot=-2)
tag(S, 80, 420, "Ai-je respecté mon budget ?", 331.1, "", 40)
tag(S, 80, 515, "Ai-je pu épargner un peu ?", 332.6, "", 40)
tag(S, 80, 610, "Ai-je donné avec joie ?", 334.1, "acc", 40)

S = nxt(335.8)
title(S, ["Ne te [condamne]", "pas"], 335.9, "Si la réponse est non", hl_t=337.0, size=104)
sticker(S, "baton-serein", 1400, 240, 320, 336.2, rot=-2)
tag(S, 80, 520, "Ajuste, et recommence le mois suivant", 338.3, "acc", 38)

S = nxt(340.5)
title(S, ["Ce qui est regardé", "est [bien géré]"], 340.6, "Ce rendez-vous change tout", hl_t=344.6, size=88)
sticker(S, "graphique-hausse", 1200, 300, 420, 341.0, rot=-2)
hit(344.8, 0.8)

# ================================================================ 05 · Exemple
S = nxt(346.1)
title(S, ["Un exemple :", "[Sophie]"], 346.2, "Prenons", hl_t=347.6, size=104)
sticker(S, "sophie-court", 1150, 260, 480, 347.3, rot=-2)
tag(S, 80, 480, "Un bon salaire, rien de côté", 348.4, "", 38)
tag(S, 80, 575, "Deux crédits, toujours à courir", 350.2, "acc", 38)

S = nxt(353.4)
title(S, ["Un seul", "[changement]"], 353.5, "Elle a commencé", hl_t=354.6, size=104)
sticker(S, "sophie-ecrit", 1100, 260, 320, 353.8, rot=-2)
sticker(S, "calendrier-mois", 1480, 360, 300, 355.7, rot=3)
tag(S, 80, 520, "Chaque 1er du mois, une mission par euro", 356.4, "acc", 36)

S = nxt(360.2)
title(S, ["Petit à", "[petit]"], 360.3, "Elle a avancé", hl_t=361.2, size=110)
sticker(S, "graphique-hausse", 1000, 300, 340, 360.6, rot=-3)
sticker(S, "sophie-donne", 1420, 260, 380, 363.6, rot=2)
tag(S, 80, 470, "Un peu de côté", 361.4, "", 38)
tag(S, 80, 565, "Un crédit remboursé", 362.4, "", 38)
tag(S, 80, 660, "Le don, avec joie", 364.2, "acc", 38)
hit(364.4, 0.7)

S = nxt(366.5)
title(S, ["Pas le salaire :", "la [manière]"], 366.6, "Ce qui a changé", hl_t=369.4, size=100)
sticker(S, "sophie-ecrit", 1400, 260, 320, 366.8, rot=-2)
bw("La manière", 369.2, 0.9)

# ================================================================ 06 · À retenir
S = nxt(370.5)
title(S, ["Une question de", "[fidélité]"], 370.6, "Pas de montant", hl_t=375.2, size=96)
sticker(S, "baton-serein", 1150, 240, 320, 370.8, rot=-2)
sticker(S, "colombe", 1500, 320, 300, 373.0, rot=4)
bw("Fidélité", 375.0, 1.0)

S = nxt(376.4)
title(S, ["Les 7 [principes]"], 376.5, "Souviens-toi", hl_t=377.4, size=84)
for k, (txt, t) in enumerate([("1 · Gestionnaire, pas propriétaire", 378.2), ("2 · Fidèle dans les petites choses", 380.5),
                              ("3 · Planifie avant de dépenser", 382.2), ("4 · Prépare l'avenir", 383.8),
                              ("5 · Libère-toi des dettes", 385.0), ("6 · Donne avec joie", 386.6),
                              ("7 · Rends des comptes chaque mois", 388.2)]):
    tag(S, 80, 330 + k * 66, txt, t, "acc" if k == 6 else "", 28)
sticker(S, "livre-croix-ouvert", 1250, 320, 420, 377.0, rot=-3)
hit(388.4, 0.7)

S = nxt(390.3)
title(S, ["Un seul principe,", "[cette semaine]"], 390.4, "Tu n'as pas à tout faire ce soir", hl_t=394.4, size=88)
sticker(S, "baton-chemin", 1150, 280, 480, 390.8, rot=-2)
tag(S, 80, 520, "Fidèle, un pas à la fois", 395.7, "acc", 42)
sticker(S, "croix-verte", 700, 600, 160, 396.4, rot=4)

S = nxt(400.4)
title(S, ["Quel principe", "en [premier] ?"], 400.5, "Et toi", hl_t=402.2, size=100)
sticker(S, "baton-pense", 1450, 240, 300, 400.8, rot=-2)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 403.4, 14)
sfx("click", 403.4, 0.8)
tag(S, 80, 620, "Abonne-toi", 406.8, "acc", 56)

cam(410.4, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Constat", 0, 48.5), ("02", "Principes 1-3", 48.5, 174.5), ("03", "Principes 4-5", 174.5, 247.8),
              ("04", "Principes 6-7", 247.8, 346.1), ("05", "Exemple", 346.1, 370.5), ("06", "À retenir", 370.5, DUR)],
    suppress=[(55.6, 60.3), (102.0, 105.6), (139.6, 148.8), (180.2, 191.7), (220.3, 225.1), (253.7, 261.2), (303.1, 307.7),
              (411.0, DUR)],   # versets affichés, carte de fin
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=411.2,
)
