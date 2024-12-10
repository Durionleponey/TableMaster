from tkinter import ttk, messagebox

from entities import *


def ShowLabel(main):
    elemViewer_window = TableMaster_windowCreator("Modifier les labels", "300x300")

    # Label principal
    TableMaster_Label(elemViewer_window.getContext(), "Ajouter un label", 80, 10, "black", 12)

    # Texte du label
    TableMaster_Label(elemViewer_window.getContext(), "Texte du label :", 10, 50, "black", 10)
    entry_text = tk.Entry(elemViewer_window.getContext(), width=20)
    entry_text.place(x=120, y=50)

    # Position X
    TableMaster_Label(elemViewer_window.getContext(), "Position X :", 10, 90, "black", 10)
    entry_x = tk.Entry(elemViewer_window.getContext(), width=5)
    entry_x.place(x=120, y=90)

    # Position Y
    TableMaster_Label(elemViewer_window.getContext(), "Position Y :", 10, 130, "black", 10)
    entry_y = tk.Entry(elemViewer_window.getContext(), width=5)
    entry_y.place(x=120, y=130)

    # Taille
    TableMaster_Label(elemViewer_window.getContext(), "Taille :", 10, 170, "black", 10)
    entry_size = tk.Entry(elemViewer_window.getContext(), width=5)
    entry_size.place(x=120, y=170)



    TableMaster_Label(elemViewer_window.getContext(), "Couleur :", 10, 210, "black", 10)
    colors = ["black", "blue" , "lightgray", "lightcyan", "lightblue", "lightcoral", "orange", "lightsalmon", "white", "gray", "pink", "brown"]
    color_combobox = ttk.Combobox(elemViewer_window.getContext(), values=colors, state="readonly")
    color_combobox.place(x=120, y=210)
    color_combobox.current(0)

    def on_button_click():
        # Action du bouton : Affiche les valeurs dans la console
        try:
            print("Texte du label :", entry_text.get())
            print("Position X :", entry_x.get())
            print("Position Y :", entry_y.get())
            print("Taille :", entry_size.get())
            TableMaster_Label(main, str(entry_text.get()), int(entry_x.get()), int(entry_y.get()),color=str(color_combobox.get()), width=int(entry_size.get()))

        except:
            messagebox.showerror(
                title="Erreur",
                message="Une ou plusieurs valeurs sont incorrectes.\nVeuillez les vérifier.",
            )
            return -1

        updateLabel = tableMaster_dbConnexion()
        query = f"""
        INSERT INTO labels (labels_txt, labels_X, labels_Y, labels_Color, labels_Width)
        VALUES ('{entry_text.get()}', {entry_x.get()}, {entry_y.get()}, '{color_combobox.get()}', {entry_size.get()});
        """
        updateLabel.rowSQLrequest(query, printSQL=True)
        updateLabel.close()

        #name = "label_" + str(entry_text.get())
        entry_text.delete(0, tk.END)
        entry_x.delete(0, tk.END)
        entry_y.delete(0, tk.END)
        entry_size.delete(0, tk.END)

        messagebox.showinfo(
            title="Succés!",
            message="Le label à bien été ajouté avec succés !",
        )


    button = tk.Button(
        elemViewer_window.getContext(),
        text="Ajouter un label", command=on_button_click, width=20, bg="lightsalmon", fg="black")
    button.place(x=80, y=260)


