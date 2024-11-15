#*** Ce code a été réalisé avec GPT4 pour la clarification et l'amélioration des idées.***
class Restaurant:
    def __init__(self, name: str, number_place: int):
        """
        PRE : name est une chaîne de caractères et number_place est un entier positif.
        POST : L'objet Restaurant est créé avec un nom, un nombre de places et une liste vide pour les commandes.
        RAISES : TypeError si name n'est pas une chaîne ou si number_place n'est pas un entier positif.
        """
        if not isinstance(name, str) or not isinstance(number_place, int) or number_place < 0:#c'est mieux de faire avec des isinstance d'après chatgpt c'est plus flexible & expressif
            raise TypeError("name doit être une chaîne de caractères et number_place un entier positif.")

        self.name = name
        self.number_place = number_place
        self.order = []

    def change_table_location(self, table_id: int, new_x: int, new_y: int) -> str:
        """
        PRE : table_id, new_x et new_y sont des entiers.
        POST : Met à jour l'emplacement de la table spécifiée et retourne une confirmation.
        RAISES : ValueError si la table n'existe pas. TypeError si table_id, new_x ou new_y ne sont pas des entiers.
        """

        try:
            notreDataBase.upgradeValue("table", table_id, new_x, new_y)
            notreSalleDeRestaurant.refresh()
            return "Emplacement de la table mis à jour avec succès."
        except:
            raise ValueError("La table spécifiée n'existe pas.")

    def manage_password(self, old_password: str, new_password: str, confirm_new_password: str) -> str:
        """
        PRE : old_password, new_password et confirm_new_password sont des chaînes de caractères.
        POST : Met à jour le mot de passe si les conditions sont remplies et retourne une confirmation.
        RAISES : ValueError si le mot de passe actuel est incorrect ou si les nouveaux mots de passe ne correspondent pas.
                TypeError si les mots de passe ne sont pas des chaînes de caractères.
        """

        if new_password != confirm_new_password:
            raise ValueError("Les nouveaux mots de passe ne correspondent pas.")

        try:
            encrypted_old_password = SHA256.encrypt(old_password)
            if notreDataBase.getValue("EncryptedPasswordTable") != encrypted_old_password:
                raise ValueError("Le mot de passe actuel est incorrect.")

            notreDataBase.upgradeValue("EncryptedPasswordTable", SHA256.encrypt(new_password))
            return "Le mot de passe a été mis à jour avec succès."
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la mise à jour du mot de passe : {e}")


class Serveur:
    def __init__(self, name: str):
        """
        PRE : name est une chaîne de caractères.
        POST : L'objet Serveur est créé avec un nom.
        RAISES : TypeError si name n'est pas une chaîne de caractères.
        """
        if not isinstance(name, str):
            raise TypeError("Le nom du serveur doit être une chaîne de caractères.")

        self.name = name

    def take_command(self, order: dict) -> str:
        """
        PRE : order est un dictionnaire représentant une commande.
        POST : La commande est ajoutée au système de commandes.
        RAISES : ValueError si la commande existe déjà dans le système.
                TypeError si order n'est pas un dictionnaire.
        """
        if not isinstance(order, dict):
            raise TypeError("La commande doit être un dictionnaire.")

        if order in notreRestaurant.order:
            raise ValueError("Cette commande existe déjà dans le système.")

        notreRestaurant.order.append(order)
        return "Commande ajoutée avec succès."

    def delete_command(self, order_id: int) -> str:
        """
        PRE : order_id est un entier représentant l'identifiant d'une commande.
        POST : La commande correspondante est supprimée du système de commandes.
        RAISES : ValueError si la commande n'existe pas dans le système.
                TypeError si order_id n'est pas un entier.
        """
        if not isinstance(order_id, int):
            raise TypeError("L'identifiant de la commande doit être un entier.")

        try:
            notreRestaurant.order.remove(order_id)
            return "Commande supprimée avec succès."
        except:
            raise TypeError("Erreur lors de la suppression.")



