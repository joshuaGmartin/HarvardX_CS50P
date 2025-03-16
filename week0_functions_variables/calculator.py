# -----------------------------------------
# example 1
# -----------------------------------------
# x = float(input("first num: "))
# y = float(input("second num: "))
# # x = int(input("first num: "))
# # y = int(input("second num: "))
# # z = int(x) + int(y)

# # z = round(x / y, 2)
# # z = round(x + y)
# # z = round(x + y, 2)
# # print(f"sum: {z:,}")

# z = x / y
# print(f"sum: {z:.2f}")


# -----------------------------------------
# example 2
# -----------------------------------------
def main():
    x = int(input("first num: "))
    print("square: ", square(x))


def square(n):
    # return n * n
    # return n**2
    return pow(n, 2)


main()
