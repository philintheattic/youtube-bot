import random
import string
from time import sleep
from pytubefix import *
from pytubefix.exceptions import VideoUnavailable

def generate_random_video_id():
    chars = string.ascii_letters + string.digits + '-_'
    return "".join(random.choice(chars) for _ in range(11))

def generate_random_video_url():
    return "https://www.youtube.com/watch?v=" + generate_random_video_id()

attempts = 100
while attempts > 0:
    try:
        yt = YouTube(generate_random_video_url())
        print(yt.streams)
    except VideoUnavailable:
        print("sad")
        attempts -= 1
        # sleep(1)
        continue
    break
    