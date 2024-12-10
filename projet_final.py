# -*- coding: utf-8 -*-
import sqlite3 as sql

DATABASE = 'restaurant.db'


def fetch_data(query):
    """Exécute une requête SQL et retourne les résultats."""

    try:
        # Établit une connexion à la base de données en utilisant 'with' pour une gestion automatique de la connexion
        with sql.connect(DATABASE) as con:
            # Crée un curseur qui permet d'interagir avec la base de données
            cur = con.cursor()

            con.text_factory = lambda x: str(x, "utf-8")

            # Exécute la requête SQL passée en paramètre
            cur.execute(query)

            # Récupère toutes les lignes résultantes de la requête exécutée
            return cur.fetchall()

    except sql.Error as e:
        # En cas d'erreur SQL, affiche un message d'erreur dans le terminal
        print(f"Erreur lors de l'exécution de la requête : {e}")

        # Si une erreur survient, retourne une liste vide
        return []


def watch_table():
    """Affiche les valeurs des tables"""
    # Tables
    table = fetch_data("Select * from tables")  # requête sql
    for i in table:
        print(f"Le numéro de la table est : {i[1]}")
    return "\n"


"""def watch_reservation():
    print("\n-----Réservation en cour-----")
    ask_date = input("Entrer la date des réservations : ")
    reserv = fetch_data(
        " SELECT T.numero, R.id, R.date, R.heure, R.client_id, R.table_id,C.prenom, C.nom, C.telephone, C.id, R.nombre_personne "
        " FROM tables AS T "
        " JOIN reservations AS R on T.id = R.table_id "
        " JOIN clients AS C on C.id = R.client_id "
        " WHERE R.date = ?", (ask_date,))
    ecrit = ""
    for i in reserv:
        ecrit += (f"La réservation : {i[1]}.\nle numéro de la table est : {i[0]} \nle : {i[2]} à {i[3]} par {i[6]} {i[7]} (id : {i[9]}). \nSon numéro de téléphone est : {i[8]} pour {i[10]} personnes\n")
    return ecrit"""


def watch_reser_date():
    """Affiche les réservations en cours en fonction de la date et de l'heure"""
    ask_date = input("Entrer la date souhaitée : ")
    reserv = fetch_data(
        " SELECT T.numero, R.id, R.date, R.heure, R.client_id, R.table_id,C.prenom, C.nom, C.telephone, C.id "
        " FROM tables AS T "
        " JOIN reservations AS R on T.id = R.table_id "
        " JOIN clients AS C on C.id = R.client_id ")
    for i in reserv:
        if ask_date == i[2]:
            print(f"(ID: {i[1]}) le numéro de la table est : {i[0]} à : {i[3]} par {i[6]}{i[7]} son numéro de téléphone est : {i[8]}")
        else:
            print("Pas de reservation à cette date / heure ci")
    return "\n"


def watch_client():
    """Affiche les clients"""
    client = fetch_data("SELECT id, prenom, nom, telephone from clients ")
    ecrit = ''
    for i in client:
        ecrit += (f"{i[0]}-{i[1]}-{i[2]}-{i[3]} \n")

    return ecrit

def get_available_tables(date, heure):
    conn = sql.connect(DATABASE)
    cur = conn.cursor()


    cur.execute("""
        SELECT T.id
        FROM tables AS T
        WHERE NOT EXISTS (
            SELECT 1
            FROM reservations AS R
            WHERE R.table_id = T.id
              AND R.date = ?
              AND (
                  (R.heure BETWEEN ? AND TIME(?, '+2 hours')) OR
                  (TIME(R.heure, '+2 hours') > ? AND R.heure < ?)
              )
        );
    """, (date, heure, heure, heure, heure))

    available_tables = [row[0] for row in cur.fetchall()]
    conn.close()

    return available_tables

def add_reservation():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()

    print("--- Ajout d'une nouvelle réservation ---")
    client_ids = watch_client()
    print(client_ids)
    client_id = int(input("Entrer l'id du client pour la réservation : "))
    heure = input("Entrez l'heure (format HH:MM) : ")
    date = input("Entrez la date (format DD/MM/YYYY) : ")
    table_id_disponible = get_available_tables(date, heure)
    if len(table_id_disponible) == 0 :
        print(f"Aucune table n'est disponible pour le {date} à {heure}.")
    else:
        print(f"Les tables disponibles pour le {date} à {heure} sont : {table_id_disponible}")
        table_id = int(input("Entrez le numéro de la table : "))
        nombre_personne = int(input("Entrez le nombre de personnes : "))
        cur.execute("""
                INSERT INTO reservations (client_id, table_id, nombre_personne, heure, date)
                VALUES (?, ?, ?, ?, ?)
            """, (client_id, table_id, nombre_personne, heure, date))
        print("Réservation ajoutée avec succès.")

    conn.commit()
    conn.close()


def add_client():
    conn = sql.connect("restaurant.db")
    cursor = conn.cursor()
    prenom = input("Prénom: ")
    nom = input('Nom: ')
    num_telephone = input('Téléphone: ')
    cursor.execute("INSERT OR IGNORE INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)",
                   (prenom, nom, num_telephone))
    print("Client bien ajouter !")
    conn.commit()
    conn.close()


def delete_reservation():
    """Supprimer réservation"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    supp = watch_reser_date()
    print(supp)
    id_supp = int(input("Entrer l'id de la réservation que vous voulez supprimer : "))
    cur.execute("DELETE FROM reservations WHERE id = ?", (id_supp,))
    print(f'La réservation à bien été supprimée : {id_supp}')
    conn.commit()
    conn.close()


def delete_client():
    """Supprimer un client avec gestion des réservations associées"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()

    print("----- Liste des clients -----")
    print(watch_client())

    id_supp = int(input("Entrez l'ID du client que vous voulez supprimer : "))

    verif_reserv = cur.execute("SELECT id FROM reservations WHERE client_id = ?", (id_supp,)).fetchall()

    if verif_reserv:
        print(f"Le client avec l'ID {id_supp} a des réservations. Suppression en cours...")
        for reserv in verif_reserv:
            id_reserv = reserv[0]
            cur.execute("DELETE FROM reservations WHERE id = ?", (id_reserv,))

    # Supprimer le client
    cur.execute("DELETE FROM clients WHERE id = ?", (id_supp,))
    conn.commit()
    conn.close()
    print(f"Le client avec l'ID {id_supp} a bien été supprimé.")


def modify_reservation():
    """Modifier une réservation"""
    # Connexion à la base de données
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()

    # Entrée de l'utilisateur pour la date
    ask_date = input('Entrez la date à modifier (format DD/MM/YYYY) : ')

    # Requête pour récupérer les réservations à la date donnée
    cur.execute(
        """
        SELECT T.numero, R.id, R.date, R.heure, R.client_id, R.table_id, C.prenom, C.nom, C.telephone, C.id
        FROM tables AS T
        JOIN reservations AS R ON T.id = R.table_id
        JOIN clients AS C ON C.id = R.client_id
        WHERE R.date = ?
        """,
        (ask_date,)
    )
    reserv = cur.fetchall()

    # Affichage des réservations
    if reserv:
        for reservation in reserv:
            print(
                f"L'id de la réservation est : {reservation[1]}\nLe numéro de la table est : {reservation[0]} à : {reservation[3]} par {reservation[6]} {reservation[7]}."
                f" Son numéro de téléphone est : {reservation[8]}")
    else:
        print("Aucune réservation trouvée pour cette date.")
        conn.close()
        return

    # Sélection de la réservation à modifier
    modif_reserv = int(input("Entrez l'ID de la réservation à modifier : "))

    # Entrée des nouvelles informations
    nouvelle_date = input("Entrez la nouvelle date (format DD/MM/YYYY) : ")
    nouvelle_heure = input("Entrez la nouvelle heure (format HH:MM) : ")
    table_id_dispo = get_available_tables(nouvelle_date, nouvelle_heure)
    if len(table_id_dispo) == 0 :
        print(f"Aucune table n'est disponible pour le {nouvelle_date} à {nouvelle_heure}.")
    else:
        print(f"Les tables disponibles pour le {nouvelle_date} à {nouvelle_heure} sont : {table_id_dispo}")
        table_id = int(input("Entrez le numéro de la table : "))
        nombre_personne = int(input("Entrez le nombre de personnes : "))
        cur.execute("""
                Update reservations 
                set table_id= ?, nombre_personne = ?, heure = ?, date = ? WHERE id = ? """,(table_id, nombre_personne, nouvelle_heure, nouvelle_date, modif_reserv))
    conn.commit()
    print(f"La réservation avec l'ID {modif_reserv} a été modifiée avec succès.")
    # Fermeture de la connexion
    conn.close()

def modif_client():
    """Modifier une client"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    affichage = watch_client()
    print(affichage)
    modif_id_client = int(input("Entrer l'id du client à modifier : "))
    nouveau_prenom = input("Entrez le nouvelle prenom : ")
    nouveau_nom = input("Entrez le nouvelle nom : ")
    nouveau_telephone = input("Entrez le telephone : ")
    cur.execute("UPDATE clients SET prenom = ?, nom = ?, telephone = ? WHERE id = ?",
                (nouveau_prenom, nouveau_nom, nouveau_telephone, modif_id_client))
    print(f"Version modifier : {nouveau_prenom}, {nouveau_nom}, {nouveau_telephone}")
    conn.commit()
    conn.close()

def add_table():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    table_exi = fetch_data("Select id, numero from tables")
    for i in table_exi:
        print(f"Le numéro de table existant : {i[1]}")
    numero_table = int(input("Entrer le nombre de la table à ajouter : "))
    cur.execute("Insert into tables(numero) values (?)",(numero_table,))
    print("La table à été ajoutée !")
    conn.commit()
    conn.close()

def watch_menu():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    affichage = fetch_data("Select * from menu")
    ecrit = ''
    for i in affichage:
        ecrit += (f"{i[0]} : {i[1]} pour {i[2]} €\n")
    conn.close()
    conn.close()
    return ecrit

def add_plat():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    label_plat = input('Entrer le nom du plat : ')
    prix_plat = float(input("Entrer le prix du plat : "))
    cur.execute("Insert into menu(nom, prix) values (?, ?)",(label_plat, prix_plat))
    print(f'Vous avez ajouté : {label_plat} pour {prix_plat} €.')
    conn.commit()
    conn.close()

def modif_plat():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    affichage_plat = fetch_data("Select * from menu")
    for i in affichage_plat:
        print(f"(ID : {i[0]}) Il y a {i[1]} pour {i[2]} €")
    plat_modif = int(input("Entrer l'id du plat modifié : "))
    new_label = input("Entrer le nom du plat : ")
    new_prix = float(input("Entrer le prix du plat : "))

    cur.execute('Update menu set nom = ?, prix = ? where id = ?',(new_label, new_prix, plat_modif))
    conn.commit()
    conn.close()


def delete_plat():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    affichage_plat = fetch_data("Select * from menu")
    for i in affichage_plat:
        print(f"(ID : {i[0]}) Il y a {i[1]} pour {i[2]} €")
    plat_supp = int(input("Entrer l'id du plat à supprimer : "))
    cur.execute("Delete from menu where id = ?",(plat_supp,))
    print('Suppression effectué !')
    conn.commit()
    conn.close()





def add_order():
    """Ajouter une commande pour une réservation"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()

    ask_date = input("Entrez la date souhaitée (format DD-MM-YYYY) : ")

    cur.execute(
        """
        SELECT T.numero, R.id, R.date, R.heure, R.client_id, R.table_id, C.prenom, C.nom, C.telephone
        FROM tables AS T
        JOIN reservations AS R ON T.id = R.table_id
        JOIN clients AS C ON C.id = R.client_id
        WHERE R.date = ?
        """,
        (ask_date,)
    )
    reserv = cur.fetchall()


    if not reserv:
        print("Aucune réservation trouvée pour cette date.")
        conn.close()
        return

    print("-- Réservations disponibles --")
    for reservation in reserv:
        print(
            f"ID : {reservation[1]}, Table : {reservation[0]}, Heure : {reservation[3]}, Client : {reservation[6]} {reservation[7]}")

    try:
        ask_id_reser = int(input("Entrez l'ID de la réservation pour ajouter une commande : "))
        selected_reservation = next(res for res in reserv if res[1] == ask_id_reser)
    except (ValueError, StopIteration):
        print("ID de réservation invalide.")
        conn.close()
        return

    while True:
        try:
            voir_menu = watch_menu()
            print("-- Le menu --")
            print(voir_menu)
            choix_plat = int(input("Entrez l'ID du plat : "))
            quanti = int(input("Entrez la quantité : "))
        except ValueError:
            print("Veuillez entrer des valeurs valides pour l'ID et la quantité.")
            continue

        cur.execute(
            """
            INSERT INTO commandes (reserv_id, table_id, plat_id, quantite)
            VALUES (?, ?, ?, ?)
            """,
            (ask_id_reser, selected_reservation[5], choix_plat, quanti)
        )

        continuer = input("Entrez SUIVANT pour choisir un nouveau plat ou STOP pour arrêter : ").strip().upper()
        if continuer == "STOP":
            break

    conn.commit()
    print("Commande(s) ajoutée(s) avec succès.")

    conn.close()

def modif_order():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    pass

def watch_order():
    """Voir les commandes d'une table pour une date donnée"""

    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    date_response = watch_reser_date()
    print(date_response)
    ask_reserv = int(input('Entrer le numéro de la réservation : '))


def complete_order():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    pass

if __name__ == "__main__":
    watch_order()
