class Usuario():
  #Colaboradores Internos:
  #username: String
  #password: String

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def getUsername(self):
    return self.username

  def validar(self, username, password):
    return username == self.username and self.password == password

  def cambiarUsername(self, username, unManagerDeUsuarios):
    unManagerDeUsuarios.eliminarUsuario(self.username)
    self.username = username
    agregarUsuario(username, self.password)

  def cambiarPassword(self, password):
    self.password = password

  def puedeAccederAGrupo(unGrupo, anio):
    unGrupo.getAnio == anio