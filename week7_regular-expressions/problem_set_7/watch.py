import re


def main():
    # html = '<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>'
    # html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    html = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    print(parse(html))


def parse(html):
    if match := re.search(
        r"src=\"(?:https?://)?(?:www\.)?youtube.com/embed/(.+?)\"", html
    ):
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
