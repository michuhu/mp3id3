"""
Manage your MP3 tags using EasyID3 lib.
"""
import glob
from typing import Any

from mutagen.easyid3 import EasyID3, EasyID3KeyError
from mutagen.id3 import ID3FileType


class Audio:
    def open_file(self, path_to_file: str) -> None:
        self.filepath = path_to_file
        with open(self.filepath, "rb") as f:
            self.audiofile = EasyID3(f)

    def return_tags(self) -> Any:
        try:
            return self.audiofile.items()
        except AttributeError as err:
            print(err)

    def set_tag(self, tag: str, value: Any) -> None:
        self.tag = tag
        try:
            self.audiofile[tag] = value
        except EasyID3KeyError as err:
            print(err)

    def get_tag(self, tag: str) -> Any:
        return self.audiofile[tag]

    def save_audiofile(self, v1: int = 2, v2_version: int = 3) -> None:
        self.audiofile.save(self.filepath, v1, v2_version)

    def delete_tags(self) -> None:
        """
        Be careful. Deletes the tags and saves the file! Do not use this unless you really know what you are doing.

        Use clear_tags() method instead and save_audiofile() after.
        """
        self.audiofile.delete(self.filepath)

    def clear_tags(self) -> None:
        """
        Clears all tags, but doesn't save the file.
        """
        self.audiofile.clear()

    def change_all_in_dir(self, dir: str, **tags: str) -> None:
        """
        Returns: nothing

        Changes tags in all mp3 files in the given folder. Saves the file.

        Use:

        change_all_in_dir(directiry, tag1=value1, tag2=value2)

        Tag must be a valid ID3 tag.

        Be careful. Using no arguments when calling, will delete the existing tags.
        """

        for file in glob.glob(dir + "*.mp3"):
            self.open_file(file)
            for tag, value in tags.items():
                self.set_tag(tag, value)

            self.save_audiofile()

    @staticmethod
    def add_missing_tags(filepath: str) -> None:
        """
        Returns: nothing.

        When you accidentally deleted all tags using delete_tags(), you can restore an empty one using this method.
        """
        tag = ID3FileType(filepath)
        tag.add_tags()
        tag.save()

    @staticmethod
    def print_valid_keys() -> None:
        print(EasyID3.valid_keys.keys())
