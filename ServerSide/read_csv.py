import csv

# Open the CSV file
with open("example.csv", mode="r") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the header
    header = next(csv_reader)
    print(f"Header: {header}")

    # Read each row of the CSV file
    for row in csv_reader:
        print(f"Row: {row}")
