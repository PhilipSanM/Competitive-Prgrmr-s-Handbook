cases = int(input())

while cases > 0:
	cases -= 1
	rating = int(input())
	if rating <= 1399:
		print("Division 4")
	elif 1400 <= rating and rating <= 1599:
		print("Division 3")
	elif 1600 <= rating and rating <= 1899:
		print("Division 2")
	else:

		print("Division 1")