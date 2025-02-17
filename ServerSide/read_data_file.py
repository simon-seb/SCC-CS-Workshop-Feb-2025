import csv

# Open the CSV file
file_path = "C:\CodeBox\SCC-CS-Workshop-Feb-2025\ServerSide\FDMS\data_file_1.csv"


def get_file_contents_as_json():
    with open(file_path, mode="r") as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        data = {}
        index = 0

        for row in csv_reader:
            data.update({index: row})
            index += 1

    return {"resources": data, "count": index}
