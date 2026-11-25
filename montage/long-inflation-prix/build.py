"""Vidéo longue « Inflation : comment garder la paix et protéger ton budget » — style 02 en 16:9, ~10 min.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 5 passages, 5 étapes, 5 pièges, exemple (Inès et Karim), récapitulatif.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Inflation : garder la paix et protéger son budget", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 594.0
s.setup(here=HERE, duration=609.3, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
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
S = nxt(0.0)
title(S, ["Tout coûte", "[plus cher]"], 0.1, "Comment garder la paix ?", hl=W("grimper", 0.0), size=100)
tg(S, 450, "Les courses", W("courses", 0.0), "", 38)
tg(S, 540, "L'énergie", W("énergie", 0.0), "", 38)
tg(S, 630, "Les loyers", W("loyers", 0.0), "acc", 38)
stk(S, "baton-courses-ticket", 1100, 220, 480, 0.6, rot=-2)

S = nxt(10.9)
title(S, ["Ton argent", "vaut [moins]"], 11.0, "Tu n'as pas tort", hl=W("moins", 10.9), size=100)
tg(S, 450, "Un pouvoir d'achat sous tension", W("tension", 10.9), "", 34)
tg(S, 540, "De moins en moins de côté ?", W("côté", 10.9), "acc", 36)
stk(S, "factures-flamme-montante", 1050, 280, 520, 11.5)

S = nxt(22.8)
title(S, ["Une situation", "qui [fatigue]"], 22.9, "On calcule de tête", hl=W("fatigue", 22.8), size=96)
tg(S, 450, "Le frigo, la facture", W("frigo", 22.8), "", 36)
tg(S, 540, "Des calculs de tête", W("calculs", 22.8), "", 36)
tg(S, 630, "Culpabilité, inquiétude", W("culpabilise", 22.8), "acc", 36)
stk(S, "baton-nuage-inquiet", 1150, 200, 270, 23.5)

S = nxt(31.3)
title(S, ["Responsable de", "ta [réaction]"], 31.4, "Pas de la hausse des prix", hl=W("réagis", 31.3), size=90)
tg(S, 450, "Pas de la hausse des prix", W("hausse", 31.3), "", 36)
tg(S, 540, "De la manière dont tu réagis", W("réagis", 31.3), "acc", 36)
stk(S, "baton-serein", 1100, 260, 300, 31.9)

S = nxt(37.0)
title(S, ["Pas de", "[miracle]"], 37.1, "Cette vidéo", hl=W("miracle", 37.0), size=110)
tg(S, 450, "Des repères bibliques", W("repères", 37.0), "", 38)
tg(S, 540, "Des gestes concrets", W("gestes", 37.0), "acc", 38)
stk(S, "pupitre-parole", 1100, 260, 380, 37.7, rot=-2)

S = nxt(44.5)
title(S, ["Au [programme]"], 44.6, "Dans cette vidéo", hl=45.2)
tg(S, 420, "5 passages", W("cinq", 44.5, 0), "", 40)
tg(S, 510, "5 étapes", W("cinq", 44.5, 1), "", 40)
tg(S, 600, "Les pièges à éviter", W("pièges", 44.5), "", 40)
tg(S, 690, "Un exemple", W("exemple", 44.5), "acc", 40)
stk(S, "liste-cinq-etapes", 1100, 240, 380, 45.2, rot=-1)

S = nxt(52.2)
title(S, ["Un exercice de", "[20 minutes]"], 52.3, "Reste jusqu'à la fin", hl=W("20", 52.2), size=90)
tg(S, 450, "Retrouver du souffle dans ton budget", W("souffle", 52.2), "", 32)
tg(S, 540, "Une question qui change le regard", W("question", 52.2), "acc", 32)
stk(S, "releves-loupe-trois-mois", 1050, 260, 500, 52.8, rot=-2)

S = nxt(60.0)
title(S, ["Pas un conseil", "[personnalisé]"], 60.1, "Une précision importante", hl=W("personnalisé", 60.0), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 60.0), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 60.0), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 60.8)
hit(W("personnalisé", 60.0), 0.8)

# ================================================================ 02 · Passage 1 : Psaume 37.19
parole(68.5, "Psaume 37.19", 70.6,
       f"« Ils ne sont {m(0, 'pas confondus au temps du malheur')}, et ils sont {m(1, 'rassasiés aux jours de famine')}. »",
       73.1, 77.8, [W("confondus", 73.0), W("rassasiés", 73.0)], size=50)

S = nxt(77.9)
title(S, ["Ceux qui vivent", "avec [intégrité]"], 78.0, "Dans ce verset", hl=W("intégrité", 77.9), size=84)
tg(S, 450, "Pas de promesse de tout facile", W("promet", 77.9), "", 34)
tg(S, 540, "Pas de garantie de ne jamais manquer", W("jamais", 77.9), "acc", 32)
stk(S, "baton-priere", 1100, 260, 300, 78.6)

S = nxt(84.7)
title(S, ["Dieu ne", "[t'abandonne] pas"], 84.8, "Même dans les temps difficiles", hl=W("abandonne", 84.7), size=90)
tg(S, 450, "Tu n'es pas livré à toi-même", W("livré", 84.7), "acc", 36)
stk(S, "colombe", 1100, 280, 300, 85.4, rot=3)

S = nxt(91.2)
title(S, ["Une promesse", "de [présence]"], 91.3, "Pas de confort garanti", hl=W("présence", 91.2), size=90)
tg(S, 450, "Pas une garantie de confort", W("garantie", 91.2), "", 36)
tg(S, 540, "Les fidèles ont traversé des temps de manque", W("fidèles", 94.3), "", 30)
tg(S, 630, "Ce qui change : la manière de traverser", W("manière", 94.3), "acc", 32)
stk(S, "baton-patient-calme", 1100, 260, 380, 91.9)

S = nxt(111.1)
title(S, ["Dépose ta", "[peur]"], 111.2, "Première étape", hl=W("peur", 111.1), size=104)
tg(S, 440, "Dis-lui ce que tu redoutes", W("redoutes", 111.1), "", 34)
tg(S, 520, "Une facture, un emploi, un loyer", W("loyer", 111.1), "", 34)
tg(S, 600, "Une prière vraie, pas belle", W("vraie", 120.8), "acc", 34)
stk(S, "baton-priere-nuit", 1050, 260, 470, 111.7)

# ================================================================ 03 · Passage 2 : Luc 12.22-24
parole(126.4, "Luc 12.22-24", 129.4,
       f"« {m(0, 'Ne vous inquiétez pas')} pour votre vie de ce que vous mangerez, ni pour votre corps de quoi vous serez vêtus. "
       f"{m(1, 'La vie est plus que la nourriture')}, et le corps plus que le vêtement. »",
       131.9, 141.8, [W("inquiétez", 131.8), W("plus", 134.5)], size=44, ref_y=880)

S = nxt(141.9)
title(S, ["L'[inquiétude]", "ne baisse pas les prix"], 142.0, "Jésus ne dit pas de ne rien faire", hl=W("inquiétude", 141.9), size=72)
tg(S, 450, "Ne te laisse pas dévorer", W("dévorer", 141.9), "", 34)
tg(S, 540, "Elle vide ton énergie et ton sommeil", W("sommeil", 149.9), "", 32)
tg(S, 630, "Elle brouille ton jugement", W("jugement", 149.9), "acc", 34)
stk(S, "baton-nuage-inquiet", 1150, 200, 270, 142.6)

S = nxt(159.4)
title(S, ["Responsabilité", "ou [angoisse] ?"], 159.5, "La différence", hl=W("angoisse", 159.4), size=90)
tg(S, 450, "Prendre soin de ton budget", W("budget", 159.4), "", 36)
tg(S, 540, "S'inquiéter sans agir", W("inquiéter", 159.4), "", 36)
tg(S, 630, "Que puis-je faire aujourd'hui ?", W("aujourd", 168.0), "acc", 36)
stk(S, "baton-pense", 1150, 230, 270, 160.0)

S = nxt(174.5)
title(S, ["Si cette vidéo", "t'[aide]…"], 174.6, "Un instant", hl=W("aide", 174.5))
tg(S, 450, "Abonne-toi", W("abonne", 174.5) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", W("chaque", 178.2) + 0.2, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 175.4, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 175.8, rot=2)
bw("Abonne-toi", W("abonne", 174.5) + 0.4, 1.0)

# ================================================================ 04 · Passage 3 : 2 Rois 4.2
parole(183.0, "2 Rois 4.2", 185.4,
       f"« Que puis-je {m(0, 'faire pour toi')} ? Dis-moi, {m(1, 'qu’as-tu à la maison')} ? »",
       194.2, 197.9, [W("faire", 194.1), W("maison", 194.1)], size=60)

S = nxt(198.0)
title(S, ["Qu'as-tu à", "la [maison] ?"], 198.1, "Une question pleine de sagesse", hl=W("sagesse", 198.0), size=96)
tg(S, 450, "Avant ce qui manque : ce que tu as", W("manque", 198.0), "", 32)
tg(S, 540, "Un petit vase d'huile", W("vase", 203.7), "", 36)
tg(S, 630, "Le point de départ de la solution", W("départ", 203.7), "acc", 32)
stk(S, "vase-huile-veuve", 1050, 280, 560, 198.7)

S = nxt(210.7)
title(S, ["Tes [ressources]", "réelles"], 210.8, "Fais l'inventaire", hl=W("ressources", 210.7), size=90)
tg(S, 440, "Compétences", W("compétences", 210.7), "", 32)
tg(S, 510, "Objets", W("objets", 210.7), "", 32)
tg(S, 580, "Relations", W("relations", 210.7), "", 32)
tg(S, 650, "Temps", W("temps", 210.7), "", 32)
tg(S, 720, "Épargne", W("épargne", 210.7), "acc", 32)
stk(S, "maison-inventaire", 1250, 240, 340, 211.4)

S = nxt(225.4)
title(S, ["L'[inventaire]"], 225.5, "Deuxième étape", hl=W("inventaire", 225.4), size=110)
tg(S, 450, "Pas pour te comparer", W("comparer", 225.4), "", 38)
tg(S, 540, "Pour voir tes ressources réelles", W("réelles", 225.4), "acc", 36)
stk(S, "maison-inventaire", 1100, 250, 340, 226.0)

# ================================================================ 05 · Passage 4 : Ecclésiaste 7.12
parole(232.5, "Ecclésiaste 7.12", 234.8,
       f"« On est à l'ombre {m(0, 'sous la sagesse')} comme on est à l'ombre sous l'argent ; mais la science a cet avantage que {m(1, 'la sagesse fait vivre')} ceux qui la possèdent. »",
       237.1, 244.5, [W("sagesse", 237.0), W("vivre", 237.0)], size=46)

S = nxt(244.6)
title(S, ["La sagesse", "[protège] mieux"], 244.7, "Comme une ombre", hl=W("protège", 244.6), size=90)
tg(S, 440, "Savoir où va ton argent", W("savoir", 250.8), "", 34)
tg(S, 520, "Repérer ce qui augmente", W("repérer", 250.8), "", 34)
tg(S, 600, "Décider calmement, pas sous la panique", W("panique", 250.8), "acc", 32)
stk(S, "arbre-ombre-sagesse", 1050, 250, 500, 245.3)

S = nxt(259.2)
title(S, ["Même salaire,", "autre [gestion]"], 259.3, "Deux personnes", hl=W("gèrent", 259.2), size=90)
tg(S, 450, "La sagesse réduit les mauvaises surprises", W("surprises", 264.9), "acc", 32)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 259.8)

# ================================================================ 06 · Passage 5 : 2 Corinthiens 9.8
parole(269.5, "2 Corinthiens 9.8", 271.3,
       f"« Et Dieu peut vous combler de toutes sortes de grâces, afin que, possédant toujours en toutes choses de quoi {m(0, 'satisfaire à tous vos besoins')}, vous ayez encore {m(1, 'en abondance pour toute bonne œuvre')}. »",
       273.8, 284.9, [W("satisfaire", 273.7), W("abondance", 273.7)], size=42, ref_y=900)

S = nxt(285.0)
title(S, ["Suffisance,", "et [générosité]"], 285.1, "Dieu ne promet pas le luxe", hl=W("générosité", 285.0), size=90)
tg(S, 440, "De quoi vivre", W("vivre", 285.0), "", 36)
tg(S, 520, "De quoi donner", W("donner", 285.0), "", 36)
tg(S, 600, "Un petit don régulier, décidé calmement", W("régulier", 300.1), "acc", 32)
stk(S, "main-petit-don", 1100, 260, 330, 285.7)

# ================================================================ 07 · Cinq étapes
S = nxt(305.6)
title(S, ["Cinq [étapes]", "pour traverser"], 305.7, "Passons à la pratique", hl=W("étapes", 305.6), size=84)
counter(S, 80, 450, 0, 5, 306.6, 0.9, " étapes", 130)
stk(S, "liste-cinq-etapes", 1100, 240, 380, 306.2, rot=-1)

S = nxt(310.1)
title(S, ["Étape 1 :", "la [réalité]"], 310.2, "Regarde en face", hl=W("réalité", 310.1), size=96)
tg(S, 440, "Tes relevés des trois derniers mois", W("relevés", 310.1), "", 32)
tg(S, 520, "Alimentation, énergie, logement, carburant", W("carburant", 310.1), "", 30)
tg(S, 600, "Comparer avec l'an dernier", W("dernier", 327.4), "acc", 34)
stk(S, "releves-loupe-trois-mois", 1050, 270, 500, 310.8, rot=-2)

S = nxt(333.2)
title(S, ["Étape 2 :", "l'[essentiel]"], 333.3, "D'abord", hl=W("essentiel", 333.2), size=96)
tg(S, 440, "Logement, nourriture, santé", W("nourriture", 333.2), "", 34)
tg(S, 520, "Transports, dettes à rembourser", W("transports", 333.2), "", 34)
tg(S, 600, "Les envies ensuite, sans culpabiliser", W("envies", 344.9), "acc", 32)
stk(S, "enveloppes-budget", 1100, 270, 340, 333.9, rot=-2)

S = nxt(360.1)
title(S, ["Étape 3 :", "tes coûts [fixes]"], 360.2, "Exercice de 20 minutes", hl=W("fixes", 360.1), size=90)
tg(S, 440, "Assurance, téléphone, internet, énergie, banque", W("assurance", 365.7), "", 28)
tg(S, 520, "Comparer et renégocier", W("renégocier", 365.7), "", 34)
tg(S, 600, "Liste, compare, prix au kilo", W("kilo", 376.9), "acc", 34)
stk(S, "contrats-renegocies", 1050, 270, 500, 360.8, rot=-2)

S = nxt(394.0)
title(S, ["Étape 4 :", "protège ta [réserve]"], 394.1, "Pas de crédit pour l'épicerie", hl=W("réserve", 394.0), size=84)
tg(S, 450, "L'épicerie à crédit ne règle rien", W("épicerie", 394.0), "", 32)
tg(S, 540, "La réserve : pour les vrais imprévus", W("imprévus", 406.7), "", 32)
tg(S, 630, "Même un peu chaque semaine", W("semaine", 412.9), "acc", 36)
stk(S, "bocal-cadenas-reserve", 1100, 260, 380, 394.7)

S = nxt(418.9)
title(S, ["Étape 5 :", "[revenu] et générosité"], 419.0, "Si c'est possible", hl=W("revenu", 418.9), size=78)
tg(S, 440, "Des heures en plus", W("heures", 418.9), "", 32)
tg(S, 510, "Une compétence à développer", W("compétence", 418.9), "", 32)
tg(S, 580, "Une demande d'augmentation préparée", W("augmentation", 418.9), "", 32)
tg(S, 650, "Vendre ce que tu n'utilises plus", W("vente", 418.9), "", 32)
tg(S, 720, "Garder une part pour donner", W("donner", 436.7), "acc", 32)
stk(S, "main-petit-don", 1250, 260, 330, 419.5)

# ================================================================ 08 · Pièges, exemple
S = nxt(447.4)
title(S, ["Cinq [pièges]", "à éviter"], 447.5, "Attention", hl=W("pièges", 447.4), size=84)
tg(S, 420, "1 · La panique : acheter et stocker", W("panique", 447.4), "", 30)
tg(S, 495, "2 · Les rendements miracles", W("rendements", 447.4), "", 30)
tg(S, 570, "3 · S'endetter pour garder son niveau", W("endetter", 447.4), "", 30)
tg(S, 645, "4 · Arrêter de donner par peur", W("arrêter", 447.4), "", 30)
tg(S, 720, "5 · Se cacher par honte", W("honte", 447.4), "acc", 30)
stk(S, "drapeau-rouge", 1250, 260, 300, 448.0)

S = nxt(467.0)
title(S, ["Épargne :", "pas de [précipitation]"], 467.1, "Si tu hésites sur un placement", hl=W("précipitées", 467.0), size=78)
tg(S, 440, "Comprends avant de placer", W("comprendre", 467.0), "", 34)
tg(S, 520, "L'avis d'un professionnel indépendant", W("professionnel", 467.0), "", 32)
tg(S, 600, "Méfie-toi de ceux qui te pressent", W("presse", 478.6), "acc", 32)
stk(S, "baton-conseillers", 1050, 280, 470, 467.7, rot=-2)

S = nxt(482.6)
title(S, ["Que m'apprend", "cette [période] ?"], 482.7, "La question qui change le regard", hl=W("apprend", 482.6), size=84)
tg(S, 450, "Et que mettre en place pour être plus solide ?", W("solide", 482.6), "acc", 32)
stk(S, "baton-pense", 1150, 230, 270, 483.2)

S = nxt(494.1)
title(S, ["Un exemple :", "[Inès] et Karim"], 494.2, "Prenons", hl=W("Inès", 494.1), size=84)
tg(S, 450, "Deux enfants, un budget serré", W("enfants", 495.7), "", 34)
tg(S, 540, "Des factures qui augmentent", W("augmenté", 495.7), "acc", 34)
stk(S, "famille-sortie", 1050, 270, 560, 494.8)

S = nxt(501.1)
title(S, ["Trois postes", "qui ont [grimpé]"], 501.2, "Un soir, ils prient", hl=W("grimpé", 501.1), size=84)
tg(S, 450, "Les courses", W("courses", 501.1), "", 36)
tg(S, 530, "L'énergie", W("énergie", 501.1), "", 36)
tg(S, 610, "L'assurance", W("assurance", 501.1), "", 36)
tg(S, 690, "Ils renégocient, comparent, préparent une liste", W("liste", 508.8), "acc", 30)
stk(S, "baton-courses-ticket", 1100, 250, 420, 501.8)

S = nxt(514.7)
title(S, ["Un peu de", "[marge]"], 514.8, "Chaque mois", hl=W("marge", 514.7), size=100)
tg(S, 450, "Une petite part de côté", W("côté", 514.7), "", 36)
tg(S, 540, "Une autre pour donner", W("donner", 514.7), "", 36)
tg(S, 630, "Retrouver de la paix", W("paix", 521.0), "acc", 36)
stk(S, "bocal-cadenas-reserve", 1100, 260, 380, 515.3)

S = nxt(533.1)
title(S, ["Un [exemple],", "pas un témoignage"], 533.2, "À retenir", hl=W("exemple", 533.1), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 533.1), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 533.8, rot=3)

# ================================================================ 09 · Récapitulatif et action
S = nxt(539.9)
title(S, ["L'[essentiel]"], 540.0, "Retenons", hl=540.4, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 540.2, rot=-3)

S = nxt(541.5)
title(S, ["Ce qu'on [retient]"], 541.6, "Garder la paix", hl=W("abandonne", 541.5), size=96)
tg(S, 420, "Dieu n'abandonne pas", W("abandonne", 541.5), "", 32)
tg(S, 500, "L'inquiétude ne règle rien, l'action calme", W("calme", 541.5), "", 30)
tg(S, 580, "Regarde ce que tu as déjà", W("déjà", 541.5), "", 32)
tg(S, 660, "La sagesse protège", W("protège", 541.5), "", 32)
tg(S, 740, "La générosité s'ajuste à tes moyens", W("générosité", 541.5), "acc", 30)
stk(S, "baton-priere", 1250, 260, 300, 542.0)

S = nxt(553.7)
title(S, ["Les cinq", "[étapes]"], 553.8, "Rappel", hl=554.4, size=90)
tg(S, 440, "1 · Regarder la réalité en face", W("regarder", 553.7), "", 32)
tg(S, 520, "2 · Mettre l'essentiel d'abord", W("mettre", 553.7), "", 32)
tg(S, 600, "3 · Alléger les coûts fixes", W("alléger", 553.7), "", 32)
tg(S, 680, "4 · Protéger ta réserve, éviter le crédit", W("protéger", 553.7), "", 32)
tg(S, 760, "5 · Augmenter ton revenu, rester généreux", W("augmenter", 553.7), "acc", 32)
stk(S, "liste-cinq-etapes", 1200, 260, 400, 554.2, rot=-1)

S = nxt(567.7)
title(S, ["Une seule chose", "cette [semaine]"], 567.8, "Ton action", hl=W("contrats", 567.7), size=78)
tg(S, 440, "Prends vingt minutes", W("20", 567.7), "", 36)
tg(S, 520, "Ouvre tes contrats", W("contrats", 567.7), "", 36)
tg(S, 600, "Compare ou renégocie", W("renégocier", 567.7), "acc", 36)
stk(S, "contrats-renegocies", 1100, 260, 440, 568.3, rot=-2)

S = nxt(575.0)
title(S, ["Tu contrôles", "tes [décisions]"], 575.1, "Pas les prix", hl=W("décisions", 575.0), size=84)
tg(S, 450, "Un cœur en paix", W("paix", 575.0), "acc", 38)
tg(S, 540, "Chaque décision calme : une victoire", W("victoire", 580.6), "", 32)
stk(S, "baton-patient-calme", 1100, 260, 400, 575.6)
stk(S, "croix-verte", 1560, 340, 220, W("victoire", 580.6), rot=4)

S = nxt(585.1)
title(S, ["Quel poste a le plus", "[augmenté] ?"], 585.2, "Et toi", hl=W("augmenté", 585.1), size=78)
stk(S, "baton-pense", 1150, 230, 260, 585.7)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 588.0) - 0.6, 14)
sfx("click", W("commentaire", 588.0) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 591.2), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 68.5), ("02", "Passages 1 à 3", 68.5, 232.5), ("03", "Passages 4 et 5", 232.5, 305.6),
              ("04", "Cinq étapes", 305.6, 447.4), ("05", "Pièges et exemple", 447.4, 539.9), ("06", "À retenir", 539.9, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)
