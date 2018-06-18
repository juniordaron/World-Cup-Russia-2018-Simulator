from equipo import Equipo
import configuracion
import random
import threading
from blessings import Terminal
from time import sleep

class Partido():
#Semaforo para la consola.
	semaforo_terminal = threading.Lock()
	ter= Terminal()

#Actualizar la pantalla.
	def _limpiar_pantalla():
		Partido.semaforo_terminal.acquire()
		Partido.ter.clear()
		Partido.semaforo_terminal.release()

	def __init__(self, equipoA, equipoB, fecha, fase, pos):
		super(Partido, self).__init__()
		#Parametros de entrada: equipos a disputar el partido, fecha, fase del torneo.
		self.fecha=fecha;
		self.fase=fase;
		self.equipos=[equipoA,equipoB]
		#Booleano para verificar si el partido termino.
		self.terminado=False
		#Estadisticas del partido.
		self.pases_exitosos=[0,0]
		self.goles=[0,0]
		self.chutes=[0,0]
		self.tiempo_en_segundos=[0,0]
		self.DURACION_EN_SEGUNDOS=90*60
		self.tiempo_extra=0
		#Velocidad de ejecucion de los partidos
		self.speed = configuracion.SPEED
		#Sortea el equipo que iniciara con la posesion del balon
		random.shuffle(self.equipos)
		#Inicio de semaforos
		self.posesionA= threading.Lock()
		self.posesionB= threading.Lock()
		self.posesionB.acquire()
		self.posesionA.acquire()
		self.posesion=0;
		#Visualizacion grafica
		self.pos=pos+2
		self.prorr=False
		self.penal=False

#Funciones para calcular el tiempo del partido.
	def _tiempo_total(self):
		return sum(self.tiempo_en_segundos)

	def _suficiente_tiempo(self,tiempo):
		return self._tiempo_total()+tiempo<self.DURACION_EN_SEGUNDOS+self.tiempo_extra

	def _duracion_pase(self):
		return 40+random.uniform(-15,15)

	def _duracion_chute(self):
		return 60 + random.uniform(-20,20)

#Determina el equipo que va ganando el partido.
	def _va_ganando(self):
		if self.goles[0]==self.goles[1]:
			return None
		elif self.goles[0]>self.goles[1]:
			return self.equipos[0]
		else:
			return self.equipos[1]

#Determina el equipo ganador del partido.
	def _definir_ganadores(self):
        #Si el partido no es de fase de grupos, y se culmian con empate, se juega prorroga.
		if self.fase!="Grupos" and self._va_ganando()==None:
			self.prorr=True
			self._imprimir_estado()
			self._prorroga()
			#Si el empate persiste, se simula una ejecucion de penales sorteando un numero para decidir el ganador.
			if self._va_ganando()==None:
				self.penal=True
				self._imprimir_estado()
				i=random.randint(0,1)
				self.goles[i]+=1
				self._imprimir_estado()
				
		#Se determina el ganador.
		self.ganador=self._va_ganando()

#Recupera el resultado del partido para la clasificacion en la fase de grupos.
#w: victoria, d: empate, l:derrota"""
	def resultado(self):
		if self.ganador == self.equipos[0]:
			res1 = (self.equipos[0].pais, self.goles[0], 'w')
			res2 = (self.equipos[1].pais, self.goles[1], 'l')
		elif self.ganador == self.equipos[1]:
			res1 = (self.equipos[0].pais, self.goles[0], 'l')
			res2 = (self.equipos[1].pais, self.goles[1], 'w')
		else:
			res1 = (self.equipos[0].pais, self.goles[0], 'd')
			res2 = (self.equipos[1].pais, self.goles[1], 'd')
		result = (res1,res2)
		return result

#Recupera el equipo ganador del partido.
	def winner(self):
		if self.ganador == self.equipos[0]:
			win = self.equipos[0]
		else:
			win = self.equipos[1]
		return win

#Region critica: Los equipos compiten por la posesion del balon.
	def iniciar_partido(self):
		#Se libera el semaforo.
		self.posesionA.release()
		#Se crean los hilos.
		self.thread_A = threading.Thread(name = 'hiloA', target = self.atacar_equipoA)
		self.thread_B = threading.Thread(name = 'hiloB', target = self.atacar_equipoB)
		#Se ejecutan los hilos.
		self.thread_A.start()
		self.thread_B.start()
		#Se espera que termine su ejecucion.
		self.thread_A.join()
		self.thread_B.join()

		self._definir_ganadores()

#Region critica: extension de iniciar_partido en caso que deba jugar una prorroga.
	def _prorroga(self):
		#Se agrega el tiempo extra.
		self.tiempo_extra=30*60
		self.terminado=False
		#Se crean los hilos.
		self.thread_prorroga_A=threading.Thread(name= 'hiloProA', target=self.atacar_equipoA)
		self.thread_prorroga_B=threading.Thread(name= 'hiloProB', target=self.atacar_equipoB)
		#Se ejecutan los hilos de prorroga.
		self.thread_prorroga_A.start()
		self.thread_prorroga_B.start()
		#Se espera que termine su ejecucion.
		self.thread_prorroga_A.join()
		self.thread_prorroga_B.join()

#Secuencia de juego del equipo A.
	def atacar_equipoA(self):
		#Mientras el juego no termine se pide el semaforo.
		while not self.terminado:
			self.posesionA.acquire()
			self.posesion=0
			#Se retornan la cantidad de goles y pases realizados.
			(pases,gol)=self.equipos[0].atacar(self.equipos[1].probabilidad["encajar"])
			#Calculo de tiempo de pases.
			for x in range(1,pases):
				sleep(self.speed)
				duracion_del_pase= self._duracion_pase()
								
				if self._suficiente_tiempo(duracion_del_pase):
					self.tiempo_en_segundos[0]+=duracion_del_pase
					self.pases_exitosos[0]+=1
					
				else:
					self.tiempo_en_segundos[0]+ self.DURACION_EN_SEGUNDOS-self.tiempo_en_segundos[1]
					self.terminado=True
					break
				self._imprimir_estado()
			#Calculo del tiempo de goles.
			if pases==4:
				sleep(self.speed)
				duracion_del_chute= self._duracion_chute()
				if self._suficiente_tiempo(duracion_del_chute):
					self.tiempo_en_segundos[0]+=duracion_del_chute
					self.chutes[0]+=1
					if gol:
						self.goles[0]+=1
				else:
					self.tiempo_en_segundos[0]+ self.DURACION_EN_SEGUNDOS-self.tiempo_en_segundos[1]
					self.terminado=True
				self._imprimir_estado()
			#Se libera el semaforo.
			self.posesionB.release()

#Secuencia de juego del equipo A.
	def atacar_equipoB(self):
		#Mientras el juego no termine se pide el semaforo.
		while not self.terminado:
			#### pide el semaforo aqui
			self.posesionB.acquire()
			#pedir sem
			self.posesion=1
			#Se retornan la cantidad de goles y pases realizados.
			(pases,gol)=self.equipos[1].atacar(self.equipos[0].probabilidad["encajar"])
			#Calculo de tiempo de pases.
			for x in range(1,pases):
				sleep(self.speed)
				duracion_del_pase= self._duracion_pase()
				if self._suficiente_tiempo(duracion_del_pase):
					self.tiempo_en_segundos[1]+=duracion_del_pase
					self.pases_exitosos[1]+=1
				else:
					self.tiempo_en_segundos[1]+ self.DURACION_EN_SEGUNDOS-self.tiempo_en_segundos[0]
					self.terminado=True
					break
				self._imprimir_estado()
			#Calculo del tiempo de goles.
			if pases==4:
				sleep(self.speed)
				duracion_del_chute= self._duracion_chute()
				if self._suficiente_tiempo(duracion_del_chute):
					self.tiempo_en_segundos[1]+=duracion_del_chute
					self.chutes[1]+=1
					if gol:
						self.goles[1]+=1
				else:
					self.tiempo_en_segundos[1]+ self.DURACION_EN_SEGUNDOS-self.tiempo_en_segundos[0]
					self.terminado=True
				self._imprimir_estado()
			#Se libera el semaforo.
			self.posesionA.release()

#Visualizacion grafica del partido.
	def _imprimir_estado(self):
		cadena=""
		if self.fase == "Grupos":
			cadena+=str(self.equipos[0].grupo)+": "
		cadena+=""+self.equipos[0].pais
		if self.posesion==0:
			cadena+="* "+str(self.goles[0])+":"+str(self.goles[1])+" "+self.equipos[1].pais
		else:
			cadena+=" "+str(self.goles[0])+":"+str(self.goles[1])+" "+self.equipos[1].pais+"*"
		cadena+="- Pas: "+str(self.pases_exitosos[0])+":"+str(self.pases_exitosos[1])
		cadena+="- Chut: "+str(self.chutes[0])+":"+str(self.chutes[1])
		cadena+="- Pos: "+str(round(self.tiempo_en_segundos[0]/self._tiempo_total()*100))+":"
		cadena+=str(round(self.tiempo_en_segundos[1]/self._tiempo_total()*100))
		cadena+="- Form: "+str(self.equipos[0].formacion)+":"+str(self.equipos[1].formacion)
		if self.prorr:
			cadena+=" + Prorroga"
		if self.penal:
			cadena+=" + Penalti"
		Partido.semaforo_terminal.acquire()
		with Partido.ter.location(0,self.pos+4):
			print(Partido.ter.clear_eol,cadena)
			
		Partido.semaforo_terminal.release()
