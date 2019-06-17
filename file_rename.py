import os

def main():
    i = 0
    path = "C:\\Users\\Ryan\\Desktop\\test"

    print(path)
    for file in os.listdir(path):

        size = (os.path.getsize(path + "\\" + file)) / 1024 # Get the file size and convert it to KB
        size = round(size, 2)
        print("File: {}\nSize: {} KB".format(file, size))

        if size < 500:
            loc1 = file.find("_")
            loc2 = file.index(".jpg")

            print("Location 1: {}\tLocation 2: {}".format(loc1, loc2))

            os.rename(file, file[loc1:loc2])

main()
