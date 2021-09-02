"""Repeating a beat in a loop."""

__author__ = "730478650"


# Begin your solution here...
counter: int = 0
beat: str = input("What beat do you want to repeat? ")
maximum: int = int(input("How many times do you want to repeat it? "))
output: str = ""

while counter < maximum:
    if counter + 1 != maximum:
        output += beat + " "
    else:
        output += beat
    counter = counter + 1

print(output)
