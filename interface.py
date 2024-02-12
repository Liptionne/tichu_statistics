import tkinter as tk
import fonctions_tichu

FICHIER_TEST = True

if(FICHIER_TEST):
    donnees_json = fonctions_tichu.chargerDonneesJson("D:/projet_stats_tichu/test_tichu.json")
else:
    donnees_json = fonctions_tichu.chargerDonneesJson("D:/projet_stats_tichu/tichu.json")

fenetre = tk.Tk()
fenetre.title("Gestion des parties")

def coucou():
    print("coucou")

def ajouterJoueur():
    nom_Joueur = contenu_nom_joueur.get()
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
    champ_joueur = tk.Entry(fenetre_ajouter_joueur,textvariable=contenu_nom_joueur)
    champ_joueur.pack(padx=10,pady=10)
    bouton_valider_ajouter_joueur = tk.Button(fenetre_ajouter_joueur, text="Ajouter", command=ajouterJoueur)
    bouton_valider_ajouter_joueur.pack(padx=10,pady=10)

contenu_nom_joueur = tk.StringVar()
# Création des boutons
bouton_ajouter_joueur = tk.Button(fenetre, text="Ajouter un joueur", command=fenetreAjouterJoueur)
bouton_ajouter_partie = tk.Button(fenetre, text="Ajouter une partie", command=coucou)
bouton_ajouter_manche = tk.Button(fenetre, text="Ajouter une manche", command=coucou)

# Placement des boutons dans la fenêtre
bouton_ajouter_joueur.pack(pady=10)
bouton_ajouter_partie.pack(pady=10)
bouton_ajouter_manche.pack(pady=10)

# Lancement de la boucle principale de l'application
fenetre.mainloop()