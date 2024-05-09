# DriveReader

A simplified interface for generating speech files for text

As of 2024-05-09, all that needs to be invoked is:

```shell
./main.py path/to/file.txt
```

The application will read the string from _within_ `path/to/file.txt` and generate a wav file from it. It doesn't 
need to be a `.txt` file - it just needs to be a file whose text may be read directly through `pathlib.Path.read_text`.
More advanced methods of reading should be added later.

## Future Features

- [ ] A GUI for pasting text and playing the generated file
- [ ] A GUI for selecting a file and playing the generated file
- [ ] A GUI where a user may read their text while listening to it in one place
- [ ] A GUI where a user may sample different voices from different datasets
- [ ] Converting the generated file into a more modern format like `.mp3`
- [ ] Integration with Google Drive to identify files for bulk interpretation
  - The Goal is to be able to have a directory on drive that has text files/objects and be able to write narration 
  automagically
- [ ] Add the ability to provide regex substitutions to make generated narration more natural
  - An example would be telling it to replace patterns like "`^\s+* `" with '' in order to prevent the narrator 
  from directly saying 'Asterisk' or replacing "DDoS" or "US" with "D-D-O-S" and "U-S" to force the reader to pronounce 
  all letters
- [ ] Allow the user to use select models and not just the default
- [ ] Allow the user to select the speaker from multi-speaker datasets