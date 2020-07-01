import sqlite3
import json
import codecs

conn = sqlite3.connect('yelpdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')

fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    js = json.dumps(row[1])
    js = js.split()
    stpos = js.index("'coordinates':")
    lat = js[stpos + 2]
    lat = lat.split(',')
    lat = float(lat[0])
    lng = js[stpos + 4]
    lng = lng.split('}')
    lng = float(lng[0])
    if lat == 0 or lng == 0 : continue
    where = row[0]
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue
    
fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
