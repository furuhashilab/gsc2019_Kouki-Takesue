#!/usr/bin/env python
# coding: utf-8

# In[43]:


import xml.etree.ElementTree as ET
import gzip
import urllib.request
import sys
import time
import os
import json
import psycopg2

conn = psycopg2.connect("dbname=")
cur = conn.cursor()
cur.execute("create table if not exists sotsurontest4 (id int, stamp timestamp, lat double precision, lon double precision)")

def download():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    url1 = "https://planet.openstreetmap.org/replication/changesets/003/"
    url2 = int(580)
    url3 = int(1)
    url3_padded = '%03d' % url3

    while int(url2) < int(targetURLNUM):
        if url3 > 999:
            url2 += 1
            url3 = 1
            url3_padded = '%03d' % url3
            print("Next sequence " + str(url2))
        else:
            url = str(url1) + str(url2) +"/" + str(url3_padded) +".osm.gz"
            title = str(url3_padded) + ".osm.gz"
            req = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(req).read()
            with open(title, mode="wb") as f:
                f.write(response)

            time.sleep(0.1)

            osmfile = gzip.open(title,"rt","utf-8")
            tree = ET.parse(osmfile)
            root = tree.getroot()

            for e in root.findall('./changeset[@id][@created_at][@max_lat][@max_lon]'):
                if 122.55 <= float(e.attrib['max_lon']) <=153.59 and 20.25 <= float(e.attrib['max_lat']) <= 45.33:
                    cur.execute("INSERT INTO sotsurontest4 (id,stamp,lat,lon) VALUES(%s , '%s' , %s , %s)" % (e.attrib['id'], e.attrib['created_at'],e.attrib['max_lat'],e.attrib['max_lon']));
                    conn.commit()

            os.remove(title)
            print(title + " is compleate.")
            url3 += 1
            url3_padded = '%03d' % url3
    else:
        print("Finish!")
        conn.close()
        return

print("Welcome to OSMUC UPDATER")
targetURLNUM = input("PLS URL NUMBER ")

download()


# In[ ]:





# In[ ]:
