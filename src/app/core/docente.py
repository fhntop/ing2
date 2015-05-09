class Docente():
  #ColaboradoresInternos
  #nombre: String

  #ColaboradoresExternos
  #unUsuario: Usuario

  def __init__(self, nombre, unUsuario):
    self.nombre = nombre
    self.unUsuario = unUsuario

  def getNombre(self):
    return self.nombre

  def getUsuario(self):
    return self.unUsuario
