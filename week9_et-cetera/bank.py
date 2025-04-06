# balance = 0


# def main():
#     print("Balance:", balance)
#     deposit(100)
#     print("Balance:", balance)
#     withdraw(50)
#     print("Balance:", balance)


# def deposit(n):
#     global balance
#     balance += n


# def withdraw(n):
#     global balance
#     balance -= n


# if __name__ == "__main__":
#     main()

# =====================================


# real world vs global keyword (globals usually bad; gets messy)
class Account:
    def __init__(self):
        self._balance = 0

    # no setter because of how banks works: account = money change
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    print("Balance: ", account.balance)
    account.withdraw(50)
    print("Balance: ", account.balance)


if __name__ == "__main__":
    main()
