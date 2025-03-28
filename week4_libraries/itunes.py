# https://itunes.apple.com/search?entity=song&limit=1&term=weezer

# json = {
#     "resultCount": 1,
#     "results": [
#         {
#             "wrapperType": "track",
#             "kind": "song",
#             "artistId": 115234,
#             "collectionId": 1440878798,
#             "trackId": 1440879325,
#             "artistName": "Weezer",
#             "collectionName": "Weezer",
#             "trackName": "Buddy Holly",
#             "collectionCensoredName": "Weezer",
#             "trackCensoredName": "Buddy Holly",
#             "artistViewUrl": "https://music.apple.com/us/artist/weezer/115234?uo=4",
#             "collectionViewUrl": "https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
#             "trackViewUrl": "https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
#             "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/b1/35/53/b13553c8-22f3-3e62-47cc-beaf65440f0e/mzaf_9734530910938773283.plus.aac.p.m4a",
#             "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/30x30bb.jpg",
#             "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/60x60bb.jpg",
#             "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/100x100bb.jpg",
#             "collectionPrice": 10.99,
#             "trackPrice": 1.29,
#             "releaseDate": "1994-05-10T12:00:00Z",
#             "collectionExplicitness": "notExplicit",
#             "trackExplicitness": "notExplicit",
#             "discCount": 1,
#             "discNumber": 1,
#             "trackCount": 10,
#             "trackNumber": 4,
#             "trackTimeMillis": 159587,
#             "country": "USA",
#             "currency": "USD",
#             "primaryGenreName": "Pop",
#             "isStreamable": true,
#         }
#     ],
# }

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("No band name provided")

response = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=5&term={sys.argv[1]}"
)

o = response.json()
for result in o["results"]:
    print(result["trackName"])
