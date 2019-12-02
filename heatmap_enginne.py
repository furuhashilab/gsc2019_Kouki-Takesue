import folium
from folium.plugins import HeatMap

conn = psycopg2.connect("dbname=test user=badapple444");
cur = conn.cursor()

m = folium.Map(location=[36,135])

cur.execute("SELECT * FROM geolattest3");
x = cur.fetchall()
print(x)
HeatMap(x).add_to(m)

m
