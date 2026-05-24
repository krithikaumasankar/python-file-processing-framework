import zipfile
import os

# Function to zip a folder using ZIP_DEFLATED
def zip_folder(folder_name, zip_name):

    # Create zip file with compression
    f = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        f.write(file_path)
    f.close()
    print("Folder compressed successfully")

# Function to unzip files using ZIP_STORED
def unzip_file(zip_name, extract_folder):

    # Open zip file
    f = zipfile.ZipFile(zip_name, "r", zipfile.ZIP_STORED)

    # Extract files
    f.extractall(extract_folder)
    f.close()
    print("Files extracted successfully")

# Main program
folder_name = input("Enter folder name: ")
zip_name = input("Enter zip file name: ")
zip_folder(folder_name, zip_name)

extract_folder = input("Enter extract folder name: ")
unzip_file(zip_name, extract_folder)
