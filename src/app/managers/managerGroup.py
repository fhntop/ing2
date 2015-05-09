class managerGroup():
	#Colaboradores internos:
	#fecha: Datetime
	
	#Colaboradores externos:
	#grupos: Conjunto<Grupo>
	
	def __init__(self):
		self.grupos = set()
		
	def crearGrupo(nombre, anio, usuario):
		for grupo in self.grupos:
			if grupo.getNombre() == nombre and grupo.getAnio() and grupo.getUsuario == usuario:
				return grupo		
		grupo = Grupo(nombre, anio, usuario);
		grupos.add(grupo)
		return grupo
		
	def getGruposDe(usuario, anio):
		gruposDeUsuario = set()
		for grupo in self.grupos:
			if grupo.usuario == usuario && grupo.anio = anio:
				gruposDeUsuario.add(campania)
		return gruposDeUsuario
	
	def eliminarGrupo(grupo):
		return self.grupos.remove(grupo)