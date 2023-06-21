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


def write_file():
    folder_lst = get_folders(directory_path)
    # Open the file in write mode
    with open(output_file, 'w') as file:
        # Write the folder names to the file
        for folder in folder_lst:
            file.write(folder + '\n')
    print("File Written.")




def main():
    print(f"Writing to File.")
    write_file()
    print("Writing Complete")

if __name__ == '__main__':
    main()
