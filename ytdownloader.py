#this program is for a youtube vid downloader
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/Matthew/Downloads/YT vid downloads')


#to run the program do this:
    #got into terminal and type python3 ytdownloader.py "(paste the url of the video here)"