import getpass

class Consola:
	def prnt(self, text):
		print(text)

	def askInput(self, text):
		return input(text)

	def askShadowInput(self, text):
		return getpass.getpass(text)

	def clear(self):
		for i in range(1, 40):
			self.prnt("")
