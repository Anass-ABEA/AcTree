import json
import urllib

read = open ("co2-concentration-long-term.csv","r")
List = read.readlines()
n = len(List)
out = List[0:1]+ List[n-6:]
out[0] = "Longitude,Latitude,"+out[0]
print (out)
read.close()
write = open ("co2-concentration-long-term-short.csv","w")
for e in out:
    write.write(e)
write.close()
