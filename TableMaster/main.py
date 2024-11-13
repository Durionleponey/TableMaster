from tkinter import messagebox

from settings import *

#interface principal menu principal
main = tk.Tk()
main.title("TableMaster")
main.geometry("800x800")
main.resizable(False, False)

#icon de la fenetre
icon = tk.PhotoImage(file="img/icon.png")
main.iconphoto(True,icon)



#Je vais faire une class pour les icones du haut ca va être plus propre

# #icon des settings
# gearImage = tk.PhotoImage(file="img/gear.png")
# gearImageSetting = tk.Button(main, image=gearImage, command=lambda: ShowSetting(restoBlueprint), width=45, height=45)#j'ai pas trouvé mieux pour faire avoir accés au fonction de refresh en dehors de main.py
# gearImageSetting.place(x=0, y=0)
# gearImageSetting.bind("<Enter>", lambda event: on_enter(event, gearImageSetting))  # Quand la souris entre dans le label
# gearImageSetting.bind("<Leave>", lambda event: on_leave(event, gearImageSetting))   # Quand la souris quitte le label

# #icon des options vues
# eyeImage = tk.PhotoImage(file="img/eye.png")
# eyeImageSetting = tk.Button(main, image=eyeImage, command="", width=45, height=45)
# eyeImageSetting.place(x=50, y=0)
# eyeImageSetting.bind("<Enter>", lambda event: on_enter(event, eyeImageSetting))
# eyeImageSetting.bind("<Leave>", lambda event: on_leave(event, eyeImageSetting))
#









#working area for the map of the restaurant

restoBlueprint = tk.Canvas(main, width=800, height=750)
restoBlueprint.place(x=0, y=50)


refresh_background_color(restoBlueprint)

def test():
    messagebox.showinfo("hello")


SettingTopButton = TableMaster_ButtonOnTop(main, "gear.png", lambda: ShowSetting(restoBlueprint))
SettingEyeButton = TableMaster_ButtonOnTop(main, "eye.png", lambda: test())


#ce qui est en bas c'est juste des exemples hors DB

mainRoom = TableMaster_RoomDrawer(main,restoBlueprint,"mainRoom","blue",50, 50, 50, 700, 450, 700, 450, 50, 50, 50)
petitSalon = TableMaster_RoomDrawer(main,restoBlueprint,"Le petit salon privé","green",500, 300, 500, 650, 650, 650, 650, 500, 500, 300)
bureauDirecteur = TableMaster_RoomDrawer(main,restoBlueprint, "Bureau du Directeur", "orange", 600, 150, 600, 350, 800, 350, 800, 150, 600, 150)


robin = TableMaster_Table(main, restoBlueprint, 1, 3,300,100,1)
robin2 = TableMaster_Table(main, restoBlueprint, 2, 3,600,100,2)
robin3 = TableMaster_Table(main, restoBlueprint, 3, 3,600,600,3)
robin4 = TableMaster_Table(main, restoBlueprint, 4, 3,100,600,4)

labelSeulTest = TableMaster_Label(main, "Bonjour les amis!", 100, 300)
labelSeulTest = TableMaster_Label(main, "50-100", 50, 100)
labelSeulTest = TableMaster_Label(main, "400-50", 400, 50)
labelSeulTest = TableMaster_Label(main, "50-400", 50, 400)
labelSeulTest = TableMaster_Label(main, "50-750", 50, 750)



main.mainloop()


