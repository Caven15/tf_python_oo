class Electrique:
	
	def definir(self, autonomie_km):
		self.autonomie_km = autonomie_km
		return f"Mode éléctrique défini (autonomie : {autonomie_km} Km)"

	def charger(self):
		return f"Charge en cours... autonomie restante : {self.autonomie_km}"