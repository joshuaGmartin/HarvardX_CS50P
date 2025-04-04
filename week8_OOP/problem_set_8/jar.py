class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self._size = size

    def __str__(self):
        cookies = ""
        for _ in range(self._size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError("That's too many cookies, man!")
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("You don't have enough cookies! OH NO!!!")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int:
            raise ValueError("Capacity must be a non-negative int")
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(10)
    jar.deposit(5)
    jar.deposit(3)
    jar.withdraw(2)
    jar.withdraw(2)
    print(jar)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()
