import io
import os
import shutil
from datetime import datetime

log_file = NotImplemented


# create functions for code in future test

def init_log(file_dir=r"D:\henry\Files\Desktop\songtest") :
    try:
        global log_file
        log_file = open(fr"{file_dir}\Log.txt", "wt") #todo change wt to at
        log_file.write(f"\nTimeStamp:{datetime.now()}\n\n")
        log_file.flush()
        return 0
    except IOError:
        return -1


def add_log(msg):
    global log_file
    print(msg)
    log_file.write(f"{msg}\n")
    log_file.flush()


# one for searching for file in text folder
def open_file(file):
    try:
        return open(file, "rt")
    except OSError as e:
        add_log(f"Error opening text file - {e}")


def get_song_id(file):
    song_id = file.readline().rstrip()
    if song_id == "":
        return -1
    else:
        return song_id


if __name__ == '__main__':
    # text_file_path = input("Text File Locations: ")
    text_file_path = R"D:\henry\Files\Desktop\songtest\songs.txt"
    # dir_input = input("Directory with Songs: ")
    dir_input = R"D:\henry\Files\Desktop\songtest\Songs"
    # dir_destination = input("Destination File: ")
    dir_destination = R"D:\henry\Files\Desktop\songtest\dest"

    init_log()
    add_log("Initialise all code")

    text_file = open(text_file_path, "rt")
    
    while get_song_id(text_file) != -1:
        pass
    
    # Song Ids have been parsed
    text_file.close()

    print(get_song_id(text_file))
    print(get_song_id(text_file))
    print(get_song_id(text_file))
    print(get_song_id(text_file))
    print(get_song_id(text_file))

    # error_file.close()
    # text_file.close()


