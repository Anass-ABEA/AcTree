import urllib.request, json

read = open ("death-rates-total-air-pollution.csv","r")
line1 = read.readline()

line1 = "Longitude,Latitude,"+line1
read.close()


def count_to_pos(country):
    c2 = ""
    for e in country:
        if e == " ":
            c2+="%20"
        else:
            c2+=e

    with urllib.request.urlopen(
            "http://nominatim.openstreetmap.org/search?country=" + c2 + "&format=json&polygon=0") as url:
        data = json.loads(url.read().decode())
        return data[0]["lon"],data[0]["lat"]

def update_csv():
    global line1
    read = open ("death-rates-total-air-pollution.csv","r")
    file_out = open ("death-rates-total-air-pollution-short_out.csv","w")
    file_out.write(line1)
    x = ""
    pos = (0, 0)
    for line in read.readlines()[1:]:
        if "2017" in line:
            comma = line.index(",")
            country = line[0:comma]
            if x != country:
                try:
                    pos = count_to_pos(country)
                    worked = True
                except IndexError:
                    worked = False
                x = country
            if worked:
                line_to_add = pos[0] + "," + pos[1] + "," + line
                print(line_to_add)
                file_out.write(line_to_add)
    file_out.close()

    read.close()

update_csv()