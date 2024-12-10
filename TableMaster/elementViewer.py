from shutil import posix
from traceback import print_tb

from TableMaster.settings import on_color_change
from entities import *
from tkinter import ttk
from manageDB import *
from utils import *



def onChangeElementViewer(label_var):


    if label_var:

        for i in TableMaster_Label.get_all_instances():
            i.show()
    else:
        for i in TableMaster_Label.get_all_instances():
            try:
                i.hide()
            except:
                pass

def onChangeElementViewer2(table_var):

    if table_var:

        for i in TableMaster_Table.get_all_instances():
            print(i)
            i.show()
    else:
        for i in TableMaster_Table.get_all_instances():
            i.hide()
        for i in TableMaster_Label.get_all_instances():
            i.show()

def onChangeElementViewer3(wall_var):

    if wall_var:

        for i in TableMaster_RoomDrawer.get_all_instances():
            print(i)
            i.show()
    else:
        for i in TableMaster_RoomDrawer.get_all_instances():
            i.hide()








def ShowElementViewer():



    elemViewer_window = TableMaster_windowCreator("Element à afficher","300x300")

#oui clairement des class ca auraient été mieux mais j'en ai déjà faites beaucoup
    TableMaster_Label(elemViewer_window.getContext(), "Elements à afficher :", 0, 0,"black",12,5)
    label_var = tk.IntVar(value=1)
    checkbox = tk.Checkbutton(elemViewer_window.getContext(), text="Label", variable=label_var, command=lambda : onChangeElementViewer(label_var.get()))
    checkbox.pack(pady=30)

    table_var = tk.IntVar(value=1)
    checkbox2 = tk.Checkbutton(elemViewer_window.getContext(), text="Table", variable=table_var, command=lambda : onChangeElementViewer2(table_var.get()))
    checkbox2.pack(pady=30)

    wall_var = tk.IntVar(value=1)
    checkbox3 = tk.Checkbutton(elemViewer_window.getContext(), text="Mur", variable=wall_var, command=lambda : onChangeElementViewer3(wall_var.get()))
    checkbox3.pack(pady=30)




