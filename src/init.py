from app.core.campania import Campania
from app.core.criterio import Criterio
from app.core.aviso import Aviso

from datetime import datetime


def main():
	da = datetime.strptime("2015-12-10", "%Y-%m-%d")
	dc = datetime.strptime("2015-12-13", "%Y-%m-%d")

	yo = "Yo"
	a = Aviso("Juntar la basura", da)
	c = Campania(a, yo, dc)

	c.agregarReceptor(yo)
	print(c.getReceptores())
	c.sacarReceptor(yo)
	print(c.getReceptores())

	d = c.getFecha()
	print(d)



if __name__ == "__main__":
	main()