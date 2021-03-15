import csv
import os
import subprocess
import json

if __name__ == '__main__':
    with open('data/Table.csv', 'r', encoding='utf-8',
                 errors='ignore') as read_obj:
        csv_reader = csv.DictReader(read_obj, delimiter = ',')
        for row in csv_reader:
            url=row['URL']
            if url :
                try:
                    output = subprocess.run(["amphtml-validator", "%s" % url, "--format=json"], stdout=subprocess.PIPE, text=True)
                    output_dict = json.loads(output.stdout)
                    print(output_dict)
                except Exception as e:
                    print("An exception occurred")
                    print(e)


