# TODO
# Add CLI or GUI to change path

import os # Import the OS library

def main(): # Define the main function
    path = "C:\\Users\\Ryan\\Desktop\\test" # Define the initial path of the non-processed images
    img_number = 0 # Image counter for naming the images

    for folder in os.listdir(path): # Loop through each folder in path
        if folder == "Processed": # If Processed is the name of the current folder
            continue # Skip to the next loop

        temp_path = path + "\\" + folder # Temporary path for each folder

        for file in os.listdir(temp_path): # Loop through each file within each folder
            size = (os.path.getsize(temp_path + "\\" + file)) / 1024 # Get the file size and convert it to KB
            size = round(size, 2) # Round file size to 2 decimal places
            print("File: {}\nSize: {} KB".format(file, size)) # Print each file & size

            if size < 500: # Checking files under 500 KB, all thermal images we are working with are under this size
                img_number += 1 # Raise the number by one for each image

                output_path = path + "\\Processed\\" # Change the output path to the processed folder
                os.rename(temp_path + "\\" + file, output_path + "Processed IMG_{}.JPG".format(img_number)) # Rename and move all the


main() # Run the main function
