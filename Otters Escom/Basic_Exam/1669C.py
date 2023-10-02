cases = int(input())

while cases > 0:
	cases -= 1


	shit = input()

	numbers = input()

	numbers = numbers.split(" ")

	pares_ind_pares = True
	pares_ind_impares = True

	impares_ind_pares = True
	impares_ind_impares = True

	for i in range(0, len(numbers) ):
		if i % 2 == 0:
			# ES indice PAR
			if int(numbers[i]) % 2 == 0:
				# Full par
				impares_ind_pares = False
			else:
				pares_ind_pares = False

			if pares_ind_pares == impares_ind_pares :
				break
		
		else:
		# ES indice imPAR
			if int(numbers[i]) % 2 == 0:
				# Full par
				impares_ind_impares = False
			else:
				pares_ind_impares = False

			if impares_ind_impares == pares_ind_impares:
				break

	if pares_ind_impares == impares_ind_impares or impares_ind_pares == pares_ind_pares:
		print('NO')
	else:
		print('YES')
