import csv

# CSV file paths
resources_data_1 = "FDMS/data_file_1.csv"
contact_us_cta = "FDMS/contact_us_cta.csv"


def get_file_contents_as_json():
    with open(resources_data_1, mode="r") as file:
        csv_reader = csv.DictReader(file)  # Create a CSV reader object
        data = {}
        index = 0

        for row in csv_reader:
            data.update({index: row})
            index += 1

    return {"resources": data, "count": index}


def write_to_file(headers, data):
    with open(contact_us_cta, mode="a+") as file:
        file.seek(0)  # Set file pointer to BOF

        if 1 > len(file.readlines()):
            file.write(str(headers))  # Write headers if file content NULL

        file.write(str(data))
        file.write("\n")
    return
