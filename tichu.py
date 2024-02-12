import json
import fonctions_tichu

FICHIER_TEST = True

if(FICHIER_TEST):
    donnees_json = fonctions_tichu.chargerDonneesJson("D:/projet_stats_tichu/test_tichu.json")
else:
    donnees_json = fonctions_tichu.chargerDonneesJson("D:/projet_stats_tichu/tichu.json")
    
#fonctions_tichu.ajouterPartie(donnees_json, "09-02-2024", ["Joshua", "Gautier"], ["Albin","Victor"])


# nouvelle_manche = {
#         "equipe_1": score_equipe1,
#         "equipe_2": score_equipe2,
#         "grand_tichu_reussi": nom_joueur_grand_tichu_reussi,
#         "grand_tichu_rate": liste_joueurs_grand_tichu_rate,
#         "tichu_reussi": nom_joueur_tichu_reussi,
#         "tichu_rate": liste_joueurs_tichu_rate,
#         "premier": joueur_premier,
#         "deuxieme": joueur_deuxieme,
#         "troisieme": joueur_troisieme,
#         "quatrieme": joueur_quatrieme
#     }
#fonctions_tichu.ajouterManche(donnees_json, nouvelle_manche)

#fonctions_tichu.construireJsonJoueursVierge(donnees_json)

fonctions_tichu.construireStatistiques(donnees_json)

#fonctions_tichu.rapportStatsJoueur(donnees_json, "Albin")
#print(fonctions_tichu.getCoequipier(donnees_json["parties"][0], "Gautier"))
