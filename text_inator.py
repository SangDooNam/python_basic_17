"""Task

Create a program that takes a single word string from a user and does the following:
Concatenates inator to the end if the word ends with a consonant otherwise, concatenate -inator instead.
Adds the word length of the original word to the end, supplied with '000'.
"""

text = input("Enter the word: ")

consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
consonant = [char.lower() for char in consonant]

length = len(text) * 1000

width = 15
space_btw = ' ' * (width - len(text))


if text[-1] in consonant:
    print(f'Enter the word: {text}{space_btw}➞ "{text}inator {length}"')
else:
    print(f'Enter the word: {text}{space_btw}➞ "{text}-inator {length}"')