import datetime

class Alumno():
  #Colaboradores internos:
  #nombre: String
  #telefono: String
  #dni: Int
  #fechaNac: Datetime

  def __init__(self, nombre, telefono, dni, fechaNac):
    self.nombre = nombre
    self.telefono = telefono
    self.dni = dni
    self.fechaNac = fechaNac

  def getDni(self):
    return self.dni

  def getFechaNacimiento(self):
    return self.fechaNac