"""Program to demonstrate numerical operators in Python."""
__author__ = "730478650"

left_side: int = int(input("Left-hand side: "))
right_side: int = int(input("Right-hand side: "))

print(str(left_side) + " ** " + str(right_side) + " is " + str(left_side ** right_side))
print(str(left_side) + " / " + str(right_side) + " is " + str(left_side / right_side))
print(str(left_side) + " // " + str(right_side) + " is " + str(left_side // right_side))
print(str(left_side) + " % " + str(right_side) + " is " + str(left_side % right_side))