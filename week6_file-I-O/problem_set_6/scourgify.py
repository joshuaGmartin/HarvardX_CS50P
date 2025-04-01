import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"{sys.argv[1]} is not a CSV file")

    try:
        with open(sys.argv[1], "r") as before_file, open(
            sys.argv[2], "w"
        ) as after_file:
            reader = csv.DictReader(before_file)
            writer = csv.DictWriter(
                after_file, fieldnames=["last_name", "first_name", "house"]
            )
            writer.writeheader()

            for row in reader:
                full_name = row["name"].split(",")
                writer.writerow(
                    {
                        "first_name": full_name[1].strip(),
                        "last_name": full_name[0],
                        "house": row["house"],
                    }
                )

    # except FileNotFoundError as e:
    #     sys.exit(f"Could not read {e.filename}")
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
