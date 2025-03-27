import random


def main():
    moisture = random.randint(0, 100)  # Sim test
    days = 0
    print(f"Moisture is {moisture}%")

    while moisture >= 20:
        moisture = random.randint(0, moisture)  # Sim test (drying)
        days += 1
        print(f"Moisture is {moisture}%")

    print(f"Water me bro, its been {days} days")


main()
