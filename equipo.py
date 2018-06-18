import configuracion
import random

class Equipo():
	def __init__(self, pais, ranking, formacion, grupo):
		super(Equipo, self).__init__()
		self.pais=pais
		self.grupo=grupo
		self.formacion=formacion
		self._obtener_probabilidades(ranking)

#Recupera las probabilidades de acertar pase, anotar gol y encajar gol segun su ranking FIFA.
	def _obtener_probabilidades(self,ranking):
		categoria=""
		if ranking<=10:
			categoria="1-10"
		elif ranking<=20:
			categoria="11-20"
		elif ranking<=30:
			categoria="21-30"
		elif ranking<=40:
			categoria="31-40"
		elif ranking<=50:
			categoria="41-50"
		elif ranking<=60:
			categoria="51-60"
		elif ranking<=70:
			categoria="61-70"
		elif ranking<=80:
			categoria="71-80"
		elif ranking<=90:
			categoria="81-90"
		else:
			categoria="91-100"
		self.categoria=categoria
		self.probabilidad=configuracion.TABLA_PROBABILIDADES[categoria]

#Determina si se acierta o falla un pase.
	def _pasar(self):
		p_pase=random.randrange(100)+self.probabilidad["pase"]
		if p_pase>100:
			paso=True
		else:
			paso=False
		return paso

#Determina si se acierta o falla un remate a porteria (intento de gol).
	def _chutar(self, encajar_equipo_contrario):
		p_anotacion=random.randrange(100)+self.probabilidad["anotar"]+ encajar_equipo_contrario
		if p_anotacion>150:
			entro= True
		else:
			entro= False
		return entro

#Secuencia de ataque del equipo. Si se logran 4 pases seguidos, se remata al arco, si no se pierde el balon.
	def atacar(self, encajar_equipo_contrario):
		pases=0
		while pases<4 and self._pasar():
			pases = pases+1
		if pases==4:
			 gol=self._chutar(encajar_equipo_contrario)
		else:
			 gol=False
		return (pases, gol)
