import subprocess
import tkinter as tk
from utils import *


import platform#pour la détection de l'os



#this file contain all objects for the restaurant
#location is the context (main)
#target is the canvas's name (restoBlueprint)


class TableMaster_Label:
    instances = []
    def __init__(self, location, txt="new label", posiX=500, posiY=500, color="black", width=16, pady=0):
        self.posiX = posiX
        self.posiY = posiY
        #creation of entity

        TableMaster_Label.instances.append(self)


        # Vérifie si l'OS est macOS et si le mode sombre est activé
        if platform.system() == "Darwin" :
            result = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                capture_output=True,
                text=True
            )
            if result.stdout.strip() == "Dark":
                color="white"

        self.label = tk.Label(location, text=txt, font=("Arial", width), fg=color, pady=pady)
        self.label.place(x=posiX, y=posiY)
    def hide(self):
        self.label.place_forget()
    def show(self):
        self.label.place(x=self.posiX, y=self.posiY)

    @classmethod
    def get_all_instances(cls):

        return cls.instances


class TableMaster_RoomDrawer:
    def __init__(self, location, target, nameOfTheRoom, color, *XYpositions):#target is the name of the targeted canvas --> try restoBlueprint
        self.nameOfTheRoom = nameOfTheRoom

        self.draw = target.create_line(*XYpositions, fill=color, width=3)
        self.label = TableMaster_Label(location, nameOfTheRoom, XYpositions[0], XYpositions[1])

class TableMaster_Table:
    def __init__(self,location, target, tableId, maxCapacity,posiX,posiY,tableType):#table type 1 2 3 4
        self.tableId = tableId
        self.maxCapacity = maxCapacity

        self.label = TableMaster_Label(location, "Table n°: " + str(tableId) + " Chaises :" + str(maxCapacity), posiX, posiY, "black", 10)

        if tableType == 1:
            self.canvasId = target.create_oval(posiX-25, posiY-25, posiX+25, posiY+25, fill="green", outline="black", width=2)

        if tableType == 2:
            self.canvasId = target.create_rectangle(posiX-25, posiY-25, posiX+25, posiY+25, fill="green", width=2)

        if tableType == 3:
            self.canvasId = target.create_rectangle(posiX - 75, posiY - 25, posiX + 75, posiY + 25, fill="green",width=2)

        if tableType == 4:
            self.canvasId = target.create_rectangle(posiX-25, posiY-75, posiX+25, posiY+75, fill="green", width=2)



class TableMaster_ButtonOnTop:
    posiX = 0
    def __init__(self, context, iconName, onClickFonction):

        self.topButtonImage = tk.PhotoImage(file="img/" + iconName)
        self.topButton = tk.Button(context, image=self.topButtonImage, command=onClickFonction, width=45, height=45)
        self.topButton.place(x=self.__class__.posiX, y=0)
        self.topButton.bind("<Enter>", lambda event: on_enter(event, self.topButton))
        self.topButton.bind("<Leave>", lambda event: on_leave(event, self.topButton))
        self.__class__.posiX += 50

class TableMaster_windowCreator:
    def __init__(self,title, geometrie):
        self.window = tk.Toplevel()
        self.window.title(title)
        self.window.geometry(geometrie)
        self.window.grab_set()

    def getContext(self):
        return self.window















