# lots of code to express simple requirements
# email = input("Enter email: ").strip()

# if "@" not in email or "." not in email:
#     print("Invalid")
# else:
#     print("Valid")

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

# =====================================

# use regex instead
import re

email = input("Enter email: ").strip()

"""
RegEx:
.       any char, no new line
*       0 or more reps
+       1 or more reps
?       0 or 1 reps
{m}     m reps
{m,n}   m-n reps 
^       match start
$       match end
[]      set of char
[^]     complementing (math) the set (all that does not match)
\d      decimal digit
\D      not decimal digit
\s      whitespace char
\S      not whitespace char
\w      word char (and underscore)
\W      not word char
\       escape character
r""     raw string: python no interpret \ in normal way, want to pass in exactly
A|B     A or B
(...)   group
(?:..)  non-capturing version

"""

# if re.search("@", email):  # accepts: @
# if re.search(".*@.*", email):  # accepts: @
# if re.search("..*@..*", email):  # accepts: @
# if re.search(".+@.+", email):  # accepts: @@@
# if re.search(".+@.+.edu", email):  # accepts: f@f#edu
# if re.search(r".+@.+\.edu", email):  # accepts: email is email@zzz.edu
# if re.search(r"^.+@.+\.edu$", email):  # accepts: @@@.edu
# if re.search(r"^[^@]+@[^@]+\.edu$", email):  # accepts: .edu@.edu.edu
# if re.search(r"^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9_-]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email):  # \w = "word character" includes _
# if re.search(r"^(\w|.|-)+@\w+\.(com|edu|gov|net|org)$", email):  # rejects: Z@Z.EDU
# if re.search(
#     r"^(\w|.|-)+@\w+\.(com|edu|gov|net|org)$",  # rejects: fds.fds@fds.fds.com
#     email,
#     re.IGNORECASE,  # or use .lower()
# ):
if re.search(
    r"^((\w+\.)|(\w+\-))*\w+@((\w+\.)|(\w+\-))*\w+\.(com|edu|gov|net|org)$",  # handles subdomains, no spec chars, use library
    email,
    re.IGNORECASE,
):
    print("Vaild")
else:
    print("Invalid")
