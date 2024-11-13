#this file contain somme usefull fonction
from manageDB import *



def on_enter(event,name):
    name.config(cursor="hand2")

def on_leave(event,name):
    name.config(cursor="")


def refresh_background_color(context):
    mainDb = tableMaster_dbConnexion()
    new_background_color = mainDb.retreaveSingleData("settings", "param_value", "param_key", "WorkingAreaColor")
    mainDb.close()
    context.config(bg=new_background_color)
