"""Vidéo longue « Ce que la Bible dit sur les cartes de crédit » — style 02 en 16:9, ~9 min 30.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 4 pièges, 5 règles, 4 signaux d'alarme, exemple (Karim), récapitulatif.
Les temps sont lus dans transcript.json (voix fournie par l'utilisateur ; répétitions de la synthèse vocale retirées).

Lancer : python3 build.py   (puis npx hyperframes check et npx hyperframes render -q draft)
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "kit-style-02", "moteur"))
import style02 as s  # noqa: E402

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Ce que la Bible dit sur les cartes de crédit", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 552.0
s.setup(here=HERE, duration=567.5, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
from style02 import *  # noqa: E402,F401,F403

ST = [(c if r % 2 == 0 else COLS - 1 - c, r) for r in range(ROWS) for c in range(COLS)]
_n = [0]
SUP = []
_TR = json.load(open(os.path.join(HERE, "transcript.json"), encoding="utf-8"))


def _norm(x):
    return re.sub(r"[^\w]+", "", unicodedata.normalize("NFC", x.lower()))


def W(prefix, after=0.0, nth=0):
    """Début (en secondes) du n-ième mot commençant par `prefix`, après l'instant `after` (repli approximatif signalé)."""
    pn = _norm(prefix).rstrip("s")
    k = 0
    for w in _TR:
        if w["start"] >= after and pn in _norm(w["text"]):
            if k == nth:
                return round(w["start"], 2)
            k += 1
    import difflib
    cand = [w for w in _TR if after <= w["start"] <= after + 25]
    best = difflib.get_close_matches(_norm(prefix), [_norm(w["text"]) for w in cand], n=1, cutoff=0.55)
    if best:
        for w in cand:
            if _norm(w["text"]) == best[0]:
                print("  ~ repli", prefix, "->", w["text"], w["start"])
                return round(w["start"], 2)
    raise KeyError((prefix, after))


def nxt(t):
    stn = ST[_n[0]]
    _n[0] += 1
    cam(t, stn)
    return stn


def title(stn, lines, t, kicker, hl=None, size=80):
    size = min(size, 78 if len(lines) > 1 else 96)
    return headline(stn, 172, lines, t, kicker=kicker, hl_t=hl, size=size, x=80)


def stk(stn, name, px, py, w, t, rot=-2):
    return sticker(stn, name, px, py, w, t, rot=rot)


def tg(stn, y, text, t, cls="", size=40):
    return tag(stn, 80, y, text, t, cls, size)


def bw(text, t, dur=0.9, size=110):
    bigword(text, t, dur, y=720, size=size)


def m(k, word):
    return f'<em class="hl m{k}"><span>{word}</span><i></i></em>'


def parole(t_cam, ref_txt, t_ref, verse_html, t_text, t_end, marks, size=44, ref_y=830, ref_label=None):
    """Séquence « Parole », identique pour chaque passage ; sous-titres coupés pendant la citation."""
    verse_html = verse_html.replace(" »", "&nbsp;»").replace("« ", "«&nbsp;").replace(" ;", "&nbsp;;").replace(" :", "&nbsp;:")
    stn = nxt(t_cam)
    title(stn, ["La [Parole]"], t_cam + 0.1, "Ce que dit la Bible", hl=t_ref, size=84)
    tag(stn, 80, 350, ref_txt, t_ref, "acc", 46)
    sfx("spark", t_ref, 1.6)
    v = put(stn, 80, 450, f'<div class="h" style="font-size:{size}px;font-weight:700;line-height:1.25">{verse_html}</div>', "headline", "width:880px")
    blur_in(v, t_text - 0.1, 20)
    for k, mt in enumerate(marks):
        tween(f"#{v} .m{k} i", "scaleX: 0", 'scaleX: 1, duration: 0.45, ease: "power3.out"', mt)
    sticker(stn, "pupitre-parole", 1080, 260, 420, min(t_ref + 0.2, t_cam + 0.6), rot=2)
    sticker(stn, "livre-croix-ouvert", 1500, 520, 330, t_text + 0.4, rot=-3)
    ref(stn, 80, ref_y, (ref_label or ref_txt.upper()) + " · LSG 1910", t_ref + 0.4)
    SUP.append((t_text - 0.1, t_end))
    return stn


# ================================================================ 01 · Introduction
S = nxt(0.0)
title(S, ["Carte de crédit :", "[bénédiction] ou piège ?"], 0.1, "Une question", hl=2.6, size=78)
stk(S, "baton-tente-carte", 1100, 240, 400, 0.4, rot=-2)
bw("Piège ?", 3.0, 1.0, 120)

S = nxt(4.6)
title(S, ["Un outil…", "ou une [spirale] ?"], 4.7, "Pour certains, pratique", hl=W("spirale", 4.6), size=84)
tg(S, 450, "Pratique, rassurant", 6.2, "", 40)
tg(S, 540, "Indispensable ?", W("indispensable", 4.6), "acc", 40)
stk(S, "carte-chaine", 1100, 260, 400, W("spirale", 4.6), rot=-3)

S = nxt(11.7)
title(S, ["Et la [Bible]", "dans tout ça ?"], 11.8, "Une précision", hl=12.0)
tg(S, 450, "Aucune carte à l'époque", W("existait", 11.7), "acc", 40)
stk(S, "livre-croix-ouvert", 1050, 290, 400, 12.4, rot=-3)

S = nxt(17.0)
title(S, ["Dettes, promesses,", "[prudence]"], 17.1, "Elle parle de", hl=W("prudence", 17.0), size=78)
tg(S, 450, "Les dettes", W("dettes", 17.0), "", 38)
tg(S, 540, "Les promesses", W("promesses", 17.0), "", 38)
tg(S, 630, "La prudence", W("prudence", 17.0), "", 38)
tg(S, 720, "Ton cœur", W("cœur", 17.0), "acc", 40)
stk(S, "coeur-receptacle", 1150, 300, 330, W("cœur", 17.0), rot=-3)

S = nxt(22.6)
title(S, ["Deux [erreurs]", "fréquentes"], 22.7, "Attention", hl=23.4)
tg(S, 450, "1 · Condamner la carte", W("première", 22.6), "", 38)
tg(S, 540, "2 · La banaliser", W("deuxième", 22.6), "acc", 38)
stk(S, "baton-fardeau", 1100, 260, 320, W("première", 22.6))
stk(S, "baton-content", 1500, 330, 300, W("deuxième", 22.6), rot=3)

S = nxt(31.6)
title(S, ["Au [programme]"], 31.7, "Dans cette vidéo", hl=32.4)
tg(S, 420, "5 passages", W("cinq", 31.6, 0), "", 40)
tg(S, 510, "5 règles simples", W("cinq", 31.6, 1), "", 40)
tg(S, 600, "Des signaux d'alarme", W("signaux", 31.6), "", 40)
tg(S, 690, "Un exemple concret", W("exemple", 31.6), "acc", 40)
stk(S, "pupitre-parole", 1100, 260, 380, 32.4, rot=-2)

S = nxt(41.4)
title(S, ["Un test en", "trois [questions]"], 41.5, "Reste jusqu'à la fin", hl=W("test", 41.4) + 0.4)
counter(S, 80, 440, 0, 3, 43.0, 0.8, " questions", 120)
tg(S, 600, "Avant chaque paiement par carte", W("chaque", 41.4), "", 36)
tg(S, 690, "La règle qui change tout", W("règle", 41.4), "acc", 38)
stk(S, "baton-test-trois", 1150, 240, 330, 42.0)

S = nxt(50.0)
title(S, ["Pas un conseil", "[personnalisé]"], 50.1, "Une précision importante", hl=W("personnalisé", 50.0), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 50.0), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 50.0), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 51.0)
hit(W("personnalisé", 50.0), 0.8)

# ================================================================ 02 · Passage 1 : Proverbes 22.7
parole(58.5, "Proverbes 22.7", 61.4,
       f"« Le riche domine sur les pauvres, et {m(0, 'celui qui emprunte')} est {m(1, 'l’esclave')} de celui qui prête. »",
       63.0, 67.9, [W("emprunte", 63.0), W("esclave", 63.0)], size=52)

S = nxt(68.1)
title(S, ["Un mot fort :", "[esclave]"], 68.2, "Remarque", hl=W("esclave", 68.1), size=84)
tg(S, 450, "Pas un péché en soi", W("péché", 68.1), "", 38)
tg(S, 540, "Il décrit : une dépendance", W("dépendance", 68.1), "acc", 38)
stk(S, "baton-fardeau", 1150, 250, 320, 68.6)

S = nxt(75.2)
title(S, ["La banque avance", "l'[argent]"], 75.3, "Quand tu paies par carte", hl=W("avance", 75.2), size=78)
tg(S, 450, "Tu empruntes", W("empruntes", 75.2), "", 40)
tg(S, 540, "Elle attend d'être remboursée", W("attend", 75.2), "acc", 36)
stk(S, "carte-bancaire", 1100, 260, 380, 75.8, rot=-3)

S = nxt(82.6)
title(S, ["Tout rembourser :", "dépendance [légère]"], 82.7, "À la date prévue", hl=W("légère", 82.6), size=72)
tg(S, 450, "Pas d'intérêts à payer", W("laisses", 82.6) - 1.2, "acc", 38)
stk(S, "releve-propre", 1100, 270, 330, 83.2, rot=-2)

S = nxt(W("laisses", 82.6) - 0.3)
title(S, ["Un solde laissé :", "les [intérêts]"], W("laisses", 82.6) - 0.2, "Mais attention", hl=W("intérêts", 82.6), size=78)
tg(S, 450, "Ils travaillent contre toi", W("travaillent", 82.6), "acc", 38)
stk(S, "pile-factures", 1150, 280, 340, W("laisses", 82.6) + 0.4)

S = nxt(92.3)
title(S, ["Un taux souvent", "[élevé]"], 92.4, "Comparé à d'autres crédits", hl=W("élevé", 92.3), size=78)
tg(S, 450, "Lis les conditions de la tienne", W("Lis", 92.3), "acc", 38)
stk(S, "graphique-hausse", 1100, 270, 360, 93.0, rot=-2)

S = nxt(97.4)
title(S, ["Un petit solde…", "[anodin] ?"], 97.5, "Ça semble sans danger", hl=W("anodin", 97.4), size=84)
stk(S, "baton-content", 1150, 250, 300, 98.0)

tM = W("Mais", 98.0)
S = nxt(tM - 0.1)
title(S, ["Des intérêts sur", "les [intérêts]"], tM, "Mois après mois", hl=W("intérêts", tM), size=78)
tg(S, 450, "Une boule de neige qui grossit", W("boule", tM), "acc", 38)
stk(S, "boule-de-neige", 1050, 250, 480, tM + 0.5, rot=-2)

S = nxt(110.2)
title(S, ["Une dette longue,", "moins de [liberté]"], 110.3, "Quand elle dure", hl=W("liberté", 110.2), size=72)
tg(S, 450, "Choisir ton travail", W("travail", 110.2), "", 36)
tg(S, 530, "Donner", W("donner", 110.2), "", 36)
tg(S, 610, "Épargner", W("épargner", 110.2), "", 36)
tg(S, 690, "Dire non", W("dire", 110.2), "acc", 36)
stk(S, "baton-fardeau", 1150, 250, 320, 111.0)

S = nxt(118.0)
title(S, ["Plus [libre],", "ou plus dépendant ?"], 118.1, "Question 1", hl=W("libre", 118.0), size=72)
tg(S, 450, "Cet achat me rend plus libre…", W("libre", 118.0), "", 36)
tg(S, 540, "… ou plus dépendant ?", W("dépendant", 118.0), "acc", 36)
stk(S, "baton-test-trois", 1350, 230, 300, 119.0)
bw("Question 1", 118.3, 0.9, 100)

# ================================================================ 03 · Passage 2 : Luc 14.28
parole(123.4, "Luc 14.28", 126.2,
       f"« Car, quel est celui d'entre vous qui, voulant {m(0, 'bâtir une tour')}, ne s'assied d'abord pour "
       f"{m(1, 'calculer la dépense')} et voir s'il a de quoi la terminer ? »",
       129.0, 136.6, [W("bâtir", 129.0), W("calculer", 129.0)], size=44, ref_y=860)

S = nxt(136.8)
title(S, ["Une image de", "[bon sens]"], 136.9, "Jésus choisit", hl=W("sens", 136.8), size=84)
tg(S, 450, "Le prix à payer pour le suivre", W("prix", 136.8), "", 36)
tg(S, 540, "L'image : calculer avant", W("image", 136.8, 1), "acc", 38)
stk(S, "tour-chantier", 1050, 260, 440, 137.6, rot=-2)

S = nxt(144.7)
title(S, ["Avec une carte,", "tout paraît [facile]"], 144.8, "Le danger", hl=W("facile", 144.7), size=72)
tg(S, 450, "On passe la carte", W("passe", 144.7), "", 38)
tg(S, 540, "L'argent ne se voit pas partir", W("voit", 144.7), "acc", 36)
stk(S, "carte-bancaire", 1100, 260, 380, 145.3, rot=-3)

S = nxt(149.8)
title(S, ["Les billets,", "plus [visibles]"], 149.9, "Beaucoup constatent", hl=W("yeux", 149.8) - 0.6, size=84)
tg(S, 450, "On dépense plus facilement", W("facilement", 149.8), "", 38)
tg(S, 540, "par carte que par billets", W("billets", 149.8, 1), "acc", 38)
stk(S, "baton-tente-carte", 1100, 250, 380, 150.4)

S = nxt(155.7)
title(S, ["Calcule", "[avant]"], 155.8, "Alors", hl=156.4, size=96)
tg(S, 440, "Combien sur mon compte ?", W("compte", 155.7), "", 36)
tg(S, 530, "Quelles factures à venir ?", W("factures", 155.7), "", 36)
tg(S, 620, "Combien me reste-t-il vraiment ?", W("vraiment", 155.7), "acc", 36)
stk(S, "baton-ecrit-liste", 1100, 260, 340, 156.2)

S = nxt(162.2)
title(S, ["Pas l'argent ?", "Pas d'[achat]"], 162.3, "La règle", hl=W("achat", 162.2), size=78)
tg(S, 450, "Sinon, ton futur toi paie", W("futur", 162.2), "acc", 40)
stk(S, "baton-soucieux", 1150, 240, 290, 163.0)

S = nxt(169.0)
title(S, ["Ton futur toi", "n'a pas [voté]"], 169.1, "Et pourtant", hl=W("voté", 169.0), size=78)
tg(S, 450, "Il reçoit la facture, avec les intérêts", W("facture", 169.0), "acc", 34)
stk(S, "pile-factures", 1100, 270, 340, 169.8, rot=-2)

S = nxt(175.4)
title(S, ["Ai-je déjà", "cet [argent] ?"], 175.5, "Question 2", hl=W("argent", 175.4), size=84)
stk(S, "baton-test-trois", 1350, 230, 300, 176.0)
bw("Question 2", 175.6, 0.9, 100)

# ================================================================ 04 · Passage 3 : Psaume 37.21
parole(178.8, "Psaume 37.21", 181.0,
       f"« Le méchant emprunte, et {m(0, 'il ne rend pas')} ; mais le juste est compatissant, et {m(1, 'il donne')}. »",
       183.4, 188.4, [W("rend", 183.0), W("donne", 183.0)], size=52)

S = nxt(188.6)
title(S, ["Le problème :", "ne pas [rendre]"], 188.7, "Ici", hl=W("rendre", 188.6), size=78)
tg(S, 450, "Pas : emprunter", W("emprunter", 188.6), "", 40)
tg(S, 540, "Mais : ne pas rendre", W("rendre", 188.6), "acc", 40)
stk(S, "carte-chaine", 1100, 270, 400, 189.4, rot=-3)

S = nxt(194.5)
title(S, ["Une [parole]", "donnée"], 194.6, "Quand tu utilises une carte", hl=W("parole", 194.5))
tg(S, 450, "Tu promets de rembourser", W("promets", 194.5), "", 38)
tg(S, 540, "Une parole donnée à quelqu'un", W("quelqu", 194.5), "acc", 36)
stk(S, "baton-donne", 1150, 250, 330, 195.2)

S = nxt(199.3)
title(S, ["En retard, ou", "[minimum] seulement"], 199.4, "À éviter", hl=W("minimum", 199.3), size=72)
tg(S, 450, "Faire attendre l'autre", W("attendre", 199.3), "", 38)
tg(S, 540, "Se faire du mal à soi-même", W("mal", 199.3), "acc", 38)
stk(S, "baton-soucieux", 1150, 250, 290, 200.0)

S = nxt(206.0)
title(S, ["Le juste", "[donne]"], 206.1, "La fin du verset", hl=W("donne", 206.0), size=96)
tg(S, 450, "Moins de dettes", W("dettes", 206.0), "", 40)
tg(S, 540, "Plus de générosité", W("capacité", 206.0), "acc", 40)
stk(S, "enveloppe-don", 1100, 280, 340, 206.8, rot=-3)
stk(S, "baton-donne", 1500, 300, 330, W("capacité", 206.0), rot=2)

S = nxt(213.2)
title(S, ["Pourrai-je [tout]", "rembourser ?"], 213.3, "Question 3", hl=W("entièrement", 213.2), size=78)
tg(S, 450, "À la date prévue", W("date", 213.2), "acc", 40)
stk(S, "baton-test-trois", 1350, 230, 300, 214.0)
bw("Question 3", 213.5, 0.9, 100)

S = nxt(218.8)
title(S, ["Si cette vidéo", "t'[aide]…"], 218.9, "Un instant", hl=W("aide", 218.8))
tg(S, 450, "Abonne-toi", W("abonne", 218.8) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", 222.8, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 219.6, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 220.0, rot=2)
bw("Abonne-toi", W("abonne", 218.8) + 0.4, 1.0)

# ================================================================ 05 · Passage 4 : Proverbes 27.12
parole(226.9, "Proverbes 27.12", 229.0,
       f"« L'homme prudent {m(0, 'voit le mal et se cache')} ; les simples avancent et {m(1, 'sont punis')}. »",
       231.6, 236.9, [W("voit", 231.0), W("punis", 231.0)], size=52)

S = nxt(237.1)
title(S, ["Des [pièges]", "classiques"], 237.2, "Les cartes en ont", hl=W("pièges", 237.1), size=84)
tg(S, 450, "Le prudent les voit venir", W("venir", 237.1), "acc", 40)
stk(S, "piege-appat", 1050, 300, 500, 237.8, rot=-2)

S = nxt(240.9)
title(S, ["Piège 1 :", "la limite [élevée]"], 241.0, "Premier piège", hl=W("élevée", 240.9), size=78)
tg(S, 450, "On te propose d'augmenter ton plafond", W("plafond", 240.9), "", 34)
tg(S, 540, "Une limite haute n'est pas ton argent", W("possèdes", 240.9), "acc", 34)
stk(S, "jauge-limite", 1100, 260, 460, 241.6)

S = nxt(248.3)
title(S, ["Piège 2 :", "payer [plus tard]"], 248.4, "Deuxième piège", hl=W("tard", 248.3, 1), size=78)
tg(S, 450, "Paiement en plusieurs fois", W("plusieurs", 248.3), "", 38)
tg(S, 540, "Achat indolore, dette invisible", W("invisible", 248.3), "acc", 36)
stk(S, "calendrier-mois", 1100, 270, 400, 249.0, rot=-2)

S = nxt(257.0)
title(S, ["Piège 3 :", "les [avantages]"], 257.1, "Troisième piège", hl=W("avantages", 257.0), size=78)
tg(S, 450, "Points, remises, avantages", W("points", 257.0), "", 38)
tg(S, 540, "Ils coûtent plus qu'ils ne rapportent", W("coûtent", 257.0), "acc", 34)
stk(S, "cartes-eventail", 1050, 280, 460, 257.8, rot=-2)

S = nxt(266.0)
title(S, ["Piège 4 :", "le [minimum]"], 266.1, "Quatrième piège", hl=W("minimum", 266.0), size=84)
tg(S, 450, "On croit gérer la situation", W("impression", 266.0), "", 38)
tg(S, 540, "La dette peut durer très longtemps", W("longtemps", 266.0), "acc", 36)
stk(S, "baton-sablier", 1100, 250, 300, 266.8)

S = nxt(273.0)
title(S, ["Prudent,", "pas [peureux]"], 273.1, "Être prudent", hl=W("peur", 273.0), size=84)
tg(S, 450, "Voir le piège avant d'y mettre le pied", W("piège", 273.0), "acc", 34)
stk(S, "baton-pense", 1150, 240, 270, 273.8)

# ================================================================ 06 · Passage 5 : Romains 13.8
parole(277.8, "Romains 13.8", 279.9,
       f"« {m(0, 'Ne devez rien à personne')}, si ce n'est de {m(1, 'vous aimer les uns les autres')}. »",
       282.1, 285.9, [W("devez", 282.0), W("aimer", 282.0)], size=52)

S = nxt(286.0)
title(S, ["Un [idéal] :", "vivre sans dette"], 286.1, "Remarque", hl=W("idéal", 286.0), size=78)
tg(S, 450, "Certains : interdiction totale", W("interdiction", 286.0), "", 36)
tg(S, 540, "Les chrétiens ne sont pas tous d'accord", W("chrétiens", 286.0), "acc", 32)
stk(S, "livre-croix-ouvert", 1100, 280, 380, 286.8, rot=-3)

S = nxt(295.2)
title(S, ["Pas la dette", "comme [mode de vie]"], 295.3, "Le principe", hl=W("mode", 295.2), size=72)
tg(S, 450, "Ce que tu dois, tu dois pouvoir le rendre", W("rendre", 295.2), "acc", 32)
stk(S, "chaine-cassee", 1100, 280, 380, 296.0, rot=-3)

S = nxt(302.9)
title(S, ["À la fin du mois :", "[zéro]"], 303.0, "Pour la carte", hl=W("zéro", 302.9), size=78)
stk(S, "releve-propre", 1100, 270, 330, 303.6, rot=-2)
bw("Solde : 0 €", W("zéro", 302.9) + 0.3, 1.0, 100)

S = nxt(309.9)
title(S, ["La seule dette :", "l'[amour]"], 310.0, "Celle qui reste", hl=W("amour", 309.9), size=78)
stk(S, "coeur-receptacle", 1150, 280, 330, 310.6, rot=-3)
stk(S, "croix-verte", 1560, 340, 220, 313.0, rot=4)

# ================================================================ 07 · Cinq règles
S = nxt(315.9)
title(S, ["Cinq [règles]", "pour ta carte"], 316.0, "Passons à la pratique", hl=W("règles", 315.9), size=84)
counter(S, 80, 450, 0, 5, 317.0, 0.9, " règles", 130)
stk(S, "garde-fou-route", 1050, 300, 520, 316.6, rot=-1)

S = nxt(321.9)
title(S, ["Dépense l'argent", "que tu [as]"], 322.0, "Règle 1", hl=323.6, size=78)
tg(S, 450, "Avant de payer :", 325.0, "", 38)
tg(S, 540, "cet argent est sur mon compte", W("compte", 321.9), "acc", 38)
stk(S, "baton-budget", 1100, 250, 380, 322.6)

S = nxt(329.6)
title(S, ["Rembourse", "[tout] chaque mois"], 329.7, "Règle 2", hl=W("totalité", 329.6), size=78)
tg(S, 450, "Prélèvement automatique", W("prélèvement", 329.6), "", 38)
tg(S, 540, "Pas d'intérêts, pas d'oubli", W("intérêts", 329.6), "acc", 38)
stk(S, "calendrier-prelevement", 1050, 270, 500, 330.4, rot=-2)

S = nxt(339.0)
title(S, ["Une seule carte,", "[limite] raisonnable"], 339.1, "Règle 3", hl=W("limite", 339.0), size=72)
tg(S, 450, "Plus de cartes, plus dur à suivre", W("difficile", 339.0), "acc", 34)
stk(S, "carte-bancaire", 1100, 270, 380, 339.8, rot=-3)

S = nxt(345.9)
title(S, ["Suis tes", "[dépenses]"], 346.0, "Règle 4", hl=W("dépenses", 345.9), size=90)
tg(S, 450, "Alertes sur ton téléphone", W("alertes", 345.9), "", 38)
tg(S, 540, "Vérifie ton compte chaque semaine", W("vérifie", 345.9), "acc", 36)
stk(S, "telephone-alerte", 1150, 220, 290, 346.6)

S = nxt(352.3)
title(S, ["Pas d'[espèces],", "pas de minimum"], 352.4, "Règle 5", hl=W("espèces", 352.3), size=78)
tg(S, 450, "Jamais de retrait d'espèces", W("retrait", 352.3), "", 36)
tg(S, 540, "Jamais le minimum comme habitude", W("minimum", 352.3), "", 36)
tg(S, 630, "Les deux plus coûteux", W("coûteuses", 352.3), "acc", 38)
stk(S, "baton-ciseaux-carte", 1100, 260, 380, 353.0)

S = nxt(361.7)
title(S, ["L'[imprévu]", "arrive"], 361.8, "D'où naissent les dettes", hl=W("imprévu", 361.7), size=90)
tg(S, 450, "Voiture en panne", W("voiture", 361.7), "", 38)
tg(S, 540, "Facture médicale", W("médicale", 361.7), "acc", 38)
stk(S, "baton-vieille-voiture", 1100, 260, 380, 362.4)

tF = W("fonds", 361.7)
S = nxt(tF - 0.3)
title(S, ["Un petit [fonds]", "d'urgence"], tF - 0.2, "Prévois", hl=tF + 0.2, size=84)
tg(S, 450, "Éviter de payer sans pouvoir rembourser", W("évite", 361.7), "acc", 32)
stk(S, "enveloppes-budget", 1100, 280, 340, tF + 0.4, rot=-2)

S = nxt(370.9)
title(S, ["Même 20 €", "par [mois]"], 371.0, "Un début", hl=W("début", 370.9), size=90)
counter(S, 80, 450, 0, 20, 371.2, 0.9, " € / mois", 120)
stk(S, "baton-epargne", 1150, 260, 300, 371.8)

S = nxt(375.8)
title(S, ["Ton [épargne],", "pas une dette"], 375.9, "Quand l'imprévu arrive", hl=W("épargne", 375.8), size=78)
tg(S, 450, "Confiance en Dieu, et responsabilité", W("confiance", 375.8), "acc", 32)
stk(S, "baton-priere", 1100, 260, 300, 376.6)
stk(S, "croix-verte", 1560, 340, 220, W("confiance", 375.8), rot=4)

S = nxt(384.3)
title(S, ["Pas de [honte]"], 384.4, "Si tu ne peux pas encore", hl=W("honte", 384.3), size=96)
tg(S, 440, "Respecter ces règles pour le moment", 385.4, "", 36)
stk(S, "baton-content", 1150, 260, 300, 385.0)

tD = W("débit", 384.3)
S = nxt(tD - 0.9)
title(S, ["Une carte de", "[débit]"], tD - 0.8, "Utilise plutôt", hl=tD, size=90)
tg(S, 450, "Prélève directement sur ton compte", W("prélève", 384.3), "", 36)
tg(S, 540, "Tu ne dépenses que ce que tu as", W("vraiment", 392.3), "acc", 36)
stk(S, "carte-bancaire", 1100, 270, 380, tD, rot=-3)

S = nxt(396.4)
title(S, ["Ni péché,", "ni [obligation]"], 396.5, "Une carte de crédit", hl=W("obligation", 396.4), size=78)
tg(S, 450, "Un outil qui demande de la discipline", W("outil", 396.4), "acc", 34)
stk(S, "balance-carte-pieces", 1050, 270, 480, 397.2, rot=-2)

# ================================================================ 08 · Signaux d'alarme et pas pour s'en sortir
S = nxt(402.8)
title(S, ["Quatre signaux", "d'[alarme]"], 402.9, "Attention", hl=W("alarme", 402.8), size=84)
counter(S, 80, 440, 0, 4, 403.2, 0.8, " signaux", 120)
stk(S, "baton-soucieux", 1150, 260, 300, 403.4)

S = nxt(405.5)
title(S, ["Te reconnais-[tu] ?"], 405.6, "Les signaux", hl=406.2, size=84)
tg(S, 400, "1 · Dette exacte : inconnue", 405.8, "", 34)
tg(S, 490, "2 · Le minimum, mois après mois", W("2", 405.0) if False else 409.3, "", 34)
tg(S, 580, "3 · Une carte paie l'autre", 412.6, "", 34)
tg(S, 670, "4 · Relevé caché à tes proches", 417.2, "acc", 34)
stk(S, "baton-fardeau", 1150, 260, 320, 406.0)

S = nxt(420.3)
title(S, ["Agir,", "[sans honte]"], 420.4, "Si tu te reconnais", hl=W("honte", 420.3), size=90)
tg(S, 450, "La Bible parle de grâce autant que de sagesse", W("grâce", 420.3), "acc", 30)
stk(S, "colombe", 1100, 280, 300, 421.0, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("grâce", 420.3), rot=4)

S = nxt(429.0)
title(S, ["Trois [pas]"], 429.1, "Pour s'en sortir", hl=429.6, size=96)
tg(S, 400, "1 · Écris tout ce que tu dois", W("écris", 429.0), "", 36)
tg(S, 490, "2 · Arrête d'ajouter", W("arrête", 429.0), "", 36)
tg(S, 580, "3 · Rembourse le plus cher d'abord", W("rembourse", 429.0), "acc", 34)
stk(S, "baton-ecrit-liste", 1100, 260, 340, 429.6)

S = nxt(438.1)
title(S, ["Demande de", "l'[aide]"], 438.2, "Si c'est trop lourd", hl=W("aide", 438.1), size=90)
tg(S, 450, "Un conseiller en budget", W("conseiller", 438.1), "", 38)
tg(S, 540, "Une association spécialisée", W("association", 438.1), "acc", 38)
stk(S, "baton-conseillers", 1050, 290, 470, 438.8, rot=-2)

# ================================================================ 09 · Exemple : Karim
S = nxt(442.9)
title(S, ["Un exemple :", "[Karim]"], 443.0, "Prenons", hl=W("Karim", 442.9), size=90)
tg(S, 450, "Sa première carte de crédit", W("première", 444.0), "", 36)
tg(S, 540, "Courses et abonnements", W("abonnements", 444.0), "", 36)
tg(S, 630, "Tout payé en fin de mois", W("fin", 444.0), "acc", 36)
stk(S, "baton-content", 1450, 250, 300, 443.6)
stk(S, "carte-bancaire", 1100, 330, 340, 444.3, rot=-3)

S = nxt(452.0)
title(S, ["Une [promotion]", "l'attire"], 452.1, "Puis", hl=W("promotion", 452.0), size=84)
tg(S, 450, "Un nouvel ordinateur", W("ordinateur", 452.0), "", 38)
tg(S, 540, "À payer en plusieurs fois", W("plusieurs", 452.0), "", 38)
tg(S, 630, "« Ça passera »", W("passera", 452.0), "acc", 40)
stk(S, "baton-vitrine", 1100, 250, 380, 452.6)

S = nxt(457.6)
title(S, ["Il n'arrive plus", "à [rembourser]"], 457.7, "Quelques mois plus tard", hl=W("rembourser", 457.6), size=78)
tg(S, 450, "Le minimum seulement", W("minimum", 457.6), "", 38)
tg(S, 540, "Il n'ose plus voir son relevé", W("ose", 457.6), "acc", 36)
stk(S, "baton-soucieux", 1150, 250, 300, 458.2)
stk(S, "pile-factures", 1530, 440, 300, W("ose", 457.6), rot=3)

S = nxt(465.2)
title(S, ["Un soir,", "il [écrit] tout"], 465.3, "Le changement", hl=W("écrit", 465.2), size=84)
tg(S, 450, "Il arrête de dépenser avec la carte", W("arrête", 465.2), "", 34)
tg(S, 540, "Un virement mensuel plus élevé", W("virement", 465.2), "", 34)
tg(S, 630, "Il en parle à un ami", W("ami", 465.2), "acc", 38)
stk(S, "baton-ecrit-liste", 1100, 260, 340, 465.8)

S = nxt(473.9)
title(S, ["Carte [soldée]"], 474.0, "Quelques mois plus tard", hl=W("soldé", 473.9), size=96)
tg(S, 440, "Il n'est pas parfait", W("parfait", 473.9), "", 38)
tg(S, 530, "Il a retrouvé la paix", W("paix", 473.9), "acc", 40)
stk(S, "releve-propre", 1050, 280, 330, 474.6, rot=-2)
stk(S, "escalier-porte", 1500, 280, 380, W("paix", 473.9), rot=2)

S = nxt(481.4)
title(S, ["Une autre [manière]", "d'utiliser sa carte"], 481.5, "Ce qui a changé", hl=W("manière", 481.4), size=72)
tg(S, 450, "Un prélèvement automatique", W("prélèvement", 481.4), "", 36)
tg(S, 540, "Des alertes sur son téléphone", W("alertes", 481.4), "", 36)
tg(S, 630, "Un rendez-vous budget chaque semaine", W("rendez", 481.4), "acc", 34)
stk(S, "calendrier-prelevement", 1100, 270, 460, 482.0, rot=-2)

S = nxt(490.7)
title(S, ["Un [exemple],", "pas un témoignage"], 490.8, "À retenir", hl=W("exemple", 490.7), size=78)
tg(S, 450, "Un principe applicable à chacun", W("principe", 490.7), "acc", 36)
stk(S, "colombe", 1100, 280, 300, 491.4, rot=3)

# ================================================================ 10 · Récapitulatif et action
S = nxt(495.2)
title(S, ["L'[essentiel]"], 495.3, "Retenons", hl=495.8, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 495.6, rot=-3)

S = nxt(496.3)
title(S, ["La Bible [éclaire]", "l'usage de la carte"], 496.4, "Pas de carte dans la Bible", hl=W("éclaire", 496.3), size=72)
tg(S, 450, "La dette crée une dépendance", W("dépendance", 496.3), "", 34)
tg(S, 530, "Calculer avant de s'engager", W("calculer", 496.3), "", 34)
tg(S, 610, "Honorer ses engagements", W("honorer", 496.3), "", 34)
tg(S, 690, "Voir les pièges", W("pièges", 496.3), "", 34)
tg(S, 770, "Ne rien devoir qui t'étouffe", W("étouffe", 496.3), "acc", 34)
stk(S, "baton-pense", 1250, 260, 280, 497.0)

S = nxt(508.4)
title(S, ["Trois [questions]", "avant de payer"], 508.5, "Le test", hl=509.2, size=84)
stk(S, "baton-test-trois", 1150, 240, 330, 509.0)

S = nxt(511.7)
title(S, ["Le [test]"], 511.8, "Les trois questions", hl=512.2, size=96)
tg(S, 400, "1 · Plus libre, ou plus dépendant ?", 512.4, "", 34)
tg(S, 490, "2 · J'ai déjà cet argent ?", W("2", 511.7), "", 34)
tg(S, 580, "3 · Je pourrai tout rembourser à temps ?", W("3", 511.7), "acc", 34)
stk(S, "baton-pense", 1150, 230, 260, 512.6)

S = nxt(522.1)
title(S, ["Les cinq", "[règles]"], 522.2, "Applique-les", hl=522.7, size=96)
tg(S, 440, "1 · Dépenser l'argent que tu as", W("dépenser", 522.1), "", 32)
tg(S, 520, "2 · Tout rembourser chaque mois", W("rembourser", 522.1), "", 32)
tg(S, 600, "3 · Une seule carte", W("seule", 522.1), "", 32)
tg(S, 680, "4 · Suivre tes dépenses", W("suivre", 522.1), "", 32)
tg(S, 760, "5 · Pas d'espèces, pas de minimum", W("espèces", 522.1), "acc", 32)
stk(S, "garde-fou-route", 1150, 300, 480, 522.6)

S = nxt(532.1)
title(S, ["Une seule [règle]", "cette semaine"], 532.2, "Ton action", hl=W("choisis", 532.1), size=78)
tg(S, 450, "Ouvre ton dernier relevé", W("ouvre", 532.1), "", 38)
tg(S, 540, "Regarde le solde", W("regarde", 532.1), "", 38)
tg(S, 630, "Choisis une règle", W("choisis", 532.1), "acc", 40)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 532.7)
stk(S, "carnet-depenses", 1540, 460, 290, 533.6, rot=3)

S = nxt(540.6)
title(S, ["La carte n'est pas", "ton [maître]"], 540.7, "Rappelle-toi", hl=W("maître", 540.6), size=78)
tg(S, 450, "C'est toi qui décides", W("décides", 540.6), "acc", 42)
stk(S, "baton-priere", 1100, 260, 300, 541.2)
stk(S, "croix-verte", 1480, 300, 240, W("décides", 540.6), rot=4)
hit(W("décides", 540.6), 0.8)

S = nxt(544.0)
title(S, ["Quelle règle", "te [manque] ?"], 544.1, "Et toi", hl=W("manque", 544.0), size=84)
stk(S, "baton-pense", 1150, 230, 260, 544.6)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 546.0) - 0.6, 14)
sfx("click", W("commentaire", 546.0) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 549.0), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 58.5), ("02", "Passages 1 à 3", 58.5, 226.9), ("03", "Passages 4 et 5", 226.9, 315.9),
              ("04", "Cinq règles", 315.9, 402.8), ("05", "Signaux et exemple", 402.8, 495.2), ("06", "À retenir et test", 495.2, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)
