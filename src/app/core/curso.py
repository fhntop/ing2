import datetime

from .turno import Turno
from .materia import Materia
from .grupo import Grupo
from .docente import Docente


class Curso():
	def __init__(self, nombre, anio, docente, turno, grupo, materias):
		self.nombre = nombre
		self.anio = anio
		self.docente = docente
		self.turno = turno
		self.grupo = grupo
		self.materias = materias
	
	def getNombre(self):
		return self.nombre
	
	def getAnio(self):
		return self.anio
		
	def getDocente(self):
		return self.docente
	
	def getMaterias(self):
		return self.materias
		
	def getTurno(self):
		return self.turno
		
	def getGrupoAlumnos(self):
		return self.grupo