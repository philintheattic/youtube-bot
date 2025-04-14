from pytubefix import *

url = "https://www.youtube.com/watch?v=QodqZofdh0c"
filename = "INSERT FILENAME HERE"

yt = YouTube(url)

# check if there is a german caption track in the video
if 'de' or 'a.de' in [caption.code for caption in yt.captions]:
    try:
        txt = yt.captions['de'].generate_txt_captions()
    except KeyError:
        txt = yt.captions['a.de'].generate_txt_captions()
    print(txt)
else:
    print("Keine deutschen Untertitel gefunden :(")





# with open(f"{filename}.txt", "w", encoding="utf-8") as file:
#     file.write(txt)