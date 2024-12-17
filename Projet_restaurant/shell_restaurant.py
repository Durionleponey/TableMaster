from restaurant import *

def menu_principal():
    database = DatabaseHandler("restaurant.db")
    while True:
        print("\n--- Shell de Restaurant ---")
        print("1. Gestion des tables")
        print("2. Gestion des clients")
        print("3. Gestion des réservations")
        print("4. Gestion des plats")
        print("5. Gestion des commandes")
        print("6. Quitter\n")

        choix = input("Choisissez une option : ")

        if choix == "1":
            gestion_tables(database)
        elif choix == "2":
            gestion_clients(database)
        elif choix == "3":
            gestion_reservations(database)
        elif choix == "4":
            gestion_plats(database)
        elif choix == "5":
            gestion_commandes(database)
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

def gestion_tables(database):
    while True:
        print("\n--- Gestion des Tables ---")
        print("1. Afficher les tables")
        print("2. Ajouter une table")
        print("3. Supprimer une table")
        print("4. Retour\n")

        choix = input("Choisissez une option : ")
        if choix == "1":
            Table.afficher_tables(database)

        elif choix == "2":
            numero = input("Numéro de la table : ")
            Table.ajouter_table(database, numero)

        elif choix == "3":
            Table.afficher_tables(database)
            table_id = input("ID de la table à supprimer : ")
            Table.supprimer_table(database, table_id)

        elif choix == "4":
            break
        else:
            print("Option invalide.")

def gestion_clients(database):
    while True:
        print("\n--- Gestion des Clients ---")
        print("1. Afficher les clients")
        print("2. Ajouter un client")
        print("3. Modifier un client")
        print("4. Supprimer un client")
        print("5. Retour\n")

        choix = input("Choisissez une option : ")
        if choix == "1":
            Client.afficher_clients(database)

        elif choix == "2":
            prenom = input("Prénom : ")
            nom = input("Nom : ")
            telephone = input("Téléphone : ")
            Client.ajouter_client(database, prenom, nom, telephone)

        elif choix == "3":
            Client.afficher_clients(database)
            client_id = input("ID du client à modifier : ")
            prenom = input("Nouveau prénom : ")
            nom = input("Nouveau nom : ")
            telephone = input("Nouveau téléphone : ")
            Client.modifier_client(database, client_id, prenom, nom, telephone)

        elif choix == "4":
            Client.afficher_clients(database)
            client_id = input("ID du client à supprimer : ")
            Client.supprimer_client(database, client_id)

        elif choix == "5":
            break

        else:
            print("Option invalide.")

def gestion_reservations(database):
    while True:
        print("\n--- Gestion des Réservations ---")
        print("1. Afficher les réservations")
        print("2. Ajouter une réservation")
        print("3. Modifier une réservation")
        print("4. Supprimer une réservation")
        print("5. Retour\n")

        choix = input("Choisissez une option : ")
        if choix == "1":
            Reservation.afficher_reservations(database)

        elif choix == "2":
            Client.afficher_clients(database)
            client_id = int(input("ID du client : "))
            date = input("Indiquez la date (AAAA-MM-JJ) : ")
            heure = input("Indiquez la heure (HH:MM) : ")
            Table.afficher_tables_disponibles(database, date, heure)
            table_id = int(input("ID de la table : "))
            nombre_personne = int(input("Nombre de personnes : "))
            Reservation.ajouter_reservation(database, client_id, table_id, nombre_personne, date, heure)

        elif choix == "3":
            Reservation.afficher_reservations(database)
            reservation_id = int(input("ID de la réservation à modifier : "))
            nouvelle_date = input("Nouvelle date (AAAA-MM-JJ) : ")
            nouvelle_heure = input("Nouvelle heure (HH:MM) : ")
            Table.afficher_tables_disponibles(database, nouvelle_date, nouvelle_heure)
            table_id = int(input("Nouvel ID de la table : "))
            nombre_personnes = int(input("Nouveau nombre de personnes : "))
            Reservation.modifier_reservation(database, reservation_id, nouvelle_date, nouvelle_heure, table_id, nombre_personnes)

        elif choix == "4":
            Reservation.afficher_reservations(database)
            reservation_id = input("ID de la réservation à supprimer : ")
            Reservation.supprimer_reservation(database, reservation_id)

        elif choix == "5":
            break

        else:
            print("Option invalide.")

def gestion_plats(database):
    while True:
        print("\n--- Gestion des Plats ---")
        print("1. Afficher le menu")
        print("2. Ajouter un plat")
        print("3. Modifier un plat")
        print("4. Supprimer un plat")
        print("5. Retour\n")

        choix = input("Choisissez une option : ")
        if choix == "1":
            Plat.afficher_menu(database)

        elif choix == "2":
            nom = input("Nom du plat : ")
            prix = input("Prix du plat : ")
            Plat.ajouter_plat(database, nom, prix)

        elif choix == "3":
            Plat.afficher_menu(database)
            plat_id = input("ID du plat à modifier : ")
            nom = input("Nouveau nom : ")
            prix = input("Nouveau prix : ")
            Plat.modifier_plat(database, plat_id, nom, prix)

        elif choix == "4":
            Plat.afficher_menu(database)
            plat_id = input("ID du plat à supprimer : ")
            Plat.supprimer_plat(database, plat_id)

        elif choix == "5":
            break

        else:
            print("Option invalide.")

def gestion_commandes(database):
    while True:
        print("\n--- Gestion des Commandes ---")
        print("1. Afficher les commandes d'une réservation")
        print("2. Ajouter une commande")
        print("3. Modifier une commande")
        print("4. Supprimer une commande")
        print("5. Retour\n")

        choix = input("Choisissez une option : ")
        if choix == "1":
            Reservation.afficher_reservations(database)
            reservation_id = input("ID de la réservation : ")
            Commande.afficher_commandes(database, reservation_id)

        elif choix == "2":
            Reservation.afficher_reservations(database)
            reservation_id = int(input("ID de la réservation : "))
            table_id = Commande.table_id_via_reservation_id(database, reservation_id)
            Plat.afficher_menu(database)
            plat_id = int(input("ID du plat : "))
            quantite = input("Quantité : ")
            Commande.ajouter_commande(database, reservation_id, table_id, plat_id, quantite)

        elif choix == "3":
            Reservation.afficher_reservations(database)
            reservation_id = input("ID de la réservation : ")
            Commande.afficher_commandes(database, reservation_id)
            commande_id = input("ID de la commande à modifier : ")
            Plat.afficher_menu(database)
            plat_id = input("Nouvel ID du plat : ")
            quantite = input("Nouvelle quantité : ")
            Commande.modifier_commande(database, commande_id, plat_id, quantite)

        elif choix == "4":
            Reservation.afficher_reservations(database)
            reservation_id = input("ID de la réservation : ")
            Commande.afficher_commandes(database, reservation_id)
            commande_id = input("ID de la commande à supprimer : ")
            Commande.supprimer_commande(database, commande_id)

        elif choix == "5":
            break

        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu_principal()
