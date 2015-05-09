class Grupo():
  #Colaboradores Internos:
  #Nombre: String
  #Anio: Int
  
  #Colaboradores Externos:
  #unUsuario: Usuario
  #receptores: Conjunto<Receptor>

  def __init__(self, nombre, anio, unUsuario):
    self.nombre = nombre
    self.anio = anio
    self.unUsuario = unUsuario
    self.receptores = set()


  def getNombre(self):
    return self.nombre

  def getAnio(self):
    return self.anio

  def agregar(self, unReceptor):
    self.receptores.add(unReceptor)

  def sacar(self, unReceptor):
    assert(unReceptor in self.receptores)
    self.receptores.remove(unReceptor)

  def getReceptores(self):
    return self.receptores

  def getCreador(self):
    return self.unUsuario

  def fueCreadoPor(unUsuario):
    return self.unUsuario == unUsuario