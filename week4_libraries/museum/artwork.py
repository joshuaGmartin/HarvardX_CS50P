import requests


def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
    except requests.HTTPError:
        print("api call failure")

    content = response.json()
    # print(json.dumps(content, indent=2))
    return [artwork["title"] for artwork in content["data"]]
