"""
TODO - PORZADKI ZE SKRYPTEM
scicezke i nazwy podawac z parametru
metoda do wyswietlania
metoda do usuwania
metoda do zapisywania
"""
import os

from mutagen.easyid3 import EasyID3


class Audio:
    def __init__(self) -> None:
        self.audiofile = EasyID3()
        self.dir = None

    def set_dir(self, dir):
        self.dir = dir

    def open_file(self, file):
        with open(self.dir + "/" + file, "rb") as f:
            self.audiofile = EasyID3(f)

    def print_tags(self):
        # try:
        print(self.audiofile.items())
        # except AttributeError:
        #     print("No audiofile yet")

    def set_tag(self, tag):
        ...

    def get_tag(self, tag):
        ...

    def save_audiofile(self):
        ...

    @staticmethod
    def print_valid_keys() -> None:
        print(EasyID3.valid_keys.keys())


# directory = "/Users/ms/Downloads/Rene Goscinny -1- Mikołajek"
# i = 0
# [
# ('album', ['Matka noc']),
# ('title', ['02. Matka noc']),
# ('artist', ['Kurt Vonnegut']),
# ('tracknumber', ['2']),
# ('genre', ['Audiobook']),
# ('date', ['2020'])
# ]

# for path, folder, files in os.walk(directory):
#     for file in files:
#         with open(path + "/" + file, "rb") as f:
#             i += 1
#             audio = EasyID3(f)
#             audio["album"] = ["Mikolajek cz.2"]
#             audio["discnumber"] = [1]
#             audio["title"] = [file[:-4].replace("ą", "ł")]
#             audio["artist"] = ["Rene Goscinny"]
#             audio["genre"] = ["Audiobook"]
#             audio["tracknumber"] = [i]
#             audio.save(path + "/" + file, v1=2, v2_version=3)
#             print(audio.items())

audio = Audio()
audio.set_dir("/Users/ms/DEV/mp3-metadata/")
audio.print_valid_keys()
audio.print_tags()
audio.open_file("test.mp3")
audio.print_tags()
