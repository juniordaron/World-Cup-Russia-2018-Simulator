from equipo import Equipo
from partido import Partido
from grupo import Grupo
from multiprocessing import Process
import threading
from blessings import Terminal

#Instancia de terminal para visualizacion grafica.
t=Terminal()

#Actualiza las estadisticas de los equipos en el grupo despues de un partido.
def _posicionar(resultado, grupo):
	#resultado es una tupla con dos elementos.
	#cada elemento tiene pais, goles y resultado del partido.
	#resultado es w: victoria, d: empate, l:derrota
	if grupo == 'A':
		grupoA.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoA.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'B':
		grupoB.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoB.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'C':
		grupoC.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoC.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'D':
		grupoD.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoD.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'E':
		grupoE.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoE.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'F':
		grupoF.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoF.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'G':
		grupoG.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoG.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])
	if grupo == 'H':
		grupoH.posicionar(resultado[0][0], resultado[0][1], resultado[0][2])
		grupoH.posicionar(resultado[1][0], resultado[1][1], resultado[1][2])

#Secuencia de juegos de la fae de grupos.
def fase_grupos(equipos, fase, strong):
	_iniciar_ronda(strong)
	juego1 = Partido(equipos[0], equipos[1], "fecha", fase,1)
	juego2 = Partido(equipos[2], equipos[3], "fecha", fase,3)
	juego3 = Partido(equipos[4], equipos[5], "fecha", fase,5)
	juego4 = Partido(equipos[6], equipos[7], "fecha", fase,7)

	#Hilos para los partidos.
	thread_grupos_1=threading.Thread(name= 'hilogrupo1', target=juego1.iniciar_partido)
	thread_grupos_2=threading.Thread(name= 'hilogrupo2', target=juego2.iniciar_partido)
	thread_grupos_3=threading.Thread(name= 'hilogrupo3', target=juego3.iniciar_partido)
	thread_grupos_4=threading.Thread(name= 'hilogrupo4', target=juego4.iniciar_partido)
	thread_grupos_1.start()
	thread_grupos_2.start()
	thread_grupos_3.start()
	thread_grupos_4.start()
	thread_grupos_1.join()
	thread_grupos_2.join()
	thread_grupos_3.join()
	thread_grupos_4.join()

	#Hilos para los resultados.
	thread_winners_1=threading.Thread(name= 'hiloposgrupo1', target=_posicionar, args=(juego1.resultado(), equipos[0].grupo))
	thread_winners_2=threading.Thread(name= 'hiloposgrupo2', target=_posicionar, args=(juego2.resultado(), equipos[2].grupo))
	thread_winners_3=threading.Thread(name= 'hiloposgrupo3', target=_posicionar, args=(juego3.resultado(), equipos[4].grupo))
	thread_winners_4=threading.Thread(name= 'hiloposgrupo4', target=_posicionar, args=(juego4.resultado(), equipos[6].grupo))
	thread_winners_1.start()
	thread_winners_2.start()
	thread_winners_3.start()
	thread_winners_4.start()
	thread_winners_1.join()
	thread_winners_2.join()
	thread_winners_3.join()
	thread_winners_4.join()

	#Pausa.
	input()

#Secuencia de juegos de octavos y cuartos de final.
def knockout(equipos, fase, strong):
	_iniciar_ronda(strong)
	juego1 = Partido(equipos[0][0], equipos[0][1], "fecha", fase,1)
	juego2 = Partido(equipos[1][0], equipos[1][1], "fecha", fase,3)
	juego3 = Partido(equipos[2][0], equipos[2][1], "fecha", fase,5)
	juego4 = Partido(equipos[3][0], equipos[3][1], "fecha", fase,7)

	#Hilos para los partidos.
	thread_grupos_1=threading.Thread(name= 'hilogrupo1', target=juego1.iniciar_partido)
	thread_grupos_2=threading.Thread(name= 'hilogrupo2', target=juego2.iniciar_partido)
	thread_grupos_3=threading.Thread(name= 'hilogrupo3', target=juego3.iniciar_partido)
	thread_grupos_4=threading.Thread(name= 'hilogrupo4', target=juego4.iniciar_partido)
	thread_grupos_1.start()
	thread_grupos_2.start()
	thread_grupos_3.start()
	thread_grupos_4.start()
	thread_grupos_1.join()
	thread_grupos_2.join()
	thread_grupos_3.join()
	thread_grupos_4.join()

	#Ganadores de los partidos
	ganadores.append(juego1.winner())
	ganadores.append(juego2.winner())
	ganadores.append(juego3.winner())
	ganadores.append(juego4.winner())
	
	#Pausa.
	input()

#Secuencia de juegos de semifinal.
def semifinal(equipos, fase, strong):
	_iniciar_ronda(strong)
	juego1 = Partido(equipos[0][0], equipos[0][1], "fecha", fase,1)
	juego2 = Partido(equipos[1][0], equipos[1][1], "fecha", fase,3)
	
	#Hilos para los partidos.
	thread_grupos_1=threading.Thread(name= 'hilogrupo1', target=juego1.iniciar_partido)
	thread_grupos_2=threading.Thread(name= 'hilogrupo2', target=juego2.iniciar_partido)
	thread_grupos_1.start()
	thread_grupos_2.start()
	thread_grupos_1.join()
	thread_grupos_2.join()
	
	#Ganadores.
	ganadores.append(juego1.winner())
	ganadores.append(juego2.winner())
	
	#Pausa.
	input()

#Secuencia de juego final.
def final(equipos, fase,strong):
	_iniciar_ronda(strong)
	juego1 = Partido(equipos[0][0], equipos[0][1], "fecha", fase,1)
	thread_grupos_1=threading.Thread(name= 'hilogrupo1', target=juego1.iniciar_partido)
	thread_grupos_1.start()
	thread_grupos_1.join()
	ganadores.append(juego1.winner())

#Limpiar la pantalla tras cada ronda.
def _iniciar_ronda(strong):
	with t.location(0,2):
		print(t.clear(),strong)
		print("El asterisco (*) indica el equipo que posee la pelota.")

#Determina los cruces de octavos.
def octavos( A, B, C, D, E, F , G, H):
		o =((A[1][2], B[2][2]), (C[1][2], D[2][2]),
			(E[1][2], F[2][2]), (G[1][2], H[2][2]),
			(A[2][2], B[1][2]), (C[2][2], D[1][2]),
			(E[2][2], F[1][2]), (G[2][2], H[1][2]))
		return o


#Creacion de los equipos con su nombre, ranking, formacion y grupo.
ARG = Equipo("Argentina", 5, "4-3-3","D")
AUS = Equipo("Australia", 36, "4-4-2", "C")
BEL = Equipo("Bélgica", 3, "4-3-3", "G")
BRA = Equipo("Brasil", 2, "4-3-3", "E")
COL = Equipo("Colombia", 16, "4-3-3", "H")
CRC = Equipo("Costa Rica", 23, "4-3-3", "E")
CRO = Equipo("Croacia", 20, "4-4-2", "D")
DEN = Equipo("Dinamarca", 12, "4-4-2", "C")
EGY = Equipo("Egipto", 45, "4-2-3-1", "A")
ENG = Equipo("Inglaterra", 13, "4-4-2", "G")
FRA = Equipo("Francia", 7, "4-3-3", "C")
GER = Equipo("Alemania", 1, "4-3-3", "F")
IRN = Equipo("Irán", 37, "4-5-1", "B")
ISL = Equipo("Islandia", 22, "4-5-1", "D")
JPN = Equipo("Japón", 61, "4-4-2", "H")
KOR = Equipo("Corea", 57, "4-4-2", "F")
MEX = Equipo("México", 15, "4-3-3", "F")
MOR = Equipo("Marruecos", 41, "5-3-2", "B")
NIG = Equipo("Nigeria", 48, "4-2-3-1", "D")
PAN = Equipo("Panamá", 55, "4-5-1", "G")
PER = Equipo("Perú", 11, "4-4-2", "C")
POL = Equipo("Polonia", 8, "4-3-2-1", "H")
POR = Equipo("Portugal", 4, "4-5-1", "B")
RUS = Equipo("Rusia", 70, "4-4-2", "A")
SAU = Equipo("A. Saudita", 67, "4-4-2", "A")
SEN = Equipo("Senegal", 27, "4-3-3", "H")
SPA = Equipo("España", 10, "4-1-3-2", "B")
SRB = Equipo("Serbia", 34, "4-2-2", "E")
SWE = Equipo("Suecia", 24, "4-4-2", "F")
SWI = Equipo("Suiza", 6, "4-3-3", "E")
TUN = Equipo("Túnez", 21, "4-4-2", "G")
URU = Equipo("Uruguay", 14, "4-3-3", "A")

#Creacion de grupos para la primera fase.
grupoA = Grupo('A', (RUS, SAU, URU, EGY))
grupoB = Grupo('B', (IRN, SPA, POR, MOR))
grupoC = Grupo('C', (FRA, AUS, PER, DEN))
grupoD = Grupo('D', (ARG, ISL, CRO, NIG))
grupoE = Grupo('E', (CRC, SRB, SWI, BRA))
grupoF = Grupo('F', (GER, MEX, SWE, KOR))
grupoG = Grupo('G', (BEL, PAN, TUN, ENG))
grupoH = Grupo('H', (POL, SEN, JPN, COL))

#AQUI INICIA LA SECUENCIA DE EJECUCION

#RONDA 1
Equipos = (RUS, SAU, EGY, URU, MOR, IRN, POR, SPA)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 1 GRUPOS A Y B")
Equipos = (FRA, AUS, ARG, ISL, PER, DEN, CRO, NIG)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 1 GRUPOS C Y D")
Equipos = (CRC, SRB, GER, MEX, BRA, SWI, SWE, KOR)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 1 GRUPOS E Y F")
Equipos = (BEL, PAN, TUN, ENG, COL, JPN, POL, SEN)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 1 GRUPOS H Y G")
#RONDA 2
Equipos = (RUS, EGY, POR, MOR, URU, SAU, IRN, SPA)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 2 GRUPOS A Y B")
Equipos = (DEN, AUS, FRA, PER, ARG, CRO, BRA, CRC)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 2 GRUPOS C, D Y E")
Equipos = (NIG, ISL, SRB, SWI, BEL, TUN, KOR, MEX)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 2 GRUPOS D, E, F Y G")
Equipos = (GER, SWE, ENG, PAN, JPN, SEN, POL, COL)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 2 GRUPOS F, G Y H")
#RONDA 3
Equipos = (SAU, EGY, URU, RUS, IRN, POR, SPA, MOR)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 3 GRUPOS A Y B")
Equipos = (AUS, PER, DEN, FRA, ISL, CRO, NIG, ARG)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 3 GRUPOS C Y D")
Equipos = (MEX, SWE, KOR, GER, SRB, BRA, SWI, CRC)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 3 GRUPOS E Y F")
Equipos = (JPN, POL, SEN, COL, ENG, BEL, PAN, TUN)
fase_grupos(Equipos, "Grupos", "Fase de grupo: RONDA 3 GRUPOS G Y H")

#CLASIFICADOS A OCTAVOS DE FINAL

A = grupoA.clasificados()
B = grupoB.clasificados()
C = grupoC.clasificados()
D = grupoD.clasificados()
E = grupoE.clasificados()
F = grupoF.clasificados()
G = grupoG.clasificados()
H = grupoH.clasificados()

print(t.move(15,0), "--Puntos--Goles--Clasificados a octavos")
print("1A:",A[1][0],"     ",A[1][1], "  ", A[1][2].pais)
print("2A:",A[2][0],"     ",A[2][1], "  ", A[2][2].pais)
print("1B:",B[1][0],"     ",B[1][1], "  ", B[1][2].pais)
print("2B:",B[2][0],"     ",B[2][1], "  ", B[2][2].pais)
print("1C:",C[1][0],"     ",C[1][1], "  ", C[1][2].pais)
print("2C:",C[2][0],"     ",C[2][1], "  ", C[2][2].pais)
print("1D:",D[1][0],"     ",D[1][1], "  ", D[1][2].pais)
print("2D:",D[2][0],"     ",D[2][1], "  ", D[2][2].pais)
print("1E:",E[1][0],"     ",E[1][1], "  ", E[1][2].pais)
print("2E:",E[2][0],"     ",E[2][1], "  ", E[2][2].pais)
print("1F:",F[1][0],"     ",F[1][1], "  ", F[1][2].pais)
print("2F:",F[2][0],"     ",F[2][1], "  ", F[2][2].pais)
print("1G:",G[1][0],"     ",G[1][1], "  ", G[1][2].pais)
print("2G:",G[2][0],"     ",G[2][1], "  ", G[2][2].pais)
print("1H:",H[1][0],"     ",H[1][1], "  ", H[1][2].pais)
print("2H:",H[2][0],"     ",H[2][1], "  ", H[2][2].pais)
input()

#Cruces de octavos de final.
o = octavos(A,B,C,D,E,F,G,H)
ganadores = []
equi=[]
equip=[]
for i in range(0,4):
	equi.append(o[i])
	equip.append(o[i+4])
knockout(equi,"Octavos", "Octavos de Final Parte 1")
knockout(equip, "Octavos", "Octavos de Final Parte 2")

#Clasificados a cuartos de final.
print(t.move(15,0),"Clasificados a cuartos")
for i in range(0,8):
	print(ganadores[i].pais)
equi.clear()

#Cruces de cuartos de final.
for i in range(0,8,2):
	equi.append((ganadores[i],ganadores[i+1]))
ganadores.clear()
input()
knockout(equi,"Cuartos","Cuartos de Final")

#Clasificados a semifinal
print(t.move(15,0),"Clasificados a semifinal")
for i in range(0,4):
	print(ganadores[i].pais)
equi.clear()

#Cruces de semifinal
for i in range(0,4,2):
	equi.append((ganadores[i], ganadores[i+1]))
ganadores.clear()
input()
semifinal(equi, "Semifinal", "SEMIFINAL")

#Clasificados a la final.
print(t.move(15,0),"Finalistas")
for i in range(0,2):
	print(ganadores[i].pais)
input()
equi.clear()
equi.append((ganadores[0], ganadores[1]))
ganadores.clear()

#Final.
final(equi,"LA GRAN FINAL","LA GRAN FINAL")
print(t.move(14,0),"CAMPEÓN:   ", ganadores[0].pais)
