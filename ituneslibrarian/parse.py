obj = untangle.parse(arguments["--input"])

tracklist = obj.plist.dict.dict

library = []
track = {}
sampletrack = {}

maxparam = 0
maxtrack = 0

for xmltrack in tracklist.dict:

    track = {}
    lastdata = ""

    for data in xmltrack.children:

        if data._name == "key":
            lastdata = data.cdata
            sampletrack[lastdata] = ""
        else:
            track[lastdata] = data.cdata

    library.append(track)

finallibrary = []
finaltrack = sampletrack.copy()

for dicttrack in library:
    for key in dicttrack:
        finaltrack[key] = dicttrack[key]
    finallibrary.append(finaltrack)
    finaltrack = sampletrack.copy()

with open(arguments["--output"], 'w') as csvfile:
    fieldnames = sampletrack.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for realtrack in finallibrary:
        writer.writerow(realtrack)
