def main():
    user_time = input("Enter time as XX:XX: ")
    convert_time = convert(user_time)

    if 7 <= convert_time <= 8:
        print("breakfast time")
    elif 12 <= convert_time <= 13:
        print("lunch time")
    elif 18 <= convert_time <= 19:
        print("dinner time")


def convert(time):
    time_list = time.split(":")
    return float(time_list[0]) + float(time_list[1]) / 60


main()
