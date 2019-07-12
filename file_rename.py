import os # os library used to perform OS functions like getting path and renaming
import subprocess # library used for launching processes seperate from python, eg. File Explorer
# Tkinter modules for selecting file input / output
from tkinter import Tk
from tkinter.filedialog import askdirectory

root = Tk()
root.withdraw()

def main(): # Define the main function
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

    output_path = askdirectory(title='Choose Output Directory') + "/output"
    os.mkdir(output_path)

    for root, dirs, files in os.walk(search_path, topdown=False): # Walk through all directories found within the search path
        for file in files: # Loop all files found
            if '.jpg' in file.lower() or '.jpeg' in file.lower(): # If the file is a .jpg / .jpeg
                if os.path.getsize(root + '/' + file) / 1000 < 500: # Check if it's < 500 kb (Thermal Image)
                    img_number += 1
                    os.rename(root + '/' + file, output_path + '/{}_Processed_IMG_{}.jpg'.format(os.path.getmtime(root + '/' + file), img_number)) # Rename it and move it to the output directory

    subprocess.call(['explorer',output_path.replace('/','\\')]) # Open the output directory once the program completes

main() # Run the main function
