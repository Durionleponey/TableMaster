class client:
    def __init__(self, lname, fname, phone_number):
        """
            Retourne une chaine de caractère dans un fichier JSON (DATABASE).

                    Parameters:
                        lname (str) : Une chaine de caractère avec le nom de famille du client
                        fname (str) : Une chaine de caractère avec le prénom du client
                        phone_number (str) : une chaine de caractère avec le numéro du client
                    Returns:
                         Le compte du client au format dictionnaire pour l'instant au format JSON ==> (DATABASE)
        """
        self.lname = lname
        self.fname = fname
        self.phone_number = phone_number

    def create_client(self, lname: str, fname: str, phone_number: str) -> str:
        """
        Retourne la création du client sur un fichier JSON

        Parameters:
                        lname (str) : Une chaine de caractère avec le nom de famille du client
                        fname (str) : Une chaine de caractère avec le prénom du client
                        phone_number (str) : une chaine de caractère avec le numéro du client
                    Returns:
                        Le compte du client au format dictionnaire pour l'instant au format JSON ==> (DATABASE)
        """
        pass
        user_account = {
            lname: "",
            fname: "",
            phone_number: ""
        }
        return user_account

    def remove_reserv(self, lname: str, fname: str, phone_number: str) -> str:
        """
        Permet la suppression du client
        """
        pass

    def modify_client(self, lname: str, fname: str, phone_number: str) -> str:
        """
        Permet la modification d'informations du client sur un fichier JSON

            Parameters:
                        lname (str) : Une chaine de caractère avec le nom de famille du client
                        fname (str) : Une chaine de caractère avec le prénom du client
                        phone_number (str) : une chaine de caractère avec le numéro du client
            Returns:
                un dictionnaire contenant les informations modifiées.
        """
        pass
        user_modify = {
            lname: "",
            fname: "",
            phone_number: ""
        }
        return user_modify


class reservation:
    def __init__(self, date: date, nbrepeople: int, hours: int, statut: bool, client: dict):
        self.date = date
        self.nbrepeople = nbrepeople
        self.hours = hours
        self.statut = statut
        self.client = client
        """
        Permet la réservation d'une table du restaurant
        
            Parameters:
                date (date) : Est la date à laquelle le client réserve la table
                nbrepeople (int) : Nombre de personnes de la table
                hours (int) : l'heure à laquelle la table sera réservée
                statut (bool ) : Si la table est disponible ou non 
                client (dict) : dictionnaire avec les informations du client
                
            Returns:
                un fichier Json (par la suite ==> DATABASE) au format disctionnaire avec les informations données et changement du statut en false 
        """

    def confirm(self, date: date, nbrepeople: int, hours: int, statut: bool, client: dict):
        pass
        """
        Permet la confirmation de la réservation d'une table 
         
        Parameters:
                date (date) : Est la date à laquelle le client réserve la table
                nbrepeople (int) : Nombre de personnes de la table
                hours (int) : l'heure à laquelle la table sera réservée
                statut (bool ) : Si la table est disponible ou non 
                client (dict) : dictionnaire avec les informations du client
                
            Returns:
                un fichier Json (par la suite ==> DATABASE) au format disctionnaire avec les informations données et changement du statut en False
        """

    def cancel(self, date: date, nbrepeople: int, hours: int, statut: bool, client: dict):
        pass

    """
    Permet l'annulation d'une table 
    
         Parameters:
                date (date) : Est la date à laquelle le client réserve la table
                nbrepeople (int) : Nombre de personnes de la table
                hours (int) : l'heure à laquelle la table sera réservée
                statut (bool ) : Si la table est disponible ou non 
                client (dict) : dictionnaire avec les informations du client
                
        Returns:
                Le fichier JSON (par la suite ==> DATABASE) mis à jour avec la suppression de la table et le changement du statut en True
    """

    def modify(self, date: date, nbrepeople: int, hours: int, statut: bool, client: dict):
        pass

    """
    Permet la modification d'informations de la réservation 
    
    Parameters:
                date (date) : Est la date à laquelle le client réserve la table
                nbrepeople (int) : Nombre de personnes de la table
                hours (int) : l'heure à laquelle la table sera réservée
                statut (bool ) : Si la table est disponible ou non 
                client (dict) : dictionnaire avec les informations du client
                
            Returns:
                un fichier Json (par la suite ==> DATABASE) au format disctionnaire avec les informations données et changement du statut en False
    """
