import tkinter
from tkinter import *

# Créer une fenêtre
formu = Tk()
formu.geometry('500x500')
formu.title("Formulaire de réservation")
formu['bg'] = 'black'
formu.resizable(height=True, width=False)


#Différentes fonctions :

def register_client():
    pass




# Création de la zone d'écriture

#Titre formu
title = Label(formu, text="Veuillez entrez vos informations :")#Afficher le titre

# Nom Client
nom = Label(formu, text='Nom :', bg='white')
zone_nom = Entry(formu, width=50)

nom.grid(row=0, column=0, padx=10, pady=10)  # Position du label Nom
zone_nom.grid(row=0, column=1, padx=10, pady=10)  # Position de la zone d'entrée Nom

# Prénom Client
prenom = Label(formu, text='Prénom :', bg='white')
zone_prenom = Entry(formu, width=50)

prenom.grid(row=1, column=0, padx=10, pady=10)  # Position du label Prénom
zone_prenom.grid(row=1, column=1, padx=10, pady=10)  # Position de la zone d'entrée Prénom

# Nombre de Personnes
nombre = Label(formu, text='Nombre de personnes :', bg='white')
zone_nombre = Entry(formu, width=50)

nombre.grid(row=2, column=0, padx=10, pady=10)  # Position du label Nombre de personnes
zone_nombre.grid(row=2, column=1, padx=10, pady=10)

#Heure
heure_reser = Label(formu, text='Heure de réservation :', bg='white')
zone_heure = Entry(formu, width=50)

heure_reser.grid(row=3, column=0, padx=10, pady=10)
zone_heure.grid(row=3, column=1, padx=10, pady=10)

validation = Button(formu, text='Valider', bg='white', fg='black', command=register_client)
validation.grid(row=4, column=0, padx=10, pady=10)


formu.mainloop()
