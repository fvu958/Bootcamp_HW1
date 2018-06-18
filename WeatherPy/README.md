
- Temperature increases as we approach the equator.
- There is very little correlation between cloudiness and latitude.
- There is a weak correlation between wind speed and latitude.


```python
import json
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import requests
from pprint import pprint
from citipy import citipy
from config import api_key
% matplotlib inline
```


```python
lat = {'min': -90, 'max': 90}
long = {'min': -180, 'max': 180}
```


```python
lat_values = np.arange(lat['min'], lat['max'],  0.01)
lon_values =  np.arange(lat['min'], lat['max'], 0.01)
```


```python
cols = ['City Name','Country Code','Random Lat','Random Lon','Latitude','Longitude','Temp (F)','Humidity (%)','Cloudiness (%)','Wind Speed (mph)']
```


```python
df = pd.DataFrame(columns=cols)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City Name</th>
      <th>Country Code</th>
      <th>Random Lat</th>
      <th>Random Lon</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temp (F)</th>
      <th>Humidity (%)</th>
      <th>Cloudiness (%)</th>
      <th>Wind Speed (mph)</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
sample = 500
count = 0
```


```python
while len(df) < sample:
    random_lat = random.choice(lat_values)
    random_lon = random.choice(lon_values)
    
    city = citipy.nearest_city(random_lat, random_lon)
    name = city.city_name
    country_code = city.country_code
    units = 'imperial'
    
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

    url = base_url + name + ',' + country_code + '&units=' + units + '&APPID=' + api_key
    weather_response = requests.get(url)
    weather_data = weather_response.json()
    
    if weather_data['cod'] == 200:
        print('City: %s. %s' % (weather_data['name'], url))
        latitude = weather_data['coord']['lat']
        longitude = weather_data['coord']['lon']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        clouds = weather_data['clouds']['all']
        wind = weather_data['wind']['speed']
        
        if name not in df['City Name'].values:
            df.at[count, "City Name"] = name
            df.at[count, "Country Code"] = country_code
            df.at[count, "Random Lat",] = random_lat
            df.at[count, "Random Lon"] = random_lon
            df.at[count, "Latitude"] = latitude
            df.at[count, "Longitude"] = longitude
            df.at[count, "Temp (F)"] = temp
            df.at[count, "Humidity (%)"] = humidity
            df.at[count, "Cloudiness (%)"] = clouds
            df.at[count, "Wind Speed (mph)"] = wind

            count += 1
            
        else:
            pass
    else:
        pass
```

    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Isabel do Rio Negro. http://api.openweathermap.org/data/2.5/weather?q=santa isabel do rio negro,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Galle. http://api.openweathermap.org/data/2.5/weather?q=galle,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Guadalajara. http://api.openweathermap.org/data/2.5/weather?q=guadalajara,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Agadez. http://api.openweathermap.org/data/2.5/weather?q=agadez,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pisco. http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Leh. http://api.openweathermap.org/data/2.5/weather?q=leh,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Itarema. http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Leamington. http://api.openweathermap.org/data/2.5/weather?q=leamington,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maldonado. http://api.openweathermap.org/data/2.5/weather?q=maldonado,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gravdal. http://api.openweathermap.org/data/2.5/weather?q=gravdal,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Margate. http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aguimes. http://api.openweathermap.org/data/2.5/weather?q=aguimes,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: The Valley. http://api.openweathermap.org/data/2.5/weather?q=the valley,ai&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Cruz. http://api.openweathermap.org/data/2.5/weather?q=santa cruz,cr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Cruz Cabralia. http://api.openweathermap.org/data/2.5/weather?q=santa cruz cabralia,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Niles. http://api.openweathermap.org/data/2.5/weather?q=niles,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Joao da Barra. http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Turayf. http://api.openweathermap.org/data/2.5/weather?q=turayf,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camacha. http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Somerset. http://api.openweathermap.org/data/2.5/weather?q=somerset,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Le Port. http://api.openweathermap.org/data/2.5/weather?q=le port,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Buzmeyin. http://api.openweathermap.org/data/2.5/weather?q=buzmeyin,tm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangnirtung. http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Alta. http://api.openweathermap.org/data/2.5/weather?q=punta alta,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tanout. http://api.openweathermap.org/data/2.5/weather?q=tanout,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muros. http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalmunai. http://api.openweathermap.org/data/2.5/weather?q=kalmunai,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krasnovishersk. http://api.openweathermap.org/data/2.5/weather?q=krasnovishersk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gurjaani. http://api.openweathermap.org/data/2.5/weather?q=gurjaani,ge&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Umm Lajj. http://api.openweathermap.org/data/2.5/weather?q=umm lajj,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atasu. http://api.openweathermap.org/data/2.5/weather?q=atasu,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vesyegonsk. http://api.openweathermap.org/data/2.5/weather?q=vesyegonsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bubaque. http://api.openweathermap.org/data/2.5/weather?q=bubaque,gw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: West Bay. http://api.openweathermap.org/data/2.5/weather?q=west bay,ky&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Conde. http://api.openweathermap.org/data/2.5/weather?q=conde,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Grande. http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Felix do Xingu. http://api.openweathermap.org/data/2.5/weather?q=sao felix do xingu,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Katima Mulilo. http://api.openweathermap.org/data/2.5/weather?q=katima mulilo,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tiznit. http://api.openweathermap.org/data/2.5/weather?q=tiznit,ma&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vire. http://api.openweathermap.org/data/2.5/weather?q=vire,fr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Manitouwadge. http://api.openweathermap.org/data/2.5/weather?q=manitouwadge,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kaspiyskiy. http://api.openweathermap.org/data/2.5/weather?q=kaspiyskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Elgin. http://api.openweathermap.org/data/2.5/weather?q=elgin,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rosetta. http://api.openweathermap.org/data/2.5/weather?q=rosetta,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Koungheul. http://api.openweathermap.org/data/2.5/weather?q=koungheul,sn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ritchie. http://api.openweathermap.org/data/2.5/weather?q=ritchie,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mitsamiouli. http://api.openweathermap.org/data/2.5/weather?q=mitsamiouli,km&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Guarapari. http://api.openweathermap.org/data/2.5/weather?q=guarapari,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sandovo. http://api.openweathermap.org/data/2.5/weather?q=sandovo,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gunjur. http://api.openweathermap.org/data/2.5/weather?q=gunjur,gm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dajabon. http://api.openweathermap.org/data/2.5/weather?q=dajabon,do&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coihaique. http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sabha. http://api.openweathermap.org/data/2.5/weather?q=sabha,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Thinadhoo. http://api.openweathermap.org/data/2.5/weather?q=thinadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lewisville. http://api.openweathermap.org/data/2.5/weather?q=lewisville,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Novyy Urengoy. http://api.openweathermap.org/data/2.5/weather?q=novyy urengoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salinopolis. http://api.openweathermap.org/data/2.5/weather?q=salinopolis,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jalu. http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chicama. http://api.openweathermap.org/data/2.5/weather?q=chicama,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Francois. http://api.openweathermap.org/data/2.5/weather?q=saint-francois,gp&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Moroni. http://api.openweathermap.org/data/2.5/weather?q=moroni,km&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kayerkan. http://api.openweathermap.org/data/2.5/weather?q=kayerkan,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Roald. http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jalu. http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chimore. http://api.openweathermap.org/data/2.5/weather?q=chimore,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vredendal. http://api.openweathermap.org/data/2.5/weather?q=vredendal,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cangas. http://api.openweathermap.org/data/2.5/weather?q=cangas,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pisco. http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Basoko. http://api.openweathermap.org/data/2.5/weather?q=basoko,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oranjestad. http://api.openweathermap.org/data/2.5/weather?q=oranjestad,aw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vuktyl. http://api.openweathermap.org/data/2.5/weather?q=vuktyl,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camargo. http://api.openweathermap.org/data/2.5/weather?q=camargo,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bhuj. http://api.openweathermap.org/data/2.5/weather?q=bhuj,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Boende. http://api.openweathermap.org/data/2.5/weather?q=boende,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Henties Bay. http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dabhol. http://api.openweathermap.org/data/2.5/weather?q=dabhol,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taltal. http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Giyon. http://api.openweathermap.org/data/2.5/weather?q=giyon,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mange. http://api.openweathermap.org/data/2.5/weather?q=mange,sl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gilgit. http://api.openweathermap.org/data/2.5/weather?q=gilgit,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bouna. http://api.openweathermap.org/data/2.5/weather?q=bouna,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Brezice. http://api.openweathermap.org/data/2.5/weather?q=brezice,si&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: At-Bashi. http://api.openweathermap.org/data/2.5/weather?q=at-bashi,kg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paamiut. http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Novobirilyussy. http://api.openweathermap.org/data/2.5/weather?q=novobirilyussy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hukuntsi. http://api.openweathermap.org/data/2.5/weather?q=hukuntsi,bw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Leshukonskoye. http://api.openweathermap.org/data/2.5/weather?q=leshukonskoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Anloga. http://api.openweathermap.org/data/2.5/weather?q=anloga,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Juan. http://api.openweathermap.org/data/2.5/weather?q=san juan,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Akdepe. http://api.openweathermap.org/data/2.5/weather?q=akdepe,tm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Grande. http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hammerfest. http://api.openweathermap.org/data/2.5/weather?q=hammerfest,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Moron. http://api.openweathermap.org/data/2.5/weather?q=moron,ve&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bud. http://api.openweathermap.org/data/2.5/weather?q=bud,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Keti Bandar. http://api.openweathermap.org/data/2.5/weather?q=keti bandar,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Campo Formoso. http://api.openweathermap.org/data/2.5/weather?q=campo formoso,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camacha. http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ancud. http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tessalit. http://api.openweathermap.org/data/2.5/weather?q=tessalit,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kaduna. http://api.openweathermap.org/data/2.5/weather?q=kaduna,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ngorongoro. http://api.openweathermap.org/data/2.5/weather?q=ngorongoro,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Znamenskoye. http://api.openweathermap.org/data/2.5/weather?q=znamenskoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dirba. http://api.openweathermap.org/data/2.5/weather?q=dirba,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saryozek. http://api.openweathermap.org/data/2.5/weather?q=saryozek,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puerto Carreno. http://api.openweathermap.org/data/2.5/weather?q=puerto carreno,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ankazoabo. http://api.openweathermap.org/data/2.5/weather?q=ankazoabo,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tupiza. http://api.openweathermap.org/data/2.5/weather?q=tupiza,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cascais. http://api.openweathermap.org/data/2.5/weather?q=cascais,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Riyadh. http://api.openweathermap.org/data/2.5/weather?q=riyadh,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bumba. http://api.openweathermap.org/data/2.5/weather?q=bumba,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kisangani. http://api.openweathermap.org/data/2.5/weather?q=kisangani,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Beloha. http://api.openweathermap.org/data/2.5/weather?q=beloha,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matay. http://api.openweathermap.org/data/2.5/weather?q=matay,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Boquira. http://api.openweathermap.org/data/2.5/weather?q=boquira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jaleswar. http://api.openweathermap.org/data/2.5/weather?q=jaleswar,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Franca do Campo. http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Leesburg. http://api.openweathermap.org/data/2.5/weather?q=leesburg,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Waddan. http://api.openweathermap.org/data/2.5/weather?q=waddan,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Conceicao do Araguaia. http://api.openweathermap.org/data/2.5/weather?q=conceicao do araguaia,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Loanda. http://api.openweathermap.org/data/2.5/weather?q=loanda,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Gallegos. http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Porto Novo. http://api.openweathermap.org/data/2.5/weather?q=porto novo,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mabaruma. http://api.openweathermap.org/data/2.5/weather?q=mabaruma,gy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abu Zabad. http://api.openweathermap.org/data/2.5/weather?q=abu zabad,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bay Saint Louis. http://api.openweathermap.org/data/2.5/weather?q=bay saint louis,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aswan. http://api.openweathermap.org/data/2.5/weather?q=aswan,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sol-Iletsk. http://api.openweathermap.org/data/2.5/weather?q=sol-iletsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Scarborough. http://api.openweathermap.org/data/2.5/weather?q=scarborough,tt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kormilovka. http://api.openweathermap.org/data/2.5/weather?q=kormilovka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Proletariy. http://api.openweathermap.org/data/2.5/weather?q=proletariy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kovdor. http://api.openweathermap.org/data/2.5/weather?q=kovdor,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pisco. http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nara. http://api.openweathermap.org/data/2.5/weather?q=nara,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dubai. http://api.openweathermap.org/data/2.5/weather?q=dubai,ae&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lakota. http://api.openweathermap.org/data/2.5/weather?q=lakota,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Udomlya. http://api.openweathermap.org/data/2.5/weather?q=udomlya,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luanda. http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oschatz. http://api.openweathermap.org/data/2.5/weather?q=oschatz,de&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hornepayne. http://api.openweathermap.org/data/2.5/weather?q=hornepayne,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mega. http://api.openweathermap.org/data/2.5/weather?q=mega,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nara. http://api.openweathermap.org/data/2.5/weather?q=nara,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Omboue. http://api.openweathermap.org/data/2.5/weather?q=omboue,ga&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Gallegos. http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sistranda. http://api.openweathermap.org/data/2.5/weather?q=sistranda,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rawson. http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Fenoarivo. http://api.openweathermap.org/data/2.5/weather?q=fenoarivo,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Alvorada. http://api.openweathermap.org/data/2.5/weather?q=alvorada,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sisimiut. http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Franca do Campo. http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bulungu. http://api.openweathermap.org/data/2.5/weather?q=bulungu,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kenosha. http://api.openweathermap.org/data/2.5/weather?q=kenosha,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Berlevag. http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mumbwa. http://api.openweathermap.org/data/2.5/weather?q=mumbwa,zm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Loknya. http://api.openweathermap.org/data/2.5/weather?q=loknya,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Guarapari. http://api.openweathermap.org/data/2.5/weather?q=guarapari,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bela. http://api.openweathermap.org/data/2.5/weather?q=bela,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zhanakorgan. http://api.openweathermap.org/data/2.5/weather?q=zhanakorgan,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Huarmey. http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Maria. http://api.openweathermap.org/data/2.5/weather?q=santa maria,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salinopolis. http://api.openweathermap.org/data/2.5/weather?q=salinopolis,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coromandel. http://api.openweathermap.org/data/2.5/weather?q=coromandel,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Betanzos. http://api.openweathermap.org/data/2.5/weather?q=betanzos,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Trairi. http://api.openweathermap.org/data/2.5/weather?q=trairi,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grindavik. http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taybad. http://api.openweathermap.org/data/2.5/weather?q=taybad,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Serdobsk. http://api.openweathermap.org/data/2.5/weather?q=serdobsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kaele. http://api.openweathermap.org/data/2.5/weather?q=kaele,cm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Naron. http://api.openweathermap.org/data/2.5/weather?q=naron,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ordu. http://api.openweathermap.org/data/2.5/weather?q=ordu,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Didwana. http://api.openweathermap.org/data/2.5/weather?q=didwana,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Malacky. http://api.openweathermap.org/data/2.5/weather?q=malacky,sk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arlit. http://api.openweathermap.org/data/2.5/weather?q=arlit,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Niny. http://api.openweathermap.org/data/2.5/weather?q=niny,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Anupgarh. http://api.openweathermap.org/data/2.5/weather?q=anupgarh,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Thunder Bay. http://api.openweathermap.org/data/2.5/weather?q=thunder bay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shevchenkove. http://api.openweathermap.org/data/2.5/weather?q=shevchenkove,ua&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Andres. http://api.openweathermap.org/data/2.5/weather?q=san andres,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bahia Blanca. http://api.openweathermap.org/data/2.5/weather?q=bahia blanca,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mezen. http://api.openweathermap.org/data/2.5/weather?q=mezen,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marsa Matruh. http://api.openweathermap.org/data/2.5/weather?q=marsa matruh,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shelburne. http://api.openweathermap.org/data/2.5/weather?q=shelburne,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puerto Carreno. http://api.openweathermap.org/data/2.5/weather?q=puerto carreno,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dapaong. http://api.openweathermap.org/data/2.5/weather?q=dapaong,tg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Gabriel da Cachoeira. http://api.openweathermap.org/data/2.5/weather?q=sao gabriel da cachoeira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arlit. http://api.openweathermap.org/data/2.5/weather?q=arlit,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lobito. http://api.openweathermap.org/data/2.5/weather?q=lobito,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Itarantim. http://api.openweathermap.org/data/2.5/weather?q=itarantim,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cerkezkoy. http://api.openweathermap.org/data/2.5/weather?q=cerkezkoy,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vestmanna. http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Danville. http://api.openweathermap.org/data/2.5/weather?q=danville,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iquique. http://api.openweathermap.org/data/2.5/weather?q=iquique,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iranshahr. http://api.openweathermap.org/data/2.5/weather?q=iranshahr,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ibra. http://api.openweathermap.org/data/2.5/weather?q=ibra,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ballina. http://api.openweathermap.org/data/2.5/weather?q=ballina,ie&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Riyadh. http://api.openweathermap.org/data/2.5/weather?q=riyadh,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paita. http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ust-Tsilma. http://api.openweathermap.org/data/2.5/weather?q=ust-tsilma,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camocim. http://api.openweathermap.org/data/2.5/weather?q=camocim,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carballo. http://api.openweathermap.org/data/2.5/weather?q=carballo,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Niteroi. http://api.openweathermap.org/data/2.5/weather?q=niteroi,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Los Llanos de Aridane. http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Leh. http://api.openweathermap.org/data/2.5/weather?q=leh,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Guararapes. http://api.openweathermap.org/data/2.5/weather?q=guararapes,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Macon. http://api.openweathermap.org/data/2.5/weather?q=macon,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marsa Matruh. http://api.openweathermap.org/data/2.5/weather?q=marsa matruh,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sur. http://api.openweathermap.org/data/2.5/weather?q=sur,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pasni. http://api.openweathermap.org/data/2.5/weather?q=pasni,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Richards Bay. http://api.openweathermap.org/data/2.5/weather?q=richards bay,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Natal. http://api.openweathermap.org/data/2.5/weather?q=natal,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shache. http://api.openweathermap.org/data/2.5/weather?q=shache,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bocas del Toro. http://api.openweathermap.org/data/2.5/weather?q=bocas del toro,pa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bonthe. http://api.openweathermap.org/data/2.5/weather?q=bonthe,sl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Machiques. http://api.openweathermap.org/data/2.5/weather?q=machiques,ve&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punalur. http://api.openweathermap.org/data/2.5/weather?q=punalur,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santiago del Estero. http://api.openweathermap.org/data/2.5/weather?q=santiago del estero,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namibe. http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namibe. http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rawson. http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tabou. http://api.openweathermap.org/data/2.5/weather?q=tabou,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ballina. http://api.openweathermap.org/data/2.5/weather?q=ballina,ie&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kargil. http://api.openweathermap.org/data/2.5/weather?q=kargil,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krasnovishersk. http://api.openweathermap.org/data/2.5/weather?q=krasnovishersk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matara. http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Buchanan. http://api.openweathermap.org/data/2.5/weather?q=buchanan,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kitangari. http://api.openweathermap.org/data/2.5/weather?q=kitangari,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aligudarz. http://api.openweathermap.org/data/2.5/weather?q=aligudarz,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Meulaboh. http://api.openweathermap.org/data/2.5/weather?q=meulaboh,id&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Darnah. http://api.openweathermap.org/data/2.5/weather?q=darnah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Glens Falls. http://api.openweathermap.org/data/2.5/weather?q=glens falls,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalevala. http://api.openweathermap.org/data/2.5/weather?q=kalevala,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matara. http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tocopilla. http://api.openweathermap.org/data/2.5/weather?q=tocopilla,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Buraydah. http://api.openweathermap.org/data/2.5/weather?q=buraydah,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jumla. http://api.openweathermap.org/data/2.5/weather?q=jumla,np&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mocuba. http://api.openweathermap.org/data/2.5/weather?q=mocuba,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Basse-Pointe. http://api.openweathermap.org/data/2.5/weather?q=basse-pointe,mq&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Joao da Barra. http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Praia da Vitoria. http://api.openweathermap.org/data/2.5/weather?q=praia da vitoria,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matadi. http://api.openweathermap.org/data/2.5/weather?q=matadi,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangnirtung. http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta Delgada. http://api.openweathermap.org/data/2.5/weather?q=ponta delgada,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Benguela. http://api.openweathermap.org/data/2.5/weather?q=benguela,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Elizabeth City. http://api.openweathermap.org/data/2.5/weather?q=elizabeth city,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kvarkeno. http://api.openweathermap.org/data/2.5/weather?q=kvarkeno,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puerto Leguizamo. http://api.openweathermap.org/data/2.5/weather?q=puerto leguizamo,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Alta Floresta. http://api.openweathermap.org/data/2.5/weather?q=alta floresta,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sochi. http://api.openweathermap.org/data/2.5/weather?q=sochi,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Awbari. http://api.openweathermap.org/data/2.5/weather?q=awbari,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Berlevag. http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Usinsk. http://api.openweathermap.org/data/2.5/weather?q=usinsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tromso. http://api.openweathermap.org/data/2.5/weather?q=tromso,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lukovetskiy. http://api.openweathermap.org/data/2.5/weather?q=lukovetskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Eganville. http://api.openweathermap.org/data/2.5/weather?q=eganville,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Maria. http://api.openweathermap.org/data/2.5/weather?q=santa maria,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oyem. http://api.openweathermap.org/data/2.5/weather?q=oyem,ga&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pasni. http://api.openweathermap.org/data/2.5/weather?q=pasni,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Progreso. http://api.openweathermap.org/data/2.5/weather?q=progreso,mx&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Soyo. http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostersund. http://api.openweathermap.org/data/2.5/weather?q=ostersund,se&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tallahassee. http://api.openweathermap.org/data/2.5/weather?q=tallahassee,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ibra. http://api.openweathermap.org/data/2.5/weather?q=ibra,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Doka. http://api.openweathermap.org/data/2.5/weather?q=doka,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qasigiannguit. http://api.openweathermap.org/data/2.5/weather?q=qasigiannguit,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Inta. http://api.openweathermap.org/data/2.5/weather?q=inta,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Urambo. http://api.openweathermap.org/data/2.5/weather?q=urambo,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ivankiv. http://api.openweathermap.org/data/2.5/weather?q=ivankiv,ua&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Adrar. http://api.openweathermap.org/data/2.5/weather?q=adrar,dz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Komarikhinskiy. http://api.openweathermap.org/data/2.5/weather?q=komarikhinskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puerto Suarez. http://api.openweathermap.org/data/2.5/weather?q=puerto suarez,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Makat. http://api.openweathermap.org/data/2.5/weather?q=makat,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pizarro. http://api.openweathermap.org/data/2.5/weather?q=pizarro,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kyzyl-Suu. http://api.openweathermap.org/data/2.5/weather?q=kyzyl-suu,kg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Plettenberg Bay. http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Komsomolskiy. http://api.openweathermap.org/data/2.5/weather?q=komsomolskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Fuengirola. http://api.openweathermap.org/data/2.5/weather?q=fuengirola,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nizhnekamsk. http://api.openweathermap.org/data/2.5/weather?q=nizhnekamsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Augustin. http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oktyabrskoye. http://api.openweathermap.org/data/2.5/weather?q=oktyabrskoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mabaruma. http://api.openweathermap.org/data/2.5/weather?q=mabaruma,gy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aasiaat. http://api.openweathermap.org/data/2.5/weather?q=aasiaat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Falavarjan. http://api.openweathermap.org/data/2.5/weather?q=falavarjan,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dudinka. http://api.openweathermap.org/data/2.5/weather?q=dudinka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nizwa. http://api.openweathermap.org/data/2.5/weather?q=nizwa,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Asuncion. http://api.openweathermap.org/data/2.5/weather?q=asuncion,py&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atbasar. http://api.openweathermap.org/data/2.5/weather?q=atbasar,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vargem Grande do Sul. http://api.openweathermap.org/data/2.5/weather?q=vargem grande do sul,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aleksandrov Gay. http://api.openweathermap.org/data/2.5/weather?q=aleksandrov gay,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Graaff-Reinet. http://api.openweathermap.org/data/2.5/weather?q=graaff-reinet,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Uvarovka. http://api.openweathermap.org/data/2.5/weather?q=uvarovka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Doha. http://api.openweathermap.org/data/2.5/weather?q=doha,qa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Balassagyarmat. http://api.openweathermap.org/data/2.5/weather?q=balassagyarmat,hu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapleau. http://api.openweathermap.org/data/2.5/weather?q=chapleau,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Apatity. http://api.openweathermap.org/data/2.5/weather?q=apatity,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bo. http://api.openweathermap.org/data/2.5/weather?q=bo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bolobo. http://api.openweathermap.org/data/2.5/weather?q=bolobo,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muros. http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Uaua. http://api.openweathermap.org/data/2.5/weather?q=uaua,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Rafael. http://api.openweathermap.org/data/2.5/weather?q=san rafael,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tocopilla. http://api.openweathermap.org/data/2.5/weather?q=tocopilla,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ancud. http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cockburn Town. http://api.openweathermap.org/data/2.5/weather?q=cockburn town,bs&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Valparaiso. http://api.openweathermap.org/data/2.5/weather?q=valparaiso,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sume. http://api.openweathermap.org/data/2.5/weather?q=sume,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iquitos. http://api.openweathermap.org/data/2.5/weather?q=iquitos,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paita. http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Barauna. http://api.openweathermap.org/data/2.5/weather?q=barauna,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Capoterra. http://api.openweathermap.org/data/2.5/weather?q=capoterra,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mirnyy. http://api.openweathermap.org/data/2.5/weather?q=mirnyy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Plettenberg Bay. http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nouadhibou. http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ancud. http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Inta. http://api.openweathermap.org/data/2.5/weather?q=inta,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dir. http://api.openweathermap.org/data/2.5/weather?q=dir,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castelbuono. http://api.openweathermap.org/data/2.5/weather?q=castelbuono,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pascagoula. http://api.openweathermap.org/data/2.5/weather?q=pascagoula,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Hawkesbury. http://api.openweathermap.org/data/2.5/weather?q=port hawkesbury,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abu Dhabi. http://api.openweathermap.org/data/2.5/weather?q=abu dhabi,ae&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rocha. http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vestmanna. http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Humberto de Campos. http://api.openweathermap.org/data/2.5/weather?q=humberto de campos,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Henties Bay. http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Acari. http://api.openweathermap.org/data/2.5/weather?q=acari,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nizwa. http://api.openweathermap.org/data/2.5/weather?q=nizwa,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rocha. http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Placetas. http://api.openweathermap.org/data/2.5/weather?q=placetas,cu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kuhdasht. http://api.openweathermap.org/data/2.5/weather?q=kuhdasht,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bandarbeyla. http://api.openweathermap.org/data/2.5/weather?q=bandarbeyla,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Olinda. http://api.openweathermap.org/data/2.5/weather?q=olinda,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tabory. http://api.openweathermap.org/data/2.5/weather?q=tabory,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rosetta. http://api.openweathermap.org/data/2.5/weather?q=rosetta,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ploemeur. http://api.openweathermap.org/data/2.5/weather?q=ploemeur,fr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rezekne. http://api.openweathermap.org/data/2.5/weather?q=rezekne,lv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sisimiut. http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Wilmington. http://api.openweathermap.org/data/2.5/weather?q=wilmington,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Benguela. http://api.openweathermap.org/data/2.5/weather?q=benguela,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: La Rochelle. http://api.openweathermap.org/data/2.5/weather?q=la rochelle,fr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hudson. http://api.openweathermap.org/data/2.5/weather?q=hudson,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapais. http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lively. http://api.openweathermap.org/data/2.5/weather?q=lively,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Middelburg. http://api.openweathermap.org/data/2.5/weather?q=middelburg,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Opuwo. http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tahta. http://api.openweathermap.org/data/2.5/weather?q=tahta,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Artyom. http://api.openweathermap.org/data/2.5/weather?q=artyom,az&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Asosa. http://api.openweathermap.org/data/2.5/weather?q=asosa,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coquimbo. http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Brae. http://api.openweathermap.org/data/2.5/weather?q=brae,gb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mutoko. http://api.openweathermap.org/data/2.5/weather?q=mutoko,zw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Semirom. http://api.openweathermap.org/data/2.5/weather?q=semirom,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Berasia. http://api.openweathermap.org/data/2.5/weather?q=berasia,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mandal. http://api.openweathermap.org/data/2.5/weather?q=mandal,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maceio. http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paamiut. http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Labytnangi. http://api.openweathermap.org/data/2.5/weather?q=labytnangi,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovskoye. http://api.openweathermap.org/data/2.5/weather?q=ostrovskoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Colorado. http://api.openweathermap.org/data/2.5/weather?q=colorado,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kimberley. http://api.openweathermap.org/data/2.5/weather?q=kimberley,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Natal. http://api.openweathermap.org/data/2.5/weather?q=natal,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Najran. http://api.openweathermap.org/data/2.5/weather?q=najran,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapada dos Guimaraes. http://api.openweathermap.org/data/2.5/weather?q=chapada dos guimaraes,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Guabito. http://api.openweathermap.org/data/2.5/weather?q=guabito,pa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tazovskiy. http://api.openweathermap.org/data/2.5/weather?q=tazovskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coquimbo. http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puerto del Rosario. http://api.openweathermap.org/data/2.5/weather?q=puerto del rosario,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Jose da Coroa Grande. http://api.openweathermap.org/data/2.5/weather?q=sao jose da coroa grande,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangody. http://api.openweathermap.org/data/2.5/weather?q=pangody,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangnirtung. http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narasannapeta. http://api.openweathermap.org/data/2.5/weather?q=narasannapeta,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kursavka. http://api.openweathermap.org/data/2.5/weather?q=kursavka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Liverpool. http://api.openweathermap.org/data/2.5/weather?q=liverpool,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Isiolo. http://api.openweathermap.org/data/2.5/weather?q=isiolo,ke&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ancud. http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dijkot. http://api.openweathermap.org/data/2.5/weather?q=dijkot,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tarquinia. http://api.openweathermap.org/data/2.5/weather?q=tarquinia,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zelenoborskiy. http://api.openweathermap.org/data/2.5/weather?q=zelenoborskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jacareacanga. http://api.openweathermap.org/data/2.5/weather?q=jacareacanga,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Misratah. http://api.openweathermap.org/data/2.5/weather?q=misratah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nuuk. http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vawkavysk. http://api.openweathermap.org/data/2.5/weather?q=vawkavysk,by&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ordzhonikidze. http://api.openweathermap.org/data/2.5/weather?q=ordzhonikidze,ua&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bolobo. http://api.openweathermap.org/data/2.5/weather?q=bolobo,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalaleh. http://api.openweathermap.org/data/2.5/weather?q=kalaleh,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Danilovka. http://api.openweathermap.org/data/2.5/weather?q=danilovka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lyuban. http://api.openweathermap.org/data/2.5/weather?q=lyuban,by&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carauari. http://api.openweathermap.org/data/2.5/weather?q=carauari,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coquimbo. http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kongoussi. http://api.openweathermap.org/data/2.5/weather?q=kongoussi,bf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Diffa. http://api.openweathermap.org/data/2.5/weather?q=diffa,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rafai. http://api.openweathermap.org/data/2.5/weather?q=rafai,cf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Porto Novo. http://api.openweathermap.org/data/2.5/weather?q=porto novo,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Henties Bay. http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bodrum. http://api.openweathermap.org/data/2.5/weather?q=bodrum,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mangan. http://api.openweathermap.org/data/2.5/weather?q=mangan,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Adeje. http://api.openweathermap.org/data/2.5/weather?q=adeje,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abonnema. http://api.openweathermap.org/data/2.5/weather?q=abonnema,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port-Cartier. http://api.openweathermap.org/data/2.5/weather?q=port-cartier,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Augustin. http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ayagoz. http://api.openweathermap.org/data/2.5/weather?q=ayagoz,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Le Port. http://api.openweathermap.org/data/2.5/weather?q=le port,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Stavern. http://api.openweathermap.org/data/2.5/weather?q=stavern,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Alta Floresta. http://api.openweathermap.org/data/2.5/weather?q=alta floresta,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zlitan. http://api.openweathermap.org/data/2.5/weather?q=zlitan,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bestobe. http://api.openweathermap.org/data/2.5/weather?q=bestobe,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Megalopoli. http://api.openweathermap.org/data/2.5/weather?q=megalopoli,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kishi. http://api.openweathermap.org/data/2.5/weather?q=kishi,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Plettenberg Bay. http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grindavik. http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Margate. http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vestmannaeyjar. http://api.openweathermap.org/data/2.5/weather?q=vestmannaeyjar,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dudinka. http://api.openweathermap.org/data/2.5/weather?q=dudinka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lubao. http://api.openweathermap.org/data/2.5/weather?q=lubao,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Swidnik. http://api.openweathermap.org/data/2.5/weather?q=swidnik,pl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bud. http://api.openweathermap.org/data/2.5/weather?q=bud,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Necochea. http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maku. http://api.openweathermap.org/data/2.5/weather?q=maku,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Myre. http://api.openweathermap.org/data/2.5/weather?q=myre,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luanda. http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bandarbeyla. http://api.openweathermap.org/data/2.5/weather?q=bandarbeyla,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint Lawrence. http://api.openweathermap.org/data/2.5/weather?q=san lawrenz,mt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Joseph. http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Altay. http://api.openweathermap.org/data/2.5/weather?q=altay,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lapas. http://api.openweathermap.org/data/2.5/weather?q=lapas,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Podporozhye. http://api.openweathermap.org/data/2.5/weather?q=podporozhye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Elliot. http://api.openweathermap.org/data/2.5/weather?q=elliot,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dabakala. http://api.openweathermap.org/data/2.5/weather?q=dabakala,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint Lawrence. http://api.openweathermap.org/data/2.5/weather?q=san lawrenz,mt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Grande. http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Minsk. http://api.openweathermap.org/data/2.5/weather?q=minsk,by&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Franca do Campo. http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tessalit. http://api.openweathermap.org/data/2.5/weather?q=tessalit,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Belyy Yar. http://api.openweathermap.org/data/2.5/weather?q=belyy yar,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mangan. http://api.openweathermap.org/data/2.5/weather?q=mangan,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port-Gentil. http://api.openweathermap.org/data/2.5/weather?q=port-gentil,ga&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Derzhavinsk. http://api.openweathermap.org/data/2.5/weather?q=derzhavinsk,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Akoupe. http://api.openweathermap.org/data/2.5/weather?q=akoupe,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Naryan-Mar. http://api.openweathermap.org/data/2.5/weather?q=naryan-mar,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Grande. http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saurimo. http://api.openweathermap.org/data/2.5/weather?q=saurimo,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sarakhs. http://api.openweathermap.org/data/2.5/weather?q=sarakhs,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luba. http://api.openweathermap.org/data/2.5/weather?q=luba,gq&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Neuquen. http://api.openweathermap.org/data/2.5/weather?q=neuquen,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Beisfjord. http://api.openweathermap.org/data/2.5/weather?q=beisfjord,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bardiyah. http://api.openweathermap.org/data/2.5/weather?q=bardiyah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upata. http://api.openweathermap.org/data/2.5/weather?q=upata,ve&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Quatre Cocos. http://api.openweathermap.org/data/2.5/weather?q=quatre cocos,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Benguela. http://api.openweathermap.org/data/2.5/weather?q=benguela,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Berlevag. http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cascais. http://api.openweathermap.org/data/2.5/weather?q=cascais,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Benguela. http://api.openweathermap.org/data/2.5/weather?q=benguela,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rypefjord. http://api.openweathermap.org/data/2.5/weather?q=rypefjord,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Gallegos. http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Westport. http://api.openweathermap.org/data/2.5/weather?q=westport,ie&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dekernes. http://api.openweathermap.org/data/2.5/weather?q=dekernes,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pisco. http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tevriz. http://api.openweathermap.org/data/2.5/weather?q=tevriz,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Esmeraldas. http://api.openweathermap.org/data/2.5/weather?q=esmeraldas,ec&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangoa. http://api.openweathermap.org/data/2.5/weather?q=pangoa,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caranavi. http://api.openweathermap.org/data/2.5/weather?q=caranavi,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abu Zabad. http://api.openweathermap.org/data/2.5/weather?q=abu zabad,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saeby. http://api.openweathermap.org/data/2.5/weather?q=saeby,dk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bolu. http://api.openweathermap.org/data/2.5/weather?q=bolu,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ajdabiya. http://api.openweathermap.org/data/2.5/weather?q=ajdabiya,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grand-Santi. http://api.openweathermap.org/data/2.5/weather?q=grand-santi,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yining. http://api.openweathermap.org/data/2.5/weather?q=yining,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Suzdal. http://api.openweathermap.org/data/2.5/weather?q=suzdal,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaqortoq. http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hobyo. http://api.openweathermap.org/data/2.5/weather?q=hobyo,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Maria. http://api.openweathermap.org/data/2.5/weather?q=santa maria,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coihaique. http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cockburn Town. http://api.openweathermap.org/data/2.5/weather?q=cockburn town,bs&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Veraval. http://api.openweathermap.org/data/2.5/weather?q=veraval,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Plettenberg Bay. http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Colares. http://api.openweathermap.org/data/2.5/weather?q=colares,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kavaratti. http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tanout. http://api.openweathermap.org/data/2.5/weather?q=tanout,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maceio. http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vila Velha. http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Santa Luzia. http://api.openweathermap.org/data/2.5/weather?q=santa luzia,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Ambroise. http://api.openweathermap.org/data/2.5/weather?q=saint-ambroise,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puerto Ayacucho. http://api.openweathermap.org/data/2.5/weather?q=puerto ayacucho,ve&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Robertsport. http://api.openweathermap.org/data/2.5/weather?q=robertsport,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carutapera. http://api.openweathermap.org/data/2.5/weather?q=carutapera,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kostino. http://api.openweathermap.org/data/2.5/weather?q=kostino,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tshane. http://api.openweathermap.org/data/2.5/weather?q=tshane,bw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rio Gallegos. http://api.openweathermap.org/data/2.5/weather?q=rio gallegos,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Truro. http://api.openweathermap.org/data/2.5/weather?q=truro,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Joseph. http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dingle. http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Banda Aceh. http://api.openweathermap.org/data/2.5/weather?q=banda aceh,id&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vagamo. http://api.openweathermap.org/data/2.5/weather?q=vagamo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jumla. http://api.openweathermap.org/data/2.5/weather?q=jumla,np&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ventspils. http://api.openweathermap.org/data/2.5/weather?q=ventspils,lv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bilma. http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abong Mbang. http://api.openweathermap.org/data/2.5/weather?q=abong mbang,cm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lusambo. http://api.openweathermap.org/data/2.5/weather?q=lusambo,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Okakarara. http://api.openweathermap.org/data/2.5/weather?q=okakarara,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ve&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kitui. http://api.openweathermap.org/data/2.5/weather?q=kitui,ke&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shache. http://api.openweathermap.org/data/2.5/weather?q=shache,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namibe. http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: The Valley. http://api.openweathermap.org/data/2.5/weather?q=the valley,ai&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Belmonte. http://api.openweathermap.org/data/2.5/weather?q=belmonte,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Farafenni. http://api.openweathermap.org/data/2.5/weather?q=farafenni,gm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muhos. http://api.openweathermap.org/data/2.5/weather?q=muhos,fi&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dom Pedrito. http://api.openweathermap.org/data/2.5/weather?q=dom pedrito,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coshocton. http://api.openweathermap.org/data/2.5/weather?q=coshocton,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Methoni. http://api.openweathermap.org/data/2.5/weather?q=methoni,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mto wa Mbu. http://api.openweathermap.org/data/2.5/weather?q=mto wa mbu,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mana. http://api.openweathermap.org/data/2.5/weather?q=mana,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Izmir. http://api.openweathermap.org/data/2.5/weather?q=izmir,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Potiskum. http://api.openweathermap.org/data/2.5/weather?q=potiskum,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arica. http://api.openweathermap.org/data/2.5/weather?q=arica,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marsh Harbour. http://api.openweathermap.org/data/2.5/weather?q=marsh harbour,bs&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Menongue. http://api.openweathermap.org/data/2.5/weather?q=menongue,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jalu. http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Girona. http://api.openweathermap.org/data/2.5/weather?q=girona,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krasnoborsk. http://api.openweathermap.org/data/2.5/weather?q=krasnoborsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gujrat. http://api.openweathermap.org/data/2.5/weather?q=gujrat,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Akureyri. http://api.openweathermap.org/data/2.5/weather?q=akureyri,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: The Valley. http://api.openweathermap.org/data/2.5/weather?q=the valley,ai&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jalu. http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: San Rafael. http://api.openweathermap.org/data/2.5/weather?q=san rafael,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Feltre. http://api.openweathermap.org/data/2.5/weather?q=feltre,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krasnyy Kurgan. http://api.openweathermap.org/data/2.5/weather?q=krasnyy kurgan,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muhos. http://api.openweathermap.org/data/2.5/weather?q=muhos,fi&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: La Trinidad. http://api.openweathermap.org/data/2.5/weather?q=la trinidad,ni&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City Name</th>
      <th>Country Code</th>
      <th>Random Lat</th>
      <th>Random Lon</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temp (F)</th>
      <th>Humidity (%)</th>
      <th>Cloudiness (%)</th>
      <th>Wind Speed (mph)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>atar</td>
      <td>mr</td>
      <td>19.17</td>
      <td>-13.27</td>
      <td>20.52</td>
      <td>-13.05</td>
      <td>74.15</td>
      <td>38</td>
      <td>8</td>
      <td>2.59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>santa isabel do rio negro</td>
      <td>br</td>
      <td>1.93</td>
      <td>-65.3</td>
      <td>-0.41</td>
      <td>-65.02</td>
      <td>76.94</td>
      <td>91</td>
      <td>80</td>
      <td>3.04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>mar del plata</td>
      <td>ar</td>
      <td>-52.52</td>
      <td>-46.77</td>
      <td>-46.43</td>
      <td>-67.52</td>
      <td>49.76</td>
      <td>69</td>
      <td>8</td>
      <td>11.43</td>
    </tr>
    <tr>
      <th>3</th>
      <td>galle</td>
      <td>lk</td>
      <td>4.52</td>
      <td>77.85</td>
      <td>6.04</td>
      <td>80.22</td>
      <td>75.59</td>
      <td>100</td>
      <td>92</td>
      <td>12.21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>guadalajara</td>
      <td>es</td>
      <td>41.18</td>
      <td>-3.26</td>
      <td>40.63</td>
      <td>-3.16</td>
      <td>69.84</td>
      <td>45</td>
      <td>0</td>
      <td>12.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df.to_csv("WeatherPy.csv", encoding="utf-8", index=False)
```


```python
plt.scatter(df['Latitude'],df['Temp (F)'])
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.title("Temperature (F) vs. Latitude at 6/19/18")

# plt.savefig("LatvsTemp.png")
```




    Text(0.5,1,'Temperature (F) vs. Latitude at 6/19/18')




![png](output_10_1.png)



```python
plt.scatter(df['Latitude'],df['Humidity (%)'])
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.title("Humidity (%) vs. Latitude at 6/19/18")

# plt.savefig("LatvsHumidity.png")
```




    Text(0.5,1,'Humidity (%) vs. Latitude at 6/19/18')




![png](output_11_1.png)



```python
plt.scatter(df['Latitude'],df['Cloudiness (%)'])
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.title("Cloudiness (%) vs. Latitude at 6/19/18")

# plt.savefig("LatvsCloudiness.png")
```




    Text(0.5,1,'Cloudiness (%) vs. Latitude at 6/19/18')




![png](output_12_1.png)



```python
plt.scatter(df['Latitude'],df['Wind Speed (mph)'])
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.title("Wind Speed (mph) vs. Latitude at 6/19/18")

# plt.savefig("LatvsWind.png")
```




    Text(0.5,1,'Wind Speed (mph) vs. Latitude at 6/19/18')




![png](output_13_1.png)

