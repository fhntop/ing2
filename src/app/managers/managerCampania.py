class managerCampania():
	#Colaboradores internos:
	#fecha: Datetime
	
	#Colaboradores externos:
	#managerGroup: ManagerGroup
	#campanias: Conjunto<Campania>
	
	def __init__(self, managerGroup):
		self.campanias = set()
		
		
	def crearCampania(nombre, anio, usuario, aviso, fechaLimite):
		for campania in self.campanias:
			if campania.getNombre() == nombre and campania.getAnio() and grupo.getUsuario == usuario:
				return grupo		
		grupo = self.managerGroup.crearGrupo("Grupo" + nombre, anio, usuario) 
		unaCampania = Campania(nombre, anio, usuario, aviso, grupo, fechaLimite)
		
	def getCampaniasActivasQueFinalicenEn(fecha):
		campaniasQueFinalizanEnFecha = set()
		for campania in self.campanias:
			if campania.fechaLimite == fecha
				campaniasQueFinalizanEnFecha.add(campania)
		return campaniasQueFinalizanEnFecha
	
	def getCampaniasDe(usuario, anio):
		campaniasDeUsuario = set()
		for campania in self.campanias:
			if campania.usuario == usuario && campania.anio = anio:
				campaniasDeUsuario.add(campania)
		return campaniasDeUsuario
	
	def eliminarCampania(campania):
		return self.campanias.remove(campania)