import sqlite3

class DatabaseHandler:
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


def get_client(database, prenom, nom, telephone) :
    database.execute_query("INSERT INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)", (prenom, nom, telephone))

def select_client(database):
    client_data = database.execute_query("SELECT id, prenom, nom, telephone FROM clients")
    return client_data

def select_id_reserv_client(database, client_id):
    id_reserv_client = database.execute_query("SELECT id FROM reservations WHERE client_id = ?", (client_id,))
    return id_reserv_client

def delete_client_by_id(database, client_id):
    database.execute_query("DELETE FROM clients WHERE id = ?", (client_id,))

def update_client(database,nouveau_prenom, nouveau_nom, nouveau_telephone, client_id):
    database.execute_query(
        "UPDATE clients SET prenom = ?, nom = ?, telephone = ? WHERE id = ?",
        (nouveau_prenom, nouveau_nom, nouveau_telephone, client_id)
    )

def get_table(database):
    tables_data = database.execute_query("SELECT id, numero FROM tables")
    return tables_data

def add_table(database, numero):
    database.execute_query("INSERT INTO tables (numero) VALUES (?)", (numero,))

def select_id_resrv_table(database, table_id):
    select_id = database.execute_query("SELECT id FROM reservations WHERE table_id = ?", (table_id,))
    return select_id

def delete_table(database, table_id):
    database.execute_query("DELETE FROM tables WHERE id = ?", (table_id,))

def select_table_dispo(database, date ,heure):
    select_dispo =database.execute_query(
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
    return select_dispo

def get_reservations(database):
    reservation = database.execute_query(
        """
        SELECT R.id, R.date, R.heure, R.nombre_personne, C.id, C.prenom, C.nom, T.id, T.numero
        FROM reservations AS R
        JOIN clients AS C ON R.client_id = C.id
        JOIN tables AS T ON R.table_id = T.id
        """
    )
    return reservation

def add_reservation(database, client_id, date, heure, table_id, nombre_personne):
    database.execute_query(
        "INSERT INTO reservations (client_id, date, heure, table_id, nombre_personne) VALUES (?, ?, ?, ?, ?)",
        (client_id, date, heure, table_id, nombre_personne)
    )

def delete_reservation(database, reservation_id):
    database.execute_query("DELETE FROM reservations WHERE id = ?", (reservation_id,))

def delete_commande_of_reservation(database, reservation_id):
    database.execute_query("DELETE FROM commandes WHERE reserv_id = ?", (reservation_id,))

def modify_reservation(database, table_id, nombre_personnes, nouvelle_date, nouvelle_heure, reservation_id):
    database.execute_query(
        "UPDATE reservations SET table_id = ?, nombre_personne = ?, date = ?, heure = ? WHERE id = ?",
        (table_id, nombre_personnes, nouvelle_date, nouvelle_heure, reservation_id)
    )

def get_plat(database):
    plats_data = database.execute_query("SELECT id, nom, prix FROM menu")
    return plats_data

def add_plat(database, nom, prix):
    database.execute_query("INSERT INTO menu (nom, prix) VALUES (?, ?)", (nom, prix))

def delete_plat(database, plat_id):
    database.execute_query("DELETE FROM menu WHERE id = ?", (plat_id,))

def modify_plat(database, nouveau_nom, nouveau_prix, plat_id):
    database.execute_query(
        "UPDATE menu SET nom = ?, prix = ? WHERE id = ?",
        (nouveau_nom, nouveau_prix, plat_id)
    )

def add_commande(database, reservation_id, table_id, plat_id, quantite):
    database.execute_query(
        "INSERT INTO commandes (reserv_id, table_id, plat_id, quantite) VALUES (?, ?, ?, ?)",
        (reservation_id, table_id, plat_id, quantite)
    )

def get_commandes(database, reservation_id):
    commandes_data = database.execute_query(
        """
        SELECT C.id, M.nom, C.quantite, M.prix
        FROM commandes AS C
        JOIN menu AS M ON C.plat_id = M.id
        WHERE C.reserv_id = ?
        """,
        (reservation_id,)
    )
    return commandes_data

def modify_commande(database, nouveau_plat_id, nouvelle_quantite, commande_id):
    database.execute_query(
        "UPDATE commandes SET plat_id = ?, quantite = ? WHERE id = ?",
        (nouveau_plat_id, nouvelle_quantite, commande_id)
    )

def delete_commande(database, commande_id):
    database.execute_query("DELETE FROM commandes WHERE id = ?", (commande_id,))

def select_commande_via_reservation(database, reservation_id):
    table_id = database.execute_query("SELECT table_id FROM reservations WHERE id = ?", (reservation_id,))
    return table_id