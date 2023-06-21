import sys

# Open input file
sys.stdin = open('inputf.in', 'r')

# Open Close file
sys.stdout = open('outputf.in', 'w')

# Code goes here

line1 = input()
line2 = input()


print(line1)
print(line2)


# Closing both *put.in files
sys.stdin.close()
sys.stdout.close()
