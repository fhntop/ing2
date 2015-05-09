import datetime


class Aviso():
	#Colaboradores internos:
	#texto: String
	#fecha: Datetime

	def __init__(self, texto, fecha):
		self.texto = texto
		self.fecha = fecha

	def getFecha(self):
		return self.fecha

	def getTexto(self):
		return self.texto

	def vencido(self, dt):
		return self.fecha <= dt

	def posteriorA(self, dt):
		return self.fecha > dt
