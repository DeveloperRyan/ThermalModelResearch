import os

def main():
    img_number = 0
    path = "C:\\Users\\Ryan\\Desktop\\test"

    print(path)

    for folder in os.listdir(path):
        print(folder)
        temp_path = path + "\\" + folder
        for file in os.listdir(temp_path):
            size = (os.path.getsize(temp_path + "\\" + file)) / 1024 # Get the file size and convert it to KB
            size = round(size, 2)
            print("File: {}\nSize: {} KB".format(file, size))

            if size < 500:
                img_number += 1
                print(img_number)

                output_path = path + "\\Processed\\"
                print(output_path)
                os.rename(temp_path + "\\" + file, output_path + "Processed IMG_{}.JPG".format(img_number))

main()
