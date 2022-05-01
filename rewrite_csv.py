import csv

matches = []
with open("AP-Referenzdaten.csv", 'r') as readfile:
    reader = csv.reader(readfile, delimiter=';')
    header = next(reader)
    for row in reader:
        ssid = row[1]
        if "HFU" in ssid or "eduroam" in ssid or "LAB" in ssid or "Lab" in ssid:
            matches.append(row)
with open("AP-Referenzdaten_filtered.csv", 'w', newline='') as writefile:
    writer = csv.writer(writefile, delimiter=';')
    writer.writerow(header)
    for row in matches:
        writer.writerow(row)
