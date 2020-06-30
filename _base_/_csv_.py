import csv

LEN = 8
MAX = 99

with open('T:\\data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(MAX + 1):
        pwd = str(i).zfill(LEN)
        print(pwd)
        if i == 0:
            writer.writerow(['id'])
        writer.writerow([f"{pwd}"])
