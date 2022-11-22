import os
import shutil

#create functions for code in future test

#one for searching for file in text folder
def textfile() :
    pass


text_file_path = input("Text File Locations: ")
#text_file_path = r"C:\Users\henry\Desktop\songs.txt"
dir_input = input("Directory with Songs: ")
# dir_input = r"C:\Users\henry\Desktop\songs\Songs"
dir_destination = input("Destination File: ")
# dir_destination = R"C:\Users\henry\Desktop\dest"

directory_list = os.listdir(dir_input)

textfile = open(text_file_path, "rt")
while True:
    # loop through text file to read all song ID's
    song_id = textfile.readline().rstrip()
    # print(f"Song id: {song_id}")
    if song_id == "":
        # exit loop as text file is empty
        print("EOF has been reached for text file")
        textfile.close()
        exit(1)

    # loop in directoroy
    song_location = None

    for x in directory_list:
        file_list = x.split(" ", 1)
        file_number = file_list[0]
        file_name = file_list[1]
        # print(f"file num: {file_number}, songid: {song_id}")
        # check if number is the song id from text file
        if file_number == song_id:

            song_directory_path = f"{dir_input}\\{x}"

            song_directory = os.listdir(song_directory_path)
            print(f"Song Directory: {song_directory_path}")
            file_found = False
            print(song_directory.count(".mp3"))
            if "audio.mp3test" in song_directory:
                print("found song")
                file_found = True
                song_location = f"{song_directory_path}\\audio.mp3"
            else:
                #check if .mp3 file is only 1,
                mp3_list = []
                for y in song_directory:
                    # print(f"y: {y}")
                    # print(y.split(".", 1)[1])
                    try:
                        if y.split(".", 1)[1] == "mp3":
                            # print("Split found", y)
                            mp3_list.append(y)
                    except IndexError:
                        print("error has occured")
                        print(y)
                        pass

                print(f"test: {song_directory_path}\\{mp3_list[0]}")
                if len(mp3_list) == 1:
                    file_found = True
                    song_location = f"{song_directory_path}\\{mp3_list[0]}"
                    pass
                elif len(mp3_list) > 1:
                    print("Multiple MP3 file have been observed, Please choose which file you want to use:")
                    for i in range(len(mp3_list)):
                        print(f"{i}: {mp3_list[i]}")

                    # ask user for input for which file to choose
                    while 1:
                        # get input from user for file number
                        num = input("File Number: ")
                        if num.isdigit():
                            num = int(num)
                            # print(num)
                            if len(mp3_list) >= num >= 0:
                                song_location = f"{song_directory_path}\\{mp3_list[num]}"
                                print(song_location)
                                file_found = True
                                break
                        print("Choose a valid File Number")

                    # print(mp3_list)

                else:
                    print("MP3 file can not be found")
                    file_found = False
                    exit(-1)

            # copy file to destination
            if not file_found:
                print("Error, file has not been found")
                exit(-1)
            else:
                shutil.copy(song_location, f"{dir_destination}\\{file_name}.mp3")

                #todo run copy and rename
                pass

            break  # todo break for x in directory list

        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


