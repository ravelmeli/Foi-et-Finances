# Foi et Finances — règles de travail (à respecter à chaque session)

## Formats
- **« Sujet short »** → vidéo **9:16** (1080 × 1920), 1 à 1 min 30 environ.
- **« Sujet long »** → vidéo **16:9** (1920 × 1080), durée demandée par l'utilisateur.
- **Shorts par lots de 4 :** l'utilisateur envoie **4 sujets short à la fois**. Pour chaque lot : 4 dossiers `montage/<projet>/` (fiche, script, prompt de planche) livrés **en une seule réponse** (4 scripts + 4 planches), puis, à réception des audios et des planches (dans n'importe quel ordre, à apparier par le contenu), montage et rendu des 4, puis les 4 `titre-description-tags.md`. Les sujets longs restent traités un par un.

## Méthode
- Une fiche par sujet (`montage/<projet>/fiche.md`, modèle `ressources/modele-fiche-video.md`), avant le script. Claude répond lui-même aux questions de la fiche (verset, adresse, durée, fin).
- Style visuel : `ressources/fiche-style-definitive.md` (bonhommes bâtons, Bible à la croix, croix flottantes, euros, règles de rétention ; section 11 pour le 16:9). Kit réutilisable : `ressources/kit-chretien/`.
- Moteur : `kit-style-02/moteur/style02.py` ; outils : `kit-style-02/outils/` (découpe, autocollants, `couper_silences.py`, `gen_musique_libre.py`, transcription `transcribe_pt.py`).
- Voix : Gemini TTS, voix Koda (Short : style « Promote » ; long : « Narration »). Ne jamais mettre de consigne de style dans le texte envoyé (elle peut être lue à voix haute) ; vérifier chaque morceau par transcription.
- Packaging : `titre-description-tags.md` dans le format de l'utilisateur, avec le disclaimer (`ressources/disclaimer.md`, version courte pour les Shorts, version complète adaptée pour les vidéos longues) ; chapitres horodatés pour les vidéos longues.
- Toujours commit + push sur la branche de travail.

## Banque de sujets longs
- L'utilisateur fournit un **document de sujets longs** (à ranger dans `ressources/sujets-longs.md`, avec une colonne « statut » : à faire / fait). À **chaque nouvelle vidéo longue**, Claude **pioche dans ce document** : il choisit le sujet **à plus fort potentiel de viralité** parmi ceux restants (curiosité, enjeu émotionnel fort, question que les gens se posent vraiment, bénéfice concret, angle chrétien distinctif, titre cliquable), l'**envoie à l'utilisateur avec une justification courte** et démarre (fiche, script, prompts de planches) ; il passe ensuite le sujet en « fait ».
- **Alerter l'utilisateur quand le stock s'épuise** : dès qu'il reste **3 sujets ou moins**, le dire clairement à chaque livraison (et proposer de nouveaux sujets) ; à 0, le dire avant de continuer.

## Banque de sujets shorts
- L'utilisateur fournit aussi un **document de sujets shorts** (à ranger dans `ressources/sujets-shorts.md`, avec une colonne « statut » : à faire / fait). **Quand l'utilisateur annonce qu'on passe aux Shorts**, Claude **pioche dans ce document** : il sélectionne **les 4 sujets restants au plus fort potentiel de viralité** (un lot de 4, voir « Formats »), les **envoie à l'utilisateur avec une justification courte** (une ligne par sujet) et démarre le lot (4 fiches, 4 scripts, 4 prompts de planche, livrés en une seule réponse) ; il passe ensuite ces sujets en « fait ». Éviter les doublons avec les Shorts déjà réalisés (dossiers de `montage/`).
- **Alerter l'utilisateur quand le stock s'épuise** : dès qu'il reste **8 sujets ou moins** (soit deux lots), le dire clairement à chaque livraison et proposer de nouveaux sujets ; en dessous de 4, le dire avant de continuer.

## Déclenchement
- **Ne jamais démarrer une production de sa propre initiative.** L'utilisateur **précise à chaque fois quoi produire** (« on produit les Shorts » ou « on produit une vidéo longue »). Claude répond alors en **envoyant les sujets correspondants** (4 sujets pour un lot de Shorts, 1 sujet pour une vidéo longue, choisis dans les banques `ressources/sujets-shorts.md` / `ressources/sujets-longs.md` selon les règles ci-dessus) avec une justification courte, puis démarre la production (fiche, script, prompts de planches).

## Cycle des vidéos longues (2 sujets de la banque, puis 1 sujet d'actualité)
- Cycle répété : **vidéo longue n° 1 et n° 2 = sujets piochés dans `ressources/sujets-longs.md`** (potentiel de viralité maximal) ; **vidéo longue n° 3 = sujet le plus actuel du moment**, trouvé par **recherche sur internet** (Google Trends et actualité, via l'outil de recherche web ; vérifier plusieurs sources) et **qui cadre avec la chaîne** (finances personnelles chrétiennes : argent, budget, dettes, don, épargne, couple, travail…). Claude **envoie ce sujet à l'utilisateur avec la justification** (ce qui le rend actuel, sources, angle chrétien) puis démarre. Ensuite le cycle **recommence** (2 de la banque, 1 d'actualité).
- Le **compteur du cycle** est tenu à jour en tête de `ressources/sujets-longs.md` (colonne « origine » : banque / actualité).
- Vérifier la sensibilité du sujet d'actualité : pas de polémique politique ou partisane, pas de conseil d'investissement, pas de promesse ; angle biblique prudent.
