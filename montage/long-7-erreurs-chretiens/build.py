"""Vidéo longue « 7 erreurs financières que les chrétiens doivent arrêter de faire » — style 02 en 16:9, ~10 min.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 7 erreurs (verset + remède), exercice, exemple (Léa), récapitulatif.
Les temps sont lus dans transcript.json (voix fournie par l'utilisateur ; mots mal transcrits corrigés).

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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - 7 erreurs financières que les chrétiens doivent arrêter de faire", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 582.3
s.setup(here=HERE, duration=597.6, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
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
        if w["start"] >= after - 0.25 and pn in _norm(w["text"]):
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
S = nxt(0.2)
title(S, ["Sept [erreurs]", "d'argent"], 0.3, "Beaucoup de chrétiens", hl=W("erreurs", 0.2), size=96)
counter(S, 80, 450, 0, 7, 1.2, 1.0, " erreurs", 130)
stk(S, "baton-sans-plan", 1100, 220, 440, 0.8, rot=-2)

S = nxt(9.84)
title(S, ["Pas un mauvais", "[chrétien]"], 9.94, "Ces erreurs sont courantes", hl=W("mauvais", 9.84), size=90)
tg(S, 450, "Héritées de l'entourage", W("entourage", 9.84), "", 36)
tg(S, 540, "De nos habitudes", W("habitudes", 9.84), "", 36)
tg(S, 630, "Elles coûtent en argent et en paix", W("paix", 9.84), "acc", 34)
stk(S, "baton-serein", 1100, 250, 300, 10.44)

S = nxt(20.36)
title(S, ["Repérer, comprendre,", "[corriger]"], 20.46, "Un pas à la fois", hl=W("corriger", 20.36), size=78)
tg(S, 450, "Repérer", W("repérer", 20.36), "", 38)
tg(S, 540, "Comprendre", W("comprendre", 20.36), "", 38)
tg(S, 630, "Corriger", W("corriger", 20.36), "acc", 38)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 20.96)

S = nxt(29.3)
title(S, ["Pour chaque", "[erreur]"], 29.4, "Dans cette vidéo", hl=W("erreur", 29.3), size=96)
tg(S, 450, "Un passage de la Bible", W("passage", 29.3), "", 38)
tg(S, 540, "Ce qu'il nous apprend", W("apprend", 29.3), "", 38)
tg(S, 630, "Ce que tu peux changer", W("changer", 29.3), "acc", 38)
stk(S, "pupitre-parole", 1100, 260, 380, 30.0, rot=-2)

S = nxt(36.86)
title(S, ["Est-ce que cela", "me [ressemble] ?"], 36.96, "Honnêtement", hl=W("ressemble", 36.86), size=84)
stk(S, "baton-pense", 1150, 230, 270, 37.46)

S = nxt(44.3)
title(S, ["La [septième]", "est la plus grave"], 44.4, "Reste jusqu'à la fin", hl=W("septième", 44.3), size=84)
tg(S, 450, "La plus grave", W("grave", 44.3), "", 38)
tg(S, 540, "La plus discrète", W("discrète", 44.3), "", 38)
tg(S, 630, "Un exercice très simple", W("exercice", 44.3), "acc", 38)
stk(S, "drapeau-rouge", 1150, 250, 330, 45.0)

S = nxt(52.96)
title(S, ["Pas un conseil", "[personnalisé]"], 53.06, "Une précision importante", hl=W("personnalisé", 52.96), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 52.96), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 52.96), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 53.77)
hit(W("personnalisé", 52.96), 0.8)

# ================================================================ 02 · Erreur 1 : vivre sans plan
S = nxt(62.6)
title(S, ["Erreur 1 :", "vivre sans [plan]"], 62.7, "Première erreur", hl=W("plan", 62.6), size=90)
tg(S, 450, "On gagne, on dépense", W("dépense", 62.6), "", 38)
tg(S, 540, "On verra bien…", W("verra", 62.6), "acc", 38)
stk(S, "baton-sans-plan", 1100, 220, 440, 63.2)

S = nxt(69.32)
title(S, ["L'erreur la plus", "[répandue]"], 69.42, "Rien de spectaculaire", hl=W("répandue", 69.32), size=84)
tg(S, 450, "Des journées normales", W("normales", 69.32), "acc", 38)
stk(S, "baton-tiraille", 1150, 250, 300, 70.02)

parole(75.54, "Proverbes 24.27", 77.58,
       f"« Soigne tes affaires au dehors, {m(0, 'mets ton champ en état')} ; après cela, {m(1, 'tu bâtiras ta maison')}. »",
       W("soigne", 75.04), 85.93, [W("champ", 75.04), W("bâtiras", 75.04)], size=46)

S = nxt(86.02)
title(S, ["D'abord ce qui", "fait [vivre]"], 86.12, "Dans ce verset", hl=W("vivre", 86.02), size=84)
tg(S, 450, "Ensuite ce qui est confortable", W("confortable", 86.02), "", 36)
tg(S, 540, "Sans plan : des petites dépenses partout", W("petites", 92.32), "acc", 32)
stk(S, "maison-roc", 1100, 260, 340, 86.72, rot=-2)

S = nxt(97.18)
title(S, ["Où est passé", "l'[argent] ?"], 97.28, "Un signe qui ne trompe pas", hl=W("argent", 97.18), size=90)
tg(S, 450, "Pas de réponse précise", W("précise", 97.18), "acc", 38)
stk(S, "baton-soucieux", 1150, 250, 290, 97.88)

S = nxt(103.18)
title(S, ["Ce que tu", "peux [changer]"], 103.28, "Un budget simple", hl=W("budget", 103.18), size=90)
tg(S, 440, "Tes revenus", W("revenus", 103.18), "", 36)
tg(S, 520, "Tes dépenses essentielles", W("essentielles", 103.18), "", 36)
tg(S, 600, "Donner · épargner · dépenser", W("épargner", 103.18), "acc", 36)
stk(S, "boussole-carnet", 1050, 270, 500, 103.88, rot=-2)

S = nxt(117.34)
title(S, ["Une feuille,", "un [crayon]"], 117.44, "Pas besoin d'un tableur", hl=W("crayon", 117.34), size=90)
tg(S, 450, "Le but : la clarté, pas la perfection", W("clarté", 117.34), "acc", 34)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 118.05)

# ================================================================ 03 · Erreur 2 : vivre pour paraître
S = nxt(124.42)
title(S, ["Erreur 2 :", "vivre pour [paraître]"], 124.52, "Deuxième erreur", hl=W("paraître", 124.42), size=84)
tg(S, 450, "On achète pour impressionner", W("impressionner", 124.42), "", 36)
tg(S, 540, "Parfois à crédit", W("crédit", 124.42), "acc", 38)
stk(S, "baton-faux-riche", 1150, 210, 380, 125.11)

S = nxt(130.24)
title(S, ["La [comparaison]", "des réseaux"], 130.34, "Une tentation plus forte", hl=W("compare", 130.24), size=84)
tg(S, 450, "On voit la vie des autres", W("voit", 130.24), "", 36)
tg(S, 540, "On veut avoir l'air de réussir", W("réussir", 130.24), "acc", 36)
stk(S, "baton-vitrine", 1100, 250, 380, 130.85)

parole(137.52, "Proverbes 13.7", 138.71,
       f"« {m(0, 'Tel fait le riche et n’a rien')} ; tel fait le pauvre et {m(1, 'a de grands biens')}. »",
       W("tel", 139.71), 145.38, [W("riche", 139.71), W("grands", 139.71)], size=56)

S = nxt(145.58)
title(S, ["L'apparence", "peut [tromper]"], 145.68, "Une belle voiture, des dettes", hl=W("tromper", 145.58), size=90)
tg(S, 450, "Belle voiture, dettes", W("dettes", 145.58), "", 38)
tg(S, 540, "Peu de signes, beaucoup de paix", W("paix", 145.58), "acc", 36)
stk(S, "baton-content-simple", 1100, 240, 380, 146.28)

S = nxt(152.76)
title(S, ["L'apparence", "se [paie]"], 152.86, "Souvent avec des intérêts", hl=W("paie", 152.76), size=96)
tg(S, 450, "Pas plus longtemps qu'un compliment", W("compliment", 152.76), "acc", 32)
stk(S, "pile-factures", 1100, 270, 340, 153.46)

S = nxt(159.46)
title(S, ["Pour moi, ou pour", "le [regard] des autres ?"], 159.56, "Avant un achat visible", hl=W("regard", 159.46), size=72)
tg(S, 450, "Laisse passer quelques jours", W("jours", 165.48), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 160.06)

S = nxt(171.3)
title(S, ["Offrir par", "[amour]"], 171.4, "Vaut souvent plus", hl=W("amour", 171.3), size=100)
tg(S, 450, "Un cadeau offert par amour", W("cadeau", 171.3), "", 36)
tg(S, 540, "Un repas entre amis", W("repas", 171.3), "", 36)
tg(S, 630, "Une soirée simple", W("soirée", 171.3), "acc", 36)
stk(S, "famille-sortie", 1050, 270, 560, 171.9)

# ================================================================ 04 · Erreur 3 : ne rien prévoir
S = nxt(178.72)
title(S, ["Erreur 3 :", "ne rien [prévoir]"], 178.82, "Troisième erreur", hl=W("prévoir", 178.72), size=90)
tg(S, 450, "Pas de réserve", W("réserve", 178.72), "", 38)
tg(S, 540, "Pas d'épargne", W("épargne", 178.72), "", 38)
tg(S, 630, "Jusqu'au jour de la panne", W("panne", 178.72), "acc", 36)
stk(S, "baton-trempe-pluie", 1100, 200, 300, 179.31)

S = nxt(184.66)
title(S, ["« Dieu", "[pourvoira] »"], 184.76, "C'est vrai, mais…", hl=W("pourvoira", 184.66), size=100)
tg(S, 450, "Souvent par la prévoyance qu'il nous donne", W("prévoyance", 184.66), "acc", 32)
stk(S, "baton-priere", 1100, 250, 300, 185.27)

parole(190.32, "Proverbes 30.25", 191.61,
       f"« Les fourmis, {m(0, 'peuple sans force')}, {m(1, 'préparent en été')} leur nourriture. »",
       W("fourmis", 192.7), 196.86, [W("force", 192.7), W("préparent", 192.7)], size=60)

S = nxt(196.96)
title(S, ["La [fourmi]", "prépare"], 197.06, "Pas puissante", hl=W("fourmi", 196.96), size=100)
tg(S, 450, "Pas puissante, mais elle prépare", W("puissante", 196.96), "", 34)
tg(S, 540, "Ce n'est pas un manque de foi", W("foi", 196.96), "acc", 36)
stk(S, "bocal-fourmi", 1100, 260, 440, 197.66, rot=-2)

S = nxt(202.34)
title(S, ["Un imprévu :", "crise ou [contretemps] ?"], 202.44, "La différence", hl=W("contretemps", 202.34), size=78)
tg(S, 450, "Sans réserve : une crise, et souvent une dette", W("dette", 202.34), "", 30)
tg(S, 540, "Avec une réserve : un simple contretemps", W("contretemps", 202.34), "acc", 30)
stk(S, "bocal-reserve", 1100, 260, 330, 202.95)

S = nxt(209.72)
title(S, ["Une petite [réserve]", "régulière"], 209.82, "L'important : l'habitude", hl=W("minuscule", 209.72), size=78)
tg(S, 440, "10 ou 20 € par semaine", W("10", 215.0), "", 36)
tg(S, 520, "Sur un compte séparé", W("séparé", 216.58), "", 36)
tg(S, 600, "Un palier à la fois", W("palier", 221.58), "acc", 36)
stk(S, "escalier-trois-paliers", 1100, 250, 380, 210.32)

S = nxt(228.66)
title(S, ["Si cette vidéo", "t'[aide]…"], 228.76, "Un instant", hl=W("aide", 228.66))
tg(S, 450, "Abonne-toi", W("abonne", 228.66) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", W("chaque", 232.82) + 0.2, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 229.67, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 230.08, rot=2)
bw("Abonne-toi", W("abonne", 228.66) + 0.4, 1.0)

# ================================================================ 05 · Erreur 4 : décider seul
S = nxt(237.64)
title(S, ["Erreur 4 :", "décider [seul]"], 237.74, "Quatrième erreur", hl=W("seul", 237.64), size=96)
tg(S, 450, "Par fierté", W("fierté", 237.64), "", 38)
tg(S, 540, "Par peur de déranger", W("déranger", 237.64), "acc", 38)
stk(S, "baton-decide-seul", 1050, 280, 520, 238.25, rot=-2)

S = nxt(243.8)
title(S, ["Des dépenses", "[cachées]"], 243.9, "Dans un couple", hl=W("cachées", 243.8), size=96)
tg(S, 450, "Des décisions prises sans en parler", W("décisions", 243.8), "", 34)
tg(S, 540, "Cela abîme la confiance", W("abîme", 243.8), "acc", 38)
stk(S, "baton-tiraille", 1150, 250, 300, 244.4)

parole(250.92, "Proverbes 12.15", 251.9,
       f"« La voie de l'insensé {m(0, 'est droite à ses yeux')}, mais celui qui {m(1, 'écoute les conseils')} est sage. »",
       W("voie", 252.68), 258.96, [W("droite", 252.68), W("écoute", 252.68)], size=52)

S = nxt(259.06)
title(S, ["Un regard", "[extérieur]"], 259.16, "Nos angles morts", hl=W("extérieur", 259.06), size=100)
tg(S, 450, "Il nous protège", W("protège", 259.06), "acc", 40)
stk(S, "table-conseillers", 1000, 260, 620, 259.67)

S = nxt(264.22)
title(S, ["Un bon", "[conseiller]"], 264.32, "Ce qu'il fait", hl=W("conseiller", 264.22), size=100)
tg(S, 440, "Il ne décide pas à ta place", W("décide", 264.22), "", 34)
tg(S, 520, "Il pose les questions que tu ne te poses pas", W("questions", 264.22), "", 30)
tg(S, 600, "Il dit ce que tu n'as pas envie d'entendre", W("entendre", 264.22), "acc", 30)
stk(S, "baton-conseillers", 1050, 280, 470, 264.81, rot=-2)

S = nxt(270.24)
title(S, ["Avant un gros achat,", "un [emprunt]…"], 270.34, "Demande conseil", hl=W("emprunt", 270.24), size=78)
tg(S, 440, "Ton conjoint", W("conjoint", 270.24), "", 36)
tg(S, 520, "Une personne de confiance", W("confiance", 270.24), "", 36)
tg(S, 600, "Sans intérêt à ce que tu dises oui", W("intérêt", 278.64), "acc", 32)
stk(S, "couple-budget", 1100, 270, 440, 270.84, rot=-2)

# ================================================================ 06 · Erreur 5 : l'argent facile
S = nxt(284.18)
title(S, ["Erreur 5 :", "l'argent [facile]"], 284.28, "Cinquième erreur", hl=W("facile", 284.18), size=90)
tg(S, 450, "Une promesse de gain rapide", W("gain", 284.18), "", 36)
tg(S, 540, "Une opportunité trop belle", W("belle", 284.18), "acc", 36)
stk(S, "baton-appat-brillant", 1100, 220, 420, 284.78)

S = nxt(290.6)
title(S, ["Sous mille", "[formes]"], 290.7, "Elle revient", hl=W("formes", 290.6), size=100)
tg(S, 440, "Un placement miracle", W("miracle", 290.6), "", 34)
tg(S, 520, "Une formation « liberté financière »", W("formation", 290.6), "", 32)
tg(S, 600, "Une vente en réseau", W("réseau", 290.6), "", 34)
tg(S, 680, "Un conseil sur internet", W("internet", 290.6), "acc", 34)
stk(S, "baton-tente-promo", 1100, 250, 400, 291.2)

parole(299.4, "Proverbes 20.21", 300.57,
       f"« Un bien {m(0, 'promptement acquis')} dès l'origine {m(1, 'ne sera pas béni')} à la fin. »",
       W("bien", 301.16), 306.06, [W("promptement", 301.16), W("béni", 301.16)], size=56)

S = nxt(306.16)
title(S, ["Rapide ?", "Souvent [fragile]"], 306.26, "Les gains rapides", hl=W("fragiles", 306.16), size=90)
tg(S, 450, "Et parfois trompeur", W("trompeurs", 306.16), "acc", 38)
stk(S, "etiquette-prix-gonfle", 1100, 260, 400, 306.77, rot=-2)

S = nxt(310.7)
title(S, ["Un seul [signal]", "d'alerte"], 310.8, "Ralentis", hl=W("signal", 310.7), size=90)
tg(S, 450, "On te presse de décider vite", W("presse", 310.7), "", 36)
tg(S, 540, "On te demande le secret", W("secret", 310.7), "acc", 38)
stk(S, "drapeau-rouge", 1150, 250, 330, 311.3)

S = nxt(316.46)
title(S, ["Prendre le [temps]", "de vérifier"], 316.56, "Avant de t'engager", hl=W("vérifier", 316.46), size=84)
tg(S, 440, "Compare, pose des questions", W("compare", 323.92), "", 34)
tg(S, 520, "Demande des documents clairs", W("documents", 323.92), "", 34)
tg(S, 600, "Jamais l'argent dont tu as besoin pour vivre", W("jamais", 323.92), "acc", 30)
stk(S, "loupe-depenses", 1100, 260, 400, 317.06, rot=-2)

S = nxt(330.22)
title(S, ["Langage [religieux]", "= confiance ?"], 330.32, "Attention", hl=W("religieux", 330.22), size=78)
tg(S, 450, "Examine toujours", W("examine", 330.22), "acc", 40)
tg(S, 540, "Même venant de ton église", W("église", 330.22), "", 36)
stk(S, "baton-pense", 1150, 230, 270, 330.82)

# ================================================================ 07 · Erreur 6 : retenir ce qu'on pourrait donner
S = nxt(339.26)
title(S, ["Erreur 6 :", "retenir [sans donner]"], 339.36, "Sixième erreur", hl=W("donner", 339.26), size=84)
tg(S, 450, "Par peur de manquer", W("manquer", 339.26), "", 38)
tg(S, 540, "On garde tout pour soi", W("garde", 339.26), "acc", 38)
stk(S, "baton-poing-ferme", 1100, 220, 330, 339.86)

S = nxt(345.14)
title(S, ["Deux [excès]"], 345.24, "Deux erreurs opposées", hl=W("excès", 345.14), size=110)
tg(S, 450, "Donner sous pression", W("pression", 345.14), "", 38)
tg(S, 540, "Se mettre en difficulté", W("difficulté", 345.14), "acc", 38)
stk(S, "baton-fardeau", 1150, 250, 320, 345.75)

parole(350.72, "Hébreux 13.16", 351.89,
       f"« N'oubliez pas {m(0, 'la bienfaisance et la libéralité')} ; car c'est à de tels sacrifices que {m(1, 'Dieu prend plaisir')}. »",
       W("oubliez", 352.67), 358.6, [W("bienfaisance", 352.67), W("plaisir", 352.67)], size=48)

S = nxt(358.7)
title(S, ["Donner ne", "[t'appauvrit] pas"], 358.8, "Pas forcément", hl=W("appauvrit", 358.7), size=84)
tg(S, 450, "Ta sécurité ne repose pas sur ton compte", W("sécurité", 358.7), "acc", 32)
stk(S, "coeur-receptacle", 1100, 270, 340, 359.3, rot=-3)

S = nxt(363.98)
title(S, ["Ouvrir la", "[main]"], 364.08, "Un outil pour servir", hl=W("main", 363.98), size=100)
tg(S, 450, "Pas seulement accumuler", W("accumuler", 363.98), "", 38)
tg(S, 540, "De la joie, même modestement", W("joie", 370.16), "acc", 36)
stk(S, "main-ouverte-don", 1150, 250, 330, 364.58)

S = nxt(375.36)
title(S, ["Une part à", "[donner]"], 375.46, "Décidée à l'avance", hl=W("avance", 375.36), size=100)
tg(S, 440, "Ni pression, ni culpabilité", W("culpabilité", 375.36), "", 36)
tg(S, 520, "Du temps, un service, un repas", W("temps", 382.58), "acc", 34)
stk(S, "enveloppe-don", 1100, 270, 340, 375.96, rot=-3)
stk(S, "baton-donne", 1520, 300, 330, W("temps", 382.58), rot=2)

# ================================================================ 08 · Erreur 7 : l'argent à la place de Dieu
S = nxt(388.16)
title(S, ["Erreur 7 :", "l'argent à la place de [Dieu]"], 388.26, "La plus grave", hl=W("Dieu", 388.16), size=72)
tg(S, 450, "La plus grave", W("grave", 388.16), "acc", 40)
stk(S, "balance-dieu-argent", 1050, 270, 520, 388.77, rot=-2)

S = nxt(392.6)
title(S, ["Les six autres,", "des [symptômes]"], 392.7, "Voilà pourquoi je l'ai gardée", hl=W("symptômes", 392.6), size=84)
tg(S, 450, "Souvent des symptômes de celle-ci", W("symptômes", 392.6), "acc", 34)
stk(S, "baton-soucieux", 1150, 250, 290, 393.2)

parole(397.48, "Matthieu 6.24", 398.6,
       f"« Vous ne pouvez {m(0, 'servir')} {m(1, 'Dieu et Mamon')}. »",
       W("vous", 399.31), 402.08, [W("servir", 399.31), W("Mamon", 399.31)], size=70)

S = nxt(402.18)
title(S, ["Une erreur", "[discrète]"], 402.28, "On peut prier et pourtant…", hl=W("discrète", 402.18), size=100)
tg(S, 450, "Prier, aller à l'église", W("prier", 402.18), "", 36)
tg(S, 540, "Organiser sa vie autour de l'argent", W("organiser", 402.18), "acc", 34)
stk(S, "baton-priere", 1100, 250, 300, 402.78)

S = nxt(410.1)
title(S, ["Pas une question", "de [somme]"], 410.2, "Ce n'est pas le montant", hl=W("somme", 410.1), size=84)
tg(S, 450, "Très riche et très libre", W("libre", 410.1), "", 36)
tg(S, 540, "Très pauvre et obsédé par l'argent", W("obsédé", 410.1), "acc", 34)
stk(S, "baton-serein", 1100, 260, 300, 410.7)

S = nxt(416.6)
title(S, ["Deux [signes]"], 416.7, "Pour reconnaître cette erreur", hl=W("signes", 416.6), size=110)
tg(S, 440, "L'argent dicte tes choix, ton humeur, ton sommeil", W("sommeil", 416.6), "", 28)
tg(S, 520, "Du mal à donner", W("donner", 422.72), "", 34)
tg(S, 600, "Du mal à te réjouir pour un autre", W("réjouir", 422.72), "", 32)
tg(S, 680, "Du mal à être reconnaissant", W("reconnaissant", 422.72), "acc", 34)
stk(S, "baton-fardeau", 1150, 250, 320, 417.2)

S = nxt(429.5)
title(S, ["Remets-lui", "tes [soucis]"], 429.6, "Dieu en première place", hl=W("soucis", 438.5), size=96)
tg(S, 440, "Qu'est-ce qui me guide le plus ?", W("guide", 429.5), "", 34)
tg(S, 520, "Prie, et reviens à lui", W("prie", 429.5), "", 36)
tg(S, 600, "Cela remet ton cœur à la bonne place", W("cœur", 438.5), "acc", 32)
stk(S, "baton-priere", 1100, 250, 300, 430.1)
stk(S, "croix-verte", 1560, 340, 220, W("cœur", 438.5), rot=4)

S = nxt(446.16)
title(S, ["L'[exercice]", "promis"], 446.26, "Prends une feuille", hl=W("exercice", 446.16), size=96)
tg(S, 440, "Écris les sept erreurs", W("écris", 446.16), "", 36)
tg(S, 520, "Un chiffre de 1 à 5 à côté de chacune", W("chiffre", 446.16), "", 32)
tg(S, 600, "Choisis le chiffre le plus élevé", W("élevé", 446.16), "acc", 34)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 446.76)
stk(S, "carnet-depenses", 1540, 460, 290, 448.16, rot=3)

S = nxt(460.08)
title(S, ["Pas sept actions :", "[une] seule"], 460.18, "C'est ainsi qu'on change", hl=W("seule", 460.08), size=84)
tg(S, 450, "Un petit changement tenu", W("petit", 464.98), "", 36)
tg(S, 540, "Vaut mieux qu'une grande résolution oubliée", W("résolution", 464.98), "acc", 30)
stk(S, "baton-content", 1150, 250, 300, 460.68)

# ================================================================ 09 · Exemple : Léa
S = nxt(473.6)
title(S, ["Un exemple :", "[Léa]"], 473.7, "Prenons", hl=W("Léa", 473.6), size=100)
tg(S, 450, "Sa plus grande erreur : la première", W("première", 475.08), "", 34)
tg(S, 540, "Aucun plan", W("aucun", 475.08), "acc", 40)
stk(S, "baton-sans-plan", 1100, 220, 420, 474.19)

S = nxt(484.56)
title(S, ["Un budget", "chaque [dimanche]"], 484.66, "Sa décision", hl=W("dimanche", 484.56), size=90)
tg(S, 450, "Elle note ses dépenses", W("note", 484.56), "", 36)
tg(S, 540, "Elle ajuste", W("ajuste", 484.56), "", 36)
tg(S, 630, "Sans se juger", W("juge", 490.52), "acc", 36)
stk(S, "boussole-carnet", 1050, 270, 480, 485.17, rot=-2)

S = nxt(496.2)
title(S, ["Plus [calme]"], 496.3, "Au bout de quelques semaines", hl=W("calme", 496.2), size=110)
tg(S, 450, "Elle a repris la main", W("main", 496.2), "", 38)
tg(S, 540, "Une petite somme chaque mois", W("somme", 502.2), "acc", 36)
stk(S, "baton-content-simple", 1050, 240, 380, 496.8)
stk(S, "bocal-fourmi", 1500, 330, 330, W("somme", 502.2), rot=3)

S = nxt(508.54)
title(S, ["Un [exemple],", "pas un témoignage"], 508.64, "À retenir", hl=W("exemple", 508.54), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 508.54), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 509.14, rot=3)

# ================================================================ 10 · Récapitulatif et action
S = nxt(515.16)
title(S, ["L'[essentiel]"], 515.26, "Retenons", hl=515.88, size=96)
tg(S, 340, "1 · Avoir un plan", W("plan", 516.08), "", 30)
tg(S, 410, "2 · Ne pas vivre pour paraître", W("paraître", 517.2), "", 30)
tg(S, 480, "3 · Prévoir", W("prévoir", 517.2), "", 30)
tg(S, 550, "4 · Demander conseil", W("conseil", 517.2), "", 30)
tg(S, 620, "5 · Se méfier de l'argent facile", W("méfier", 517.2), "", 30)
tg(S, 690, "6 · Donner avec sagesse", W("sagesse", 517.2), "", 30)
tg(S, 760, "7 · Garder Dieu à la première place", W("première", 517.2), "acc", 30)
stk(S, "livre-croix-ouvert", 1200, 300, 400, 515.67, rot=-3)

S = nxt(533.34)
title(S, ["Aucune ne demande", "un grand [revenu]"], 533.44, "Ces corrections", hl=W("revenu", 533.34), size=78)
tg(S, 450, "De l'humilité", W("humilité", 533.34), "", 38)
tg(S, 540, "De la constance", W("constance", 533.34), "acc", 38)
stk(S, "baton-serein", 1100, 260, 300, 533.94)

S = nxt(540.94)
title(S, ["Pas de", "[condamnation]"], 541.04, "Si tu fais une de ces erreurs", hl=W("condamne", 540.94), size=90)
tg(S, 450, "La grâce autant que la sagesse", W("grâce", 540.94), "acc", 36)
stk(S, "colombe", 1100, 280, 300, 541.64, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("grâce", 540.94), rot=4)

S = nxt(548.98)
title(S, ["Des erreurs qui se", "tiennent la [main]"], 549.08, "Corriger l'une aide les autres", hl=W("main", 548.98), size=78)
tg(S, 450, "Sans plan : plus tenté par l'argent facile", W("tenté", 548.98), "", 30)
tg(S, 540, "Décider seul : plus tenté de paraître", W("paraître", 554.68), "acc", 30)
stk(S, "baton-tiraille", 1150, 250, 300, 549.68)

S = nxt(560.48)
title(S, ["Une seule chose", "cette [semaine]"], 560.58, "Ton action", hl=W("exercice", 560.48), size=78)
tg(S, 440, "Sept erreurs", W("7", 560.0), "", 38)
tg(S, 520, "Un chiffre de 1 à 5", W("chiffre", 560.48), "", 38)
tg(S, 600, "Une seule action", W("action", 560.48), "acc", 38)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 561.08)
stk(S, "carnet-depenses", 1540, 460, 290, 562.07, rot=3)

S = nxt(565.94)
title(S, ["En couple :", "[comparez] avec douceur"], 566.04, "Si tu es marié", hl=W("comparez", 565.94), size=78)
tg(S, 450, "Chacun de son côté", W("côté", 565.94), "acc", 38)
stk(S, "couple-budget", 1100, 270, 440, 566.54, rot=-2)

S = nxt(572.86)
title(S, ["Quelle erreur", "te [concerne] le plus ?"], 572.96, "Et toi", hl=W("concerne", 572.86), size=84)
stk(S, "baton-pense", 1150, 230, 260, 573.47)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 572.86) - 0.6, 14)
sfx("click", W("commentaire", 572.86) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 579.22), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 62.6), ("02", "Erreurs 1 à 3", 62.6, 237.64), ("03", "Erreurs 4 à 6", 237.64, 388.16),
              ("04", "Erreur 7 et exercice", 388.16, 473.6), ("05", "Exemple et rappel", 473.6, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)
