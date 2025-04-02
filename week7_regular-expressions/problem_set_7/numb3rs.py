import re


def main():
    IPv4 = input("IPv4: ").strip()
    print(validate_IP(IPv4))


def validate_IP(IPv4):
    # if re.search(r"^([0-255]\.){3}[0-255]$", IPv4):
    # if re.search(r"^[0-9]+[0-9]*[0-9]*$", IPv4):
    if re.search(
        r"^((([0-9])|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-9])|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))$",
        IPv4,
    ):
        return True
    return False


if __name__ == "__main__":
    main()
