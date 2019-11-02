import tvdbsimple as tvdb
from pip._vendor.distlib.compat import raw_input
import os

tvdb.KEYS.API_KEY = 'UB0SOLRB8XH3I39L'


def main():
    series_name = raw_input("What's the name of anime? eg naruto One Piece . Be precise line caps etc: ")
    search = tvdb.Search()
    matched_names = search.series(series_name)
    i=0
    for series in matched_names:
        sep()
        print('No   :', i)
        print('Series name       : ', series['seriesName'])
        print('Overview          : ', series['overview'])
        sep()
        i=i+1
    id = raw_input("Please enter the Series NUMBER from the above list ")
    seriesid=matched_names[int(id)-1]['id']
    print('seriesid:'+str(seriesid))
    print('Series name       : ', matched_names[int(id)-1]['seriesName'], 'SELECTED')
    prepareressult=raw_input("Do you want to prepare folder(y/n)(read docs!) ")
    if prepareressult == 'y':
        os.system("python prepare.py")
        print("all required files are in folder and continuing")
        sep()
    else:
        print("assuming all required files are in folder and continuing")
        sep()
    removeresult=raw_input("Remove text to only leave episode number(y/n)(read docs!) ")
    if removeresult == 'y':
        remove()
        print("all required files are in correct format and continuing")
        sep()
    else:
        print("assuming all required files are in correct format and continuing")
        sep()
    renameresult=raw_input("Rename episodes(y/n)(read docs!) ")
    if renameresult == 'y':
        os.system("python renamer.py "+ str(seriesid))
        print('If any files remaining copy them toa different folder and do the rename')
        sep()
    else:
        print('If any files remaining copy them toa different folder and do the rename')
        sep()
    oraganizeresult=raw_input("Do you want to oraganize result back into season folders(y/n)(read docs!) ")
    if oraganizeresult == 'y':
        os.system("python organiser.py")
        print("continuing after organization complete")
        sep()
    else:
        print("continuing after organization complete")
        sep()
    downloadresult=raw_input("Do you want to download metadata for everything(y/n)(read docs!) ")
    if downloadresult == 'y':
        os.system("python downloader.py "+ str(seriesid))
        print("hope everything went smoothly for you **BUY ME coffee if you are happy** ")
        sep()
    else:
        print("hope everything went smoothly for you **BUY ME coffee if you are happy** ")
        sep()


    return

def sep():
    """
    this is used to drawline in the terminal window
    :return:
    """
    print("-" * 100)
    return
def remove():
    os.system("python remover.py")
    removeresult=raw_input("Remove text to only leave episode number(y/n)(read docs!) ")
    if removeresult == 'y':
        remove()

    return

main()