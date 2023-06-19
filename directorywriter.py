import os

# Specify the directory path and file name
directory = "S:\Osu\Songs"
filename = "song_list.txt"

# Get a list of all files in the directory
file_list = os.listdir(directory)

# Open the specified file in write mode
with open(filename, 'w') as file:
    # Write each file name to the file, one name per line
    for name in file_list:
        #only get the first part of the string up to " " and then copy it to the textfile
        # file.write(name.split(" ", 1)[0] + '\n')
        file.write(name + '\n')
