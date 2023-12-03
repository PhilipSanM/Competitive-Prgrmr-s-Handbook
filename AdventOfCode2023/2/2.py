import sys

# Open input file
sys.stdin = open('inputf.in', 'r')

# Open Close file
sys.stdout = open('outputf.in', 'w')

# Code goes here
configuration = {
	'red' : 12,
	'green': 13,
	'blue': 14
}

games_document = open("inputf.in", "r")

total_ids = 0
curr_id = 0

for line in games_document:
	games_sets = line.split(":")[1]
	games = games_sets.split(";")
	curr_id += 1


	possible = True




	for game in games:

		game_cubes = {
			'red' : 0,
			'blue': 0,
			'green': 0
		}

		# todo
		cubes = game.replace("\n", '').replace(",", '').split(" ")
		
		for i in range(1, len(cubes), 2):
			number_cube = int(cubes[i])
			color_cube = cubes[i + 1]

			game_cubes[color_cube] += number_cube

			if game_cubes[color_cube] > configuration[color_cube]:

				possible = False
				break			

		if not possible:
			break




	if possible:
		total_ids += curr_id


print(total_ids)


# Closing both *put.in files
sys.stdin.close()
sys.stdout.close()
