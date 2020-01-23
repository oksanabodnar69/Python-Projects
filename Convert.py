import json
import csv
import os.path
import argparse


def convert_csv_to_json(csvfilepath, jsonfilepath):
    if os.path.isfile(csvfilepath):
        with open(csvfilepath,'r') as csvfile:
            data={}
            reader = csv.DictReader(csvfile, delimiter=',')
            for rows in reader:
                if rows['password']:
                    rows['password'] = None
                    id = rows['user_id']
                    data[id] = rows
        with open(jsonfilepath,'w') as jsonfile:
            jsonfile.write(json.dumps(data,indent=4))
    else: print("File not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Please provide file path for CSV and JSON files')
    parser.add_argument('csv',help='provide a path to csv file')
    parser.add_argument('json',help='provide a path to JSON file')
    my_namespace = parser.parse_args()
    convert_csv_to_json(my_namespace.csv, my_namespace.json)
