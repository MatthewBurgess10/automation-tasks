import random, os

music_directory = ''  #enter the file for ur music here#

songs = os.listdir(music_directory)
song = random.randing(0, len(music_directory))

print(songs[song])

os.startfile(os.path.join(music_directory, songs[0]))

