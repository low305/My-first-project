# This part of the application gets the raw search results from each county cleans them up 
# and stores them in a database. 
import time
import requests
import json
import sqlite3

api_key = 'mlLvj..........TnXnYx' ## Put your yelp API key here
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'

conn = sqlite3.connect('yelpdb.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations
         (business TEXT UNIQUE, geodata TEXT UNIQUE)''')

fh = open('counties.txt')

for county in fh:
    county = county.rstrip()
    
    ### set and add prams make request ###
    locapram = county
    params = {'term':'landscaping','location': locapram}
    req = requests.get(url, params = params, headers = headers)
    
    ###gets the status code###
    status = int(format(req.status_code))
    print('The status code is', status)
    
    ### checks to make sure status is 200 ###
    if status != 200:
        print('Failed to retrive search', locapram)
        print('')
        continue
    
    ### checks if data in search ###
    data = json.loads(req.text)
    if len(data['businesses']) == 0:
        print('the search', locapram, 'returned no data')
        print('')
        continue
    
    ### prints how many results found per county ###
    print('Retrivied', len(data['businesses']), '''Results from search
for Landscaping companies''', locapram)
    print('')
     
    bus = 0
    count = len(data['businesses'])
    while count > 0:
        print(county)
        res = data['businesses'][bus]
        busname = data['businesses'][bus]['name']
        print(json.dumps(res, indent = 4))
        bus += 1
        count -= 1
        print('')
        print('')
        strres = str(res)
        
    ###insert data into database and commit to disk###
        cur.execute('''INSERT OR IGNORE INTO Locations (business, geodata)
                    VALUES ( ?, ? )''', (busname, strres))
        conn.commit()
    
