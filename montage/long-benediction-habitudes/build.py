"""Vidéo longue « Pourquoi Dieu pourrait ne pas bénir vos habitudes financières » — style 02 en 16:9, ~10 min.
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

THEME = {"brand": "Foi et Finances", "title": "Foi et Finances - Habitudes financières et bénédiction de Dieu", "lang": "fr"}
COLS, ROWS = 10, 9
VOICE_END = 583.9
s.setup(here=HERE, duration=599.2, cols=COLS, rows=ROWS, fmt="16:9", theme=THEME)
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
title(S, ["Tu pries,", "rien ne [bouge]"], 0.1, "Et si c'était tes habitudes ?", hl=W("avancer", 0.0), size=96)
tg(S, 450, "Tu fais des efforts", W("efforts", 0.0), "", 38)
tg(S, 540, "Tu pries pour ton budget", W("pries", 0.0), "", 38)
tg(S, 630, "Cinq habitudes à examiner", W("habitudes", 4.0), "acc", 38)
stk(S, "baton-priere-liste-courses", 1100, 220, 480, 0.6, rot=-2)

S = nxt(12.6)
title(S, ["Pas pour te", "[culpabiliser]"], 12.7, "Une chose très importante", hl=W("culpabiliser", 12.6), size=90)
tg(S, 450, "Dieu n'est pas un distributeur", W("distributeur", 22.9), "", 34)
tg(S, 540, "La bénédiction ≠ plus d'argent", W("bénédiction", 12.6), "acc", 34)
stk(S, "baton-serein", 1100, 260, 300, 13.2)

S = nxt(22.9)
title(S, ["Ce qui abîme", "ta [paix]"], 23.0, "Ce que montre la Bible", hl=W("paix", 22.9), size=96)
tg(S, 450, "Notre paix", W("paix", 22.9), "", 36)
tg(S, 540, "Nos relations", W("relations", 22.9), "", 36)
tg(S, 630, "Notre témoignage", W("témoignage", 22.9), "acc", 36)
stk(S, "balance-juste-coche", 1100, 240, 440, 23.6)

S = nxt(32.8)
title(S, ["Au [programme]"], 32.9, "Dans cette vidéo", hl=33.5)
tg(S, 420, "5 passages", W("cinq", 32.8, 0), "", 40)
tg(S, 510, "5 habitudes", W("cinq", 32.8, 1), "", 40)
tg(S, 600, "5 idées fausses", W("cinq", 32.8, 2), "", 40)
tg(S, 690, "Un exemple", W("exemple", 32.8), "acc", 40)
stk(S, "liste-cinq-etapes", 1100, 240, 380, 33.5, rot=-1)

S = nxt(40.4)
title(S, ["Un audit de", "[quinze minutes]"], 40.5, "Reste jusqu'à la fin", hl=W("audit", 40.4), size=88)
tg(S, 450, "La 5e habitude : la plus discrète", W("discrète", 40.4), "", 34)
tg(S, 540, "Savoir laquelle te concerne", W("laquelle", 40.4), "acc", 34)
stk(S, "feuille-audit-cinq", 1100, 250, 420, 41.0, rot=-2)

S = nxt(47.1)
title(S, ["Pas un conseil", "[personnalisé]"], 47.2, "Une précision importante", hl=W("personnalisé", 47.1), size=78)
tg(S, 450, "Une réflexion biblique générale", W("réflexion", 47.1), "", 36)
tg(S, 540, "À adapter à ta situation", W("adaptes", 47.1), "acc", 38)
stk(S, "baton-pense", 1150, 230, 270, 47.8)
hit(W("personnalisé", 47.1), 0.8)

# ================================================================ 02 · Habitude 1 : arranger la vérité
S = nxt(55.8)
title(S, ["Habitude 1 :", "[arranger] la vérité"], 55.9, "Première habitude", hl=W("arranger", 55.8), size=84)
tg(S, 450, "Un petit arrondi", W("arrondi", 55.8), "", 34)
tg(S, 540, "Un revenu non déclaré", W("revenu", 55.8), "", 34)
tg(S, 630, "Une facture en ta faveur, jamais corrigée", W("facture", 55.8), "acc", 30)
stk(S, "balance-truquee-doigt", 1050, 250, 540, 56.5, rot=-2)

parole(63.9, "Proverbes 11.1", 65.4,
       f"« La balance fausse est en horreur à l'Éternel, mais {m(0, 'le poids juste lui est agréable.')} »",
       67.1, 71.5, [W("juste", 67.0)], size=54)

S = nxt(71.6)
title(S, ["L'[honnêteté]", "même dans le petit"], 71.7, "Au marché, hier et aujourd'hui", hl=W("honnêteté", 71.6), size=84)
tg(S, 450, "Hier : balances truquées", W("balances", 71.6), "", 34)
tg(S, 540, "Aujourd'hui : d'autres formes", W("formes", 71.6), "", 34)
tg(S, 630, "Dieu tient à l'honnêteté", W("honnêteté", 71.6) + 0.3, "acc", 34)
stk(S, "balance-juste-coche", 1100, 250, 440, 72.3)

S = nxt(80.7)
title(S, ["La petite triche", "[n'enrichit] pas"], 80.8, "Ce qu'elle ajoute", hl=W("enrichit", 80.7), size=84)
tg(S, 450, "De la peur", W("peur", 80.7), "", 36)
tg(S, 540, "Du secret", W("secret", 80.7), "", 36)
tg(S, 630, "Une conscience qui s'alourdit", W("conscience", 80.7), "acc", 34)
stk(S, "baton-nuage-inquiet", 1150, 200, 270, 81.4)

S = nxt(87.3)
title(S, ["Le signe qui", "[ne trompe pas]"], 87.4, "Tu te reconnais ?", hl=W("trompe", 87.3), size=84)
tg(S, 440, "Tu évites certains documents", W("documents", 87.3), "", 32)
tg(S, 520, "Tu n'en parles pas à ton conjoint", W("conjoint", 87.3), "", 32)
tg(S, 600, "« Personne ne le saura »", W("saura", 87.3), "acc", 34)
stk(S, "drapeau-rouge", 1150, 270, 300, 88.0)

S = nxt(99.2)
title(S, ["Remets [une chose]", "d'aplomb"], 99.3, "Ce que tu peux changer", hl=W("aplomb", 99.2), size=84)
tg(S, 440, "Corriger une erreur de caisse", W("caisse", 99.2), "", 32)
tg(S, 520, "Régulariser une situation", W("régulariser", 99.2), "", 32)
tg(S, 600, "Dire la vérité sur un montant", W("vérité", 99.2), "acc", 32)
stk(S, "escalier-trois-marches", 1100, 260, 420, 99.9)

# ================================================================ 03 · Habitude 2 : agir sans réfléchir
S = nxt(110.8)
title(S, ["Habitude 2 :", "agir sans [réfléchir]"], 110.9, "Deuxième habitude", hl=W("réfléchir", 110.8), size=84)
tg(S, 450, "Achat sur un coup de tête", W("tête", 110.8), "", 34)
tg(S, 540, "Signer sans lire", W("signe", 110.8), "", 34)
tg(S, 630, "Suivre une promesse sans vérifier", W("vérifier", 110.8), "acc", 32)
stk(S, "baton-pause-sablier", 1050, 250, 520, 111.5)

parole(119.0, "Proverbes 21.5", 120.4,
       f"« Les projets de l'homme diligent ne mènent qu'à {m(0, 'l\'abondance')}, mais celui qui agit avec {m(1, 'précipitation')} n'arrive qu'à la disette. »",
       122.3, 129.3, [W("abondance", 122.2), W("précipitation", 122.2)], size=46)

S = nxt(129.4)
title(S, ["Deux manières", "d'[avancer]"], 129.5, "Pas une promesse de richesse", hl=W("avancer", 129.4), size=88)
tg(S, 450, "Avec application", W("application", 129.4), "", 36)
tg(S, 540, "Ou dans la précipitation", W("précipitation", 129.4), "acc", 36)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 130.1)

S = nxt(136.5)
title(S, ["Un manque", "de [plan]"], 136.6, "Plus que de revenus", hl=W("plan", 136.5), size=96)
tg(S, 450, "Sans plan : décisions dans l'urgence", W("urgence", 136.5), "acc", 32)
stk(S, "enveloppes-budget", 1100, 260, 340, 137.2, rot=-2)

S = nxt(145.2)
title(S, ["La règle", "du [délai]"], 145.3, "Ce que tu peux changer", hl=W("délai", 145.2), size=96)
tg(S, 440, "Achat important : 24 heures", W("achat", 145.2), "", 34)
tg(S, 520, "Engagement lourd : une semaine", W("semaine", 145.2), "", 34)
tg(S, 600, "Et un avis extérieur", W("avis", 145.2), "acc", 34)
stk(S, "baton-pause-sablier", 1100, 250, 520, 145.9)

S = nxt(156.1)
title(S, ["Une pause coûte", "rarement [cher]"], 156.2, "Un détail qui change tout", hl=W("cher", 156.1), size=84)
tg(S, 450, "La précipitation : des années", W("années", 156.1), "acc", 34)
stk(S, "baton-patient-calme", 1100, 260, 380, 156.8)

S = nxt(162.4)
title(S, ["Le signe : [regretter]", "après coup"], 162.5, "Tu te reconnais ?", hl=W("regrettes", 162.4), size=78)
tg(S, 450, "Tu regrettes un achat", W("regrettes", 162.4), "", 34)
tg(S, 540, "« Je lirai les détails plus tard »", W("tard", 162.4), "acc", 32)
stk(S, "drapeau-rouge", 1150, 270, 300, 163.1)

S = nxt(171.3)
title(S, ["Si cette vidéo", "t'[aide]…"], 171.4, "Un instant", hl=W("aide", 171.3))
tg(S, 450, "Abonne-toi", W("abonne", 171.3) + 0.2, "acc", 72)
tg(S, 600, "Chaque semaine, un principe biblique simple", W("chaque", 175.0) + 0.2, "", 34)
stk(S, "croix-verte", 1200, 280, 260, 172.1, rot=-3)
stk(S, "baton-lit-livre", 1520, 300, 300, 172.5, rot=2)
bw("Abonne-toi", W("abonne", 171.3) + 0.4, 1.0)

# ================================================================ 04 · Habitude 3 : tout garder pour soi
S = nxt(179.7)
title(S, ["Habitude 3 :", "tout [garder]"], 179.8, "Troisième habitude", hl=W("garder", 179.7), size=90)
tg(S, 450, "Accumuler", W("accumuler", 179.7), "", 36)
tg(S, 540, "Protéger, ne jamais partager", W("partager", 179.7), "", 34)
tg(S, 630, "Par peur de manquer", W("manquer", 179.7), "acc", 36)
stk(S, "poing-sac-pieces", 1100, 250, 460, 180.4, rot=2)

parole(186.8, "Luc 12.15", 188.1,
       f"« Gardez-vous avec soin de {m(0, 'toute avarice')} ; car, quand on serait dans l'abondance, {m(1, 'la vie d\'un homme ne dépend pas de ses biens.')} »",
       189.5, 196.7, [W("avarice", 189.4), W("dépend", 189.4)], size=46)

S = nxt(196.8)
title(S, ["Épargner,", "pas [condamné]"], 196.9, "Jésus met en garde", hl=W("condamne", 196.8), size=88)
tg(S, 450, "Prévoir : pas condamné", W("prévoir", 196.8), "", 34)
tg(S, 540, "L'avarice : toujours en avoir plus", W("avarice", 196.8) , "acc", 32)
stk(S, "livre-croix-ouvert", 1100, 260, 420, 197.5, rot=-3)

S = nxt(204.9)
title(S, ["Aucune somme", "[ne suffit]"], 205.0, "Quand ta sécurité, c'est ton compte", hl=W("suffit", 204.9), size=88)
tg(S, 450, "Il y a toujours un montant de plus", W("toujours", 204.9) , "acc", 32)
stk(S, "poing-sac-pieces", 1100, 250, 460, 205.6, rot=2)

S = nxt(213.5)
title(S, ["Ouvre [la main]"], 213.6, "Ce que tu peux changer", hl=W("ouvrir", 213.5) , size=100)
tg(S, 440, "Décide d'une petite part à donner", W("part", 213.5), "", 32)
tg(S, 520, "Selon ta situation", W("situation", 213.5), "", 34)
tg(S, 600, "Pas par pression ni par culpabilité", W("culpabilité", 213.5), "acc", 32)
stk(S, "main-grace-releve", 1100, 250, 460, 214.2)

S = nxt(223.6)
title(S, ["Budget serré ?", "Donne [autrement]"], 223.7, "Pas que de l'argent", hl=W("autrement", 223.6) if False else 224.4, size=84)
tg(S, 440, "Du temps", W("temps", 223.6), "", 36)
tg(S, 520, "Un service", W("service", 223.6), "", 36)
tg(S, 600, "Un repas partagé", W("repas", 223.6), "acc", 36)
stk(S, "baton-priere", 1100, 260, 300, 224.2)

S = nxt(228.3)
title(S, ["Le signe :", "[quand j'aurai plus]"], 228.4, "Tu te reconnais ?", hl=W("aurai", 228.3), size=78)
tg(S, 440, "Donner te met mal à l'aise", W("aise", 228.3), "", 32)
tg(S, 520, "Ce « plus » ne vient pas tout seul", W("seul", 228.3), "", 32)
tg(S, 600, "Donne dans la situation où tu es", W("situation", 233.0), "acc", 32)
stk(S, "baton-nuage-inquiet", 1150, 200, 270, 229.0)

# ================================================================ 05 · Habitude 4 : demander pour de mauvaises raisons
S = nxt(241.8)
title(S, ["Habitude 4 :", "demander [mal]"], 241.9, "Quatrième habitude", hl=W("mauvaises", 241.8), size=90)
tg(S, 450, "On prie pour l'argent", W("prie", 241.8), "", 36)
tg(S, 540, "Seulement pour ce qui nous plaît", W("plairait", 241.8) if False else 244.5, "acc", 34)
stk(S, "baton-priere-liste-courses", 1100, 220, 480, 242.5, rot=-2)

parole(248.2, "Jacques 4.3", 249.4,
       f"« Vous demandez, et vous ne recevez pas, parce que vous {m(0, 'demandez mal')}, dans le dessein de {m(1, 'satisfaire vos passions.')} »",
       250.8, 256.8, [W("demandez", 251.0, 1), W("satisfaire", 250.8)], size=52)

S = nxt(256.9)
title(S, ["Pas toute prière", "est [mauvaise]"], 257.0, "Un verset sévère", hl=W("sévère", 256.9), size=84)
tg(S, 450, "Jésus nous invite à demander", W("invite", 256.9), "", 34)
tg(S, 540, "Notre pain de chaque jour", W("pain", 256.9), "acc", 34)
stk(S, "baton-priere", 1100, 260, 300, 257.6)

S = nxt(264.8)
title(S, ["Pourquoi je veux", "cet [argent] ?"], 264.9, "Une question honnête", hl=W("argent", 264.8), size=84)
tg(S, 440, "Pour vivre, pour servir, protéger", W("servir", 264.8), "", 32)
tg(S, 520, "Ou pour impressionner", W("impressionner", 264.8), "", 32)
tg(S, 600, "Pour combler un vide", W("vide", 264.8), "acc", 32)
stk(S, "baton-pense", 1150, 230, 270, 265.5)

S = nxt(276.8)
title(S, ["Le signe : une", "[liste de courses]"], 276.9, "Tu te reconnais ?", hl=W("courses", 276.8), size=80)
tg(S, 450, "Ta prière s'arrête quand le besoin est comblé", W("comblé", 276.8), "", 30)
tg(S, 540, "Dieu devient un moyen", W("moyen", 276.8), "acc", 34)
stk(S, "baton-priere-liste-courses", 1100, 220, 480, 277.5, rot=-2)

S = nxt(286.2)
title(S, ["Note en une", "[phrase]"], 286.3, "Ce que tu peux changer", hl=W("phrase", 286.2), size=100)
tg(S, 440, "Ce que tu ferais de cet argent", W("ferais", 286.2), "", 32)
tg(S, 520, "Et à qui il pourrait aussi profiter", W("profiter", 286.2), "acc", 32)
stk(S, "baton-ecrit-liste", 1100, 250, 340, 286.9)

# ================================================================ 06 · Habitude 5 : ne jamais être content
S = nxt(294.8)
title(S, ["Habitude 5 :", "jamais [content]"], 294.9, "La plus discrète", hl=W("content", 294.8), size=90)
tg(S, 450, "Regarder ce que les autres ont", W("autres", 294.8), "", 34)
tg(S, 540, "Se sentir en retard", W("retard", 294.8), "acc", 36)
stk(S, "baton-envieux-telephone", 1100, 230, 480, 295.5)

parole(301.9, "Hébreux 13.5", 303.1,
       f"« Que votre conduite ne soit point avare ; {m(0, 'contentez-vous de ce que vous avez')} ; car Dieu lui-même a dit : {m(1, 'Je ne te délaisserai point')}, et je ne t'abandonnerai point. »",
       304.6, 313.6, [W("contentez", 304.5), W("délaisserai", 304.5)], size=46, ref_y=880)

S = nxt(313.8)
title(S, ["Contentement,", "pas [résignation]"], 313.9, "Continuer à progresser", hl=W("résignation", 313.8), size=82)
tg(S, 450, "Le bonheur n'est pas un achat plus loin", W("achat", 313.8), "acc", 30)
stk(S, "escalier-trois-marches", 1100, 260, 420, 314.5)

S = nxt(322.6)
title(S, ["Dieu ne nous", "[abandonne] pas"], 322.7, "La raison du verset", hl=W("abandonne", 322.6), size=88)
tg(S, 450, "Ta sécurité : sa présence", W("présence", 322.6), "", 34)
tg(S, 540, "Pas ton niveau de vie", W("niveau", 322.6), "acc", 34)
stk(S, "colombe", 1100, 280, 300, 323.3, rot=3)

S = nxt(330.3)
title(S, ["Trois [mercis]", "chaque soir"], 330.4, "Ce que tu peux changer", hl=W("trois", 330.3), size=96)
tg(S, 440, "Pendant une semaine", W("semaine", 330.3), "", 34)
tg(S, 520, "Un repas, un toit, un message d'ami", W("toit", 330.3), "", 30)
tg(S, 600, "Cela change doucement le regard", W("regard", 336.0), "acc", 32)
stk(S, "baton-gratitude-carnet", 1050, 270, 520, 331.0)

S = nxt(342.1)
title(S, ["Le signe : plus", "[pauvre] après"], 342.2, "Tu te reconnais ?", hl=W("pauvre", 342.1), size=84)
tg(S, 450, "Tu scrolles, tu te sens en retard", W("réseaux", 342.1), "", 32)
tg(S, 540, "L'envie ne rassasie jamais", W("rassasie", 342.1), "acc", 34)
stk(S, "baton-envieux-telephone", 1100, 230, 480, 342.8)

# ================================================================ 07 · L'audit
S = nxt(351.0)
title(S, ["L'[audit]", "de 15 minutes"], 351.1, "Passons à la pratique", hl=W("audit", 351.0), size=100)
tg(S, 450, "Ce que je t'ai promis", W("promis", 351.0), "acc", 38)
stk(S, "feuille-audit-cinq", 1100, 250, 440, 351.7, rot=-2)

S = nxt(355.2)
title(S, ["Écris les", "[cinq habitudes]"], 355.3, "Sur une feuille", hl=W("feuille", 355.2), size=88)
tg(S, 430, "1 · Arranger la vérité", W("arranger", 355.2), "", 30)
tg(S, 505, "2 · Agir sans réfléchir", W("agir", 355.2), "", 30)
tg(S, 580, "3 · Tout garder pour soi", W("garder", 355.2), "", 30)
tg(S, 655, "4 · Demander pour de mauvaises raisons", W("mauvaises", 355.2), "", 28)
tg(S, 730, "5 · Ne jamais être content", W("content", 355.2), "acc", 30)
stk(S, "baton-ecrit-liste", 1250, 260, 340, 355.8)

S = nxt(366.2)
title(S, ["Note de 1 à 5", "[honnêtement]"], 366.3, "À côté de chacune", hl=W("honnête", 366.2), size=84)
tg(S, 450, "À quel point elle te ressemble", W("ressemble", 366.2), "", 34)
tg(S, 540, "Personne d'autre ne lira cette feuille", W("lira", 366.2), "acc", 32)
stk(S, "feuille-audit-cinq", 1100, 250, 440, 366.9, rot=-2)

S = nxt(373.9)
title(S, ["Choisis [une]", "seule habitude"], 374.0, "Le chiffre le plus élevé", hl=W("seule", 373.9), size=88)
tg(S, 450, "Une action très concrète", W("concrète", 373.9), "", 34)
tg(S, 540, "Pour cette semaine", W("semaine", 373.9), "acc", 36)
stk(S, "escalier-trois-marches", 1100, 260, 420, 374.6)

S = nxt(380.5)
title(S, ["Une action,", "pas [cinq]"], 380.6, "Pour tenir", hl=W("cinq", 380.5), size=100)
tg(S, 450, "Tout changer d'un coup : on se décourage", W("décourage", 380.5), "", 30)
tg(S, 540, "Un petit changement tenu vaut mieux", W("tenu", 380.5), "acc", 32)
stk(S, "baton-patient-calme", 1100, 260, 380, 381.2)

S = nxt(388.8)
title(S, ["En [couple] ?"], 388.9, "Si tu es marié", hl=W("conjoint", 388.8), size=100)
tg(S, 440, "Chacun de son côté", W("côté", 388.8), "", 36)
tg(S, 520, "Puis comparez avec douceur", W("douceur", 388.8), "acc", 36)
stk(S, "couple-audit-table", 1050, 270, 560, 389.5)

# ================================================================ 08 · Idées fausses, plante
S = nxt(394.3)
title(S, ["Cinq [idées fausses]", "à éviter"], 394.4, "Attention", hl=W("idées", 394.3), size=84)
tg(S, 440, "Elles transforment ce message en poids", W("poids", 394.3) if False else 396.5, "acc", 30)
stk(S, "drapeau-rouge", 1150, 270, 300, 395.0)

S = nxt(399.9)
title(S, ["Idée fausse 1 :", "« [Pauvre] = refusé »"], 400.0, "Non", hl=W("pauvre", 399.9), size=76)
tg(S, 450, "Des fidèles ont traversé le manque", W("fidèles", 399.9), "", 32)
tg(S, 540, "Des riches loin de Dieu", W("aisées", 399.9), "acc", 34)
stk(S, "baton-serein", 1100, 260, 300, 400.6)

S = nxt(410.7)
title(S, ["Idée fausse 2 :", "« Dieu doit [m'enrichir] »"], 410.8, "Non plus", hl=W("enrichir", 410.7), size=72)
tg(S, 450, "Ce n'est pas un contrat", W("contrat", 410.7), "", 34)
tg(S, 540, "Paix et stabilité, sans garantie", W("garantir", 410.7), "acc", 32)
stk(S, "baton-pense", 1150, 230, 270, 411.4)

S = nxt(423.6)
title(S, ["Idée fausse 3 :", "« Tout [réparer] »"], 423.7, "Non", hl=W("réparer", 423.6), size=80)
tg(S, 450, "Un pas à la fois", W("pas", 423.6), "", 36)
tg(S, 540, "Dieu n'est pas impatient devant toi", W("impatient", 423.6), "acc", 32)
stk(S, "escalier-trois-marches", 1100, 260, 420, 424.3)

S = nxt(431.2)
title(S, ["Idée fausse 4 :", "« Mes [échecs] »"], 431.3, "Non", hl=W("échecs", 431.2), size=80)
tg(S, 450, "La grâce autant que la sagesse", W("grâce", 431.2), "", 34)
tg(S, 540, "Tu peux changer de direction", W("direction", 431.2), "acc", 34)
stk(S, "main-grace-releve", 1100, 250, 460, 431.9)

S = nxt(440.6)
title(S, ["Idée fausse 5 :", "« C'est la [faute] des autres »"], 440.7, "Parfois oui, mais", hl=W("faute", 440.6), size=70)
tg(S, 450, "Certaines difficultés t'échappent", W("échappent", 440.6), "", 32)
tg(S, 540, "Regarde la petite part que tu peux changer", W("part", 440.6), "acc", 30)
stk(S, "baton-nuage-inquiet", 1150, 200, 270, 441.3)

S = nxt(453.4)
title(S, ["Habitude saine,", "pas de [honte]"], 453.5, "Une question de paix", hl=W("honte", 453.4), size=84)
tg(S, 450, "Une habitude saine : de la clarté", W("clarté", 453.4), "acc", 34)
stk(S, "baton-serein", 1100, 260, 300, 454.1)

S = nxt(462.3)
title(S, ["Pense à une [plante]"], 462.4, "On soigne, on laisse faire", hl=W("plante", 462.3), size=88)
tg(S, 450, "On ne la tire pas", W("tire", 462.3), "", 36)
tg(S, 540, "On l'arrose, on laisse le temps", W("arrose", 462.3), "", 34)
tg(S, 630, "À Dieu la part qui lui revient", W("revient", 462.3), "acc", 34)
stk(S, "plante-arrosoir", 1100, 250, 480, 463.0)

# ================================================================ 09 · Exemple
S = nxt(474.8)
title(S, ["Un exemple :", "[Thomas] et Claire"], 474.9, "Prenons", hl=W("Thomas", 474.8), size=84)
tg(S, 450, "Un bon revenu, des fins de mois tendues", W("tension", 476.3), "acc", 30)
stk(S, "famille-sortie", 1050, 270, 560, 475.5)

S = nxt(484.1)
title(S, ["Chacun", "fait son [audit]"], 484.2, "Un dimanche", hl=W("audit", 484.1), size=90)
tg(S, 450, "Thomas : acheter vite", W("achète", 484.1), "", 34)
tg(S, 540, "Claire : se comparer", W("cinquième", 484.1), "acc", 34)
stk(S, "couple-audit-table", 1050, 270, 560, 484.8)

S = nxt(495.2)
title(S, ["Une [action]", "chacun"], 495.3, "Petite et tenue", hl=W("action", 495.2), size=96)
tg(S, 450, "Thomas : la règle de 24 heures", W("Thomas", 495.2), "", 32)
tg(S, 540, "Claire : trois mercis chaque soir", W("Claire", 495.2), "acc", 32)
stk(S, "baton-gratitude-carnet", 1050, 270, 520, 495.9)

S = nxt(503.4)
title(S, ["Rien de [spectaculaire]", "mais plus calme"], 503.5, "Quelques mois plus tard", hl=W("spectaculaire", 503.4), size=70)
tg(S, 450, "Ils se parlent plus calmement", W("calmement", 503.4), "", 32)
tg(S, 540, "Un peu plus de marge", W("marge", 503.4), "acc", 34)
stk(S, "baton-patient-calme", 1100, 260, 380, 504.1)

S = nxt(511.3)
title(S, ["Ce qu'ils", "n'ont [pas fait]"], 511.4, "Remarque", hl=W("fait", 511.3), size=90)
tg(S, 440, "Pas de grande résolution", W("résolution", 511.3), "", 32)
tg(S, 520, "Pas de honte, pas de reproches", W("reproches", 511.3), "", 32)
tg(S, 600, "Une petite action tenue", W("tenue", 511.3), "acc", 32)
stk(S, "escalier-trois-marches", 1100, 260, 420, 512.0)

S = nxt(519.7)
title(S, ["Un [exemple],", "pas un témoignage"], 519.8, "À retenir", hl=W("exemple", 519.7), size=78)
tg(S, 450, "Aucune méthode ne garantit un résultat", W("garantit", 519.7), "acc", 32)
stk(S, "colombe", 1100, 280, 300, 520.4, rot=3)

# ================================================================ 10 · Récapitulatif et action
S = nxt(527.5)
title(S, ["L'[essentiel]"], 527.6, "Retenons", hl=528.0, size=96)
stk(S, "livre-croix-ouvert", 1050, 300, 420, 527.8, rot=-3)

S = nxt(529.6)
title(S, ["Ce qu'on [retient]"], 529.7, "Cinq points", hl=W("bénédiction", 529.6), size=96)
tg(S, 420, "La bénédiction ≠ seulement l'argent", W("bénédiction", 529.6), "", 30)
tg(S, 500, "Des habitudes abîment la paix", W("abîment", 529.6), "", 32)
tg(S, 580, "Honnête, réfléchi, partage, droiture, merci", W("reconnaissant", 529.6), "", 28)
tg(S, 660, "Une seule action suffit", W("action", 539.0), "", 32)
tg(S, 740, "La grâce couvre le passé", W("grâce", 545.0), "acc", 32)
stk(S, "baton-priere", 1250, 260, 300, 530.2)

S = nxt(550.3)
title(S, ["Cinq habitudes,", "cinq [passages]"], 550.4, "Rappel", hl=W("passage", 550.3), size=84)
tg(S, 440, "La balance juste", W("balance", 550.3), "", 32)
tg(S, 520, "Le projet réfléchi", W("projet", 550.3), "", 32)
tg(S, 600, "L'avarice dont Jésus nous protège", W("avarice", 550.3), "", 30)
tg(S, 680, "La prière honnête", W("prière", 550.3), "", 32)
tg(S, 760, "Le contentement", W("contentement", 550.3), "acc", 32)
stk(S, "liste-cinq-etapes", 1200, 260, 400, 551.0, rot=-1)

S = nxt(559.8)
title(S, ["Simple,", "avec [constance]"], 559.9, "Aucun grand revenu requis", hl=W("constance", 559.8), size=88)
tg(S, 450, "Un peu d'humilité", W("humilité", 559.8), "", 36)
tg(S, 540, "Un peu de constance", W("constance", 559.8), "acc", 36)
stk(S, "baton-patient-calme", 1100, 260, 380, 560.5)

S = nxt(568.0)
title(S, ["Cette semaine :", "[l'audit]"], 568.1, "Ton action", hl=W("audit", 568.0), size=96)
tg(S, 440, "Cinq habitudes", W("habitudes", 568.0), "", 36)
tg(S, 520, "Un chiffre de 1 à 5", W("chiffre", 568.0), "", 36)
tg(S, 600, "Une seule action", W("action", 568.0), "acc", 36)
stk(S, "feuille-audit-cinq", 1100, 260, 440, 568.7, rot=-2)

S = nxt(574.3)
title(S, ["Laquelle te", "[concerne] le plus ?"], 574.4, "Et toi", hl=W("concerne", 574.3), size=80)
stk(S, "baton-pense", 1150, 230, 260, 575.0)
cta = put(S, 80, 470, '<svg viewBox="0 0 120 100"><path d="M10 12 h100 a8 8 0 0 1 8 8 v46 a8 8 0 0 1 -8 8 h-58 l-22 20 v-20 h-20 a8 8 0 0 1 -8 -8 v-46 a8 8 0 0 1 8 -8 z"/></svg>Réponds en commentaire', "cta")
blur_in(cta, W("commentaire", 574.3) - 0.6, 14)
sfx("click", W("commentaire", 574.3) - 0.6, 0.8)
tg(S, 620, "Abonne-toi", W("abonne", 581.0), "acc", 56)

cam(VOICE_END + 0.2, "all")

# ================================================================ assemble
build(
    chapters=[("01", "Introduction", 0, 55.8), ("02", "Habitudes 1 et 2", 55.8, 179.7), ("03", "Habitudes 3 à 5", 179.7, 351.0),
              ("04", "Audit et idées fausses", 351.0, 474.8), ("05", "Exemple", 474.8, 527.5), ("06", "À retenir", 527.5, DUR)],
    suppress=SUP + [(VOICE_END + 0.3, DUR)],
    endcard={"kicker": "Abonne-toi", "title": "Foi et [Finances]", "button": "S'abonner",
             "stickers": [("livre-croix-ferme", 140, 620, 320, -6), ("baton-priere", 1560, 560, 240, 4)]},
    endcard_t=VOICE_END + 0.8,
)
