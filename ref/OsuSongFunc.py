import os
import shutil
import logging

global logger

def read_song_ids(file_path) -> list[str]:
    """Reads all song IDs from a text file and returns them as a list."""
    with open(file_path, "rt") as f:
        return [line.strip() for line in f if line.strip()]


def get_song_directory_path(directory_list, song_id, dir_input):
    """Returns the path to the directory of the song with the given ID, or None if not found."""
    for x in directory_list:
        file_list = x.split(" ", 1)
        file_number = file_list[0]
        if file_number == song_id:
            return os.path.join(dir_input, x)
    logger.warning(f"Song with ID {song_id} could not be found")
    return None


def get_audio_mp3_path(song_directory_path):
    """Returns the path to the audio.mp3 file in the given directory path, or None if not found."""
    if "audio.mp3" in os.listdir(song_directory_path):
        return os.path.join(song_directory_path, "audio.mp3")
    return None


def get_mp3_list(song_directory_path):
    """Returns a list of paths to all MP3 files in the given directory path."""
    return [os.path.join(song_directory_path, y) for y in os.listdir(song_directory_path) if y.endswith(".mp3")]


def get_song_location(song_directory_path):
    """Returns the location of the song file within the given directory path, or None if not found."""
    audio_mp3_path = get_audio_mp3_path(song_directory_path)
    if audio_mp3_path is not None:
        return audio_mp3_path
    mp3_list = get_mp3_list(song_directory_path)
    if len(mp3_list) == 1:
        return mp3_list[0]
    if len(mp3_list) > 1:
        logger.warning("Multiple MP3 files have been observed.")
        logger.warning("Please choose which file you want to use:")
        for i, mp3_file in enumerate(mp3_list):
            logger.warning(f"{i}: {mp3_file}")
        while True:
            num = input("File number: ")
            if num.isdigit() and 0 <= int(num) < len(mp3_list):
                return mp3_list[int(num)]
            logger.warning("Choose a valid file number")
    logger.warning(f"No MP3 file could be found in directory {song_directory_path}")
    return None


def get_dest_filename(file_list):
    """Returns the destination filename based on the given file list."""
    return f"{file_list[1]}.mp3"


def get_song_location_and_dest_filename(directory_list, song_id, dir_input):
    """Returns a tuple containing the location of the song file and its destination filename."""
    song_directory_path = get_song_directory_path(directory_list, song_id, dir_input)
    if song_directory_path is None:
        return None, None
    song_location = get_song_location(song_directory_path)
    if song_location is None:
        return None, None
    dest_filename = get_dest_filename(song_directory_path.split(" ", 1))
    return song_location, dest_filename


def check_file_existence(file_path, dest_dir):
    """Checks if a file already exists in the destination directory."""
    filename = os.path.basename(file_path)
    dest_path = os.path.join(dest_dir, filename)
    if os.path.exists(dest_path):
        return True
    # check for similar filenames
    for existing_file in os.listdir(dest_dir):
        if existing_file.lower().startswith(filename.lower()):
            return True
    return False


def copy_and_rename_song(src_path, dest_dir, dest_filename):
    """Copies a song file from src_path to dest_dir, and renames it to dest_filename."""
    dest_path = os.path.join(dest_dir, dest_filename)
    shutil.copy(src_path, dest_path)
    logger.info(f"Copied {src_path} to {dest_path}")


def main(text_file_path, dir_input, dir_destination):
    #ask if input from file or parse all songs
    while True:
        print()
        stage = input("Option: ")

    song_ids = read_song_ids(text_file_path)
    directory_list = os.listdir(dir_input)
    for song_id in song_ids:
        song_location, dest_filename = get_song_location_and_dest_filename(directory_list, song_id, dir_input)
        if song_location is None:
            continue
        if check_file_existence(dest_filename, dir_destination):
            logger.warning(f"Song {dest_filename} already exists in {dir_destination}")
            continue
        copy_and_rename_song(song_location, dir_destination, dest_filename)

def setup_logger():
    # Create a logger instance
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler that logs debug and above to a file
    file_handler = logging.FileHandler('OsuSong.log')
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler that logs info and above to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter that specifies the log message format
    formatter = logging.Formatter('%(asctime)s - OsuSongCopy - %(levelname)s - %(message)s')

    # Set the formatter for the file and console handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the file and console handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


if __name__ == "__main__":
    text_file_path = R"D:\henry\Files\Desktop\songtest\file.txt"
    dir_input = R"D:\henry\Files\Desktop\songtest\Songs"
    dir_destination = R"D:\henry\Files\Desktop\songtest\dest"

    setup_logger()

    # # Test the logger by writing some log messages
    # logger.debug('This is a debug message')
    # logger.info('This is an info message')
    # logger.warning('This is a warning message')
    # logger.error('This is an error message')
    # logger.critical('This is a critical message')



    try:
        # execute main function
        main(text_file_path, dir_input, dir_destination)
    except Exception as e:
        # log any unhandled exceptions
        logging.exception("Unhandled exception occurred")
        print("An error occurred. Please check the log file for details.")
    
