def main():
    # n = int("1000000")  # out of memory if use "return"
    n = int("10")

    for s in sheep(n):
        print(s)


# too many sheep means too big a flock returned at once
# would be better to print one at a time—but thats stepping backwards
# use generators and "yield" vs "return"
def sheep(n):
    # flock = []
    # for i in range(n):
    #     flock.append("🐑" * (i + 1))
    # return flock # returns all at once

    for i in range(n):
        yield "🐑" * (i + 1)  # yield = "return one value at a time"
    # yield returns "iterators"; only uses mem on each iteration vs mem on the millions of sheep at once


if __name__ == "__main__":
    main()
