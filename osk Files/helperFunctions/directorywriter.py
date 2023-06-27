import os

def get_folders(directory):
    folders = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            folders.append(entry.name)
    return folders

# Specify the directory path and file name
directory_path = "S:\Osu\Songs"
output_file = "files\song_list.txt"


def write_file(dir_path = directory_path, out_file = output_file):
    folder_lst = get_folders(dir_path)
    # Open the file in write mode
    with open(out_file, 'w') as file:
        # Write the folder names to the file
        for folder in folder_lst:
            file.write(folder + '\n')
    print("File Written.")
    return out_file

def get_song_id(in_file, out_file):
    digits_list = []
    with open(in_file, 'r') as in_file:
        with open(out_file, 'w') as out_file:
            for line in in_file:
                line = line.strip()  # Remove leading/trailing whitespace and newline characters
                digits = ""
                for char in line:
                    if char.isdigit():
                        digits += char
                    else:
                        break  # Stop collecting digits if a non-digit character is encountered
                if digits:
                    out_file.write(digits + '\n')
                    digits_list.append(digits)
    
    print("digit list", digits_list)




def main():
    print(f"Writing to File.")
    # directory_path_in = input("Directory Path: ")
    directory_path_in = R"D:\henry\Files\Desktop\songtest\Songs"
    output_file_in = R"D:\henry\Files\Desktop\songtest\file.txt"
    # output_file_in = input("Output File: ")
    print(directory_path_in)
    write_file(dir_path=directory_path_in, out_file=output_file_in)
    print("Writing Complete")

if __name__ == '__main__':
    main()
