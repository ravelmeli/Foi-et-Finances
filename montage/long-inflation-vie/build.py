"""Vidéo longue « Comment éviter l'inflation du mode de vie selon la Bible » — style 02 en 16:9, ~9 min 37.
Le piège, 3 signes, 3 passages d'avertissement, abonnement au milieu, 2 passages sur le contentement, 5 étapes,
prière de Proverbes 30, exemple (Marc), récapitulatif, carte de fin. Temps lus dans transcript.json.

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comment éviter l'inflation du mode de vie selon la Bible", "lang": "fr"}
COLS, ROWS = 10, 8
VOICE_END = 561.3
s.setup(here=HERE, duration=577.0, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]
SUP = []


def nxt(x):
    stn = ST[_n[0]]
    _n[0] += 1
    cam(x, stn)
    return stn


def title(stn, lines, x, kicker, hl=None, size=80):
    size = min(size, 78 if len(lines) > 1 else 96)
    return headline(stn, 172, lines, x, kicker=kicker, hl_t=hl, size=size, x=80)


def stk(stn, name, px, py, w, x, rot=-2):
    return sticker(stn, name, px, py, w, x, rot=rot)


def tg(stn, y, text, x, cls="", size=40):
    return tag(stn, 80, y, text, x, cls, size)


def bw(text, x, dur=0.9, size=110):
    bigword(text, x, dur, y=640, size=size)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


def parole(x_cam, ref_txt, x_ref, verse_html, x_text, x_end, marks, size=48):
    """Séquence « Parole », identique pour chaque passage ; sous-titres coupés pendant la citation."""
    verse_html = verse_html.replace(" »", "&nbsp;»").replace("« ", "«&nbsp;").replace(" ;", "&nbsp;;")
    stn = nxt(x_cam)
    title(stn, ["La [Parole]"], x_cam + 0.1, "Ce que dit la Bible", hl=x_ref, size=84)
    tag(stn, 80, 350, ref_txt, x_ref, "acc", 46)
    sfx("spark", x_ref, 1.6)
    v = put(stn, 80, 450, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.25">{verse_html}</div>', "headline", "width:880px")
    blur_in(v, x_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    sticker(stn, "pupitre-parole", 1080, 260, 420, x_ref + 0.2, rot=2)
    sticker(stn, "livre-croix-ouvert", 1500, 520, 330, x_text + 0.4, rot=-3)
    ref(stn, 80, 830, ref_txt.upper() + " · LSG 1910", x_ref + 0.4)
    SUP.append((x_text - 0.15, x_end))
    return stn


# ================================================================ 01 · Le piège
S = nxt(0.0)
sticker(S, "baton-augmentation", 1060, 250, 380, 0.0, rot=-2, instant=True)
title(S, ["Une augmentation…", "et [rien] de plus ?"], 0.0, "À la fin du mois", hl=5.0)
stk(S, "seau-perce", 1500, 380, 300, 4.0, rot=4)
tg(S, 480, "Où est passé cet argent ?", 8.1, "acc", 40)
hit(8.2, 0.7)

S = nxt(10.2)
title(S, ["L'inflation du", "[mode de vie]"], 10.3, "Ce phénomène a un nom", hl=11.6)
stk(S, "escalier-depenses", 1150, 300, 560, 10.8)
tg(S, 480, "Plus on gagne, plus on dépense", 13.6, "acc", 40)
hit(11.8)

S = nxt(17.3)
title(S, ["La Bible en", "parlait [déjà]"], 17.4, "Bien avant nos cartes", hl=18.4)
stk(S, "livre-croix-ouvert", 1050, 300, 380, 17.6, rot=-3)
stk(S, "carte-bancaire", 1500, 280, 260, 19.6, rot=6)
stk(S, "colis-livraison", 1520, 520, 240, 20.6, rot=-4)

S = nxt(21.8)
title(S, ["Au [programme]"], 21.9, "Dans cette vidéo", hl=22.6)
tg(S, 400, "Ce que c'est vraiment", 23.6, "", 40)
tg(S, 490, "Pourquoi c'est dangereux", 25.4, "", 40)
tg(S, 580, "Ce que dit la Bible", 27.0, "", 40)
tg(S, 670, "5 étapes concrètes", 28.4, "acc", 40)
stk(S, "baton-pense", 1450, 260, 320, 22.2)

S = nxt(30.4)
title(S, ["Une règle", "très [simple]"], 30.5, "Reste jusqu'à la fin", hl=33.4)
stk(S, "enveloppe-salaire", 1050, 300, 300, 31.0, rot=-4)
stk(S, "pieces-moitie", 1450, 340, 380, 33.6, rot=2)
tg(S, 480, "À chaque augmentation", 34.6, "acc", 40)
hit(33.6)

S = nxt(36.8)
title(S, ["Qu'est-ce que", "l'[inflation] du mode de vie ?"], 36.9, "Commençons", hl=39.4, size=70)
stk(S, "graphique-hausse", 1250, 300, 420, 40.6, rot=-2)
tg(S, 480, "Les dépenses montent au rythme des revenus", 40.8, "acc", 34)

S = nxt(43.9)
title(S, ["+100 € gagnés…", "+100 € [dépensés]"], 44.0, "Exemple", hl=45.6)
stk(S, "baton-augmentation", 1150, 260, 360, 44.2)
coins(S, 1500, 520, 44.6, n=5, spread=220, size=60)
bw("Parfois plus", 47.1, 0.9, 100)

S = nxt(48.8)
title(S, ["De petites", "[choses]"], 48.9, "Au début", hl=49.8)
tg(S, 430, "Le restaurant plus souvent", 50.7, "", 38)
tg(S, 520, "Un abonnement de plus", 52.6, "", 38)
tg(S, 610, "Un téléphone plus récent", 54.0, "acc", 38)
stk(S, "cafe", 1050, 300, 220, 50.8, rot=-4)
stk(S, "telephone-abonnements", 1350, 260, 260, 52.7, rot=3)
stk(S, "boite-smartphone", 1600, 480, 240, 54.1, rot=-3)

S = nxt(57.3)
title(S, ["Les grandes", "[décisions]"], 57.4, "Puis viennent", hl=58.4)
stk(S, "baton-voiture-hesite", 1050, 260, 460, 59.0)
stk(S, "maison-garage", 1530, 420, 320, 60.6, rot=3)
tg(S, 480, "Voiture, appartement, vacances", 59.4, "", 38)

S = nxt(63.6)
title(S, ["Aucun choix", "n'est [mauvais]"], 63.7, "Pris un par un", hl=64.6)
stk(S, "escalier-depenses", 1150, 300, 560, 65.8)
tg(S, 480, "Mais ils deviennent la normalité", 65.8, "acc", 38)

S = nxt(69.0)
title(S, ["Plaisir, habitude,", "puis [besoin]"], 69.1, "Petit à petit", hl=72.0)
stk(S, "baton-tapis-roulant", 1150, 260, 520, 69.6)
bw("Besoin", 72.0, 0.9)

S = nxt(73.3)
title(S, ["Deux fois plus…", "toujours [serré]"], 73.4, "Un jour", hl=76.4)
stk(S, "baton-soucieux", 1080, 260, 320, 73.8)
stk(S, "pile-factures", 1480, 380, 300, 79.0, rot=4)
tg(S, 480, "Pas plus de paix", 78.0, "", 38)
tg(S, 570, "Seulement des factures plus grandes", 79.4, "acc", 36)

S = nxt(81.5)
title(S, ["Une récompense", "[méritée]"], 81.6, "Le piège", hl=87.4)
stk(S, "baton-vitrine", 1250, 260, 460, 82.0)
tg(S, 480, "Jamais une mauvaise décision en apparence", 83.6, "", 34)
hit(87.6)

S = nxt(89.0)
title(S, ["Es-tu", "[concerné] ?"], 89.1, "Trois signes", hl=89.9)
stk(S, "baton-pense", 1100, 260, 320, 89.4)
stk(S, "bocal-presque-vide", 1500, 400, 260, 94.6, rot=4)
tg(S, 480, "1 · Ton revenu a augmenté…", 92.9, "", 38)
tg(S, 570, "… mais ton épargne n'a pas bougé", 95.4, "acc", 36)

S = nxt(98.5)
title(S, ["L'exception devient", "[automatique]"], 98.6, "Signe 2", hl=102.4)
tg(S, 430, "Le restaurant du vendredi", 102.8, "", 38)
tg(S, 520, "La livraison du dimanche", 104.4, "", 38)
tg(S, 610, "Le dernier modèle", 105.9, "acc", 38)
stk(S, "cafe", 1080, 300, 240, 102.9, rot=-4)
stk(S, "colis-livraison", 1450, 300, 300, 104.5, rot=3)

S = nxt(107.3)
title(S, ["« Quand je gagnerai", "un peu [plus]… »"], 107.4, "Signe 3", hl=110.0)
stk(S, "baton-tapis-roulant", 1150, 260, 520, 107.8)
bw("Enfin tranquille ?", 110.4, 1.0, 90)

S = nxt(112.6)
title(S, ["Ne te juge pas", "trop [durement]"], 112.7, "Si tu te reconnais", hl=115.0)
stk(S, "baton-serein", 1400, 260, 320, 113.0)
tg(S, 480, "C'est très courant", 115.6, "", 38)
tg(S, 570, "Le voir pour changer de direction", 118.6, "acc", 36)

# ================================================================ 02 · Ce que dit la Bible
parole(122.1, "Ecclésiaste 5.9", 125.8,
       f"« Celui qui aime l'argent {m(0, 'n’est pas rassasié')} par l'argent, et celui qui aime les richesses "
       f"{m(1, 'n’en profite pas')}. C'est encore là une vanité. »", 128.9, 136.3, [130.4, 133.6], size=48)

S = nxt(136.3)
title(S, ["Le plus riche", "de son [époque]"], 136.4, "Salomon", hl=139.2)
stk(S, "piedestal-pieces", 1250, 300, 380, 136.8)
tg(S, 480, "L'argent ne rassasie pas", 141.6, "acc", 40)

S = nxt(144.9)
title(S, ["Plus on en a,", "plus on en [veut]"], 145.0, "Le constat", hl=146.2)
stk(S, "tapis-roulant-pieces", 1200, 320, 480, 145.2)
tg(S, 480, "« C'est assez » : jamais", 148.6, "acc", 40)

S = nxt(151.3)
title(S, ["Chaque confort,", "un nouveau [départ]"], 151.4, "L'inflation, c'est cela", hl=155.2)
stk(S, "escalier-depenses", 1150, 300, 560, 151.6)
tg(S, 480, "On ne profite pas de ce qu'on a", 157.2, "acc", 38)

parole(162.0, "Luc 12.15", 165.2,
       f"« Gardez-vous avec soin de toute {m(0, 'avarice')} ; car la vie d'un homme {m(1, 'ne dépend pas de ses biens')}, "
       "fût-il dans l'abondance. »", 167.4, 174.0, [169.4, 171.2], size=52)

S = nxt(174.0)
title(S, ["L'homme", "[riche]"], 174.1, "Une histoire de Jésus", hl=176.4)
stk(S, "greniers", 1200, 300, 560, 176.2)
tg(S, 480, "Une récolte exceptionnelle", 176.6, "acc", 38)

S = nxt(178.6)
title(S, ["Des greniers", "plus [grands]"], 178.7, "Sa première pensée", hl=183.6)
tg(S, 430, "Ni remercier, ni partager", 179.4, "", 38)
tg(S, 520, "« J'abattrai mes greniers… »", 181.8, "acc", 38)
stk(S, "greniers", 1250, 320, 520, 179.0, rot=2)
ref(S, 80, 830, "LUC 12.18 · LSG 1910", 182.0)
hit(186.0, 0.7)

S = nxt(186.2)
title(S, ["L'inflation du mode de vie", "il y a [2000 ans]"], 186.3, "Plus de revenus, plus grand", hl=189.4, size=70)
stk(S, "baton-pense", 1400, 260, 320, 186.6)

S = nxt(191.6)
title(S, ["« [Insensé] ! »"], 191.7, "Dieu lui répond", hl=192.6)
tg(S, 420, "Cette nuit même ton âme te sera redemandée", 193.6, "acc", 34)
stk(S, "livre-croix-ouvert", 1300, 300, 400, 192.0, rot=-3)
ref(S, 80, 830, "LUC 12.20 · LSG 1910", 192.4)
bw("Insensé", 192.6, 0.8)
SUP.append((191.5, 196.6))

S = nxt(196.7)
title(S, ["Riche pour", "[Dieu]"], 196.8, "Jésus ne condamne pas la récolte", hl=203.6)
stk(S, "baton-priere", 1100, 260, 300, 197.0)
stk(S, "croix-verte", 1500, 320, 240, 202.4, rot=4)
tg(S, 480, "Mais un cœur qui ne pense qu'à agrandir", 199.2, "acc", 34)

parole(204.8, "Proverbes 21.20", 208.6,
       f"« De précieux trésors et de l'huile sont dans la {m(0, 'demeure du sage')} ; mais l'homme insensé {m(1, 'les engloutit')}. »",
       210.6, 216.8, [213.4, 215.4], size=52)

S = nxt(216.8)
title(S, ["Le sage garde", "une [réserve]"], 216.9, "La différence", hl=217.6)
stk(S, "tresor-huile", 1050, 320, 380, 217.2, rot=-3)
stk(S, "seau-perce", 1500, 360, 280, 219.0, rot=4)
tg(S, 480, "L'insensé consomme tout", 218.8, "", 38)

S = nxt(222.2)
title(S, ["Une question", "d'[habitude]"], 222.3, "Pas de montant", hl=224.6)
stk(S, "bocal-plein", 1300, 320, 320, 226.2, rot=-3)
tg(S, 480, "Gagner peu et mettre de côté", 226.2, "", 38)
tg(S, 570, "c'est déjà la sagesse", 229.0, "acc", 38)

S = nxt(232.1)
title(S, ["La [comparaison]"], 232.2, "Ce qui pousse à tout engloutir", hl=234.6)
stk(S, "baton-reseaux", 1300, 260, 400, 232.6)
tg(S, 430, "Les collègues changent de voiture", 236.8, "", 36)
tg(S, 520, "Les amis publient leurs vacances", 238.9, "", 36)
tg(S, 610, "Une vie plus belle que la nôtre", 241.0, "acc", 36)

S = nxt(244.6)
title(S, ["Vivre pour", "être [vu] ?"], 244.7, "Sans le vouloir", hl=246.4)
stk(S, "baton-jaloux", 1250, 260, 420, 244.9)
tg(S, 480, "… ou pour être fidèle", 247.6, "acc", 40)

S = nxt(249.1)
title(S, ["Si cette vidéo", "t'[aide]…"], 249.2, "Un instant", hl=250.4)
tg(S, 470, "Abonne-toi", 251.8, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", 253.6, "", 36)
stk(S, "croix-verte", 1200, 280, 260, 249.5, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 249.9, rot=2)
bw("Abonne-toi", 251.8, 1.0)

# ================================================================ 03 · Le remède
S = nxt(258.2)
title(S, ["Quel est le", "[remède] ?"], 258.3, "Alors", hl=259.0)
stk(S, "baton-pense", 1400, 260, 320, 258.6)
tg(S, 480, "Pas refuser tout confort", 259.8, "", 38)
tg(S, 570, "Le contentement", 264.6, "acc", 44)
bw("Contentement", 264.6, 1.0, 100)

parole(266.3, "Philippiens 4.11-12", 270.0,
       f"« J'ai {m(0, 'appris')} à être content de l'état où je me trouve. Je sais vivre dans l'humiliation, "
       f"et je sais vivre {m(1, 'dans l’abondance')}. »", 270.8, 278.0, [271.4, 276.4], size=50)

S = nxt(278.0)
title(S, ["Le contentement", "[s'apprend]"], 278.1, "Remarque le mot", hl=281.6)
bw("Appris", 279.0, 0.8, 130)
stk(S, "baton-lit-livre", 1350, 260, 320, 278.4)
tg(S, 480, "Il n'est pas naturel", 280.2, "", 38)

S = nxt(283.1)
title(S, ["Manque ou", "[abondance]"], 283.2, "Paul a connu les deux", hl=285.0)
stk(S, "baton-serein", 1100, 260, 320, 283.6)
stk(S, "croix-verte", 1500, 320, 240, 288.2, rot=4)
tg(S, 480, "Son cœur restait en Christ", 286.4, "acc", 38)

S = nxt(290.4)
title(S, ["Pas de la", "[résignation]"], 290.5, "Le contentement", hl=293.2)
stk(S, "colombe", 1300, 300, 360, 294.4, rot=3)
tg(S, 480, "Ne plus laisser tes revenus", 294.4, "", 36)
tg(S, 570, "décider de ta paix", 295.8, "acc", 36)

S = nxt(297.3)
title(S, ["Dire [merci]", "aujourd'hui"], 297.4, "Concrètement", hl=298.6)
stk(S, "baton-content", 1300, 260, 420, 297.6)
tg(S, 480, "Sans attendre d'avoir plus", 300.6, "acc", 38)

S = nxt(303.3)
title(S, ["La place que seul", "[Dieu] peut remplir"], 303.4, "Ni voiture, ni salon", hl=307.6)
stk(S, "coeur-receptacle", 1100, 300, 340, 304.0, rot=-3)
stk(S, "maison-garage", 1530, 420, 300, 305.4, rot=3)

S = nxt(309.8)
title(S, ["Une liberté", "[immense]"], 309.9, "Ne plus courir", hl=311.4)
stk(S, "chaine-cassee", 1050, 320, 320, 310.4, rot=-3)
stk(S, "tapis-roulant-pieces", 1480, 340, 360, 312.6, rot=3)
tg(S, 480, "après ce que les autres possèdent", 312.6, "acc", 36)

parole(314.7, "1 Timothée 6.6-8", 318.6,
       f"« C'est, en effet, une grande source de gain que {m(0, 'la piété avec le contentement')} ; car nous n'avons rien apporté "
       "dans le monde, et il est évident que nous n'en pouvons rien emporter ; si donc nous avons la nourriture et le vêtement, "
       f"{m(1, 'cela nous suffira')}. »", 320.4, 333.7, [322.6, 331.8], size=36)

S = nxt(333.7)
title(S, ["Le vrai", "[gain]"], 333.8, "Pas un salaire plus élevé", hl=334.8)
stk(S, "panier-besoins", 1100, 300, 320, 334.0, rot=-3)
stk(S, "vetements-plies", 1500, 360, 280, 334.6, rot=3)
tg(S, 480, "La piété avec le contentement", 336.6, "acc", 38)

S = nxt(339.1)
title(S, ["Dieu, contre", "ton [confort] ?"], 339.2, "Attention", hl=341.0)
stk(S, "baton-content", 1300, 260, 400, 339.4)
tg(S, 480, "« Dieu nous donne… pour que nous en jouissions »", 342.6, "acc", 30)
ref(S, 80, 830, "1 TIMOTHÉE 6.17 · LSG 1910", 343.0)

S = nxt(347.6)
title(S, ["Profiter n'est", "pas un [péché]"], 347.7, "Une augmentation", hl=348.8)
stk(S, "famille-sortie", 1250, 300, 520, 348.0)
tg(S, 480, "Le danger : un train de vie", 349.6, "", 36)
tg(S, 570, "qui monte tout seul", 352.4, "acc", 36)

# ================================================================ 04 · 5 étapes
S = nxt(355.4)
title(S, ["étapes", "[concrètes]"], 355.5, "Passons à la pratique", hl=357.8)
counter(S, 80, 430, 0, 5, 357.4, 0.8, " étapes", 170)
stk(S, "baton-budget", 1250, 260, 480, 355.8)

S = nxt(360.1)
title(S, ["Définis ton", "« [assez] »"], 360.2, "Étape 1", hl=361.8)
bw("Assez", 361.8, 0.8, 130)
stk(S, "baton-ecrit-liste", 1250, 260, 460, 363.0)
tg(S, 480, "Logement, nourriture, transport", 365.8, "", 36)
tg(S, 570, "Santé, un peu de loisirs", 368.8, "acc", 36)

S = nxt(371.3)
title(S, ["Ton niveau de vie", "[choisi]"], 371.4, "Ce chiffre", hl=372.6)
stk(S, "feuille-liste", 1080, 320, 300, 371.6, rot=-3)
stk(S, "baton-reseaux", 1500, 280, 320, 375.8, rot=2)
tg(S, 480, "Sinon : décidé par tes envies", 373.8, "", 36)
tg(S, 570, "et par ton entourage", 376.4, "acc", 36)

S = nxt(378.8)
title(S, ["La règle de", "l'[augmentation]"], 378.9, "Étape 2", hl=380.4)
tg(S, 480, "La règle promise au début", 381.4, "acc", 38)
tg(S, 570, "Décide avant que l'argent arrive", 383.4, "", 36)
stk(S, "enveloppe-salaire", 1250, 300, 380, 383.0, rot=-3)
hit(381.6)

S = nxt(388.5)
title(S, ["Moitié, [moitié]"], 388.6, "Par exemple", hl=389.2)
stk(S, "pieces-moitie", 1250, 300, 520, 388.8)
tg(S, 420, "½ pour construire : dette, épargne, don", 390.0, "", 32)
tg(S, 510, "½ pour profiter, avec joie", 394.6, "acc", 36)

S = nxt(399.3)
title(S, ["Tes finances", "vont plus [vite]"], 399.4, "Ta vie progresse", hl=401.4)
stk(S, "piles-croissantes", 1100, 340, 420, 399.6, rot=-2)
stk(S, "graphique-hausse", 1550, 320, 300, 401.4, rot=3)

S = nxt(402.9)
title(S, ["Le principe", "du [sage]"], 403.0, "Pas un verset : une application", hl=406.6)
stk(S, "tresor-huile", 1300, 320, 400, 404.0, rot=-2)
tg(S, 480, "Garder une réserve", 406.8, "", 38)
tg(S, 570, "au lieu de tout engloutir", 408.0, "acc", 38)

S = nxt(409.8)
title(S, ["Attends avant les", "gros [achats]"], 409.9, "Étape 3", hl=411.4)
counter(S, 80, 430, 0, 30, 412.8, 1.0, " jours", 150)
stk(S, "baton-sablier", 1300, 260, 420, 410.2)

S = nxt(416.5)
title(S, ["Prie, parles-en,", "[compare]"], 416.6, "Pendant ce temps", hl=418.0)
stk(S, "couple-lit-bible", 1250, 280, 460, 416.8)
tg(S, 480, "Toujours là après un mois ?", 419.6, "", 36)
tg(S, 570, "Achète en paix", 422.6, "", 36)
tg(S, 660, "Souvent, l'envie disparaît", 424.4, "acc", 36)

S = nxt(427.0)
title(S, ["Fais le", "[tri]"], 427.1, "Étape 4", hl=428.0)
stk(S, "baton-ciseaux-carte", 1100, 260, 320, 427.4)
stk(S, "telephone-abonnements", 1500, 320, 280, 432.0, rot=3)
tg(S, 480, "Une fois par trimestre", 429.2, "", 38)
tg(S, 570, "Abonnements, forfaits, assurances", 434.0, "acc", 34)

S = nxt(435.8)
title(S, ["Sans [bruit]"], 435.9, "Les petites sommes", hl=437.6)
stk(S, "robinet-goutte", 1300, 300, 380, 436.2)
tg(S, 420, "La première trace", 438.6, "", 38)
tg(S, 510, "de l'inflation du mode de vie", 439.6, "acc", 38)

S = nxt(441.1)
title(S, ["Fais grandir ta", "[générosité]"], 441.2, "Étape 5", hl=443.0)
stk(S, "baton-donne", 1250, 260, 500, 441.4)
tg(S, 480, "Revenus en hausse, don en hausse", 444.6, "acc", 36)

S = nxt(447.9)
title(S, ["L'argent n'est pas", "ton [maître]"], 448.0, "Donner en premier", hl=450.6)
stk(S, "enveloppe-don", 1080, 340, 280, 448.2, rot=-4)
stk(S, "coeur-receptacle", 1480, 320, 300, 449.0, rot=3)
tg(S, 480, "Ta richesse ne sert pas qu'à toi", 452.0, "acc", 36)

parole(455.6, "Proverbes 30.8", 458.0,
       f"« Ne me donne {m(0, 'ni pauvreté, ni richesse')}, accorde-moi {m(1, 'le pain qui m’est nécessaire')}. »",
       459.7, 464.8, [460.6, 462.6], size=56)

S = nxt(464.8)
title(S, ["Un cœur", "[libre]"], 464.9, "Ni manquer, ni oublier Dieu", hl=466.0)
stk(S, "baton-priere", 1100, 260, 300, 465.0)
stk(S, "colombe", 1500, 320, 320, 466.4, rot=3)

# ================================================================ 05 · Exemple
S = nxt(470.1)
title(S, ["Un exemple :", "[Marc]"], 470.2, "Prenons", hl=472.0)
stk(S, "baton-augmentation", 1250, 260, 400, 471.7)
tg(S, 480, "+300 € par mois", 473.0, "acc", 48)

S = nxt(474.9)
title(S, ["Changer de", "[voiture] ?"], 475.0, "Sa première idée", hl=476.2)
stk(S, "baton-voiture-hesite", 1250, 260, 500, 475.2)
tg(S, 480, "… et prendre un crédit", 476.8, "", 38)

S = nxt(478.2)
title(S, ["Il décide", "à l'[avance]"], 478.3, "La règle de l'augmentation", hl=483.0)
stk(S, "couple-budget", 1250, 280, 480, 481.1)
tg(S, 480, "Avec sa femme, dans la prière", 481.4, "acc", 36)

S = nxt(485.0)
title(S, ["Les [300 €]", "sont partagés"], 485.1, "Avant d'arriver", hl=485.8)
tg(S, 430, "150 € · crédit, puis épargne", 485.4, "", 36)
tg(S, 520, "50 € · don", 489.3, "", 36)
tg(S, 610, "100 € · sorties et vacances", 490.6, "acc", 36)
stk(S, "enveloppes-budget", 1300, 300, 460, 485.6, rot=-2)

S = nxt(495.3)
title(S, ["Il garde sa", "[voiture]"], 495.4, "Elle roule très bien", hl=496.6)
stk(S, "baton-vieille-voiture", 1250, 260, 480, 495.6)

S = nxt(497.8)
title(S, ["Un an plus", "[tard]"], 497.9, "Résultat", hl=498.6)
tg(S, 430, "Crédit soldé", 499.6, "", 38)
tg(S, 520, "Une vraie réserve", 501.0, "", 38)
tg(S, 610, "Une famille qui profite", 502.8, "acc", 38)
stk(S, "couple-epargne", 1050, 300, 360, 500.4, rot=-2)
stk(S, "famille-sortie", 1480, 360, 380, 502.8, rot=2)

S = nxt(505.0)
title(S, ["Avancer, sans", "entrer dans la [course]"], 505.1, "Marc a su", hl=506.6, size=72)
stk(S, "tapis-roulant-pieces", 1300, 320, 420, 505.4)
tg(S, 480, "Un exemple, à adapter à ta situation", 507.8, "", 34)

# ================================================================ 06 · À retenir
S = nxt(512.8)
title(S, ["L'[essentiel]"], 512.9, "Retenons", hl=513.4)
tg(S, 420, "Dépenser plus chaque fois", 513.8, "", 38)
tg(S, 510, "que l'on gagne plus", 515.6, "acc", 38)
stk(S, "escalier-depenses", 1300, 300, 520, 514.0)

S = nxt(519.2)
title(S, ["Ce que dit la", "[Bible]"], 519.3, "Trois avertissements", hl=520.0)
tg(S, 430, "L'argent ne rassasie pas", 520.6, "", 38)
tg(S, 520, "La vie ne dépend pas des biens", 522.6, "", 38)
tg(S, 610, "Le sage garde une réserve", 524.4, "acc", 38)
stk(S, "livre-croix-ouvert", 1350, 300, 400, 519.6, rot=-3)

S = nxt(526.1)
title(S, ["Le [contentement]"], 526.2, "Le remède", hl=527.0)
stk(S, "baton-content", 1300, 260, 420, 526.4)
tg(S, 450, "Il s'apprend", 527.8, "acc", 40)

S = nxt(529.1)
title(S, ["5 [étapes]"], 529.2, "Retiens", hl=529.6)
for k, (txt, x) in enumerate([("1 · Définis ton « assez »", 530.6), ("2 · La règle de l'augmentation", 532.6),
                              ("3 · Attends avant les gros achats", 535.0), ("4 · Fais le tri régulièrement", 537.0),
                              ("5 · Fais grandir ta générosité", 538.6)]):
    tag(S, 80, 360 + k * 80, txt, x, "acc" if k == 4 else "", 32)
stk(S, "pieces-moitie", 1350, 320, 440, 529.6)

S = nxt(541.0)
title(S, ["Écris ton", "« [assez] »"], 541.1, "Cette semaine", hl=543.6)
stk(S, "baton-ecrit-liste", 1250, 260, 460, 541.3)
tg(S, 480, "… et prie sur ce chiffre", 545.4, "acc", 38)

S = nxt(547.8)
title(S, ["Ta paix ne dépend", "pas de ton [salaire]"], 547.9, "Souviens-toi", hl=549.6)
stk(S, "baton-priere", 1100, 260, 300, 548.0)
stk(S, "colombe", 1500, 320, 300, 549.6, rot=3)
tg(S, 480, "Elle dépend de Celui", 549.8, "", 36)
tg(S, 570, "à qui tu fais confiance", 550.6, "acc", 36)

S = nxt(551.7)
title(S, ["Ton niveau de vie", "a-t-il [grimpé] ?"], 551.8, "Et toi", hl=553.4)
stk(S, "baton-pense", 1450, 240, 300, 551.9)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, 555.5, 14)
sfx("click", 555.5, 0.8)
tg(S, 620, "Abonne-toi", 558.7, "acc", 56)

cam(VOICE_END + 0.1, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Le piège", 0, 122.1), ("02", "L'avertissement", 122.1, 258.2), ("03", "Le remède", 258.2, 355.4),
              ("04", "5 étapes", 355.4, 470.1), ("05", "Exemple", 470.1, 512.8), ("06", "À retenir", 512.8, DUR)],
    suppress=SUP + [(VOICE_END + 0.2, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.7,
)
