"""Vidéo longue « Comment prendre de sages décisions financières selon la Bible » — style 02 en 16:9, ~9 min.
5 passages (séquence « Parole » identique), 3 questions à retenir, appel à s'abonner au milieu, 5 étapes, règle de délai, 4 signaux d'alerte, exemple (Nadia et Samir), récapitulatif.
Les temps sont lus dans transcript.json (voix fournie par l'utilisateur ; versets réinsérés là où la transcription était incertaine).

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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Comment prendre de sages décisions financières", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 537.4
s.setup(here=HERE, duration=552.8, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
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
title(S, ["Décider avec", "[sagesse] ?"], 0.1, "Chaque semaine", hl=W("sagesse", 0.0), size=90)
tg(S, 420, "Acheter", W("acheter", 0.0) + 0.3, "", 34)
tg(S, 490, "Emprunter", W("emprunter", 0.0), "", 34)
tg(S, 560, "Changer de travail", W("travail", 0.0), "", 34)
tg(S, 630, "Épargner", W("épargner", 0.0), "", 34)
tg(S, 700, "Donner", W("donner", 0.0), "acc", 34)
stk(S, "baton-carrefour", 1100, 240, 500, 0.5, rot=-2)

S = nxt(9.3)
title(S, ["Trop [vite]", "ou jamais ?"], 9.4, "Deux réflexes", hl=W("vite", 9.3), size=90)
tg(S, 450, "Décider vite, sous pression", W("pression", 9.3), "", 38)
tg(S, 540, "Ne jamais décider", W("jamais", 9.3), "acc", 38)
stk(S, "baton-presse", 1050, 250, 500, 9.8, rot=-2)

S = nxt(16.1)
title(S, ["L'argent,", "source de [stress]"], 16.2, "Dans les deux cas", hl=W("stress", 16.1), size=78)
tg(S, 450, "Tes priorités", W("priorités", 16.1), "", 38)
tg(S, 540, "Ta famille", W("famille", 16.1), "", 38)
tg(S, 630, "Ta foi", W("foi", 16.1), "acc", 38)
stk(S, "baton-soucieux", 1150, 250, 290, 16.8)

S = nxt(24.2)
title(S, ["Pas une réponse,", "une [manière]"], 24.3, "La Bible ne donne pas", hl=W("manière", 24.2), size=78)
tg(S, 450, "Une manière de décider", W("manière", 24.2) + 0.4, "acc", 40)
stk(S, "livre-croix-ouvert", 1050, 290, 400, 24.8, rot=-3)

S = nxt(31.4)
title(S, ["Au [programme]"], 31.5, "Dans cette vidéo", hl=32.2)
tg(S, 420, "5 passages", W("cinq", 31.4, 0), "", 40)
tg(S, 510, "5 étapes concrètes", W("cinq", 31.4, 1), "", 40)
tg(S, 600, "Les signaux d'alerte", W("signaux", 31.4), "", 40)
tg(S, 690, "Un exemple", W("exemple", 31.4), "acc", 40)
stk(S, "pupitre-parole", 1100, 260, 380, 32.2, rot=-2)

S = nxt(40.7)
title(S, ["Une règle de", "[délai]"], 40.8, "Reste jusqu'à la fin", hl=W("délai", 40.7), size=90)
tg(S, 450, "Une règle de délai très simple", W("règle", 40.7), "", 38)
tg(S, 540, "Une grille de décision", W("grille", 40.7), "acc", 38)
stk(S, "sablier-calendrier", 1100, 270, 440, 41.4, rot=-2)

S = nxt(46.8)
title(S, ["Pas un conseil", "[personnalisé]"], 46.9, "Une précision importante", hl=W("personnalisé", 46.8), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 46.8), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 46.8), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 47.6)
hit(W("personnalisé", 46.8), 0.8)

# ================================================================ 02 · Passage 1 : Proverbes 3.5-6
parole(55.0, "Proverbes 3.5-6", 57.4,
       f"« Confie-toi en l'Éternel de tout ton cœur, et {m(0, 'ne t’appuie pas sur ta sagesse')} ; reconnais-le dans toutes tes voies, "
       f"et {m(1, 'il aplanira tes sentiers')}. »",
       59.2, 67.9, [W("appuie", 59.2), W("aplanira", 59.2)], size=46)

S = nxt(68.1)
title(S, ["Ce que le verset", "[ne dit pas]"], 68.2, "Remarque", hl=68.9, size=72)
tg(S, 450, "Pas : ne réfléchis jamais", W("réfléchis", 68.1), "", 36)
tg(S, 540, "Pas : tout ira bien", W("ira", 68.1), "", 36)
tg(S, 630, "Aucun résultat promis", W("résultat", 68.1), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 68.7)

S = nxt(76.6)
title(S, ["Où placer ta", "[confiance]"], 76.7, "Le verset dit", hl=W("confiance", 76.6), size=84)
tg(S, 450, "Ton intelligence ne suffit pas toujours", W("intelligence", 76.6), "", 34)
tg(S, 540, "L'envie ou la peur parlent plus fort", W("peur", 76.6), "acc", 34)
stk(S, "baton-tiraille", 1150, 250, 300, 77.2)

S = nxt(85.1)
title(S, ["Un coup de", "[tête]"], 85.2, "Souviens-toi", hl=W("tête", 85.1), size=96)
tg(S, 450, "Sur le moment, tout semble évident", W("évident", 85.1) - 1.2, "", 34)
tg(S, 540, "Ensuite, le doute arrive", W("doute", 85.1), "acc", 38)
stk(S, "baton-tente-carte", 1100, 250, 380, 85.8)

S = nxt(91.4)
title(S, ["Inviter [Dieu]", "dans ton argent"], 91.5, "Le reconnaître", hl=W("inviter", 91.4), size=78)
tg(S, 450, "Pas seulement le dimanche", W("dimanche", 91.4), "acc", 38)
stk(S, "baton-priere", 1100, 250, 300, 92.2)

S = nxt(97.6)
title(S, ["Prendre de la", "[distance]"], 97.7, "Quand tu pries", hl=W("distance", 97.6), size=84)
tg(S, 450, "Plus clair quelques minutes plus tard", W("minutes", 97.6), "acc", 34)
stk(S, "baton-serein", 1100, 250, 300, 98.4)

S = nxt(104.9)
title(S, ["Étape 1 :", "[prie]"], 105.0, "Première étape", hl=W("prier", 104.9), size=96)
tg(S, 450, "Ce que tu veux vraiment", W("veux", 104.9), "", 38)
tg(S, 540, "Ce qui te fait peur", W("peur", 104.9), "acc", 38)
stk(S, "baton-priere", 1150, 250, 300, 105.4)
stk(S, "croix-verte", 1560, 340, 220, W("peur", 104.9), rot=4)

# ================================================================ 03 · Passage 2 : Jacques 1.5
parole(110.0, "Jacques 1.5", 112.2,
       f"« Si quelqu'un d'entre vous {m(0, 'manque de sagesse')}, qu'il la demande à Dieu, qui donne à tous libéralement et sans reproche, "
       f"et {m(1, 'elle lui sera donnée')}. »",
       114.5, 121.4, [W("manque", 114.5), W("sera", 114.5)], size=46)

S = nxt(121.6)
title(S, ["Une [invitation]"], 121.7, "Ce verset", hl=W("invitation", 121.6), size=96)
tg(S, 450, "Pas besoin de tout comprendre", W("comprendre", 121.6), "", 36)
tg(S, 540, "Manquer de sagesse : le point de départ", W("départ", 121.6), "acc", 34)
stk(S, "baton-lit-livre", 1100, 260, 340, 122.2)

S = nxt(129.0)
title(S, ["Prier et", "[réfléchir]"], 129.1, "Ensemble", hl=W("réfléchir", 129.0), size=90)
tg(S, 450, "Tu demandes la sagesse", W("demandes", 129.0), "", 38)
tg(S, 540, "Tu l'exerces", W("exerces", 129.0), "acc", 38)
stk(S, "baton-pense", 1100, 250, 270, 129.6)
stk(S, "baton-priere", 1500, 300, 280, W("exerces", 129.0), rot=3)

S = nxt(137.5)
title(S, ["Si cette vidéo", "t'[aide]…"], 137.6, "Un instant", hl=W("aide", 137.5))
tg(S, 450, "Abonne-toi", W("abonne", 137.5) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", W("chaque", 137.5, 0) + 0.2, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 138.4, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 138.8, rot=2)
bw("Abonne-toi", W("abonne", 137.5) + 0.4, 1.0)

# ================================================================ 04 · Passage 3 : Proverbes 15.22
parole(145.4, "Proverbes 15.22", 147.8,
       f"« Les projets échouent, {m(0, 'faute d’une assemblée qui délibère')} ; mais ils réussissent quand il y a "
       f"{m(1, 'de nombreux conseillers')}. »",
       149.8, 155.7, [W("faute", 149.8), W("nombreux", 149.8)], size=48)

S = nxt(155.9)
title(S, ["Seul,", "plus [fragile]"], 156.0, "Les décisions", hl=W("fragiles", 155.9), size=90)
tg(S, 450, "Des angles morts", W("angles", 155.9), "", 38)
tg(S, 540, "On ne voit que ce qui nous arrange", W("arrange", 155.9), "acc", 34)
stk(S, "baton-soucieux", 1150, 250, 290, 156.6)

S = nxt(163.0)
title(S, ["Un bon", "[conseiller]"], 163.1, "Il te pose", hl=W("conseiller", 163.0), size=90)
tg(S, 450, "Des questions que tu ne te poses pas", W("questions", 163.0), "", 34)
tg(S, 540, "Ce que tu n'as pas envie d'entendre", W("entendre", 163.0), "acc", 34)
stk(S, "baton-conseillers", 1050, 280, 470, 163.6, rot=-2)

S = nxt(169.2)
title(S, ["Bien choisir", "tes [conseillers]"], 169.3, "Les critères", hl=W("conseillers", 169.2), size=78)
tg(S, 450, "Mûrs", W("mûres", 169.2), "", 38)
tg(S, 540, "Honnêtes", W("honnêtes", 169.2), "", 38)
tg(S, 630, "Sans intérêt dans ta décision", W("intérêt", 169.2), "acc", 36)
stk(S, "couple-budget", 1100, 260, 440, 169.8, rot=-2)

S = nxt(175.8)
title(S, ["Premier conseiller :", "ton [conjoint]"], 175.9, "Si tu es marié", hl=W("conjoint", 175.8), size=72)
tg(S, 450, "Sujet technique : un professionnel qualifié", W("technique", 175.8), "acc", 32)
stk(S, "couple-epargne", 1100, 260, 440, 176.4, rot=-2)

S = nxt(183.1)
title(S, ["Célibataire ?", "Un [ami]"], 183.2, "Si tu es célibataire", hl=W("ami", 183.1), size=90)
tg(S, 450, "Ou un responsable de ton église", W("responsable", 183.1), "", 34)
tg(S, 540, "Ils t'aident à voir plus clair", W("clair", 183.1), "acc", 34)
stk(S, "baton-ami", 1100, 260, 340, 183.7)

S = nxt(190.4)
title(S, ["Méfie-toi de", "l'[intérêt]"], 190.5, "Attention", hl=W("gagne", 190.4), size=84)
tg(S, 450, "Celui qui gagne si tu dis oui", W("gagne", 190.4), "", 36)
tg(S, 540, "Sincère, et pourtant intéressé", W("sincère", 190.4), "acc", 36)
stk(S, "drapeau-rouge", 1150, 270, 330, 191.0)

# ================================================================ 05 · Passage 4 : Proverbes 14.15
parole(196.7, "Proverbes 14.15", 198.8,
       f"« L'homme simple {m(0, 'croit tout ce qu’on dit')}, mais l'homme prudent {m(1, 'veille sur ses pas')}. »",
       200.7, 205.0, [W("croit", 200.7), W("veille", 200.7)], size=52)

S = nxt(205.1)
title(S, ["De belles", "[paroles]"], 205.2, "Dans l'argent", hl=W("paroles", 205.1), size=90)
tg(S, 450, "Gains faciles", W("gains", 205.1), "", 38)
tg(S, 540, "Offres limitées dans le temps", W("offres", 205.1), "", 38)
tg(S, 630, "Témoignages qui font rêver", W("témoignages", 205.1), "acc", 38)
stk(S, "baton-vitrine", 1100, 250, 380, 205.7)

S = nxt(212.5)
title(S, ["L'homme prudent", "[vérifie]"], 212.6, "Des questions", hl=W("vérifie", 212.5), size=78)
tg(S, 450, "Qui me propose cela ?", W("propose", 212.5), "", 36)
tg(S, 530, "Que dit le contrat ?", W("contrat", 212.5), "", 36)
tg(S, 610, "Quels sont les risques ?", W("risques", 212.5), "", 36)
tg(S, 690, "Et si ça tourne mal ?", W("mal", 212.5), "acc", 36)
stk(S, "loupe-contrat", 1100, 260, 400, 213.0, rot=-2)

S = nxt(222.6)
title(S, ["Prudent,", "pas sans [foi]"], 222.7, "Être prudent", hl=W("foi", 222.6), size=84)
tg(S, 450, "Prendre au sérieux la responsabilité confiée", W("responsabilité", 222.6), "acc", 32)
stk(S, "baton-budget", 1100, 260, 380, 223.2)

S = nxt(227.4)
title(S, ["Lis les", "[conditions]"], 227.5, "Concrètement", hl=W("conditions", 227.4), size=90)
tg(S, 450, "Les conditions par écrit", W("écrit", 227.4), "", 36)
tg(S, 540, "Comparer au moins deux offres", W("offres", 227.4), "", 36)
tg(S, 630, "Ne signe jamais sans comprendre", W("signe", 227.4), "acc", 36)
stk(S, "feuille-options-chiffres", 1100, 260, 400, 228.0, rot=-2)

# ================================================================ 06 · Passage 5 : Proverbes 19.2
parole(232.9, "Proverbes 19.2", 234.9,
       f"« {m(0, 'Le manque de science')} n'est bon pour personne, et celui qui {m(1, 'précipite ses pas')} s'égare. »",
       236.7, 240.9, [W("manque", 236.7), W("précipite", 236.7)], size=52)

S = nxt(241.1)
title(S, ["Deux", "[dangers]"], 241.2, "Ce verset", hl=W("dangers", 241.1), size=96)
tg(S, 450, "Décider sans information", W("information", 241.1), "", 36)
tg(S, 540, "Décider trop vite", W("vite", 241.1), "", 36)
tg(S, 630, "L'urgence fabriquée par les vendeurs", W("vendeurs", 241.1), "acc", 34)
stk(S, "horloge-urgence", 1150, 250, 400, 241.7)

S = nxt(252.3)
title(S, ["Une bonne décision", "[attend]"], 252.4, "Retiens", hl=W("attendre", 252.3), size=78)
tg(S, 450, "Si elle ne le supporte pas : pourquoi ?", W("pourquoi", 252.3), "acc", 34)
stk(S, "baton-attend", 1100, 250, 400, 253.0)

S = nxt(257.9)
title(S, ["Diligence,", "pas [précipitation]"], 258.0, "La différence", hl=W("précipitation", 257.9, 1), size=72)
tg(S, 450, "La diligence avance avec méthode", W("diligence", 257.9, 1), "", 34)
tg(S, 540, "La précipitation fonce sans regarder", W("fonce", 257.9), "acc", 34)
stk(S, "baton-travaille", 1100, 260, 340, 258.6)
stk(S, "baton-presse", 1500, 330, 330, W("fonce", 257.9), rot=3)

# ================================================================ 07 · Cinq étapes
S = nxt(266.4)
title(S, ["Cinq [étapes]", "avant de décider"], 266.5, "Passons à la pratique", hl=W("étapes", 266.4), size=78)
counter(S, 80, 450, 0, 5, 267.4, 0.9, " étapes", 130)
stk(S, "liste-cinq-etapes", 1100, 240, 420, 267.0, rot=-1)

S = nxt(271.2)
title(S, ["Étape 1 :", "[prie]"], 271.3, "Étape 1", hl=W("prie", 271.2), size=96)
tg(S, 450, "Remets ta décision à Dieu", W("remets", 271.2), "", 38)
tg(S, 540, "Demande-lui la sagesse", W("demande", 271.2), "acc", 38)
stk(S, "baton-priere", 1100, 260, 300, 271.8)

S = nxt(276.3)
title(S, ["Étape 2 :", "les [faits]"], 276.4, "Étape 2", hl=W("faits", 276.3), size=96)
tg(S, 450, "Écris tes options", W("options", 276.3), "", 36)
tg(S, 540, "Le coût total sur la durée", W("durée", 276.3), "", 36)
tg(S, 630, "Ce que tu gagnes, ce que tu risques", W("risques", 276.3), "acc", 32)
stk(S, "feuille-options-chiffres", 1100, 260, 400, 276.9, rot=-2)

S = nxt(285.3)
title(S, ["Étape 3 :", "le [conseil]"], 285.4, "Étape 3", hl=W("conseil", 285.3), size=96)
tg(S, 450, "Ton conjoint", W("conjoint", 285.3), "", 36)
tg(S, 530, "Une personne de confiance", W("confiance", 285.3), "", 36)
tg(S, 610, "Un professionnel qualifié", W("professionnel", 285.3), "", 36)
tg(S, 690, "Que vois-tu que je ne vois pas ?", W("vois", 285.3), "acc", 34)
stk(S, "baton-conseillers", 1050, 280, 470, 285.9, rot=-2)

S = nxt(296.3)
title(S, ["Étape 4 :", "le [temps]"], 296.4, "Étape 4", hl=W("temps", 296.3), size=96)
tg(S, 450, "Petit achat : 24 heures", W("24", 296.3), "", 36)
tg(S, 540, "Achat important : 1 semaine", W("semaine", 296.3), "", 36)
tg(S, 630, "Très grosse décision : plus encore", W("grosse", 296.3), "acc", 36)
stk(S, "sablier-calendrier", 1050, 270, 480, 296.9, rot=-2)

S = nxt(311.0)
title(S, ["Si l'offre", "[disparaît]"], 311.1, "Entre-temps", hl=W("disparaît", 311.0), size=90)
tg(S, 450, "Presque rien de perdu", W("perdu", 311.0), "", 38)
tg(S, 540, "Si elle reste : la tête plus claire", W("claire", 311.0), "acc", 36)
stk(S, "baton-serein", 1100, 250, 300, 311.6)

S = nxt(317.4)
title(S, ["Difficile à", "[annuler]"], 317.5, "Plus tu dois attendre", hl=W("annuler", 317.4), size=90)
tg(S, 450, "Un petit achat se rattrape", W("rattrape", 317.4), "", 36)
tg(S, 540, "Un crédit sur des années, beaucoup moins", W("crédit", 317.4), "acc", 32)
stk(S, "tour-pieces-bascule", 1100, 260, 340, 318.0, rot=-2)

S = nxt(325.6)
title(S, ["Étape 5 :", "trois [questions]"], 325.7, "Étape 5", hl=W("questions", 325.6), size=84)
tg(S, 450, "1 · Puis-je me le permettre ?", W("permettre", 325.6), "", 34)
tg(S, 540, "2 · Cela respecte mes priorités ?", W("2", 325.6), "", 34)
tg(S, 630, "3 · Si le pire arrive, pourrai-je l'assumer ?", W("3", 325.6), "acc", 32)
stk(S, "baton-test-trois", 1150, 250, 330, 326.2)

S = nxt(341.3)
title(S, ["Pas de garantie,", "moins de [surprises]"], 341.4, "Ces trois questions", hl=W("surprises", 341.3), size=72)
tg(S, 450, "Elles évitent beaucoup de mauvaises surprises", W("évitent", 341.3), "acc", 32)
stk(S, "baton-content", 1150, 260, 300, 342.0)

S = nxt(347.0)
title(S, ["Elles valent", "pour [tout]"], 347.1, "Dans tous les cas", hl=W("tout", 347.0, 0) + 0.3, size=90)
tg(S, 440, "Un achat", W("achat", 347.0), "", 34)
tg(S, 510, "Un emprunt", W("emprunt", 347.0), "", 34)
tg(S, 580, "Un changement de travail", W("travail", 347.0), "", 34)
tg(S, 650, "Un don important", W("don", 347.0), "", 34)
tg(S, 720, "Un projet de couple", W("couple", 347.0), "acc", 34)
stk(S, "baton-ecrit-liste", 1150, 260, 340, 347.6)

# ================================================================ 08 · Signaux d'alerte, grâce
S = nxt(357.3)
title(S, ["Quatre signaux", "d'[alerte]"], 357.4, "Attention", hl=W("alerte", 357.3), size=84)
counter(S, 80, 450, 0, 4, 358.0, 0.8, " signaux", 120)
stk(S, "drapeau-rouge", 1150, 260, 330, 358.2)

S = nxt(W("presse", 357.3) - 0.5)
title(S, ["Te [reconnais]-tu ?"], W("presse", 357.3) - 0.4, "Les signaux", hl=W("presse", 357.3) + 0.5, size=84)
tg(S, 420, "1 · On te presse de décider", W("presse", 357.3), "", 34)
tg(S, 510, "2 · Un gain garanti, sans risque", W("garanti", 357.3), "", 34)
tg(S, 600, "3 · Le secret, même envers ton conjoint", W("secret", 357.3), "", 34)
tg(S, 690, "4 · Impossible à expliquer simplement", W("expliquer", 357.3), "acc", 34)
stk(S, "horloge-urgence", 1250, 260, 360, W("presse", 357.3))

S = nxt(373.4)
title(S, ["Alors", "[ralentis]"], 373.5, "Si un signal apparaît", hl=W("ralentis", 373.4), size=96)
tg(S, 450, "Rien à perdre à prendre le temps", W("rien", 373.4), "", 36)
tg(S, 540, "Beaucoup à perdre à te presser", W("presser", 373.4), "acc", 36)
stk(S, "baton-attend", 1100, 250, 400, 374.0)

S = nxt(379.6)
title(S, ["Un bon projet", "résiste aux [questions]"], 379.7, "Rappelle-toi", hl=W("résiste", 379.6), size=72)
tg(S, 450, "Ni questions, ni temps, ni avis : mauvais signe", W("rarement", 379.6), "acc", 30)
stk(S, "loupe-contrat", 1100, 270, 380, 380.2, rot=-2)

S = nxt(386.8)
title(S, ["Reste [honnête]", "avec toi-même"], 386.9, "Un dernier test", hl=W("honnête", 386.8), size=78)
tg(S, 450, "Chercher seulement des raisons de dire oui ?", W("raisons", 386.8), "acc", 32)
stk(S, "baton-pense", 1150, 240, 270, 387.4)

S = nxt(394.4)
title(S, ["Pas de", "[condamnation]"], 394.5, "Déjà une mauvaise décision ?", hl=W("condamnes", 394.4), size=84)
tg(S, 450, "La grâce autant que la sagesse", W("grâce", 394.4), "", 34)
tg(S, 530, "Tire la leçon", W("leçon", 394.4), "", 34)
tg(S, 610, "Corrige ce qui peut l'être", W("corrige", 394.4), "", 34)
tg(S, 690, "Et avance", W("avance", 394.4), "acc", 34)
stk(S, "colombe", 1100, 280, 300, 395.0, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("grâce", 394.4), rot=4)

S = nxt(405.5)
title(S, ["Imparfaite,", "mais [avancer]"], 405.6, "Si tu hésites toujours", hl=W("paralysie", 405.5), size=84)
tg(S, 450, "Prière et conseil", W("prière", 405.5), "", 36)
tg(S, 540, "Un pas après l'autre", W("avance", 405.5), "acc", 38)
stk(S, "sentier-aplani", 1050, 260, 480, 406.2, rot=-2)

# ================================================================ 09 · Exemple : Nadia et Samir
S = nxt(415.8)
title(S, ["Un exemple :", "[Nadia] et Samir"], 415.9, "Prenons", hl=W("Nadia", 415.8), size=78)
tg(S, 450, "Changer de voiture", W("voiture", 417.4), "", 36)
tg(S, 530, "Plus chère que leur budget", W("budget", 417.4), "", 36)
tg(S, 610, "Vendue à crédit", W("crédit", 417.4), "", 36)
tg(S, 690, "Offre jusqu'au week-end", W("week", 417.4), "acc", 36)
stk(S, "voiture-neuve-credit", 1100, 270, 470, 416.6, rot=-2)

S = nxt(427.3)
title(S, ["Dire oui,", "[tout de suite] ?"], 427.4, "Samir est tenté", hl=W("suite", 427.3), size=84)
tg(S, 450, "Nadia propose les 5 étapes", W("propose", 427.3), "", 36)
tg(S, 540, "Ils prient ensemble", W("prient", 427.3), "", 36)
tg(S, 630, "Ils écrivent les chiffres", W("écrivent", 427.3), "acc", 36)
stk(S, "couple-budget", 1100, 260, 440, 427.9, rot=-2)

S = nxt(437.5)
title(S, ["Une [question]", "simple"], 437.6, "Un couple de l'église", hl=W("travail", 437.5), size=90)
tg(S, 450, "Et si l'un de vous perd son travail ?", W("perd", 437.5), "acc", 34)
stk(S, "baton-conseillers", 1050, 280, 470, 438.0, rot=-2)

tA = W("attendent", 437.5)
S = nxt(tA - 0.3)
title(S, ["Ils [attendent]", "une semaine"], tA - 0.2, "L'offre est terminée", hl=tA + 0.2, size=84)
tg(S, 450, "Une voiture d'occasion plus modeste", W("occasion", 437.5), "", 34)
tg(S, 540, "Payée avec leur épargne", W("épargne", 437.5), "acc", 36)
stk(S, "voiture-occasion", 1050, 300, 540, tA + 0.5, rot=-2)

S = nxt(451.3)
title(S, ["Pas de", "[regret]"], 451.4, "Au contraire", hl=W("regret", 451.3), size=96)
tg(S, 450, "De la marge pour donner", W("donner", 451.3), "", 36)
tg(S, 540, "De la marge pour les imprévus", W("imprévus", 451.3), "acc", 36)
stk(S, "baton-content", 1150, 260, 300, 452.0)
stk(S, "enveloppe-don", 1540, 440, 290, W("donner", 451.3), rot=3)

S = nxt(457.2)
title(S, ["Un [exemple],", "pas un témoignage"], 457.3, "À retenir", hl=W("exemple", 457.2), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 457.2), "acc", 32)
tg(S, 540, "La manière de décider peut toujours être sage", W("manière", 457.2), "", 32)
stk(S, "colombe", 1100, 280, 300, 458.0, rot=3)

# ================================================================ 10 · Récapitulatif et action
S = nxt(468.8)
title(S, ["L'[essentiel]"], 468.9, "Retenons", hl=469.3, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 469.0, rot=-3)

S = nxt(469.9)
title(S, ["Une [manière]", "de décider"], 470.0, "Pas un verset par décision", hl=W("manière", 469.9), size=84)
tg(S, 440, "Confier ton cœur à Dieu", W("confier", 469.9), "", 34)
tg(S, 520, "Demander la sagesse", W("demander", 469.9), "", 34)
tg(S, 600, "Chercher des conseillers", W("chercher", 469.9), "", 34)
tg(S, 680, "Vérifier avant de croire", W("vérifier", 469.9), "", 34)
tg(S, 760, "Ne pas te précipiter", W("précipiter", 469.9), "acc", 34)
stk(S, "baton-carrefour", 1250, 260, 420, 470.6, rot=-2)

S = nxt(483.1)
title(S, ["Les cinq", "[étapes]"], 483.2, "Rappel", hl=483.8, size=90)
tg(S, 440, "1 · Prier", W("1", 483.1), "", 32)
tg(S, 520, "2 · Rassembler les faits", W("2", 483.1), "", 32)
tg(S, 600, "3 · Demander conseil", W("3", 483.1), "", 32)
tg(S, 680, "4 · Laisser passer du temps", W("4", 483.1), "", 32)
tg(S, 760, "5 · Vérifier avec les trois questions", W("5", 483.1), "acc", 32)
stk(S, "liste-cinq-etapes", 1200, 260, 400, 483.6, rot=-1)

S = nxt(493.8)
title(S, ["La règle de", "[délai]"], 493.9, "À retenir", hl=W("délai", 493.8), size=96)
tg(S, 450, "Petit achat : 24 heures", W("24", 493.8), "", 36)
tg(S, 540, "Achat important : 1 semaine", W("semaine", 493.8), "", 36)
tg(S, 630, "Très grosse décision : davantage", W("davantage", 493.8), "acc", 36)
stk(S, "sablier-calendrier", 1100, 270, 440, 494.4, rot=-2)

S = nxt(501.5)
title(S, ["Une seule chose", "cette [semaine]"], 501.6, "Ton action", hl=W("semaine", 501.5), size=78)
tg(S, 450, "Ta prochaine décision financière", W("prochaine", 501.5), "", 36)
tg(S, 540, "Note les 3 questions de l'étape 5", W("note", 501.5), "acc", 36)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 502.0)
stk(S, "carnet-depenses", 1540, 460, 290, 503.0, rot=3)

S = nxt(509.4)
title(S, ["Ni rapide,", "ni [parfaite]"], 509.5, "Une décision sage", hl=W("parfaite", 509.4), size=90)
tg(S, 450, "Avec Dieu", W("Dieu", 509.4), "", 38)
tg(S, 540, "Avec conseil", W("conseil", 509.4), "", 38)
tg(S, 630, "Avec le temps nécessaire", W("temps", 509.4), "acc", 38)
stk(S, "baton-priere", 1100, 260, 300, 510.0)

S = nxt(519.3)
title(S, ["Tu n'es pas", "[seul]"], 519.4, "Face à l'argent", hl=W("seul", 519.3), size=96)
tg(S, 450, "La Bible", W("Bible", 519.3), "", 38)
tg(S, 540, "Des conseillers", W("conseillers", 519.3), "", 38)
tg(S, 630, "Un Dieu qui promet la sagesse", W("promet", 519.3), "acc", 36)
stk(S, "colombe", 1100, 280, 300, 520.0, rot=3)
stk(S, "croix-verte", 1560, 340, 220, W("promet", 519.3), rot=4)
hit(W("promet", 519.3), 0.8)

S = nxt(527.0)
title(S, ["Ta prochaine", "[décision] ?"], 527.1, "Et toi", hl=W("prochaine", 527.0), size=84)
stk(S, "baton-pense", 1150, 230, 260, 527.6)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 530.9) - 0.6, 14)
sfx("click", W("commentaire", 530.9) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 534.0), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 55.0), ("02", "Passages 1 à 3", 55.0, 196.7), ("03", "Passages 4 et 5", 196.7, 266.4),
              ("04", "Cinq étapes", 266.4, 415.8), ("05", "Un exemple", 415.8, 468.8), ("06", "À retenir", 468.8, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)
