import csv

data = [
]

# Use w to overwrite a file, use a to append to a file (w is probably fine)
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open('example.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
