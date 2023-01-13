import csv
import json

with open('output/veggies2.csv', 'r') as f:
    vegetables = csv.DictReader(f)
    rows = list(vegetables)
    print(rows)

green_veggies = []

with open('output/green_veggies.csv', 'w') as o:
    writer = csv.writer(o)
    for row in rows:
        if row['color'] == 'green':
            print(row)
            writer.writerow([row['name'], row['color'], str(row['length'])])

with open('output/green_veggies.json', 'w') as f:
    green_veggies = []

    for row in rows:
        if row['color'] == 'green':
            green_veggies.append(row)

    json.dump(green_veggies, f, indent=2)
