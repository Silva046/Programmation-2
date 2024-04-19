#TP2 par ........

import time
if __name__ == '__main__' : from Composantes import *
else :                      from .Composantes import *


class SousReseau:
    def __init__(self, _nom:str, _ls_composantes:list[Composante]):
        self._nom = _nom
        self._ls_composantes = self._ls_composantes

    @property 
    def nom(self):
        return self._nom
    @property 
    def ls_composantes(self):
        return self._ls_composantes
    
    @staticmethod
    def ping(self):
        try: 
            sb.check_output( ['ping', '-n', '1', str(self.adresse_ip.valeur)], stderr=sb.STDOUT )
            return True
        except sb.CalledProcessError: 
            return False
        
    def get_composante_par_ip(self, adresse_ip_composante:str):
        composante:Composante
        for composante in self._ls_composantes:
            if adresse_ip_composante == str(composante.adresse_ip):
                return composante
        else: return None

    def ajouter_composante(self, composante_add:Composante):
        if composante_add in self._ls_composantes:
            self._ls_composantes.append(composante_add)
        else: return print("Ce composant est déjà dans la liste")

    def supprimer_composante(self, composante_remove):
        if composante_remove in self._ls_composantes:
            self._ls_composantes.remove(composante_remove)
        else: return print("le composant que vous voulez supprimer n'éxiste pas")

class Gestionnaire:
    def __init__(self,_nom,_reseau:SousReseau = None):
        self._nom = _nom
        self._reseau = _reseau

    @property
    def nom(self):
        return self._nom
    @property
    def reseau(self):
        return self._reseau
    
    def tester_connexion(self, composante_test_connexion:Composante):
        resultat_ping = composante_test_connexion.ping()
        return print(f"{composante_test_connexion.nom} : {resultat_ping}")

    def tester_connexion(self):
        pass
    def redemarrer_station(self):
        pass
    def tester_toutes_les_connexions(self):
        pass


if __name__ == "__main__" :
    pass