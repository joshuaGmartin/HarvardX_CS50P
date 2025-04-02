# # name = input("name: ").strip()
# # name = "   Josh Martin    "
# # name = "   Martin, Josh    "
# name = "martin,josh"
# name = name.strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"


# print("hey,", name)

# ========================================

import re

# name = input("name: ").strip()
# name = "martin,josh".strip()
# name = "martin, josh".strip()
name = "martin,           josh".strip()

# # () in re return that value (and then (?:...) for non-caputure)
# matches = re.search(r"^(.+), *(.+)$", name)  # optional space(s)
# if matches:
#     # last = matches.group(1)

#     # first = matches.group(2)
#     # last, first = matches.groups()

#     # name = first + " " + last
#     name = matches.group(2) + " " + matches.group(1)  # something else in group(0)

# assign and check, ":=" is the walrus operator
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print("hello,", name)
