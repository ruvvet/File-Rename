# BATCH FILE RENAMER PROGRAM
# Rename all files within a folder using the folder name, a specified name, or last modified date as the prefix.
import os
import glob
import sys
import time


def main():
    # Input the directory with all files.
    # Returns all files in the folder and the # of files in the folder.
    filePath = str(input('Folder path: '))
    print('List of files:', os.listdir(filePath))
    print('with', len(os.listdir(filePath)), 'files in', filePath)

    choice = optionsMenu()

    if choice == 1:
        folderRename(filePath)

    elif choice == 2:
        inputRename(filePath)

    elif choice == 3:
        dateRename(filePath)

    else:
        print('Oops, try again.')
        optionsMenu()

    # Loop
    goAgain = str(input('Rename more files: Y or N >>> '))
    while goAgain == 'Y':
        main()

    print('END')


# Menu selection
def optionsMenu():
    # User selects 1 of 3 options.
    print('1. Rename files with dir name.')
    print('2. Rename files with user input.')
    print('3. Rename files with last modified date.')
    choice = int(input('Option 1, 2 or 3: '))

    return choice


# This function renames all files in the directory using the root dir name.
def folderRename(absFilePath):
    # For each file in the directory,
    # Print the name of the old file
    # Print the name of the new file name
    # Rename file
    folderName = os.path.basename(absFilePath)
    for filePath in os.listdir(absFilePath):
        full_path = os.path.join(absFilePath, filePath)
        print('Old:', full_path)
        if os.path.isfile(full_path):
            new_path = os.path.join(absFilePath, folderName + "_" + filePath)
            print('Renamed to: ', new_path)
            os.rename(full_path, new_path)


# This function renames all files in the directory using a user input.
def inputRename(absFilePath):
    inputName = input('Input file rename prefix: ')
    for filePath in os.listdir(absFilePath):
        full_path = os.path.join(absFilePath, filePath)
        print('Old: ', full_path)
        if os.path.isfile(full_path):
            new_path = os.path.join(absFilePath, inputName + "_" + filePath)
            print('Renamed to:', new_path)
            os.rename(full_path, new_path)


def dateRename(absFilePath):
    for filePath in os.listdir(absFilePath):
        full_path = os.path.join(absFilePath, filePath)
        dateModified = time.strftime('%m_%d_%Y', time.localtime(os.path.getmtime(full_path)))
        print('Old: ', full_path, ' >> Date Last Modified: ', dateModified)
        if os.path.isfile(full_path):
            new_path = os.path.join(absFilePath, dateModified + "_" + filePath)
            print('Renamed to:', new_path)
            os.rename(full_path, new_path)


main()
