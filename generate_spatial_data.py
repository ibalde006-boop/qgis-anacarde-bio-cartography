# ==============================================================================
# PIPELINE DATA SIG - SIMULATION DES PARCELLES D'ANACARDE (SOKONE & TOUBACOUTA)
# Objectif : Structuration d'une base de données géospatiale pour certification bio
# Auteur : Ibrahima BALDE (Chargé de Cartographie)
# ==============================================================================

import json
import random

# Fixer la graine aléatoire pour la reproductibilité
random.seed(77)

# 1. Configuration des centres géographiques (Sokone & Toubacouta, Sénégal)
ZONES = {
    "Sokone": {"lat": 13.883, "lon": -16.433},
    "Toubacouta": {"lat": 13.783, "lon": -16.483}
}

print("⚡ Initialisation de la simulation des 150 parcelles d'anacarde...")

# 2. Génération de la structure GeoJSON
geojson_data = {
    "type": "FeatureCollection",
    "name": "parcelles_anacarde_biologique",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
    "features": []
}

# 3. Simulation des données des 150 producteurs
for i in range(1, 151):
    # Sélection de la zone géographique
    zone_nom = random.choice(["Sokone", "Toubacouta"])
    centre = ZONES[zone_nom]
    
    # Génération d'une fausse géométrie de parcelle (petit polygone carré)
    # On applique une légère variation aléatoire autour du centre de la commune
    delta_lon = random.uniform(-0.04, 0.04)
    delta_lat = random.uniform(-0.04, 0.04)
    
    lon_base = centre["lon"] + delta_lon
    lat_base = centre["lat"] + delta_lat
    
    # Taille de la parcelle (simule des superficies réalistes entre 0.5 et 5 hectares)
    taille_degre = random.uniform(0.001, 0.003) 
    
    # Coordonnées des 5 sommets du polygone (le premier et le dernier sont identiques pour fermer le polygone)
    coords = [
        [lon_base, lat_base],
        [lon_base + taille_degre, lat_base],
        [lon_base + taille_degre, lat_base + taille_degre],
        [lon_base, lat_base + taille_degre],
        [lon_base, lat_base] # Fermeture
    ]
    
    # Simulation des attributs métiers pour le cahier des charges de la certification Bio
    superficie_ha = round((taille_degre * 111) ** 2, 2) # Conversion approximative en Ha
    statut_bio = random.choices(["Certifié Bio", "En Conversion (C2)", "En Conversion (C1)"], weights=[75, 15, 10])[0]
    distance_zone_tampon_m = round(random.uniform(5, 50), 1)
    risque_contamination = "Faible" if distance_zone_tampon_m > 15 else "Modéré (Besoin de haie vive)"
    rendement_est_t = round(superficie_ha * random.uniform(0.4, 0.8), 2) # Rendement moyen anacarde au Sénégal
    
    # Construction de la feature spatiale
    feature = {
        "type": "Feature",
        "properties": {
            "id_producteur": f"PROD-{i:03d}",
            "nom_complet": f"Producteur Anacarde Option Bio {i}",
            "commune": zone_nom,
            "superficie_ha": superficie_ha,
            "statut_certification": statut_bio,
            "tampon_zone_m": distance_zone_tampon_m,
            "risque_voisinage": risque_contamination,
            "rendement_est_t": rendimiento_est_t
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [coords]
        }
    }
    
    geojson_data["features"].append(feature)

# 4. Exportation du fichier de base de données spatiale
output_filename = "parcelles_anacarde_simulees.geojson"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=4)

print(f"✅ Succès ! Fichier '{output_filename}' généré avec 150 entités géographiques.")
print("💡 Tu peux maintenant glisser ce fichier directement dans QGIS pour l'analyser et créer ton Atlas.")
