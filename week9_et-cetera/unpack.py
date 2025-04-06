# # input("name: ").split(" ")
# # first, last = "Josh Martin".split(" ")
# first, _ = "Josh Martin".split(" ")
# print(f"hello, {first}")


# def total(gall, sick, knut):
#     return (gall * 17 + sick) * 29 + knut


# coins = [100, 50, 25]

# # print(
# #     total(
# #         coins[0],
# #         coins[1],
# #         coins[2],
# #     ),
# #     "knuts",
# # )

# # *var unpacks variable
# print(total(*coins), "knuts")


# ================================================


# # def total(galleons, sickles, knuts):
# def total(galleons, knuts, sickles):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# # coins = {"galleons": 100, "sickles": 50, "knuts": 25, "pennies": 1}

# # print(total(galleons=100, sickles=50, knuts=25), "knuts")
# # print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
# # ** unpacks the dict, like so: galleons=100, sickles=50, knuts=25
# print(total(**coins), "Knuts")


# ================================================


# *args: some number of positional (left to right) args
# **kwargs: some number of callable named args
def f(*args, **kwargs):
    print("Positional:", args)
    print("Key words:", kwargs)


# f(100)
# f(100, 50, 25) # *args makes tuple
# f(100, 50, 25, 5)  # able to add in a non-set number of args and no error
f(galleons=100, sickles=50, knuts=25)  # **kwargs makes dict
# f(100, 50, 25, test="hello")

# (function) def print(*values: object, sep: str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False) -> None
# def print(*objects, sep=" ", end="\n", ...):
#     for object in objects:
#         # print to console

# print("hello,", "world") equals {"hello,", "world"}
