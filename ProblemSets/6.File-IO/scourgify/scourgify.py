import sys
import csv

if len(sys.argv) == 3:
    if not sys.argv[1 and 2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        
        try:

            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in reader:
                        last, first = row["name"].split(", ")
                        writer.writerow({"first": first, "last": last, "house": row["house"]})
                
        except FileNotFoundError:
            sys.exit("File does not exist")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")