import os
import sys

source_file = input("Enter source file name: ")
target_file = input("Enter target file name: ")

# Check whether source file exists
if os.path.isfile(source_file):

     # Open source file and read contents
    file1 = open(source_file, "r")
    content = file1.read()

    # Reverse the content character by character
    reversed_content = content[::-1]

    # Write reversed content into another file
    file2 = open(target_file, "w")
    file2.write(reversed_content)

    print("File reversed successfully")

    file1.close()
    file2.close()

else:
    print("Source file does not exist")
    sys.exit(0)
