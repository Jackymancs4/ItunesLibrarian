tags = {}

# Create a stylesheet.
error_style = style_from_dict({
    Token.Error: '#ff0066 bold',
    Token.Message: '#000000 italic',
})

warning_style = style_from_dict({
    Token.Warning: '#d3ac2b bold',
    Token.Message: '#000000 italic',
})

notice_style = style_from_dict({
    Token.Notice: '#44ff44 bold',
    Token.Message: '#000000 italic',
})

for track in finallibrary:

    title = track["Name"]

    tokens = [
        (Token.Notice, 'Notice: '),
        (Token.Message, title),
        (Token, '\n'),
    ]
    print_tokens(tokens, style=notice_style)

    tokens = []

    location = urllib.request.unquote(
        track["Location"][7:].replace("%20", " "))

    filename, file_extension = os.path.splitext(location)

    if os.path.exists(location):
        if file_extension == ".mp3":

            audio = MP3(location, ID3=EasyID3)

            audio["artistsort"] = ['']
            audio["titlesort"] = ['']
            audio["albumsort"] = ['']

            if "title" in audio.keys():
                if audio["title"][0] != title:
                    tokens = [
                        (Token.Warning, 'Warning:\n'),
                        (Token.Message, '\tTitle: ' +
                         str(audio["title"]) + "\n" + '\tName: ' + title),
                        (Token, '\n'),
                    ]
                    print_tokens(tokens, style=warning_style)

                    title_selection_accepts = ["1", "2", "s"]
                    title_selection = ""

                    while title_selection not in title_selection_accepts:
                        title_selection = prompt(
                            'Which one would you like to keep? [1 | 2 | s] ')

                    if title_selection == "1":
                        audio["title"] = [title]
                    elif title_selection == "2":
                        title = audio["title"][0]

            else:
                tokens = [
                    (Token.Warning, 'Warning: '),
                    (Token.Message, 'no title'),
                    (Token, '\n'),
                ]
                print_tokens(tokens, style=warning_style)

                title_duplication_accepts = ["1", "2"]
                title_duplication = ""

                while title_duplication not in title_duplication_accepts:
                    title_duplication = prompt(
                        'Would you like to clone the name? [1 | 2] ')

                if title_duplication == "1":
                    audio["title"] = [title]
                elif title_duplication == "2":
                    audio["title"] = []

            if "artist" in audio.keys():
                if "albumartist" in audio.keys():

                    if audio["artist"] != audio["albumartist"]:
                        tokens = [
                            (Token.Warning, 'Warning:\n'),
                            (Token.Message, '\tArtist: ' + str(
                                audio["artist"]) + "\n" + '\tAlbum artist: ' + str(audio["albumartist"])),
                            (Token, '\n'),
                        ]
                        print_tokens(tokens, style=warning_style)

                        artist_selection_accepts = ["1", "2", "s"]
                        artist_selection = ""

                        while artist_selection not in artist_selection_accepts:
                            artist_selection = prompt(
                                'Wich one would you like to keep? [1 | 2 | s] ')

                        if artist_selection == "1":
                            audio["albumartist"] = audio["artist"]
                        elif artist_selection == "2":
                            audio["artist"] = audio["albumartist"]

                else:
                    tokens = [
                        (Token.Warning, 'Warning: '),
                        (Token.Message, 'no album artist'),
                        (Token, '\n'),
                    ]
                    print_tokens(tokens, style=warning_style)

                    artist_duplication_accepts = ["1", "2", "s"]
                    artist_duplication = ""

                    while artist_duplication not in artist_duplication_accepts:
                        artist_duplication = prompt(
                            'Would you like to substitute <no album> with <' + audio["artist"][0] + '>? [1 | 2 | s] ')

                    if artist_duplication == "1":
                        audio["albumartist"] = audio["artist"]
                    elif artist_duplication == "2":
                        audio["albumartist"] = []

            else:
                tokens = [
                    (Token.Warning, 'Warning: '),
                    (Token.Message, 'no artist'),
                    (Token, '\n'),
                ]
                print_tokens(tokens, style=warning_style)

            title_components = title.split("-")

            i = 1

            noconflicts = {"title": False, "artist": False}

            if len(title_components) > 1:

                tokens = [
                    (Token.Warning, 'Warning: '),
                    (Token.Message, 'splittable name'),
                    (Token, '\n'),
                ]
                print_tokens(tokens, style=warning_style)

                for comp in title_components:

                    comp = comp.strip()

                    if "title" in audio.keys() and len(audio["title"]) > 0 and comp.lower() == audio["title"][0].lower():
                        noconflicts["title"] = comp

                    if "artist" in audio.keys() and len(audio["artist"]) > 0 and comp.lower() == audio["artist"][0].lower():
                        noconflicts["artist"] = comp

                    print("\t"+str(i) + " - " + comp)
                    i += 1

                if noconflicts["title"] == False:
                    # while artist_duplication not in
                    # artist_duplication_accepts:
                    newtitle = prompt(
                        'Which term is the title? ')

                    audio["title"] = title_components[
                        int(newtitle) - 1].strip()

                if noconflicts["artist"] == False:
                    # while artist_duplication not in
                    # artist_duplication_accepts:
                    newartist = prompt(
                        'Which term is the artist? ')

                    audio["artist"] = title_components[
                        int(newartist) - 1].strip()

            for tag in audio:
                tags[tag] = audio[tag]

            audio.save()

        else:

            tokens = [
                (Token.Error, 'Error: '),
                (Token.Message, 'Wrong file extension.'),
                (Token, 'Extension: ' + file_extension),
                (Token, '\n'),
            ]
            # Print the result.
            print_tokens(tokens, style=error_style)
    else:

        # Make a list of (Token, text) tuples.
        tokens = [
            (Token.Error, 'Error: '),
            (Token.Message, 'File not found.'),
            (Token, 'Location: ' + location),
            (Token, '\n'),
        ]

        # Print the result.
        print_tokens(tokens, style=error_style)

    tokens = [
        (Token.Notice, 'Notice: '),
        (Token.Message, 'all Done.'),
        (Token, '\n\n'),
    ]
    print_tokens(tokens, style=notice_style)

print(tags)
