import csv
import json

from enum import Enum

# CSV file paths
resources_data_1_csv = "FDMS/data_file_1.csv"
contact_us_cta_csv = "FDMS/contact_us_cta.csv"

# JSON file paths
resources_data_1_json = "FDMS/resources_data_1.json"
models_data_1_json = "FDMS/models_data_1.json"
contact_us_cta_json = ""


def get_file_contents_as_json(resource):
    if "RES" == resource:

        with open(resources_data_1_csv, mode="r") as file:
            csv_reader = csv.DictReader(file)  # Create a CSV reader object
            data = {}
            index = 0

            for row in csv_reader:
                data.update({index: row})
                index += 1

        return {"resources": data, "count": index}

    if "CON" == resource:
        with open(contact_us_cta_csv, mode="r") as file:
            csv_reader = csv.DictReader(file)  # Create a CSV reader object
            data = {}
            index = 0

            for row in csv_reader:
                data.update({index: row})
                index += 1

        return {"contact_us": data, "count": index}


def write_to_file(headers, data, table_name):
    if "CON" == table_name:
        file_path = contact_us_cta_csv
    if "RES" == table_name:
        file_path = resources_data_1_csv

    with open(file_path, mode="a+") as file_object:
        file_object.seek(0)  # Set file pointer to BOF

        if 1 > len(file_object.readlines()):
            file_object.write(str(headers))  # Write headers if file content NULL

        file_object.write(str(data))
        file_object.write("\n")
    return


def read_from_json_file(resource):
    # Read from JSON file and return file contents as a JSON object
    if "RES" == resource:
        return_json_from_file(resources_data_1_json)
    if "MOD" == resource:
        return_json_from_file(models_data_1_json)


def return_json_from_file(file_name):
    with open(file_name, "r") as json_file:
        return json.load(json_file)


def write_to_json_file(json_object):  # Write a JSON object into a JSON file
    with open("sample.json", "w") as json_file:
        json.dump(json_object, json_file)
