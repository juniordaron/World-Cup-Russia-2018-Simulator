from equipo import Equipo

class Grupo():
	def __init__(self, group, teams):
		super(Grupo, self).__init__()
		self.group=group
		self.team1 = {"nombre" : teams[0].pais, "goles" : 0, "win" : 0, "draw" : 0, "lose" : 0, "puntos" : 0, "objeto" : teams[0]}
		self.team2 = {"nombre" : teams[1].pais, "goles" : 0, "win" : 0, "draw" : 0, "lose" : 0, "puntos" : 0, "objeto" : teams[1]}
		self.team3 = {"nombre" : teams[2].pais, "goles" : 0, "win" : 0, "draw" : 0, "lose" : 0, "puntos" : 0, "objeto" : teams[2]}
		self.team4 = {"nombre" : teams[3].pais, "goles" : 0, "win" : 0, "draw" : 0, "lose" : 0, "puntos" : 0, "objeto" : teams[3]}
		self.tabla = {1:self.team1,2:self.team2,3:self.team3,4:self.team4}
#Simulacion de tablas de grupo, con nombre, goles, victorias, derrotas y empates.

#Actualiza las estadísticas del equipo en el grupo dependiendo del resutado.
#w: victoria suma 3 puntos
#d: empate suma un punto
#l: derrota no suma puntos"""
	def posicionar(self, pais, goles, resultado):
		for pos in self.tabla:
			team = self.tabla[pos]
			if team["nombre"] == pais:
				team["goles"]+= goles
				if resultado == 'w':
					team["win"] += 1
					team["puntos"] += 3
				elif resultado == 'd':
					team["draw"] += 1
					team["puntos"] += 1
				else:
					team["lose"] += 1

#Recupera el primer y segundo clasificado para la siguiente ronda.
#La clasificacion se determina por los puntos obtenidos durante los tres partidos.
#En caso de empate en puntos, el desempate se determina por la cantidad de goles."""
	def clasificados(self):
		lis = []
		for pos in self.tabla:
			team = self.tabla[pos]
			lis.append((team["puntos"], team["goles"]))
		lis.sort()
		clas={}
		for pos in self.tabla:
			team = self.tabla[pos]
			if lis[3][0] == team["puntos"] and lis[3][1] == team["goles"]:
				clas[1]=(lis[3][0], lis[3][1], team["objeto"])
			if lis[2][0] == team["puntos"] and lis[2][1] == team["goles"]:
				clas[2]=(lis[2][0], lis[2][1], team["objeto"])
		return clas


