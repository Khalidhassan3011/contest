import csv
from csv import writer
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

path = "C:/Users/KhaliD HassaN/Desktop/New folder/"

with open(path + 'test.csv', 'r') as file:
    reader = csv.reader(file)
    data = []
    i = 0
    # countRow = len(list(reader))
    # currentRow = 0
    for row in reader:
        # print("CURRENT: " + currentRow + " ROW LEFT:" + countRow - currentRow)
        # currentRow = currentRow + 1
        if i == 0:
            data.append(
                [
                    "id",
                    "lat",
                    "long",
                    "address",
                ]
            )
            i = i + 1
            continue
        else:
            try:
                uid = int(row[0])
                lat = row[1]
                long = row[2]

                tlat = lat

                if uid > 636797 and float(tlat) > 24.0 and float(tlat) < 25:
                    location = geolocator.reverse(lat + "," + long)
                    address = location.raw['address']
                    temp = [
                        row[0],
                        row[1],
                        row[2],
                        address.get('state_district', ''),
                    ]
                    print(temp)
                    data.append(temp)

                    with open(path + 'output.csv', 'a', newline='', encoding='utf-8') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(temp)
                        f_object.close()

                        # with open(path + 'output.csv', 'w', newline='', encoding='utf-8') as nfile:
                        # writer = csv.writer(nfile)
                        # writer.writerows(data)
            except:
                print(row)
                print("ERROR -> id: " + row[0] + " lat: " + row[1] + " long: " + row[2])
