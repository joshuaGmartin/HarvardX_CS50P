def main():
    extension = input("File name: ").strip().split(".")[1].lower()

    match extension:
        case "gif" | "jpg" | "jpeg" | "png":
            print("image/", extension, sep="")
        case "pdf" | "zip":
            print("application/", extension, sep="")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


main()
