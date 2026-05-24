import os
import sys

filename = input("Enter the file name: ")

# Check whether file exists
if os.path.isfile(filename):

    file = open(filename, "r")
    content = file.read()

    # Count characters
    characters = len(content)

    # Count words
    words = len(content.split())

    # Count vowels
    vowels = 0
    for ch in content.lower():
        if ch in "aeiou":
            vowels += 1

    # Count lines
    file.seek(0)
    lines = len(file.readlines())

    # Display results
    print("Number of characters :", characters)
    print("Number of words      :", words)
    print("Number of vowels     :", vowels)
    print("Number of lines      :", lines)

    file.close()
else:
    print("File does not exist")
    sys.exit(0)
