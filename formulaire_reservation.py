import tkinter as tk
from tkinter import *

# Créer une fenêtre
formu = Tk()
formu.geometry('500x400')
formu.title("Formulaire de réservation")
formu.configure(bg='lightgrey')  # Couleur de fond sombre (noir ou gris foncé)
formu.resizable(height=False, width=False)

# Différentes fonctions :
def register_client():
    register_nom = zone_nom.get()
    register_prenom = zone_prenom.get()
    register_nbre = zone_nombre.get()
    register_heure = zone_heure.get()

    print(f"Vous êtes {register_nom} {register_prenom}, vous serez {register_nbre} et vous avez réservé à {register_heure}.")

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
