import json
import requests


def main():
    print("search art database")
    artist = input("artist: ")

    try:
        # check api docs for specifics
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist}
        )
        response.raise_for_status()  # Checks for 200 OK
    except requests.HTTPError:
        print("api call failure")
        return

    content = response.json()
    # print(json.dumps(content, indent=2))
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
