from models import Voiture, VoitureElectrique

def main():
	voiture = Voiture()
	voiture_electrique = VoitureElectrique()

	voiture.definir("Honda", "Civic", "Noir", 2006, 86452)
	voiture_electrique.definir("Porsche", "Carerra", "Jaune", 2006, 26748,50)

	print("-" * 50)

	print(voiture_electrique.afficher_info())
	print(voiture_electrique.demarrer())
	print(voiture_electrique.charger())

	print("-" * 50)

if __name__ == "__main__":
	main()