from pytubefix import *
from pytubefix.exceptions import VideoUnavailable
import random
import string

def generate_random_video_url():
    return "https://www.youtube.com/watch?v=" + Search("".join(random.choices(string.ascii_lowercase, k=3)) + "deutsch").videos[0].video_id

def get_caption_from_random_video(attempts=10):

    while attempts > 0:
        yt = YouTube(generate_random_video_url())

        # check if there is a german caption track in the video
        codes = [caption.code for caption in yt.captions]
        if 'de' in codes or 'a.de' in codes:
            try:
                txt = yt.captions['de'].generate_txt_captions()
            except KeyError:
                txt = yt.captions['a.de'].generate_txt_captions()
            return txt
            break
        else:
            attempts -= 1
            print(yt.title)
            print(f"Keine deutschen Untertitel gefunden. Suche läuft weiter... {attempts} Versuche übrig.")
            
print(get_caption_from_random_video())
