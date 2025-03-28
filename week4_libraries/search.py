# from artwork import get_artworks
# from artists import get_artists
from museum.artists import get_artists
from museum.artwork import get_artworks


def main():
    artwork = input("artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

    # artist = input("artist: ")
    # artists = get_artists(query=artist, limit=3)
    # for artist in artists:
    #     print(f"* {artist}")


if __name__ == "__main__":
    main()
