import urllib.request, json


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

def read_file():
    file = open ("co-emission-out.csv","r")
    #file2 = open("co-emission-out.csv", "w")
    x =""
    pos=(0,0)
    for line in file.readlines()[1:]:
        print(line)
        comma = line.index(",")
        country = line[0:comma]
        if x != country:
            try:
                pos = count_to_pos(country)
                worked = True
            except IndexError:
                worked = False
            x=country
        if worked:
            line_to_add = pos[0]+","+pos[1]+","+line
            #file2.write(line_to_add)
    file.close()

def save_countries():
    L = []
    file = open("co-emission-out.csv", "r")
    # file2 = open("co-emission-out.csv", "w")
    x = ""
    pos = (0, 0)
    for line in file.readlines()[1:]:
        comma = line.index(",")
        country = line[comma+1:]
        comma = country.index(",")
        country = country[comma + 1:]
        comma = country.index(",")
        country = country[0:comma]

        if x != country:
            L.append(country)
            x = country
    print(L)
    file.close()
save_countries()
print("DONE!")