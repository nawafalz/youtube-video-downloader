from pytube import *

# function to receive a YouTube link
def download(link):
    # assign the YouTube function + get the lowest resolution
    youtube = YouTube(link).streams.get_lowest_resolution()
    # try to download the file
    try:
        youtube.download()
    except:
        print('error downloading')
    print('downloaded')

link = input('Enter Youtube link : ')
download(link)
