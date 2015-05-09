from .consola import Consola
from .uiscreen import UIScreen
from .homeDocente import HomeDocente

from ..core.usuario import Usuario
from ..core.docente import Docente

class Login(UIScreen):
	def __init__(self, unMain):
		super().__init__(unMain)

	def run(self):
		self.consola.prnt("================")
		self.consola.prnt("Inicio de sesion")
		self.consola.prnt("")
		user = self.consola.askInput("Usuario: ")
		passwd = self.consola.askShadowInput("Password: ")

		if user == "juan" and passwd == "1234":
			usr = Usuario(user, passwd)
			doc = self.main.getSecretaria().crearDocente("Juan Perez", usr)

			self.consola.clear()
			self.main.setScreen(HomeDocente(self.main, doc))
		else:
			self.consola.clear()
			self.consola.prnt("[Error] Usuario y contraseña incorrectos.")
