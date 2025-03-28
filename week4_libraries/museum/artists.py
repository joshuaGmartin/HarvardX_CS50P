import requests


def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit}
        )
    except requests.HTTPError:
        print("api call failure")

    content = response.json()
    # print(json.dumps(content, indent=2))
    return [artist["title"] for artist in content["data"]]
