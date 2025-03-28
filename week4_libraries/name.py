import sys

# argument vectors (all user CLI inputs before enter key at run file)
"""
ex: 
jgmartin@Laptop-Joshua:~/python/CS50P_2022/week4_libraries$ python3 name.py Josh
hello, my name is Josh
"""

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few args; input name after file")

# ========================================

# if len(sys.argv) < 2:
#     print("Too few args; input name after file name")
# elif len(sys.argv) > 2:
#     print("Too many args; only input name after file name")
# else:
#     print("hello, my name is", sys.argv[1])

# ========================================

# # good to keep error handling seperate
# if len(sys.argv) < 2:
#     sys.exit("Too few args; input name after file name")
# elif len(sys.argv) > 2:
#     sys.exit("Too many args; only input name after file name")


# print("hello, my name is", sys.argv[1])

# ========================================

if len(sys.argv) < 2:
    sys.exit("Too few args; input name after file name")

for arg in sys.argv[1:]:  # Avoid file name arg
    print("hello, my name is", arg)

print(sys.argv)
