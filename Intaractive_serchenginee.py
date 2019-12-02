#!/usr/bin/env python
# coding: utf-8

import requests
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import psycopg2

conn = psycopg2.connect("dbname=test user=badapple444")
cur = conn.cursor()
cur.execute("create table if not exists herokutest (lat double precision, lon double precision, stamp timestamp)")
cur.execute("create table if not exists searchnumber (changesetnumber int)")

def changesetloop(setnumber):
    url = "https://www.openstreetmap.org/api/0.6/changeset/" + str(setnumber)

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        xml_string = response.read()
    root = ET.fromstring(xml_string)

    child = root[0]

    osm = str(child.attrib)
    osm2 = osm.split()
    try:
        lat_p = osm2[17].strip("','")
        lon_p = osm2[19].strip("','")
        stamp = osm2[5].strip("','")
    except IndexError:
        return print('%s is out of range type.' % setnumber)

    req_url = "http://www.finds.jp/ws/rgeocode.php?lat={0}&lon={1}&json" .format(lat_p, lon_p)

    res = requests.get(req_url).text
    jpcheck = json.loads(res)["status"]

    try:
        if not jpcheck  == 200:
            return print('%s is not Japan.' % setnumber)
        else:
            cur.execute("INSERT INTO herokutest (lat , lon , stamp) VALUES(%s , %s , '%s')" % (lat_p , lon_p , stamp));
            conn.commit()
            return print('%s is compleated.' % setnumber)
    except ValueError:
        return print('%s is unformat xml type.' % setnumber)
"""
  try:
        if 123 <= float(lon_p) <=140:
            item = (lat_p ,lon_p)
            cur.execute("INSERT INTO geolatlon VALUES (? , ?)" , item)
            conn.commit()
            return print('%s is compleated.' % setnumber)
        else:
            return print('%s is not Japan.' % setnumber)
    except ValueError:
        return print('%s is unformat xml type.' % setnumber)
"""

print("Welcome to OSM UPDETA CHECKER Chengeset finder.")

cur.execute("select * from searchnumber");
searNum = cur.fetchone()
SearNum = int(searNum[0])

rangeNum = input("Plese input range number : ")
RangeNum = int (rangeNum)

print("OK. we will find " + str(RangeNum) + " changesets from " + str(SearNum) )

for searchchange in range(RangeNum):
    changesetloop(SearNum)
    SearNum +=1
    cur.execute("update searchnumber set changesetnumber = %s" % (SearNum))
    conn.commit()

conn.close()
