import os
import shutil
from datetime import datetime

error_file = None

#create functions for code in future test

def init_error_log():
    try:
        error_file = open(fr"D:\henry\Files\Desktop\book buffer\File.txt", "at")
        error_file.write(f"\nTimeStamp:{datetime.now()}\n\n")
        error_file.flush()
        return 1
    except IOError:
        return -1

def error_log(msg):
    error_file.write(msg)
    error_file.flush()

#one for searching for file in text folder
def textfile(text_file_path) :
    try:
        text_file = open(text_file_path, "rt")
    except OSError:
        print()
    





if __name__ == '__main__':
    #text_file_path = input("Text File Locations: ")
    text_file_path = R"C:\Users\henry\Desktop\songs.txt"
    #dir_input = input("Directory with Songs: ")
    dir_input = R"C:\Users\henry\Desktop\songs\Songs"
    #dir_destination = input("Destination File: ")
    dir_destination = R"C:\Users\henry\Desktop\dest"
    init_error_log()


    

    #error_file.write("test")
    #error_file.flush()
    print(fr"D:\henry\Files\Desktop\book buffer\File.txt")
    print(datetime.now())
    
    text_file = textfile(text_file_path)

    #error_file.close()
    #text_file.close()


