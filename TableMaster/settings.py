from entities import *
from tkinter import ttk
from manageDB import *
from utils import *




def ShowSetting(context):

    settings_window = TableMaster_windowCreator("Settings","500x600")


    TableMaster_Label(settings_window.getContext(), "Couleur de fond :", 0, 0,"black",12,2)

    colors = ["lightgray", "lightcyan", "lightblue", "lightcoral", "orange", "lightsalmon", "white", "gray", "pink", "brown"]

    color_combobox = ttk.Combobox(settings_window.getContext(), values=colors, state="readonly")

    mainDb = tableMaster_dbConnexion()
    backgroundColorFromDb = (mainDb.retreaveSingleData("settings", "param_value", "param_key", "WorkingAreaColor"))
    mainDb.close()

    color_combobox.set(backgroundColorFromDb)
    color_combobox.pack(pady=2)

    color_combobox.bind("<<ComboboxSelected>>", lambda event: on_color_change(color_combobox.get(),context))


def on_color_change(newColor,context):
    db = tableMaster_dbConnexion()
    db.updateValue("settings", "param_value", "param_key", "WorkingAreaColor", newColor,  True)
    db.close()
    refresh_background_color(context)





