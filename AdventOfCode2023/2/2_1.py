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

total_power = 0
curr_id = 0

for line in games_document:
	games_sets = line.split(":")[1]
	games = games_sets.split(";")
	curr_id += 1


	possible = True

	minimuns = {
		'red' : 0,
		'blue': 0,
		'green': 0
	}




	for game in games:

		game_cubes = {
			'red' : 0,
			'blue': 0,
			'green': 0
		}

		
		cubes = game.replace("\n", '').replace(",", '').split(" ")
		
		for i in range(1, len(cubes), 2):
			number_cube = int(cubes[i])
			color_cube = cubes[i + 1]

			game_cubes[color_cube] += number_cube

		# Updating mix cbes
		for color_cube, total_cube in game_cubes.items():
			minimuns[color_cube] = max(minimuns[color_cube], total_cube)

	power = 1
	for color_cube, max_number_cube in minimuns.items():
		power *= max_number_cube




	
	total_power += power


print(total_power)


# Closing both *put.in files
sys.stdin.close()
sys.stdout.close()
