"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730478650"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

print("Your fortune cookie says...")
# some random quote is printed
rand: int = randint(1, 4)
print("rand = " + str(rand))
if(rand == 1):
    print("Meeting adversity well is the source of your strength")
else: 
    if(rand == 2):
        print("Everyone agrees. You are the best.")
    else:
        if(rand == 3):
            print("Fortune favors the brave")
        else:
            if(rand == 4):
                print("You will conquer your obstacles!")
print("Now, go spread positive vibes!")

