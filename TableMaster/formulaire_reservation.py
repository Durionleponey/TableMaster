import tkinter as tk
from tkinter import *
import re



# Différentes fonctions :
def register_client():
    register_nom = zone_nom.get()

    #Vérification remplissage de case :
    if register_nom == "":
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, vous n'avez pas rempli la case du Nom", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

    elif register_nom.isalpha() == False:
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, vous avez entrer un numéro dans la case du Nom", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

    register_prenom = zone_prenom.get()

    if register_prenom == "":
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, vous n'avez pas rempli la case du prénom", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

    elif register_prenom.isalpha() == False:
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, vous avez entrer un numéro dans la case du prénom", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)


    register_nbre = zone_nombre.get()

    #Vérification c'est un nombre

    if register_nbre =="":
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, vous n'avez pas rempli la case du nombres de personnes présentes", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

    #Vérification nombre et entier :
    elif register_nbre.isdigit() == False:
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, le chiffre que vous avez rentrer n'est pas un entier !", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

#Vérifier si la zone n'est pas vide :

    register_heure = zone_heure.get()
    if register_heure =="":
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, vous n'avez pas rempli la case du nombres de personnes présentes", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

    # Vérifier si c'est bien un format d'heure (HH:MM)
    pattern_heure = r"^([01]\d|2[0-3]):([0-5]\d)$"

    if not re.match(pattern_heure, register_heure):
        fenetre_erreur = Tk()
        fenetre_erreur.geometry('300x150')
        fenetre_erreur.title("Erreur")
        fenetre_erreur.configure(bg='lightgrey')
        fenetre_erreur.resizable(height=False, width=False)

        error_mess = Label(fenetre_erreur, text="Error, l'heure que vous avez entrée n'est pas valide !", bg='Red')
        error_mess.pack()

        # Bouton pour fermer la fenêtre d'erreur
        close_button = Button(fenetre_erreur, text="Revenir au formulaire", bg='red', fg='white',
                              command=fenetre_erreur.destroy)
        close_button.pack(pady=10)

    print(f"Vous êtes {register_nom} {register_prenom}, vous serez {register_nbre} et vous avez réservé à {register_heure}.")



def formulaire_reservation_line():

    # Créer une fenêtre
    formu = Tk()
    formu.geometry('500x400')
    formu.title("Formulaire de réservation")
    formu.configure(bg='lightgrey')  # Couleur de fond sombre (noir ou gris foncé)
    formu.resizable(height=False, width=False)
    # Style commun des labels
    label_style = {'bg': 'lightgrey', 'fg': 'white', 'font': ('Arial', 12)}
    entry_style = {'width': 40, 'font': ('Arial', 12)}

    # Titre du formulaire
    title = Label(formu, text="Veuillez entrer vos informations", font=('Arial', 16, 'bold'), fg='white', bg='lightgrey')
    title.grid(row=0, column=0, columnspan=2, pady=20)

    # Nom Client
    nom = Label(formu, text='Nom :', **label_style)
    zone_nom = Entry(formu, **entry_style)

    nom.grid(row=1, column=0, padx=20, pady=10, sticky='e')
    zone_nom.grid(row=1, column=1, padx=20, pady=10)

    # Prénom Client
    prenom = Label(formu, text='Prénom :', **label_style)
    zone_prenom = Entry(formu, **entry_style)

    prenom.grid(row=2, column=0, padx=20, pady=10, sticky='e')
    zone_prenom.grid(row=2, column=1, padx=20, pady=10)

    # Nombre de Personnes
    nombre = Label(formu, text='Nombre de personnes :', **label_style)
    zone_nombre = Entry(formu, **entry_style)

    nombre.grid(row=3, column=0, padx=20, pady=10, sticky='e')
    zone_nombre.grid(row=3, column=1, padx=20, pady=10)

    # Heure
    heure_reser = Label(formu, text='Heure de réservation :', **label_style)
    zone_heure = Entry(formu, **entry_style)

    heure_reser.grid(row=4, column=0, padx=20, pady=10, sticky='e')
    zone_heure.grid(row=4, column=1, padx=20, pady=10)

    # Bouton de validation
    validation = Button(formu, text='Valider', bg='#e74c3c', fg='white', font=('Arial', 12, 'bold'), command=register_client)
    validation.grid(row=5, column=0, columnspan=2, pady=20)

    # Lancement de la fenêtre
    formu.mainloop()


    #if __name__ = "__main__"
