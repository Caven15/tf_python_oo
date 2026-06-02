from .voiture import Voiture
from .electrique import Electrique

class VoitureElectrique(Voiture, Electrique):

	#region Attributs
	def definir(self, marque, modele, couleur, annee, kilometrage, autonomie_km):
		"""
		Méthode pour initialiser les attributs (remplace le constructeur)
		"""
		Voiture.definir(self, marque, modele, couleur, annee, kilometrage)
		Electrique.definir(self, autonomie_km)
		return f"Véhicule {marque} {modele} défini"
	#endregion

	#region Methodes
	def demarrer(self):
		resultat = "Voiture électrique :\n"
		resultat += "=> Mode silencieux\n"
		resultat += super().demarrer() + "\n"
		return resultat
	#endregion