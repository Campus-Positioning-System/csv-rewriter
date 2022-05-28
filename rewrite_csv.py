import csv

filtered = []
coords = []
matches = []
with open("csv_combined_unfiltered.csv", 'r') as readCSV:
    readerCSV = csv.reader(readCSV, delimiter=';')
    header = next(readerCSV)
    for rowCSV in readerCSV:
        ssid = rowCSV[2]
        if "HFU" in ssid or "eduroam" in ssid or "LAB" in ssid or "Lab" in ssid:
            filtered.append(rowCSV)
with open("nodereference.csv", 'r') as readRef:
    readerRef = csv.reader(readRef, delimiter=';')
    headerRef = next(readerRef)
    for rowRef in readerRef:
        coords.append(rowRef)
for k in range(len(coords)):
    for l in range(len(filtered)):
        if coords[k][0] == filtered[l][0]:
            filtered[l][0] = coords[k][1]
            matches.append(filtered[l])
with open("csv_combined_filtered.csv", 'w', newline='') as writefile:
    writer = csv.writer(writefile, delimiter=';')
    writer.writerow(header)
    for row in matches:
        writer.writerow(row)
