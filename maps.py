import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
lat=data["LAT"]
lon=data["LON"]
el=data["ELEV"]
map=folium.Map(location=[39,-111])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<elevation<3000:
        return 'orange'
    else:
        return 'red'
fg_v=folium.FeatureGroup("Volcanoes")
for i, j, z in zip(lat,lon,el):
    fg_v.add_child(folium.CircleMarker(location=[i,j], radius=6, popup=str(z)+" Elevation in Meters",
    fill_color=color_producer(z),color='grey', fill_opacity=0.7))
fg=folium.FeatureGroup("Population")
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'green' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fg_v)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
