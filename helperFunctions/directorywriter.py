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
