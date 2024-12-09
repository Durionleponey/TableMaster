from shutil import posix
from traceback import print_tb

from TableMaster.settings import on_color_change
from entities import *
from tkinter import ttk
from manageDB import *
from utils import *



def onChangeElementViewer(label_var):
    print(label_var)
    if label_var:
        print(TableMaster_Label.get_all_instances())
        for i in TableMaster_Label.get_all_instances():
            i.hide()
    else:
        print(TableMaster_Label.get_all_instances())
        for i in TableMaster_Label.get_all_instances():
            print(i.posiX)
            i.show()






def ShowElementViewer():



    elemViewer_window = TableMaster_windowCreator("Element à afficher","300x300")

#oui clairement des class ca auraient été mieux mais j'en ai déjà faites beaucoup
    TableMaster_Label(elemViewer_window.getContext(), "Elements à afficher :", 0, 0,"black",12,5)
    label_var = tk.IntVar()
    checkbox = tk.Checkbutton(elemViewer_window.getContext(), text="Label", variable=label_var, command=lambda : onChangeElementViewer(label_var.get()))
    checkbox.pack(pady=30)

    table_var = tk.IntVar()
    checkbox2 = tk.Checkbutton(elemViewer_window.getContext(), text="Table", variable=table_var, command=onChangeElementViewer)
    checkbox2.pack(pady=30)

    wall_var = tk.IntVar()
    checkbox3 = tk.Checkbutton(elemViewer_window.getContext(), text="Mur", variable=wall_var, command=onChangeElementViewer)
    checkbox3.pack(pady=30)




