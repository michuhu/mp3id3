"""
TODO - PORZADKI ZE SKRYPTEM
scicezke i nazwy podawac z parametru
metoda do wyswietlania
metoda do usuwania
metoda do zapisywania
przemyślec return vs print
zlikwidowac printy

"""
import glob
from typing import Any

from mutagen.easyid3 import EasyID3


class Audio:
    # def __init__(self) -> None:
    #     self.dir = None
    #     self.audiofile = EasyID3()

    def open_file(self, path_to_file: str) -> None:
        self.filepath = path_to_file
        with open(self.filepath, "rb") as f:
            self.audiofile = EasyID3(f)

    def print_tags(self) -> None:
        try:
            print(self.audiofile.items())
        except AttributeError:
            print("No audiofile yet")

    def set_tag(self, tag: str, value: Any) -> None:
        self.tag = tag
        self.audiofile[tag] = value

    def get_tag(self, tag: str) -> Any:
        return self.audiofile[tag]

    def save_audiofile(self, v1: int = 2, v2_version: int = 3) -> None:
        self.audiofile.save(self.filepath, v1, v2_version)

    # def set_dir(self, dir: str) -> None:
    #     self.dir = dir

    def change_all_in_dir(self, dir, **tags):
        """
        Be careful. Using no arguments when calling, will delete the existing ones.
        TODO: jesli nie ma takiego taga, dwać None

        This is another line.
        """

        for file in glob.glob(dir + "*.mp3"):
            print(file)
            self.open_file(file)
            for tag, value in tags.items():
                self.set_tag(tag, value)

            self.print_tags()
            self.save_audiofile()

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
# audio.set_dir("/Users/ms/DEV/mp3-metadata/")
# audio.print_valid_keys()
# audio.print_tags()
audio.open_file("/Users/ms/DEV/mp3-metadata/mp3/test.mp3")
audio.print_tags()
# audio.get_tag("album")
# audio.set_tag("album", "testowy")
# audio.get_tag("album")
# audio.save_audiofile()

audio.change_all_in_dir(
    "/Users/ms/DEV/mp3-metadata/mp3/", album="ana", artist="beta", zys="ddd"
)
# audio.print_tags()
