cases = int(input())

while cases > 0:
	cases -= 1


	shit = int(input())

	if shit == 0:
		continue

	paquetes = input()
	paquetes = paquetes.split(" ")
	minima = int(paquetes[0])

	for paquete in paquetes:
		minima = min(minima, int(paquete))

	dani_tragon = 0

	for paquete in paquetes:
		dani_tragon += int(paquete) - minima

	print(dani_tragon)
