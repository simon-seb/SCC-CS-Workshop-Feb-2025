import csv

# Open the CSV file
resources_data_1 = "C:\CodeBox\SCC-CS-Workshop-Feb-2025\ServerSide\FDMS\data_file_1.csv"
contact_us_cta = (
    "C:\CodeBox\SCC-CS-Workshop-Feb-2025\ServerSide\FDMS\contact_us_cta.csv"
)


def get_file_contents_as_json():
    with open(resources_data_1, mode="r") as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        data = {}
        index = 0

        for row in csv_reader:
            data.update({index: row})
            index += 1

    return {"resources": data, "count": index}


def write_to_file(headers, data):
    with open(contact_us_cta, mode="a+") as file:
        file.seek(0) # Set file pointer to SOF
        
        if 1 > len(file.readlines()):
            file.write(str(headers)) # Write headers if file content NULL

        file.write(str(data))
        file.write("\n")
    return
