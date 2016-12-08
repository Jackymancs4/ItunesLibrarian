"""ItunesLibrarian.

Usage:
  ituneslibrarian.py parse [-i <input>] [-o <output>] [-c]
  ituneslibrarian.py search -f <name> [-s] [-c] [-p | -n] [--no-album | --album=<album>] [--no-artist | --artist=<artist>] [--no-title | --title=<title>]
  ituneslibrarian.py modify split [-b <symbol>] -f <name> [-s]

Options:
  -i, --input <input>     [default: Library.xml]
  -o, --output <output>     [default: Library.csv]
  -b, --symbol <symbol> [default: -]
  -s, --save            [default: false]
  -p, --print           [default: true]
  -n, --no-print        [default: true]
  -c, --check           [default: false]

"""
import os.path
import urllib.request

import ituneslibrarian.parse
from docopt import docopt
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_tokens
from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

if __name__ == '__main__':
    arguments = docopt(__doc__, version='ItunesLibrary 1.0')

    if arguments["parse"]:
        ituneslibrarian.parse.to_csv(
            arguments["--input"], arguments["--output"])

    if arguments["search"]:
        print("Not implemented yet")

    if arguments["modify"]:
        print("Not implemented yet")
