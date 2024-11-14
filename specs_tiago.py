class Table:
    """
    Représente une table dans un restaurant avec un numéro d'identification unique
    et un nombre de places disponibles.

    Parameters:
        number_table (int): Le numéro d'identification de la table.
        number_places (int): Le nombre de places disponibles à la table.
    """
    def __init__(self, number_table: int, number_places: int):
        """
        Initialise une instance de la classe Table.

        Parameters:
            number_table (int): Le numéro d'identification de la table.
            number_places (int): Le nombre de places disponibles à la table.
        """
        pass

    def create_table(self) -> dict:
        """
        Crée une représentation de la table qui sera enregistrée dans une base de données.

        Returns:
            dict: Un dictionnaire contenant les informations de la table à enregistrer.

        Raises:
            Exception: Si la table existe déjà dans la base de données.
        """
        pass

    def delete_table(self):
        """
        Supprime la table de la base de données associée.

        Raises:
            Exception: Si la table n'existe pas dans la base de données.
        """
        pass

    def is_available(self) -> bool:
        """
        Vérifie si la table est disponible.

        Returns:
            bool: True si la table est disponible, False sinon.

        Raises:
            Exception: Si la table n'existe pas dans la base de données.
        """
        pass


class Order:
    """
    Représente une commande passée dans un restaurant.

    Parameters:
        number_order (int): Le numéro de la commande.
        status (str): Le statut de la commande (ex: 'en cours', 'terminée').
    """
    def __init__(self, number_order: int, status: str):
        """
        Initialise une instance de la classe Order.

        Parameters:
            number_order (int): Le numéro d'identification de la commande.
            status (str): Le statut de la commande.
        """
        pass

    def add_plat(self, plat: str) -> dict:
        """
        Ajoute un plat à la commande.

        Parameters:
            plat (str): Le nom du plat à ajouter se trouvant dans la DB des plats.

        Returns:
            dict: Un dictionnaire mis à jour avec les informations de la commande incluant le plat ajouté.

        Raises:
            Exception: Si le plat n'existe pas dans la classe Plats.
        """
        pass

    def delete_plat(self, plat: str):
        """
        Supprime un plat de la commande.

        Parameters:
            plat (str): Le nom du plat à supprimer.

        Raises:
            Exception: Si le plat n'existe pas dans la commande.
        """
        pass

    def modify_plat(self, plat: str) -> dict:
        """
        Modifie un plat de la commande en fonction des préférences du client.

        Parameters:
            plat (str): Le nom du plat à modifier se trouvant dans la DB des plats..

        Returns:
            dict: Un dictionnaire mis à jour avec les informations de la commande incluant le plat modifié.

        Raises:
            Exception: Si le plat n'existe pas dans la commande.
        """
        pass


class Plat():
    pass
