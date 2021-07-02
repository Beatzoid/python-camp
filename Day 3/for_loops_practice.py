# for_loops_practice.py
# By Beatzoid
# 6/30/21
import random

print("Print a different random integer between 1 and 100, ten times")
for i in range(1, 11):
	print(random.randint(1, 100), end=" ")

print("\n")

print("Print the twelve times table up 12 x 12")
for col in range(1, 13):
	for row in range(1, 13):
		# Image col = 1
		# It would go 1x1, 1x2, 1x3, 1x4, etc up until 1x12
		# The \t is just to make the spacing even
		print(col * row, end="\t")

	# Once the above for loop gets to 1x12 and finishes,
	# this prints a newline character
	print("\n")