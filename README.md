Don't you just hate when you have a dozen **mp3**s, be it your best album, audiobook or whatever, and they don't "add up" to a single album? You just need to edit their **ID3** tags, so they belong to one album, one artist.

Use this library. It's really easy.

For all files in one directory:
```python
change_all_in_dir(directory, tag1=value1, tag2=value2)

# e.g.
change_all_in_dir("path/to/folder/", album="Before the Storm", artist="Darude", title="Sandstorm")
```

don't forget the trailing "/"


If you want to play with particular files and tags :
```
audio = Audio()

audio.print_valid_keys() # to view which tags can be used

audio.open_file("path/to/file")
audio.get_tag("album")
audio.set_tag("album", "My best album")
audio.save_audiofile()

# see which tags are in the file:
filetags = audio.return_tags()
print(filetags)


```

You can also clear or delete all tags and add new ones.

