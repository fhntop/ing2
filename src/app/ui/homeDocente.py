from .consola import Consola
from .uiscreen import UIScreen

class HomeDocente(UIScreen):
	def __init__(self, unMain, unDocente):
		super().__init__(unMain)
		self.docente = unDocente

	def run(self):
		self.consola.prnt("WELCOME MR %s" % self.docente.getNombre())
		self.main.terminate()
