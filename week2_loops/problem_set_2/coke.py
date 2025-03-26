def main():
    buy_coke()


def buy_coke():
    total_owed = 50

    while total_owed > 0:
        print("Amount due: ¢", total_owed, sep="")
        coin = int(input("Insert Coin:  ¢"))

        if coin == 5 or coin == 10 or coin == 25:
            total_owed -= coin
        else:
            print("Wrong denomination; coin returned")
    print("Change: ¢", total_owed * -1, sep="")
    print("Enjoy!")


main()
