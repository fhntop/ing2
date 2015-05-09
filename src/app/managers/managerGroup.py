class managerGroup():
	#Colaboradores internos:
	#fecha: Datetime
	
	#Colaboradores externos:
	#grupos: Conjunto<Grupo>
	
	def __init__(self):
		self.grupos = set()
		
	def agregarGrupo(nombre, anio, usuario):
		grupo = Grupo(nombre, anio, usuario);
		grupos.add(grupo)
		
	def getGruposDe(usuario, anio):
		gruposDeUsuario = set()
		for grupo in self.grupos:
			if grupo.usuario == usuario && grupo.anio = anio:
				gruposDeUsuario.add(campania)
		return gruposDeUsuario
	
	def eliminarGrupo(grupo):
		return self.grupos.remove(grupo)