import sys

# Open input file
sys.stdin = open('inputf.in', 'r')

# Open Close file
sys.stdout = open('outputf.in', 'w')

# Code goes here

# Reading input
schematic_document = open("inputf.in", "r")
schematic = []

for line in schematic_document:
	part = []
	i = 0
	while i < len(line):
		if line[i] == '\n':
			break

		symbol = line[i]
		part.append(symbol)
		i += 1

	schematic.append(part)


# Logic

def getNumber(schematic, row, column):
	number = ''

	start = column
	while start >= 0  and schematic[row][start].isnumeric():
		start -=1

	start += 1

	while start < len(schematic[0]) and schematic[row][start].isnumeric():
		number += schematic[row][start]
		schematic[row][start] = '.'
		start += 1



	return int(number)



total_number = 0
for row in range(len(schematic)):
	for column in range(len(schematic[0])):
		if schematic[row][column] == '.' or schematic[row][column].isnumeric():
			continue

		number=  0
		# changing for dot
		schematic[row][column] ='.'

		# diagonalls
		
		if min(row - 1, column - 1) >= 0 and schematic[row - 1][column - 1].isnumeric():
			number += getNumber(schematic, row - 1, column - 1)
			

		if row + 1 < len(schematic) and column + 1 < len(schematic[0]) and schematic[row+ 1][column + 1].isnumeric():
			number += getNumber(schematic, row + 1, column + 1)
			
		
		if row -1 >= 0 and column + 1 < len(schematic[0]) and schematic[row - 1][column + 1].isnumeric():
			number += getNumber(schematic, row - 1, column + 1)
			

		if row + 1 < len(schematic) and column - 1 >= 0  and schematic[row + 1][column - 1].isnumeric():
			number += getNumber(schematic, row + 1, column - 1)
			

		# 4-dot
		if row - 1 >= 0 and schematic[row - 1][column].isnumeric():
			number += getNumber(schematic, row - 1, column)


		if row + 1 < len(schematic) and schematic[row + 1][column].isnumeric():
			number += getNumber(schematic, row + 1, column)

		if column - 1 >= 0 and schematic[row][column - 1].isnumeric():
			number += getNumber(schematic, row, column - 1)

		if column + 1 < len(schematic[0]) and schematic[row][column + 1].isnumeric():
			number += getNumber(schematic, row, column + 1)


		total_number += number




'''
row, column
[0,0][0, 1][0,2]
[1,0][1,1][1,2]
[2,0][2,1][2,2]

'''	

print(total_number)



# Closing both *put.in files
sys.stdin.close()
sys.stdout.close()
