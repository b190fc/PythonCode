import helperFunctions.directorywriter as dw
import requests
import json

from ossapi import Ossapi, UserLookupKey, GameMode, RankingType


oskFolder = R'D:\henry\Files\Desktop\songtest\osk'
SongFolder = R'D:\henry\Files\Desktop\songtest\Songs'
DestFolder = R'D:\henry\Files\Desktop\songtest\dest'
secFolder = R''
SongInfo = R'D:\henry\Files\Desktop\songtest\SongInfo.txt'
SongID = R'D:\henry\Files\Desktop\songtest\SongId.txt'
#checks if the song file exists


def main():
    #generate song list file with names and id
    dw.write_file(SongFolder,SongInfo)
    #get song id's for the songs
    dw.get_song_id(SongInfo, SongID)

    #test



if __name__ == '__main__':
    main()
