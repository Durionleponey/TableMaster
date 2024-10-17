
#Permet de tout importer dans tkinter
from tkinter import *
from PIL import Image, ImageTk
from imaplib import *



#Créer une feneter
fenetre = Tk()
#régler la taille de la fenêtre (1x2) 1 = longueur, 2 =largeur
fenetre.geometry('600x600')
#mettre un tritre  dans la fenêtre
fenetre.title("Mon application")
#Changer la couleur du bg de la fenetre
fenetre['bg'] = 'cyan'
#empecher la redimension de la feneter
fenetre.resizable(height=False, width=False)







#Image clickable  ---------------------

def image_click():
    fenetre2 = Tk()
    fenetre2.geometry('400x400')
    fenetre2.title('Réservation')
    fenetre2['bg'] = 'lightgreen'
    fenetre2.resizable(height=True, width=True)

    label = Label(fenetre2, text='Trop stylaxe')
    label.pack()


image = Image.open('img\\table_restau.jpeg')
image = image.resize((70, 70))
photo = ImageTk.PhotoImage(image)



image_bouton = Button(fenetre, image=photo, command=image_click)
image_bouton.pack()

#Appeler la feneter
fenetre.mainloop()






"""
Fausse version : 

# Importer les modules nécessaires
from tkinter import *
from PIL import Image, ImageTk  # Importer les modules pour gérer les images avec Pillow

# Fonction pour basculer vers une nouvelle interface
def switch_frame(new_frame):
    # Masquer l'ancienne interface
    current_frame.pack_forget()
    # Afficher la nouvelle interface
    new_frame.pack(fill='both', expand=True)

# Créer une fenêtre
fenetre = Tk()
fenetre.geometry('600x600')
fenetre.title("Mon application")
fenetre['bg'] = 'cyan'
fenetre.resizable(height=False, width=False)

# Interface 1 : Afficher une image et un bouton
current_frame = Frame(fenetre)
current_frame.pack(fill='both', expand=True)

# Charger et redimensionner l'image avec Pillow
try:
    image = Image.open('img\\table_restau.jpeg')
    image = image.resize((300, 300))  # Redimensionner l'image
    photo = ImageTk.PhotoImage(image)  # Convertir l'image pour Tkinter
except FileNotFoundError:
    print("L'image n'a pas été trouvée. Vérifiez le chemin du fichier.")
    photo = None

# Afficher l'image si elle est chargée
if photo:
    image_label = Label(current_frame, image=photo)
    image_label.pack()

# Interface 2 : Nouvelle interface après le clic
new_frame = Frame(fenetre)

# Ajouter du contenu à la nouvelle interface
new_label = Label(new_frame, text="Vous êtes sur la nouvelle interface !", font=('Helvetica', 16))
new_label.pack(pady=20)

# Bouton pour retourner à l'interface d'origine
back_button = Button(new_frame, text="Retour", command=lambda: switch_frame(current_frame))
back_button.pack(pady=20)

# Clic sur l'image pour basculer vers la nouvelle interface
if photo:
    image_bouton = Button(current_frame, text="Cliquez ici !", command=lambda: switch_frame(new_frame))
    image_bouton.pack()

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
"""

