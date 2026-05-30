# 🛰️ Cartographie SIG & Certification Biologique de l'Anacarde (Sokone & Toubacouta)

Ce dépôt présente la structure méthodologique et technique développée lors de ma mission en tant que **Chargé de Cartographie chez NOURSERVI** dans la zone de Sokone et Toubacouta. Ce projet met en valeur l'application concrète des Systèmes d'Information Géographique (SIG) pour répondre aux exigences strictes de la certification biologique réglementaire.

## 🎯 Objectifs et Impact Réel
* **Périmètre :** Structuration de bases de données géospatiales pour **150 producteurs d’anacarde**.
* **Enjeu Qualité :** Assurer la traçabilité totale et la conformité biologique via la délimitation précise des parcelles pour éviter les zones de contamination.
* **Localisation :** Zone de Sokone et Toubacouta (Sénégal).

## 🛠️ Implémentation Technique sous QGIS
Le projet s'articule autour de 4 axes techniques majeurs :

1. **Collecte et Nettoyage des Données Terrain :**
   * Importation et correction des levés topographiques GPS (coordonnées UTM/WGS84) issus du terrain.
   * Filtrage des erreurs géométriques et des doublons de parcelles.

2. **Structuration de la Base de Données Spatiale :**
   * Création d'un modèle conceptuel de données (MCD) sous format **GeoPackage** standardisé.
   * Renseignement des tables attributaires : ID producteur, surface certifiée (ha), rendement estimé, historique cultural.

3. **Analyse Spatiale et Traitement Géométrique :**
   * Calcul précis des superficies parcellaires via des fonctions géométriques intégrées.
   * Création de zones tampons (*Buffer*) pour matérialiser les distances de sécurité réglementaires face aux cultures conventionnelles limitrophes.

4. **Production Cartographique Automatisée :**
   * Configuration de la mise en page via l'outil **Atlas de QGIS** pour générer automatiquement une fiche cartographique personnalisée par producteur (indispensable pour les audits de certification).
![Carte Officielle de Certification Anacarde](carte_officielle_anacarde.png)
## 🧰 Outils & Compétences mobilisés
`QGIS` | `GeoPackage` | `Analyse Spatiale` | `Gestion de Base de Données` | `Cartographie Thématique` | `GPS & Mobile Data Collection`
