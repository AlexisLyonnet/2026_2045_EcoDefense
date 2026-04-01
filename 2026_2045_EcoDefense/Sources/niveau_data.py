#Projet : EcoDefense - Sauver la Terre !
#Auteurs : Adam Hzeg, Alexis Lyonnet, Martin Mechin

import constante as c

NIVEAU_DATA =   {
    1: {
        "map_0": "actif/Map/grass_map_opacity_0.png",
        "map_100": "actif/Map/grass_map_opacity_100.png",
        "waypoints": [ 
            (0*c.GRILLE, 7.5*c.GRILLE), 
            (2.5*c.GRILLE, 7.5*c.GRILLE),
            (3*c.GRILLE, 7.7*c.GRILLE),
            (3.3*c.GRILLE, 8*c.GRILLE),
            (3.5*c.GRILLE, 8.5*c.GRILLE), 

            (3.5*c.GRILLE, 11*c.GRILLE),
            (3.7*c.GRILLE, 11.5*c.GRILLE), 
            (4*c.GRILLE, 12*c.GRILLE),
            (4.5*c.GRILLE, 12.3*c.GRILLE),
            (5*c.GRILLE, 12.4*c.GRILLE),
            (5.5*c.GRILLE, 12.3*c.GRILLE),
            (6*c.GRILLE, 12*c.GRILLE),
            (6.4*c.GRILLE, 11.5*c.GRILLE),
            (6.6*c.GRILLE, 11*c.GRILLE),

            (6.6*c.GRILLE, 6.7*c.GRILLE),
            (6.4*c.GRILLE, 6.2*c.GRILLE),
            (6*c.GRILLE, 5.8*c.GRILLE),
            (5.5*c.GRILLE, 5.6*c.GRILLE),

            (4*c.GRILLE, 5.6*c.GRILLE),
            (3.5*c.GRILLE, 5.4*c.GRILLE),
            (3.2*c.GRILLE, 5.1*c.GRILLE),
            (3*c.GRILLE, 4.5*c.GRILLE),
            (3.2*c.GRILLE, 3.9*c.GRILLE),
            (3.5*c.GRILLE, 3.6*c.GRILLE),
            (4*c.GRILLE, 3.5*c.GRILLE),
            
            (8.5*c.GRILLE, 3.5*c.GRILLE),
            (9*c.GRILLE, 3.7*c.GRILLE),
            (9.3*c.GRILLE, 4.0*c.GRILLE),
            (9.5*c.GRILLE, 4.5*c.GRILLE),

            (9.5*c.GRILLE, 13*c.GRILLE),
            (9.6*c.GRILLE, 13.3*c.GRILLE),
            (10*c.GRILLE, 13.8*c.GRILLE),
            (10.5*c.GRILLE, 14.1*c.GRILLE),
            (11*c.GRILLE, 14.15*c.GRILLE),
            (11.5*c.GRILLE, 14.1*c.GRILLE),
            (12*c.GRILLE, 13.8*c.GRILLE),
            (12.4*c.GRILLE, 13.4*c.GRILLE),
            (12.6*c.GRILLE, 13*c.GRILLE),

            (12.6*c.GRILLE, 7.5*c.GRILLE),
            (12.7*c.GRILLE, 7.1*c.GRILLE),
            (13*c.GRILLE, 6.7*c.GRILLE),
            (13.5*c.GRILLE, 6.4*c.GRILLE),
            (16*c.GRILLE, 6.4*c.GRILLE),
        ],
        "placement_interdit": [
            (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
            (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0),
            (0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1),
            (0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
            (0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
            (0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
            (0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1),
            (0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0),
            (1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
            (0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
        ]
    },

    2: {
        "map_0": "actif/Map/sand_map_opacity_0.png",
        "map_100": "actif/Map/sand_map_opacity_100.png",
        "waypoints": [ 
            (0*c.GRILLE, 11.6*c.GRILLE),

            (5.5*c.GRILLE, 11.6*c.GRILLE),
            (6*c.GRILLE, 11.25*c.GRILLE),
            (6.25*c.GRILLE, 11*c.GRILLE),
            (6.5*c.GRILLE, 10.5*c.GRILLE),
            (6.25*c.GRILLE, 10*c.GRILLE),
            (6*c.GRILLE, 9.75*c.GRILLE),
            (5.5*c.GRILLE, 9.5*c.GRILLE),  

            (3.5*c.GRILLE, 9.5*c.GRILLE),
            (3*c.GRILLE, 9.25*c.GRILLE), 
            (2.75*c.GRILLE, 9*c.GRILLE), 
            (2.5*c.GRILLE, 8.5*c.GRILLE),  

            (2.5*c.GRILLE, 4.5*c.GRILLE), 
            (2.75*c.GRILLE, 4.25*c.GRILLE), 
            (3*c.GRILLE, 4*c.GRILLE), 
            (3.5*c.GRILLE, 3.6*c.GRILLE), 
            (4*c.GRILLE, 3.5*c.GRILLE), 
            (4.5*c.GRILLE, 3.6 *c.GRILLE), 
            (5*c.GRILLE, 4*c.GRILLE), 
            (5.25*c.GRILLE, 4.25*c.GRILLE), 
            (5.3*c.GRILLE, 4.5*c.GRILLE),

            (5.5*c.GRILLE, 5.5*c.GRILLE),
            (5.75*c.GRILLE, 6*c.GRILLE),
            (6*c.GRILLE, 6.25*c.GRILLE),
            (7*c.GRILLE, 6.6*c.GRILLE),
            (8*c.GRILLE, 6.25*c.GRILLE),
            (8.15*c.GRILLE, 6*c.GRILLE),
            (8.3*c.GRILLE, 5.5*c.GRILLE),

            (8.5*c.GRILLE, 4.5*c.GRILLE),
            (8.75*c.GRILLE, 4*c.GRILLE),
            (9*c.GRILLE, 3.75*c.GRILLE),
            (9.5*c.GRILLE, 3.6*c.GRILLE),
            (10*c.GRILLE, 3.75*c.GRILLE),
            (10.25*c.GRILLE, 4*c.GRILLE),
            (10.5*c.GRILLE, 4.5*c.GRILLE),

            (10.6*c.GRILLE, 12.5*c.GRILLE),
            (10.75*c.GRILLE, 13*c.GRILLE), 
            (11*c.GRILLE, 13.35*c.GRILLE), 
            (12*c.GRILLE, 13.7*c.GRILLE), 
            (13*c.GRILLE, 13.35*c.GRILLE), 
            (13.25*c.GRILLE, 13*c.GRILLE), 
            (13.5*c.GRILLE, 12.5*c.GRILLE),

            (13.5*c.GRILLE, 8.5*c.GRILLE),
            (13.75*c.GRILLE, 8*c.GRILLE), 
            (14*c.GRILLE, 7.75*c.GRILLE), 
            (14.5*c.GRILLE, 7.5*c.GRILLE),   

            (16*c.GRILLE, 7.5*c.GRILLE),          
            
        ],

        "placement_interdit": [
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0), 
            (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0),
            (1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1),
            (1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1),
            (1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0),
            (1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1),
            (1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1),
            (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1),
            (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1),
            (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        ]
    },

    3: {
        "map_0": "actif/Map/ice_map_opacity_0.png",
        "map_100": "actif/Map/ice_map_opacity_100.png",
        "waypoints": [
            (0 * c.GRILLE, 7.5 * c.GRILLE),
            (2.5 * c.GRILLE, 7.5 * c.GRILLE),
            (3 * c.GRILLE, 7.25 * c.GRILLE),
            (3.25 * c.GRILLE, 7 * c.GRILLE),
            (3.5 * c.GRILLE, 6.5 * c.GRILLE),

            (3.5 * c.GRILLE, 4.5 * c.GRILLE),
            (3.8 * c.GRILLE, 4.0 * c.GRILLE),
            (4.5 * c.GRILLE, 3.6 * c.GRILLE),
            (5 * c.GRILLE, 3.5 * c.GRILLE),
            (5.5 * c.GRILLE, 3.6 * c.GRILLE),
            (6.2 * c.GRILLE, 4.0 * c.GRILLE),
            (6.5 * c.GRILLE, 4.5 * c.GRILLE),

            (6.5 * c.GRILLE, 10.5 * c.GRILLE),
            (6.25 * c.GRILLE, 11 * c.GRILLE),
            (6 * c.GRILLE, 11.25 * c.GRILLE),
            (5.5 * c.GRILLE, 11.5 * c.GRILLE),

            (3.23 * c.GRILLE, 11.5 * c.GRILLE),
            (2.75 * c.GRILLE, 11.75 * c.GRILLE),
            (2.5 * c.GRILLE, 12 * c.GRILLE),
            (2.45 * c.GRILLE, 12.4 * c.GRILLE),
            (2.45 * c.GRILLE, 12.6 * c.GRILLE),
            (2.5 * c.GRILLE, 13 * c.GRILLE),
            (2.75 * c.GRILLE, 13.25 * c.GRILLE),
            (3.25 * c.GRILLE, 13.5 * c.GRILLE),

            (9.75 * c.GRILLE, 13.5 * c.GRILLE),
            (10.25 * c.GRILLE, 13.25 * c.GRILLE),
            (10.5 * c.GRILLE, 13 * c.GRILLE),
            (10.6 * c.GRILLE, 12 * c.GRILLE),

            (11 * c.GRILLE, 11.25 * c.GRILLE),
            (11.75 * c.GRILLE, 10.75* c.GRILLE),
            (12.5 * c.GRILLE, 10.5 * c.GRILLE),

            (12.5 * c.GRILLE, 10.5 * c.GRILLE),
            (13 * c.GRILLE, 10.2 * c.GRILLE),
            (13.4 * c.GRILLE, 9.5 * c.GRILLE),
            (13.5 * c.GRILLE, 9 * c.GRILLE),
            (13.4 * c.GRILLE, 8.5 * c.GRILLE),
            (13 * c.GRILLE, 7.8 * c.GRILLE),
            (12.5 * c.GRILLE, 7.5 * c.GRILLE),
            
            (10.5 * c.GRILLE, 7.5 * c.GRILLE),
            (10 * c.GRILLE, 7.2 * c.GRILLE),
            (9.6 * c.GRILLE, 6.5 * c.GRILLE),
            (9.5 * c.GRILLE, 6 * c.GRILLE),
            (9.6 * c.GRILLE, 5.5 * c.GRILLE),
            (10 * c.GRILLE, 4.8 * c.GRILLE),
            (10.5 * c.GRILLE, 4.5 * c.GRILLE),
            
            (16 * c.GRILLE, 4.5 * c.GRILLE),

        
        ],
        "placement_interdit": [
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
            (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1),
            (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
            (0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
            (1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1),
            (1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1),
            (0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0),
            (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
            (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0),
            (1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0),
            (1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
            (1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
            (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
            (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        ]
    }
}