#Permet de tout importer dans tkinter
from tkinter import *
from PIL import Image, ImageTk




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


# #Créer une zone de texte ------------------------

# label = Label(fenetre, text='Je fais des testes', font=('Helvetica', 20, 'bold italic'), fg="red", bg='cyan')
# afficher le label 
# label.pack()#side coter et padx nombre de pixel
# label.place(x='180', y='160')
# Mettre du texte en dessous 

# sub_label = Label(fenetre, text="J'aime python", font=('Helvetica', 20, 'bold italic'), fg="red", bg='cyan')
# #Change le texte grace à un input
# change_texte = input("Changer le texte : ")
# sub_label['text'] = change_texte
# sub_label.pack()

#Les boutons ----------------------------------

# def dire_bjr():
#     print("Bonjour !")

# bouton = Button(fenetre, text="Click me !", bg="red", fg='white', command=dire_bjr)
# bouton.pack()

#Les interfaces utilisateurs ----------------

# def function():
#     label["text"] = ma_var.get()

# ma_var = StringVar()
# label = Label(fenetre, text="Texte modifiable") 
# label.pack()
# entree = Entry(fenetre, bg="white", textvariable=ma_var)
# entree.pack()
# bouton = Button(fenetre, bg="white", command=function, text="Valider")
# bouton.pack()

#Interface Graphique --------------------

# mon_menu = Menu(fenetre)

# def save():
#     print(f"Vous avez cliqué sue le sous onglet fichier")
# def options():
#     print(f"Vous avez cliqué sue le sous onglet option")

# #Sous onglet Fichier

# fichier = Menu(mon_menu, tearoff=0)
# fichier.add_command(label="Enregistrer sous...", command=save)

# #Sous onglet Option

# option = Menu(mon_menu, tearoff=0)
# option.add_command(label="Modifier la taille", command=options)

# #Les 2 principaux onglets
# mon_menu.add_cascade(label="fichier", menu=fichier)
# mon_menu.add_cascade(label='Option',  menu=option)


# fenetre.config(menu=mon_menu)

#Les boites ---------------------

# boite = Frame(fenetre, bg="green")

# label = Label(boite, text="Mon premier texte")
# label.pack()
# label2 = Label(boite, text="Mon 2 eme texte")
# label2.pack()

# boite.pack(expand=YES)



#Afficher des images --------------------

# photo = PhotoImage(file='photo.jpg')
# label = Label(fenetre, image=photo)
# label.pack()



#Image clickable  ---------------------

def image_click():
    print("Vous avez cliqué sur l'image")


image = Image.open('C:\\Users\\tiago\\Desktop\\ok\\table.jpg')
image = image.resize((300, 300)) 
photo = ImageTk.PhotoImage(image)



image_bouton = Button(fenetre, image=photo, command=image_click)
image_bouton.pack()

#Appeler la feneter 
fenetre.mainloop()