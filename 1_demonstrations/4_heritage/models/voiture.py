from .vehicule import Vehicule

class Voiture(Vehicule):
	"""
	Classe Voiture
	"""
	
	#region Attributs
	nombre_voitures = 0 		# Attribut de classe

	def definir(self, marque, modele, couleur, annee, kilometrage):
		"""
		Méthode pour initialiser les attributs (remplace le constructeur)
		"""
		super().definir(marque, modele, annee)
		self._couleur = couleur
		self.kilometrage = kilometrage
		self.est_demarre = False

		Voiture.nombre_voitures += 1

		print("nombre voiture(s) :", Voiture.nombre_voitures)

	#endregion

	#region	Prop's

	@property
	def couleur(self):
		"""
		Getter => lit la couleur
		"""
		return self._couleur

	@couleur.setter
	def couleur(self, nouvelle_couleur):
		if not isinstance(nouvelle_couleur, str):
			raise TypeError("La couleur doit être du texte")
		self._couleur = nouvelle_couleur.capitalize() 
	#endregion

	#region Methodes
	def demarrer(self):
		if not hasattr(self, 'est_demarre'):
			return "[Erreur] Veuillez d'abord définir la voiture avec définir_voiture()"
		if not self.est_demarre:
			self.est_demarre = True
			return super().demarrer()
		return f"[Succès] {self.marque} {self.modele} est déjà démarré !"

	def arreter(self):
		pass

	def rouler(self):
		pass

	def afficher_info(self):
		if not hasattr(self, 'marque'):
			return "voiture non définie."
		resultat = super().afficher_info()
		resultat += f"Couleur : {self.couleur}"
		return resultat

	def __str__(self):
		if hasattr(self, 'marque'):
			return f"{self.marque}"
		return "Voiture (non définie)"
	#endregion
