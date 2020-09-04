import os
from mutagen.mp3 import MP3
import time


def music():

    # Enter your directory name
    music_dir = 'F:\\Songs\\Best'
    songs = os.listdir(music_dir)

    for i in range(len(songs)):

        audio = MP3(os.path.join(music_dir, songs[i]))
        audio_info = audio.info
        length_in_secs = int(audio_info.length)  # Length of mp3 File

        os.startfile(os.path.join(music_dir, songs[i]))  # Start mp3 file in your default music player app

        time.sleep(length_in_secs)


def video():
    class Video(object):
        def __init__(self, path):
            self.path = path

        def play(self):
            from os import startfile
            startfile(self.path)  # Start your video in your default video player app

    class Movie_MP4(Video):
        type = "mp4"

    # Enter your movie directory name
    movie_dir = r'F:\\'
    movies = os.listdir(movie_dir)
    a = os.path.join(movie_dir, movies[1])
    movie = Movie_MP4(a)
    movie.play()
