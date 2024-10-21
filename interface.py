from tkinter import *
from PIL import Image, ImageTk
import subprocess

# Créer la fenêtre
fenetre = Tk()
fenetre.geometry('600x600')
fenetre.title("La Bonne Fourchette")
fenetre['bg'] = 'lightgrey'
fenetre.resizable(height=False, width=False)

# Frame principale
frame_principale = Frame(fenetre, bg='lightgrey')
frame_principale.pack(fill='both', expand=True)

# Frame pour le formulaire
frame_formulaire = Frame(fenetre, bg='lightgrey')

def afficher_formulaire():

    # Masquer la frame principale et afficher la frame formulaire
    frame_principale.pack_forget()
    frame_formulaire.pack(fill='both', expand=True)
    subprocess.Popen(["python", "formulaire_reservation.py"])

def revenir_principal():

    # Masquer la frame formulaire et revenir à la frame principale
    frame_formulaire.pack_forget()
    frame_principale.pack(fill='both', expand=True)

# Ajouter le bouton dans la frame principale
image = Image.open('img\\table_restau.jpeg')
image = image.resize((70, 70))
photo = ImageTk.PhotoImage(image)

image_bouton = Button(frame_principale, image=photo, command=afficher_formulaire)
image_bouton.pack()

Label(frame_formulaire, text="Formulaire de réservation", font=("Helvetica", 16), bg='white').pack(pady=20)
Button(frame_formulaire, text="Retour à la page principale", command=revenir_principal).pack(pady=20)

# Appeler la fenêtre
fenetre.mainloop()
