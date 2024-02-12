import json 

def chargerDonneesJson(chemin):
    with open(chemin, "r") as fichier:
        donnees_json = fichier.read()
        return json.loads(donnees_json)
    
def ecrireDonneesJson(donneesEnAttente):
    with open("D:/projet_stats_tichu/test_tichu.json", "w") as fichier:
        json.dump(donneesEnAttente, fichier, indent=4)

def ajouterJoueur(_nomJoueur, donnees_json):
    donnees_json["liste des joueurs"].append(_nomJoueur)
    ecrireDonneesJson(donnees_json)

#Une equipe doit etre écrite avec deux noms de joueurs valide, ex : "Joshua-Gautier"
def ajouterPartie(donnees_json, date, equipe_1, equipe_2):
    print("Ajout d'une partie")
    nouvelle_partie = {
        "date": date,
        "equipe 1": equipe_1,
        "equipe 2": equipe_2,
        "manches": []
    }
    donnees_json["parties"].append(nouvelle_partie)
    ecrireDonneesJson(donnees_json)

def ajouterManche(_donnees_json,nouvelle_manche):
    _donnees_json["parties"][-1]["manches"].append(nouvelle_manche)
    ecrireDonneesJson(_donnees_json)

def getCoequipier(_partie,_joueur):
    equipe_1 = _partie["equipe_1"]
    equipe_2 = _partie["equipe_2"]
    if _joueur in equipe_1:
        return equipe_1[1] if _joueur == equipe_1[0] else equipe_1[0]
    elif _joueur in equipe_2:
        return equipe_2[1] if _joueur == equipe_2[0] else equipe_2[0]
    else:
        return None

def construireJsonJoueursVierge(_donnees_json):
    statistiques = {}
    for joueur in _donnees_json["liste des joueurs"]:
        statistiques[joueur] = {}
        for coequipier in _donnees_json["liste des joueurs"]:
            if coequipier == joueur:
                pass
            else:
                statistiques[joueur][coequipier] = {
                    "manches_jouees": 0,
                    "points_gagnes": 0,
                    "tichu_reussi": 0,
                    "tichu_rate": 0,
                    "grand_tichu_reussi": 0,
                    "grand_tichu_rate": 0,
                    "positions": {
                        "premier": 0,
                        "deuxieme": 0,
                        "troisieme": 0,
                        "quatrieme": 0
                    }
                }
    _donnees_json["statistiques"] = statistiques
    print("liste statistiques vierge finie.")
    ecrireDonneesJson(_donnees_json)
    return _donnees_json

def construireStatistiques(_donnees_json):
    donnees_json = construireJsonJoueursVierge(_donnees_json)
    for partie in donnees_json["parties"]:

        for manche in partie["manches"]:

            # Gestion des points gagnés et des manches jouées
            liste_cle_equipe = ["equipe_1", "equipe_2"]
            for cle_equipe in liste_cle_equipe:
                for joueur in partie[cle_equipe]:
                    coequipier = getCoequipier(partie, joueur)
                    donnees_json["statistiques"][joueur][coequipier]["points_gagnes"] += manche[cle_equipe]
                    donnees_json["statistiques"][joueur][coequipier]["manches_jouees"] += 1
            
            
            # Gestion des tichus et grands tichus réussis
            liste_cle_reussis = ["grand_tichu_reussi", "tichu_reussi"]
            for cle_reussi in liste_cle_reussis:
                if (manche[cle_reussi] != "none"):
                    coequipier_reussi = getCoequipier(partie,manche[cle_reussi])
                    donnees_json["statistiques"][manche[cle_reussi]][coequipier_reussi][cle_reussi] += 1

            liste_cle_rates = ["grand_tichu_rate", "tichu_rate"]
            # Gestion des tichus et grands tichus ratés
            for cle_rate in liste_cle_rates:
                for joueur in manche[cle_rate]:
                    coequipier_2 = getCoequipier(partie, joueur)
                    donnees_json["statistiques"][joueur][coequipier_2][cle_rate] += 1


            # Gestion des premières place
            liste_positions = ["premier", "deuxieme", "troisieme", "quatrieme"]
            for position in liste_positions:
                coequipier_position = getCoequipier(partie, manche[position])
                donnees_json["statistiques"][manche[position]][coequipier_position]["positions"][position] += 1

    ecrireDonneesJson(donnees_json)

def rapportStatsJoueur(donnees_json, joueur):
    
    print("-----------------------------------------------------------------------------")
    print(f"Rapport statistiques de : {joueur}")
    print("-----------------------------------------------------------------------------")

    statistiquesJoueur = donnees_json["statistiques"][joueur]
    print(f"Manches jouées : {statistiquesJoueur['manches_jouees']}")
    print(f"Points gagnés au total : {statistiquesJoueur['points_gagnes']}")
    print(f"Points en moyenne par manche : {statistiquesJoueur['points_gagnes']/statistiquesJoueur['manches_jouees']}")
    print("-----------------------------------------------------------------------------")
    print(f"Repartition des placements")

    liste_placements = ['premier', 'deuxieme', 'troisieme', 'quatrieme']
    for placement in liste_placements:
        print(f"{statistiquesJoueur['positions'][placement]} fois premier : {statistiquesJoueur['positions'][placement]/statistiquesJoueur['manches_jouees']*100}%")

    print("-----------------------------------------------------------------------------")

    print("Succès des tichus et grands tichus")
    print("-----------------------------------------------------------------------------")
    tichus_tentes = statistiquesJoueur['tichu_reussi'] + statistiquesJoueur['tichu_rate']
    grand_tichus_tentes = statistiquesJoueur['grand_tichu_reussi'] + statistiquesJoueur['grand_tichu_rate']
    print(f"{joueur} a tenté {tichus_tentes} tichus, et en a réussi : {statistiquesJoueur['tichu_reussi']}")
    if(tichus_tentes > 0):
        print(f"Donc un taux de réussite de tichus de {statistiquesJoueur['tichu_reussi']/tichus_tentes*100}%")
    
    print(f"{joueur} a tenté {grand_tichus_tentes} grand tichus, et en a réussi : {statistiquesJoueur['grand_tichu_reussi']}")
    if(grand_tichus_tentes > 0):
        print(f"Donc un taux de réussite de grands tichus de {statistiquesJoueur['grand_tichu_reussi']/grand_tichus_tentes*100}%")

print()
# TO DO 
# - ajouter les coequipiers au stats des joueurs
# Je pense que le meilleur moyen serait d'ajouter les memes stats mais avec un clé coequipier
# et donc il faudrait à chaque manche ajouter tout ce qui est déjà ajouter mais au coeqipier de cette partie.