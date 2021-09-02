"""Counting letters in a string."""

__author__ = "730478650"


# Begin your solution here...
search_letter: str = input("What letter do you want to seach for?: ")
phrase: str = input("Enter a word: ")
count: int = 0
i: int = 0

while i < len(phrase):
    if phrase[i] == search_letter:
        count = count + 1
    i = i + 1

print("Count: " + str(count))
    