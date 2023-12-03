import sys

# Open input file
sys.stdin = open('inputf.in', 'r')

# Open Close file
sys.stdout = open('outputf.in', 'w')

# Code goes here
import re   


calibration_document = open("inputf.in", "r")


word_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

reversed_word_digits= {}

for key,value in word_digits.items():
	reversed_word_digits[key[::-1]] = value



digits = set(['1','2','3','4','5','6','7','8','9'])

additions = 0

for calibration in calibration_document:
	number = ''
	word = ""

	# First digit:
	for letter in calibration:
		word += letter

		if len(number) > 0:
			break

		if letter in digits:
			number += letter
			break

		for exp in word_digits:
			pattern = re.compile(rf'{exp}')
			if pattern.search(word):
				number += word_digits[exp]
				break

	# Second digit
	word = ""
	reverserd_calibration = calibration[::-1]

	# First digit:
	for letter in reverserd_calibration:
		word += letter

		if len(number) > 1:
			break

		if letter in digits:
			number += letter
			break

		for exp in reversed_word_digits:
			pattern = re.compile(rf'{exp}')
			if pattern.search(word):
				number += reversed_word_digits[exp]
				break

	additions += int(number)
	# print(number)

print(additions)


# Closing both *put.in files
sys.stdin.close()
sys.stdout.close()
