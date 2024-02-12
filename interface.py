import tkinter as tk
import fonctions_tichu

FICHIER_TEST = True

if(FICHIER_TEST):
    donnees_json = fonctions_tichu.chargerDonneesJson("D:/projet_stats_tichu/test_tichu.json")
else:
    donnees_json = fonctions_tichu.chargerDonneesJson("D:/projet_stats_tichu/tichu.json")

liste_joueurs_dispos = donnees_json["liste des joueurs"]

fenetre = tk.Tk()
fenetre.title("Gestion des parties")


def ajouterJoueur():
    nom_Joueur = champ_joueur.get()
    print(nom_Joueur)
    fonctions_tichu.ajouterJoueur(nom_Joueur, donnees_json)
    fenetre_ajouter_joueur.destroy()

def fenetreAjouterJoueur():
    global fenetre_ajouter_joueur
    fenetre_ajouter_joueur = tk.Toplevel()
    fenetre_ajouter_joueur.title("Ajouter un joueur")
    fenetre_ajouter_joueur.geometry("300x200")
    texte_ajouter_joueur = tk.Label(fenetre_ajouter_joueur, text="Ajouter un joueur")   
    texte_ajouter_joueur.pack(padx=10,pady=10)
    global champ_joueur
    champ_joueur = tk.Entry(fenetre_ajouter_joueur)
    champ_joueur.pack(padx=10,pady=10)
    bouton_valider_ajouter_joueur = tk.Button(fenetre_ajouter_joueur, text="Ajouter", command=ajouterJoueur)
    bouton_valider_ajouter_joueur.pack(padx=10,pady=10)

def validerPartie():
    fonctions_tichu.ajouterPartie(donnees_json, entry_date.get(),[joueur_1_equipe_1.get(), joueur_2_equipe_1.get()],[joueur_1_equipe_2.get(), joueur_2_equipe_2.get()])
    fenetreAjouterPartie.destroy()
    ## Appel de la fonction pour entrer une manche


def ajouterPartie():

    global fenetreAjouterPartie
    fenetreAjouterPartie = tk.Toplevel()
    
    label_joueur_1_equipe_1 = tk.Label(fenetreAjouterPartie, text="Joueur 1 de l'équipe 1")
    label_joueur_1_equipe_1.grid(row=0, column=0, padx=10, pady=10)
    global joueur_1_equipe_1
    joueur_1_equipe_1 = tk.Entry(fenetreAjouterPartie)
    joueur_1_equipe_1.grid(row=0, column=1, padx=10, pady=10)

    label_joueur_2_equipe_1 = tk.Label(fenetreAjouterPartie, text="Joueur 2 de l'équipe 1")
    label_joueur_2_equipe_1.grid(row=1, column=0, padx=10, pady=10)
    global joueur_2_equipe_1
    joueur_2_equipe_1 = tk.Entry(fenetreAjouterPartie)
    joueur_2_equipe_1.grid(row=1, column=1, padx=10, pady=10)

    label_joueur_1_equipe_2 = tk.Label(fenetreAjouterPartie, text="Joueur 1 de l'équipe 2")
    label_joueur_1_equipe_2.grid(row=0, column=3, padx=10, pady=10)
    global joueur_1_equipe_2
    joueur_1_equipe_2 = tk.Entry(fenetreAjouterPartie)
    joueur_1_equipe_2.grid(row=0, column=4, padx=10, pady=10)

    label_joueur_2_equipe_2 = tk.Label(fenetreAjouterPartie, text="Joueur 1 de l'équipe 1")
    label_joueur_2_equipe_2.grid(row=1, column=3, padx=10, pady=10)
    global joueur_2_equipe_2
    joueur_2_equipe_2 = tk.Entry(fenetreAjouterPartie)
    joueur_2_equipe_2.grid(row=1, column=4, padx=10, pady=10)

    label_date = tk.Label(fenetreAjouterPartie, text="Date de la partie")
    label_date.grid(row=3, column = 1, padx=10, pady=10)
    global entry_date
    entry_date = tk.Entry(fenetreAjouterPartie)
    entry_date.grid(row=3, column=2,padx=10, pady=10)


    bouton_valider_partie = tk.Button(fenetreAjouterPartie, text="Valider", command=validerPartie)
    bouton_valider_partie.grid(row=4, column = 2,padx=10, pady=10)











# Création des boutons
bouton_ajouter_joueur = tk.Button(fenetre, text="Ajouter un joueur", command=fenetreAjouterJoueur)
bouton_ajouter_partie = tk.Button(fenetre, text="Ajouter une partie", command=ajouterPartie)

# Placement des boutons dans la fenêtre
bouton_ajouter_joueur.pack(pady=10)
bouton_ajouter_partie.pack(pady=10)

# Lancement de la boucle principale de l'application
fenetre.mainloop()