import os # os library used to perform OS functions like getting path and renaming
import subprocess # library used for launching processes seperate from python, eg. File Explorer

# Tkinter modules for selecting file input / output
from tkinter import Tk
from tkinter.filedialog import askdirectory

root = Tk()
root.withdraw()

def main(): # Define the main function

    # Code to get directory path & confirm
    # (Choosing a folder like the main drive will iteratively open, rename, and move all photos it finds smaller than 500 KB)
    while True: # Emulate Do-While loop
        search_path = askdirectory(title='Choose Search Directory') # Define the initial path of the non-processed images
        print('Current search path: ', search_path)

        while True: # Emulate Do-While loop
            choice = input('To Begin the Process type \'Y\', if you wish to choose the directory again type \'N\', if you wish to exit type \'exit\': ')
            # Check if the input is a valid option. If so, exit the inner loop
            if choice.lower().strip() == 'exit':
                exit()
            elif choice.lower().strip() != 'y' and choice.lower().strip() != 'n':
                continue
            else:
                break

        # Check if the user input was to begin the program, else go back and loop again
        if choice.strip().lower() == 'y':
            break
        else:
            continue


    img_number = 0 # Image counter for naming the images

    output_path = askdirectory(tile='Choose Output Directory') + "/output"

    for folder in os.listdir(search_path): # Loop through each folder in path
        if folder == "Processed": # If Processed is the name of the current folder
            continue # Skip to the next loop

        temp_path = search_path + "\\" + folder # Temporary path for each folder

        for file in os.listdir(temp_path): # Loop through each file within each folder
            size = (os.path.getsize(temp_path + "\\" + file)) / 1024 # Get the file size and convert it to KB
            size = round(size, 2) # Round file size to 2 decimal places
            print("File: {}\nSize: {} KB".format(file, size)) # Print each file & size

            if size < 500: # Checking files under 500 KB, all thermal images we are working with are under this size
                img_number += 1 # Raise the number by one for each image
                os.rename(temp_path + "\\" + file, output_path + "Processed IMG_{}.JPG".format(img_number)) # Rename and move all the

    subprocess.call(['explorer',output_path.replace('/','\\')]) # Open the output directory once the program completes

main() # Run the main function
