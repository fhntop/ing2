from .consola import Consola
from .uiscreen import UIScreen

class SeleccionarReceptoresDocente(UIScreen):
	def __init__(self, unMain, unDocente):
		super().__init__(unMain)
		self.docente = unDocente

	def run(self):
		self.consola.prnt("sup")
		self.main.terminate()
