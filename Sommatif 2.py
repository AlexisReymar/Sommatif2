import json
import csv

with open("data.json","r") as json_file:
    complex_numbers = json.load(json_file)

with open("complex_numbers","w",newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["reel","imaginaire"])


    for number in complex_numbers:
        csv_writer.writerow(number)

print("Les nombres complexes on été écrits")
#