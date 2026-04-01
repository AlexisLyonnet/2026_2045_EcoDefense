#Projet : EcoDefense - Sauver la Terre !
#Auteurs : Adam Hzeg, Alexis Lyonnet, Martin Mechin

import constante as c

TYPES_TOURS = {
    "eolienne": {
        "nom": "Éolienne",
        "cout": 50,
        "icone": "actif/bouton/icone_eolienne.png",
        "images": {
            1: ["actif/tours/eolienne_plaine_1.png", "actif/tours/eolienne_plaine_2.png", "actif/tours/eolienne_plaine_3.png"],
            2: ["actif/tours/eolienne_sable_1.png",  "actif/tours/eolienne_sable_2.png",  "actif/tours/eolienne_sable_3.png"],
            3: ["actif/tours/eolienne_glace_1.png",  "actif/tours/eolienne_glace_2.png",  "actif/tours/eolienne_glace_3.png"],
        },
        "stats": [
            {"range": 2.5*c.GRILLE, "cooldown": 800, "degats": 40, "cout_amelioration":0},
            {"range": 3.0*c.GRILLE, "cooldown": 700, "degats": 50, "cout_amelioration":75},
            {"range": 3.5*c.GRILLE, "cooldown": 600, "degats": 60, "cout_amelioration":100},
        ],
        "projectile": "actif/tours/projectile1.png",
    },

    "solaire": {
        "nom": "Solaire",
        "cout": 75,
        "icone": "actif/bouton/icone_eolienne.png",
        "images": {
            1: ["actif/tours/solaire_plaine_1.png", "actif/tours/solaire_plaine_2.png", "actif/tours/solaire_plaine_3.png"],
            2: ["actif/tours/solaire_sable_1.png",  "actif/tours/solaire_sable_2.png",  "actif/tours/solaire_sable_3.png"],
            3: ["actif/tours/solaire_glace_1.png",  "actif/tours/solaire_glace_2.png",  "actif/tours/solaire_glace_3.png"],
        },
        "stats": [
            {"range": 4*c.GRILLE, "cooldown": 2000, "degats": 120, "cout_amelioration":0},
            {"range": 4.5*c.GRILLE, "cooldown": 1800, "degats": 140,"cout_amelioration":75},
            {"range": 5*c.GRILLE, "cooldown": 1600, "degats": 160, "cout_amelioration":100},

        ],
        "projectile": "actif/tours/projectile2.png",
    },

    "recyclage": {
        "nom": "Recyclage",
        "cout": 100,
        "icone": "actif/bouton/icone_eolienne.png",
        "images": {
            1: ["actif/tours/recyclage_plaine_1.png", "actif/tours/recyclage_plaine_2.png", "actif/tours/recyclage_plaine_3.png"],
            2: ["actif/tours/recyclage_sable_1.png",  "actif/tours/recyclage_sable_2.png",  "actif/tours/recyclage_sable_3.png"],
            3: ["actif/tours/recyclage_glace_1.png",  "actif/tours/recyclage_glace_2.png",  "actif/tours/recyclage_glace_3.png"],
        },
        "stats": [
            {"range": 1.5*c.GRILLE, "cooldown": 400, "degats": 30, "cout_amelioration":0},
            {"range": 2*c.GRILLE, "cooldown": 350, "degats": 38, "cout_amelioration":75},
            {"range": 2.5*c.GRILLE, "cooldown": 300, "degats": 45, "cout_amelioration":100},
        ],
        "projectile": "actif/tours/projectile3.png",
        
    },
}