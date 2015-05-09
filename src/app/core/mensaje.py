#from mensajeProgramado import mensajeProgramado
import Datetime

class ClassName(object):
  #Colaboradores Internos
  #texto: String
  #fecha: Datetime
  
  #Colaboradores Externos
  #tipoMensaje: TipoMensaje
  #campania: Campania
  #mensajeProgramado: MensajeProgramado
  #estadoMensaje: EstadoMensaje


  def __init__(self, texto, unTipoMensaje, fecha, unaCampania, unEstado=None):
    self.texto = texto
    self.fecha = fecha
    self.campania = unaCampania
    self.tipoMensaje = unTipoMensaje
    if unEstado:
      self.mensajeProgramado = mensajeProgramado()
      self.estadoMensaje = unEstado


  def getTexto():
    return self.texto

  def tipoMensaje():
    return self.tipoMensaje

  def fecha():
    return self.fecha

  def campania():
    return self.campania

  def setEstado(unEstado):
    self.estado = unEstado

  def estaPendiente():
    return self.estado.estaPendiente()

  def enviarSiPendiente(unMensajero):
    self.estado.enviarSiPendiente(unMensajero)

  def getConfirmaciones():
    self.estado.getConfirmaciones()

  def posteriorA(fecha):
    return self.fecha >= fecha 

  def antesDe(fecha):
    return self.fecha < fecha