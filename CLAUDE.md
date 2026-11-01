# Foi et Finances — règles de travail (à respecter à chaque session)

## Formats
- **« Sujet short »** → vidéo **9:16** (1080 × 1920), 1 à 1 min 30 environ.
- **« Sujet long »** → vidéo **16:9** (1920 × 1080), durée demandée par l'utilisateur.

## Méthode
- Une fiche par sujet (`montage/<projet>/fiche.md`, modèle `ressources/modele-fiche-video.md`), avant le script. Claude répond lui-même aux questions de la fiche (verset, adresse, durée, fin).
- Style visuel : `ressources/fiche-style-definitive.md` (bonhommes bâtons, Bible à la croix, croix flottantes, euros, règles de rétention ; section 11 pour le 16:9). Kit réutilisable : `ressources/kit-chretien/`.
- Moteur : `kit-style-02/moteur/style02.py` ; outils : `kit-style-02/outils/` (découpe, autocollants, `couper_silences.py`, `gen_musique_libre.py`, transcription `transcribe_pt.py`).
- Voix : Gemini TTS, voix Koda (Short : style « Promote » ; long : « Narration »). Ne jamais mettre de consigne de style dans le texte envoyé (elle peut être lue à voix haute) ; vérifier chaque morceau par transcription.
- Packaging : `titre-description-tags.md` dans le format de l'utilisateur, avec le disclaimer (`ressources/disclaimer.md`, version courte pour les Shorts, version complète adaptée pour les vidéos longues) ; chapitres horodatés pour les vidéos longues.
- Toujours commit + push sur la branche de travail.
