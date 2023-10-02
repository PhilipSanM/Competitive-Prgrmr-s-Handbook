cases = int(input())

while cases > 0:
	cases -= 1


	shit = input()
	shit = shit.split(" ")

	rows = int(shit[0])
	columns = int(shit[1])

	board = []
	for _ in range(rows):

		row = []
		read = input()
		for char in read:
			row.append(char)

		board.append(row)


	# LOGIC
	for r in range(len(board) -1 , -1, -1):

		for c in range(len(board[0])):
			if board[r][c] == "*":
				# move down
				board[r][c] = '.'
				for down in range(r, len(board)):
					# if down == len(board) - 1:
					# 	board[down][c] = "*" 

					if board[down][c] == "o" or board[down][c] == "*":
						# stop
						board[down - 1][c] = "*" 
						break
					if down == len(board) - 1:
						board[down][c] = "*" 

				if r == len(board) - 1:
					board[r][c] = '*'


					





	for r in range(len(board)):
		if r == 0:
			pass
		else:
			print()
		for c in range(len(board[0])):
			print(board[r][c], end = '')

	print()
	print()