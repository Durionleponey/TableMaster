import sqlite3

class database_handler:
    def __init__(self, database):
        self.database = database

    def execute_query(self, query, params=()):
        try:
            with sqlite3.connect(self.database) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                conn.commit()
                return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")
            return []

class Client:
    def __init__(self, id, prenom, nom, telephone):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone

    def __str__(self):
        return f"{self.id}: {self.prenom} {self.nom}, Téléphone: {self.telephone}"

    @staticmethod
    def ajouter_client(database, prenom, nom, telephone):
        try:
            database.execute_query("INSERT INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)", (prenom, nom, telephone))
            print(f"Client ajouté : {prenom} {nom}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def afficher_clients(database):
        try:
            clients_data = database.execute_query("SELECT id, prenom, nom, telephone FROM clients")
            clients = [Client(*data) for data in clients_data]
            for client in clients:
                print(client)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_client(database, client_id):
        reservations = database.execute_query("SELECT id FROM reservations WHERE client_id = ?", (client_id,))
        for reserv in reservations:
            Reservation.supprimer_reservation(database, reserv[0])
        database.execute_query("DELETE FROM clients WHERE id = ?", (client_id,))
        print(f"Client {client_id} supprimé.")

    @staticmethod
    def modifier_client(database, client_id, nouveau_prenom, nouveau_nom, nouveau_telephone):
        try:
            database.execute_query(
                "UPDATE clients SET prenom = ?, nom = ?, telephone = ? WHERE id = ?",
                (nouveau_prenom, nouveau_nom, nouveau_telephone, client_id)
            )
            print(f"Client {client_id} modifié : {nouveau_prenom} {nouveau_nom}, Téléphone: {nouveau_telephone}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

class Table:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero

    def __str__(self):
        return f"Table {self.numero}"

    @staticmethod
    def afficher_tables(database):
        try:
            tables_data = database.execute_query("SELECT id, numero FROM tables")
            tables = [Table(*data) for data in tables_data]
            for table in tables:
                print(f"Id : {table.id} -- {table}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def ajouter_table(database, numero):
        try: 
            database.execute_query("INSERT INTO tables (numero) VALUES (?)", (numero,))
            print(f"Table {numero} ajoutée.")
        except sqlite3.Error as e:
            print(f"La table {numero} existe déjà.")

    @staticmethod
    def supprimer_table(database, table_id):
        try:
            reservations = database.execute_query("SELECT id FROM reservations WHERE table_id = ?", (table_id,))
            if reservations:
                print(f"La table {table_id} est associée à des réservations et ne peut pas être supprimée.")
                return

            database.execute_query("DELETE FROM tables WHERE id = ?", (table_id,))
            print(f"Table {table_id} supprimée.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def get_tables_disponibles(database, date, heure):
        tables_data = database.execute_query(
            """
            SELECT T.id, T.numero
            FROM tables AS T
            WHERE NOT EXISTS (
                SELECT 1 FROM reservations AS R
                WHERE R.table_id = T.id AND R.date = ? AND (
                    (R.heure BETWEEN ? AND TIME(?, '+2 hours')) OR
                    (TIME(R.heure, '+2 hours') > ? AND R.heure < ?)
                )
            )
            """,
            (date, heure, heure, heure, heure)
        )
        return [Table(*data) for data in tables_data]

    @staticmethod
    def afficher_tables_disponibles(database, date, heure):
        try:
            tables_disponibles = Table.get_tables_disponibles(database, date, heure)
            if not tables_disponibles:
                print("Aucune table disponible pour cette date et heure.")
            else:
                print(f"Tables disponibles pour le {date} à {heure}:")
                for table in tables_disponibles:
                    print(table)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

class Reservation:
    def __init__(self, id, client, table, nombre_personnes, date, heure):
        self.id = id
        self.client = client
        self.table = table
        self.nombre_personnes = nombre_personnes
        self.date = date
        self.heure = heure

    def __str__(self):
        return (f"Réservation {self.id}: Client {self.client.prenom} {self.client.nom}, "
                f"Table {self.table.numero}, {self.date} à {self.heure}, "
                f"pour {self.nombre_personnes} personnes")

    @staticmethod
    def afficher_reservations(database):
        try:
            reservations_data = database.execute_query(
                """
                SELECT R.id, R.date, R.heure, R.nombre_personne, C.id, C.prenom, C.nom, T.id, T.numero
                FROM reservations AS R
                JOIN clients AS C ON R.client_id = C.id
                JOIN tables AS T ON R.table_id = T.id
                """
            )
            reservations = [
                Reservation(res[0], Client(res[4], res[5], res[6], None), Table(res[7], res[8]), res[3], res[1], res[2])
                for res in reservations_data
            ]
            for reservation in reservations:
                print(reservation)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def ajouter_reservation(database, client_id, table_id, nombre_personne, date, heure):
        try:
            tables_disponibles = Table.get_tables_disponibles(database, date, heure)
            if table_id not in [table.id for table in tables_disponibles]:
                print(f"Table {table_id} non disponible.")
                return

            database.execute_query(
                "INSERT INTO reservations (client_id, date, heure, table_id, nombre_personne) VALUES (?, ?, ?, ?, ?)",
                (client_id, date, heure, table_id, nombre_personne)
            )
            print(f"Réservation ajoutée pour le client {client_id}.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_reservation(database, reservation_id):
        try:
            database.execute_query("DELETE FROM commandes WHERE reserv_id = ?", (reservation_id,))
            database.execute_query("DELETE FROM reservations WHERE id = ?", (reservation_id,))
            print(f"Réservation {reservation_id} supprimée.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def modifier_reservation(database, reservation_id, nouvelle_date, nouvelle_heure, table_id, nombre_personnes):
        try:
            tables_disponibles = Table.get_tables_disponibles(database, nouvelle_date, nouvelle_heure)
            if table_id not in [table.id for table in tables_disponibles]:
                print(f"Table {table_id} non disponible pour {nouvelle_date} à {nouvelle_heure}.")
                return

            database.execute_query(
                "UPDATE reservations SET table_id = ?, nombre_personne = ?, date = ?, heure = ? WHERE id = ?",
                (table_id, nombre_personnes, nouvelle_date, nouvelle_heure, reservation_id)
            )
            print(f"Réservation {reservation_id} modifiée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

class Plat:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.id}: {self.nom} - {self.prix}€"

    @staticmethod
    def afficher_menu(database):
        try:
            plats_data = database.execute_query("SELECT id, nom, prix FROM menu")
            plats = [Plat(*data) for data in plats_data]
            for plat in plats:
                print(plat)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def ajouter_plat(database, nom, prix):
        try:
            database.execute_query("INSERT INTO menu (nom, prix) VALUES (?, ?)", (nom, prix))
            print(f"Plat ajouté : {nom} - {prix}€")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_plat(database, plat_id):
        try:
            database.execute_query("DELETE FROM menu WHERE id = ?", (plat_id,))
            print(f"Plat {plat_id} supprimé.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def modifier_plat(database, plat_id, nouveau_nom, nouveau_prix):
        try:
            database.execute_query(
                "UPDATE menu SET nom = ?, prix = ? WHERE id = ?",
                (nouveau_nom, nouveau_prix, plat_id)
            )
            print(f"Plat {plat_id} modifié en {nouveau_nom} - {nouveau_prix}€.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

class Commande:

    @staticmethod
    def ajouter_commande(database, reservation_id, table_id, plat_id, quantite):
        try:
            database.execute_query(
                "INSERT INTO commandes (reserv_id, table_id, plat_id, quantite) VALUES (?, ?, ?, ?)",
                (reservation_id, table_id, plat_id, quantite)
            )
            print(f"Commande ajoutée pour la réservation {reservation_id}.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def afficher_commandes(database, reservation_id):
        try:
            commandes_data = database.execute_query(
                """
                SELECT C.id, M.nom, C.quantite, M.prix
                FROM commandes AS C
                JOIN menu AS M ON C.plat_id = M.id
                WHERE C.reserv_id = ?
                """,
                (reservation_id,)
            )
            total = 0
            for commande in commandes_data:
                id_commande, nom, quantite, prix = commande
                total += quantite * prix
                print(f"Commande {id_commande}: {nom}, Quantité: {quantite}, Prix: {prix}€, Total: {quantite * prix}€")
            print(f"Total: {total}€")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def modifier_commande(database, commande_id, nouveau_plat_id, nouvelle_quantite):
        try:
            database.execute_query(
                "UPDATE commandes SET plat_id = ?, quantite = ? WHERE id = ?",
                (nouveau_plat_id, nouvelle_quantite, commande_id)
            )
            print(f"Commande {commande_id} modifiée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_commande(database, commande_id):
        try:
            database.execute_query("DELETE FROM commandes WHERE id = ?", (commande_id,))
            print(f"Commande {commande_id} supprimée.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def table_id_via_reservation_id(database, reservation_id):
        try:
            table_id = database.execute_query("SELECT table_id FROM reservations WHERE id = ?", (reservation_id,))
            return table_id[0][0]
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

database = database_handler("restaurant.db")
