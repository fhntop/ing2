import datetime

from .aviso import Aviso


class Campania():
	#Colaboradores internos:
	#fecha: Datetime

	#Colaboradores externos:
	#aviso: Aviso
	#owner: Usuario
	#receptores: Conjunto<Receptor>

	def __init__(self, nombre, anio, usuario, aviso, grupo, fechaLimite):
		if aviso.posteriorA(fecha): raise Exception("No se puede crear una Campaña con fecha previa al Aviso")
		self.nombre = nombre
		self.anio = anio
		self.usuario = usuario
		self.aviso = aviso
		self.grupo = grupo
		self.fechaLimite = fechaLimite
		self.receptores = set()
		self.mensajes = set()
	
	def getNombre(self):
		return self.nombre
	
	def getUsuario(self):
		return self.usuario
		
	def getAviso(self):
		return self.aviso
	
	def getAnio(self):
		return self.anio

	def getFechaLimite(self):
		return self.fechaLimite

	def getReceptores(self):
		return set(self.receptores)

	def agregarReceptor(self, receptor):
		self.receptores.add(receptor)

	def sacarReceptor(self, receptor):
		self.receptores.remove(receptor)

	def getMensajes(self):
		return set(self.mensajes)

	def agregarMensaje(self, mensaje):
		self.mensajes.add(receptor)

	def sacarMensaje(self, mensaje):
		self.mensajes.remove(receptor)

	def posteriorA(self, fecha):
		return self.fechaLimite > fecha
		
	def antesDe(self, fecha):
		return self.fechaLimite < fecha
