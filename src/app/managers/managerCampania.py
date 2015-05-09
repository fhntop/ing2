class managerCampania():
	#Colaboradores internos:
	#fecha: Datetime
	
	#Colaboradores externos:
	#managerGroup: ManagerGroup
	#campanias: Conjunto<Campania>
	
	def __init__(self, managerGroup):
		self.campanias = set()
		
	def agregarCampania(nombre, anio, usuario, aviso, fechaLimite):
		grupo = self.managerGroup.agregarGrupo("Grupo" + nombre, anio, usuario) 
		unaCampania = Campania(nombre, anio, usuario, aviso, grupo, fechaLimite)
		
	def getCampaniasDe(usuario, anio):
		campaniasDeUsuario = set()
		for campania in self.campanias:
			if campania.usuario == usuario && campania.anio = anio:
				campaniasDeUsuario.add(campania)
		return campaniasDeUsuario
	
	def eliminarCampania(campania):
		return self.campanias.remove(campania)