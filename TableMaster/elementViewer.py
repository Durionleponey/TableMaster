from entities import *
from tkinter import ttk
from manageDB import *
from utils import *



def ShowElementViewer():



    elemViewer_window = TableMaster_windowCreator("Element à afficher","300x300")


    TableMaster_Label(elemViewer_window.getContext(), "Elements à afficher :", 0, 0,"black",12,2)

