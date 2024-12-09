from entities import *
from tkinter import ttk
from manageDB import *
from utils import *


def ShowBoking():



    elemViewer_window = TableMaster_windowCreator("Faire une réservation","300x300")


    TableMaster_Label(elemViewer_window.getContext(), "Table à réserver:", 0, 0,"black",12,2)

    freeTable = ["lightgray", "lightcyan", "lightblue", "lightcoral", "orange", "lightsalmon", "white", "gray", "pink", "brown"]

    freeTable_combobox = ttk.Combobox(elemViewer_window.getContext(), values=freeTable, state="readonly")

    freeTable_combobox.pack(pady=30)

