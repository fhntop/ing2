from app.ui.login import Login
from app.ui.consola import Consola
from app.managers.secretaria import SecretariaDeAlumnos

class Main():
	#Colaboradores externos
	#consola: Consola
	#screen: Screen
	#secretaria: SecretariaDeAlumnos

	#Colaboradores internos
	#loop: Bool

	def __init__(self):
		self.loop = True
		self.consola = Consola()
		self.screen = Login(self)

		self.secretaria = SecretariaDeAlumnos()

	def setScreen(self, screen):
		self.screen = screen
		
	def terminate(self):
		self.loop = False

	def start(self):
		while (self.loop):
			self.screen.run()


	def getSecretaria(self):
		return self.secretaria

if __name__ == "__main__":
	m = Main()
	m.start()