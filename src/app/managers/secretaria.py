from ..core.alumno import Alumno
from ..core.docente import Docente
from ..core.turno import Turno
from ..core.responsable import Responsable
from ..core.materia import Materia
from ..core.curso import Curso

class SecretariaDeAlumnos():
	def __init__(self):
		self.alumnos = set()
		self.responzables = set()
		self.alumnosACargo = dict()
		self.responsablesDe = dict()
		self.docentes = set()
		self.materias = set()
		self.turnos = set()
		self.cursos = set()
		
	def getAlumnos(self, anio):
		return self.alumnos
		
	def getAlumnosDe(self,docente,anio):
		ret = set()
		for curso in self.cursos:
			if curso.getDocente() == docente and curso.getAnio() == getAnio:
				for alumno in curso.getGrupoAlumnos():
					ret.add(alumno)
		return ret
		
	def getAlumnosTurno(self,turno,anio):
		ret = set()
		for curso in self.cursos:
			if curso.getTurno() == turno and curso.getAnio() == getAnio:
				for alumno in curso.getGrupoAlumnos():
					ret.add(alumno)
		return ret
	
	def getAlumnosTurnosDe(self,docente,turno,anio):
		ret = set()
		for curso in self.cursos:
			if curso.getDocente() == docente and curso.getTurno() == turno and curso.getAnio() == getAnio:
				for alumno in curso.getGrupoAlumnos():
					ret.add(alumno)
		return ret
	
	def crearAlumno(self,nombre,telefono,dni):
		for i in self.alumnos:
			if i.getNombre() == nombre and \
				i.getTelefono() == telefono and \
				i.getDni() == dni:

					return i

		unAlumno = Alumno(nombre,telefono,dni)
		self.alumnos.add(unAlumno)
		self.responsablesDe[unAlumno] = set()

		return unAlumno
		
	def eliminarAlumno(self,alumno):
		self.alumnos.remove(alumno)
		del self.responsablesDe[alumno]
		
	def crearResponsable(self,nombre,telefono,dni):
		for i in self.responsables:
			if i.getNombre() == nombre and \
				i.getTelefono() == telefono and \
				i.getDni() == dni:

					return i

		unResponsable = Responsable(nombre,telefono,dni)
		self.responsables.add(unResponsable)
		self.alumnosACargo[unResponsable] = set()

		return unResponsable
		
		
	def eliminarResponsable(self,responsable):
		self.responsales.remove(responsable)
		del self.alumnosACargo[responsable]
		
	def responsabilizar(self,alumno,responsable):
		self.alumnosACargo[responsable].add(alumno)
		self.responsablesDe[alumno].add(responsable)
		
	def desresponzabilizar(self,alumno,responsable):
		self.alumnosACargo[responsable].remove(alumno)
		self.responsablesDe[alumno].remove(responsable)
	
	def crearDocente(self,nombre,usuario):
		for i in self.docentes:
			if i.getNombre() == nombre and \
				i.getUsuario() == usuario:

					return i

		unDocente = Docente(nombre,usuario)
		self.docentes.add(unDocente)
		return unDocente
	
	def eliminarDocente(self,docente):
		self.docentes.remove(docente)
	
	def getCursosDe(self,docente,anio):
		ret = set()
		for curso in self.cursos:
			if curso.getDocente() == docente and curso.getAnio() == anio:
				ret.add(curso)
		return ret
	
	def getMateriasDe(self,docente,anio):
		ret = set()
		for curso in self.cursos:
			if curso.getDocente() == docente and curso.getAnio() == anio:
				for materia in curso.getMaterias():
					ret.add(materia)
		return ret
	
	def getResponablesDe(self,alumno):
		return responsablesDe[alumno]
	
	def getTuteladosPor(self,responsable):
		return alumnosACargo[responsable]
	
	def crearMateria(self,nombre):
		self.materias.add(Materia(nombre))
	
	def eliminarMateria(self,materia):
		self.materias.remove(materia)
		
	def getMaterias(self):
		return self.materias
	
	def crearTurno(self,nombre):
		self.turnos.add(Turno(nombre))
	
	def eliminarTurno(self,turno):
		self.turnos.remove(turno)	
	
	def getTurnos(self):
		return self.turnos
	
	def getCursos(self):
		return self.cursos
	
	def getCursos(self,anio):
		ret = set()
		for curso in self.cursos:
			if curso.getAnio() == anio:
				ret.add(curso)
		return ret
	
	def crearCurso(self,nombre,anio,docente,turno,grupo,conjMaterias):
		self.cursos.add(Curso(nombre,anio,docente,turno,grupo,conjMaterias))
	
	def eliminarCurso(self,curso):
		self.cursos.remove(curso)
	