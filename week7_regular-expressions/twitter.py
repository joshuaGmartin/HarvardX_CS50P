import re

# url = input("url: ").strip()
# url = "  https://github.com/joshuaGmartin  ".strip()
# url = "  http://github.com/joshuaGmartin  ".strip()
# url = "  i dunno maybe https://github.com/joshuaGmartin  ".strip()
# url = "  http://www.github.com/joshuaGmartin  ".strip()
# url = "  www.github.com/joshuaGmartin  ".strip()
# url = "  github.com/joshuaGmartin  ".strip()
# url = "  https://github.com/  ".strip()
# url = "  github.com/joshuaGmartin_3  ".strip()
# url = "  github.com/joshuaGmartin_3/fdsfdsf/fdsf/  ".strip()
url = "  google.com/joshuaGmartin  ".strip()

# username = url.replace("https://github.com/", "")
# username = url.removeprefix("https://github.com/")  # just use regex
# username = re.sub(r"https://github.com/", "", url)  # like replace with regex
# watch for "." in r string
# username = re.sub(r"^.*(https?://)?(www\.)?github\.com/", "", url)
# matches = re.search(r"^https?://(www\.)?github\.com/(.+)$", url, re.IGNORECASE)


# matches = re.search(r"^.*(https?://)?(www\.)?github\.com/(.+)$", url, re.IGNORECASE)
# # count set of () to find ground number
# if matches:
#     print(matches.group(3))

# if matches := re.search(
#     r"^.*(https?://)?(www\.)?github\.com/(.+)$", url, re.IGNORECASE
# ):
#     print(matches.group(3))

# use (?:...) do not capture matches
if matches := re.search(
    r"^.*(?:https?://)?(?:www\.)?github\.com/(\w+)(?:/.*)*$",
    url,
    re.IGNORECASE,  # username twitter docs
):
    print(matches.group(1))  # can use index 1 now
else:
    print("Invalid URL")


# print("username:", username)
