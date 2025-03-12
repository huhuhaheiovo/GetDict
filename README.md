# Word Pronunciation Downloader

A simple Python tool for downloading word pronunciation MP3 files from online dictionaries.

## Features

- Input words through console, multiple words separated by commas
- Automatically fetch word pronunciations from online sources
- Support for both American and British pronunciation options
- Download MP3 files to a local directory

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the program:
   ```
   python main.py
   ```

3. Follow the prompts to input words, save directory, and pronunciation type

## Example

```
Welcome to Word Pronunciation Downloader
Please enter words to download, separated by commas
Words: hello, world, python

Enter save directory (default is 'pronunciations'): 

Select pronunciation type:
1. American
2. British
Enter option (default is American): 1

Processing word: hello
Downloaded 'hello' pronunciation to pronunciations/hello.mp3

Processing word: world
Downloaded 'world' pronunciation to pronunciations/world.mp3

Processing word: python
Downloaded 'python' pronunciation to pronunciations/python.mp3

Download complete! Successfully downloaded 3/3 word pronunciations
```

## Notes

- The program adds a 1-second delay between requests to avoid IP blocking
- Default save directory is "pronunciations" folder in the current directory
- This program uses public APIs which may change over time