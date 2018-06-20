
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

    url = base_url + name.replace(' ','_') + ',' + country_code + '&units=' + units + '&APPID=' + api_key
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

    City: Colombo. http://api.openweathermap.org/data/2.5/weather?q=colombo,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kikwit. http://api.openweathermap.org/data/2.5/weather?q=kikwit,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bilma. http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cadillac. http://api.openweathermap.org/data/2.5/weather?q=cadillac,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dalbandin. http://api.openweathermap.org/data/2.5/weather?q=dalbandin,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ibra. http://api.openweathermap.org/data/2.5/weather?q=ibra,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taft. http://api.openweathermap.org/data/2.5/weather?q=taft,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mantua. http://api.openweathermap.org/data/2.5/weather?q=mantua,cu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Minas. http://api.openweathermap.org/data/2.5/weather?q=minas,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mapiripan. http://api.openweathermap.org/data/2.5/weather?q=mapiripan,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tamiami. http://api.openweathermap.org/data/2.5/weather?q=tamiami,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aligudarz. http://api.openweathermap.org/data/2.5/weather?q=aligudarz,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Komsomolets. http://api.openweathermap.org/data/2.5/weather?q=komsomolets,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ambilobe. http://api.openweathermap.org/data/2.5/weather?q=ambilobe,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lunino. http://api.openweathermap.org/data/2.5/weather?q=lunino,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ancud. http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lotoshino. http://api.openweathermap.org/data/2.5/weather?q=lotoshino,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iquitos. http://api.openweathermap.org/data/2.5/weather?q=iquitos,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qasigiannguit. http://api.openweathermap.org/data/2.5/weather?q=qasigiannguit,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paita. http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lovozero. http://api.openweathermap.org/data/2.5/weather?q=lovozero,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camocim. http://api.openweathermap.org/data/2.5/weather?q=camocim,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gombe. http://api.openweathermap.org/data/2.5/weather?q=gombe,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dingle. http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salinopolis. http://api.openweathermap.org/data/2.5/weather?q=salinopolis,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tripoli. http://api.openweathermap.org/data/2.5/weather?q=tripoli,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Filingue. http://api.openweathermap.org/data/2.5/weather?q=filingue,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Forestville. http://api.openweathermap.org/data/2.5/weather?q=forestville,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atbasar. http://api.openweathermap.org/data/2.5/weather?q=atbasar,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marawi. http://api.openweathermap.org/data/2.5/weather?q=marawi,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Karcag. http://api.openweathermap.org/data/2.5/weather?q=karcag,hu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kulhudhuffushi. http://api.openweathermap.org/data/2.5/weather?q=kulhudhuffushi,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Joseph. http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Portree. http://api.openweathermap.org/data/2.5/weather?q=portree,gb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilhabela. http://api.openweathermap.org/data/2.5/weather?q=ilhabela,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Soligalich. http://api.openweathermap.org/data/2.5/weather?q=soligalich,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kolobrzeg. http://api.openweathermap.org/data/2.5/weather?q=kolobrzeg,pl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sabratah. http://api.openweathermap.org/data/2.5/weather?q=sabratah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Volovo. http://api.openweathermap.org/data/2.5/weather?q=volovo,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalmunai. http://api.openweathermap.org/data/2.5/weather?q=kalmunai,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kodino. http://api.openweathermap.org/data/2.5/weather?q=kodino,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Najran. http://api.openweathermap.org/data/2.5/weather?q=najran,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mokrous. http://api.openweathermap.org/data/2.5/weather?q=mokrous,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dalvik. http://api.openweathermap.org/data/2.5/weather?q=dalvik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narva-Joesuu. http://api.openweathermap.org/data/2.5/weather?q=narva-joesuu,ee&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Piacabucu. http://api.openweathermap.org/data/2.5/weather?q=piacabucu,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Takoradi. http://api.openweathermap.org/data/2.5/weather?q=takoradi,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Wagar. http://api.openweathermap.org/data/2.5/weather?q=wagar,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Garissa. http://api.openweathermap.org/data/2.5/weather?q=garissa,ke&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Druskininkai. http://api.openweathermap.org/data/2.5/weather?q=druskininkai,lt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iracoubo. http://api.openweathermap.org/data/2.5/weather?q=iracoubo,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paamiut. http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taoudenni. http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangnirtung. http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Berlevag. http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vallenar. http://api.openweathermap.org/data/2.5/weather?q=vallenar,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pisco. http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Uyovu. http://api.openweathermap.org/data/2.5/weather?q=uyovu,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yining. http://api.openweathermap.org/data/2.5/weather?q=yining,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Coquimbo. http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hamina. http://api.openweathermap.org/data/2.5/weather?q=hamina,fi&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Doha. http://api.openweathermap.org/data/2.5/weather?q=doha,qa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sisimiut. http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ainazi. http://api.openweathermap.org/data/2.5/weather?q=ainazi,lv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yabrud. http://api.openweathermap.org/data/2.5/weather?q=yabrud,sy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Constitucion. http://api.openweathermap.org/data/2.5/weather?q=constitucion,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taoudenni. http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Notre-Dame-du-Lac. http://api.openweathermap.org/data/2.5/weather?q=notre-dame-du-lac,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bani. http://api.openweathermap.org/data/2.5/weather?q=bani,do&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ginir. http://api.openweathermap.org/data/2.5/weather?q=ginir,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Huancavelica. http://api.openweathermap.org/data/2.5/weather?q=huancavelica,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namwala. http://api.openweathermap.org/data/2.5/weather?q=namwala,zm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Moroni. http://api.openweathermap.org/data/2.5/weather?q=moroni,km&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Pierre. http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,pm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Artyom. http://api.openweathermap.org/data/2.5/weather?q=artyom,az&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Halifax. http://api.openweathermap.org/data/2.5/weather?q=halifax,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Morondava. http://api.openweathermap.org/data/2.5/weather?q=morondava,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grindavik. http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marrakesh. http://api.openweathermap.org/data/2.5/weather?q=marrakesh,ma&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Constitucion. http://api.openweathermap.org/data/2.5/weather?q=constitucion,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kpandae. http://api.openweathermap.org/data/2.5/weather?q=kpandae,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pemba. http://api.openweathermap.org/data/2.5/weather?q=pemba,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carballo. http://api.openweathermap.org/data/2.5/weather?q=carballo,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muncie. http://api.openweathermap.org/data/2.5/weather?q=muncie,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Massaranduba. http://api.openweathermap.org/data/2.5/weather?q=massaranduba,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namibe. http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namibe. http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maceio. http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nouadhibou. http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Berlevag. http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Agadez. http://api.openweathermap.org/data/2.5/weather?q=agadez,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sevierville. http://api.openweathermap.org/data/2.5/weather?q=sevierville,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ugoofaaru. http://api.openweathermap.org/data/2.5/weather?q=ugoofaaru,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dhidhdhoo. http://api.openweathermap.org/data/2.5/weather?q=dhidhdhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mercedes. http://api.openweathermap.org/data/2.5/weather?q=mercedes,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Turukhansk. http://api.openweathermap.org/data/2.5/weather?q=turukhansk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Semey. http://api.openweathermap.org/data/2.5/weather?q=semey,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Najran. http://api.openweathermap.org/data/2.5/weather?q=najran,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kilimatinde. http://api.openweathermap.org/data/2.5/weather?q=kilimatinde,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Phaltan. http://api.openweathermap.org/data/2.5/weather?q=phaltan,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nuuk. http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Alanya. http://api.openweathermap.org/data/2.5/weather?q=alanya,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Konza. http://api.openweathermap.org/data/2.5/weather?q=konza,ke&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Troitsk. http://api.openweathermap.org/data/2.5/weather?q=troitsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gouyave. http://api.openweathermap.org/data/2.5/weather?q=gouyave,gd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kondinskoye. http://api.openweathermap.org/data/2.5/weather?q=kondinskoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Diamantino. http://api.openweathermap.org/data/2.5/weather?q=diamantino,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Constitucion. http://api.openweathermap.org/data/2.5/weather?q=constitucion,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Crotone. http://api.openweathermap.org/data/2.5/weather?q=crotone,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Havoysund. http://api.openweathermap.org/data/2.5/weather?q=havoysund,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Moron. http://api.openweathermap.org/data/2.5/weather?q=moron,ve&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Opuwo. http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushtobe. http://api.openweathermap.org/data/2.5/weather?q=ushtobe,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mitu. http://api.openweathermap.org/data/2.5/weather?q=mitu,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zharkent. http://api.openweathermap.org/data/2.5/weather?q=zharkent,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hearst. http://api.openweathermap.org/data/2.5/weather?q=hearst,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aljezur. http://api.openweathermap.org/data/2.5/weather?q=aljezur,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bonthe. http://api.openweathermap.org/data/2.5/weather?q=bonthe,sl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taltal. http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahibadhoo. http://api.openweathermap.org/data/2.5/weather?q=mahibadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Misratah. http://api.openweathermap.org/data/2.5/weather?q=misratah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ati. http://api.openweathermap.org/data/2.5/weather?q=ati,td&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cassilandia. http://api.openweathermap.org/data/2.5/weather?q=cassilandia,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rozkishne. http://api.openweathermap.org/data/2.5/weather?q=rozkishne,ua&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grindavik. http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rognan. http://api.openweathermap.org/data/2.5/weather?q=rognan,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vieux-Habitants. http://api.openweathermap.org/data/2.5/weather?q=vieux-habitants,gp&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Skelleftea. http://api.openweathermap.org/data/2.5/weather?q=skelleftea,se&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taltal. http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Talcahuano. http://api.openweathermap.org/data/2.5/weather?q=talcahuano,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Poros. http://api.openweathermap.org/data/2.5/weather?q=poros,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gopalpur. http://api.openweathermap.org/data/2.5/weather?q=gopalpur,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Elmina. http://api.openweathermap.org/data/2.5/weather?q=elmina,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bhimunipatnam. http://api.openweathermap.org/data/2.5/weather?q=bhimunipatnam,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hammerfest. http://api.openweathermap.org/data/2.5/weather?q=hammerfest,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ambatolampy. http://api.openweathermap.org/data/2.5/weather?q=ambatolampy,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bizhbulyak. http://api.openweathermap.org/data/2.5/weather?q=bizhbulyak,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ipinda. http://api.openweathermap.org/data/2.5/weather?q=ipinda,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tsumeb. http://api.openweathermap.org/data/2.5/weather?q=tsumeb,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vagur. http://api.openweathermap.org/data/2.5/weather?q=vagur,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zaysan. http://api.openweathermap.org/data/2.5/weather?q=zaysan,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tarko-Sale. http://api.openweathermap.org/data/2.5/weather?q=tarko-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hamilton. http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sisimiut. http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nsanje. http://api.openweathermap.org/data/2.5/weather?q=nsanje,mw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bonanza. http://api.openweathermap.org/data/2.5/weather?q=bonanza,ni&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Romodanovo. http://api.openweathermap.org/data/2.5/weather?q=romodanovo,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rawson. http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapais. http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Urengoy. http://api.openweathermap.org/data/2.5/weather?q=urengoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Letlhakane. http://api.openweathermap.org/data/2.5/weather?q=letlhakane,bw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Riyadh. http://api.openweathermap.org/data/2.5/weather?q=riyadh,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ripoll. http://api.openweathermap.org/data/2.5/weather?q=ripoll,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shubarkuduk. http://api.openweathermap.org/data/2.5/weather?q=shubarkuduk,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Manaure. http://api.openweathermap.org/data/2.5/weather?q=manaure,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tutoia. http://api.openweathermap.org/data/2.5/weather?q=tutoia,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marawi. http://api.openweathermap.org/data/2.5/weather?q=marawi,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matay. http://api.openweathermap.org/data/2.5/weather?q=matay,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oistins. http://api.openweathermap.org/data/2.5/weather?q=oistins,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mangan. http://api.openweathermap.org/data/2.5/weather?q=mangan,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Soyo. http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ugoofaaru. http://api.openweathermap.org/data/2.5/weather?q=ugoofaaru,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dodola. http://api.openweathermap.org/data/2.5/weather?q=dodola,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Polyarnyy. http://api.openweathermap.org/data/2.5/weather?q=polyarnyy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Turochak. http://api.openweathermap.org/data/2.5/weather?q=turochak,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Timra. http://api.openweathermap.org/data/2.5/weather?q=timra,se&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Brigantine. http://api.openweathermap.org/data/2.5/weather?q=brigantine,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ngama. http://api.openweathermap.org/data/2.5/weather?q=ngama,td&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bestobe. http://api.openweathermap.org/data/2.5/weather?q=bestobe,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Soyo. http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Temirtau. http://api.openweathermap.org/data/2.5/weather?q=temirtau,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dakar. http://api.openweathermap.org/data/2.5/weather?q=dakar,sn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hun. http://api.openweathermap.org/data/2.5/weather?q=hun,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kotri. http://api.openweathermap.org/data/2.5/weather?q=kotri,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nchelenge. http://api.openweathermap.org/data/2.5/weather?q=nchelenge,zm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Huarmey. http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ous. http://api.openweathermap.org/data/2.5/weather?q=ous,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vyshestebliyevskaya. http://api.openweathermap.org/data/2.5/weather?q=vyshestebliyevskaya,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Huarmey. http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vyartsilya. http://api.openweathermap.org/data/2.5/weather?q=vyartsilya,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bundibugyo. http://api.openweathermap.org/data/2.5/weather?q=bundibugyo,ug&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lodja. http://api.openweathermap.org/data/2.5/weather?q=lodja,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ust-Kalmanka. http://api.openweathermap.org/data/2.5/weather?q=ust-kalmanka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Weligama. http://api.openweathermap.org/data/2.5/weather?q=weligama,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Akom. http://api.openweathermap.org/data/2.5/weather?q=akom,cm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jaciara. http://api.openweathermap.org/data/2.5/weather?q=jaciara,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kangaatsiaq. http://api.openweathermap.org/data/2.5/weather?q=kangaatsiaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rawson. http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mollendo. http://api.openweathermap.org/data/2.5/weather?q=mollendo,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Alcains. http://api.openweathermap.org/data/2.5/weather?q=alcains,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lamu. http://api.openweathermap.org/data/2.5/weather?q=lamu,ke&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mao. http://api.openweathermap.org/data/2.5/weather?q=mao,td&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nevel. http://api.openweathermap.org/data/2.5/weather?q=nevel,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shieli. http://api.openweathermap.org/data/2.5/weather?q=shieli,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bonavista. http://api.openweathermap.org/data/2.5/weather?q=bonavista,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Buraydah. http://api.openweathermap.org/data/2.5/weather?q=buraydah,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aksarayskiy. http://api.openweathermap.org/data/2.5/weather?q=aksarayskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matadi. http://api.openweathermap.org/data/2.5/weather?q=matadi,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Diamantino. http://api.openweathermap.org/data/2.5/weather?q=diamantino,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vilcun. http://api.openweathermap.org/data/2.5/weather?q=vilcun,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chastyye. http://api.openweathermap.org/data/2.5/weather?q=chastyye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Trairi. http://api.openweathermap.org/data/2.5/weather?q=trairi,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carutapera. http://api.openweathermap.org/data/2.5/weather?q=carutapera,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vestmanna. http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marquette. http://api.openweathermap.org/data/2.5/weather?q=marquette,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Batsfjord. http://api.openweathermap.org/data/2.5/weather?q=batsfjord,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorgun. http://api.openweathermap.org/data/2.5/weather?q=sorgun,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aktau. http://api.openweathermap.org/data/2.5/weather?q=aktau,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Villaviciosa. http://api.openweathermap.org/data/2.5/weather?q=villaviciosa,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vianopolis. http://api.openweathermap.org/data/2.5/weather?q=vianopolis,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Havelock. http://api.openweathermap.org/data/2.5/weather?q=havelock,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Areni. http://api.openweathermap.org/data/2.5/weather?q=areni,am&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krylovskaya. http://api.openweathermap.org/data/2.5/weather?q=krylovskaya,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abha. http://api.openweathermap.org/data/2.5/weather?q=abha,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luba. http://api.openweathermap.org/data/2.5/weather?q=luba,gq&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Margate. http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Itarema. http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Savinka. http://api.openweathermap.org/data/2.5/weather?q=savinka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bembereke. http://api.openweathermap.org/data/2.5/weather?q=bembereke,bj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ardabil. http://api.openweathermap.org/data/2.5/weather?q=ardabil,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tevriz. http://api.openweathermap.org/data/2.5/weather?q=tevriz,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Takoradi. http://api.openweathermap.org/data/2.5/weather?q=takoradi,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Birjand. http://api.openweathermap.org/data/2.5/weather?q=birjand,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taoudenni. http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bani. http://api.openweathermap.org/data/2.5/weather?q=bani,do&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salinas. http://api.openweathermap.org/data/2.5/weather?q=salinas,ec&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaqortoq. http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Goure. http://api.openweathermap.org/data/2.5/weather?q=goure,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bageshwar. http://api.openweathermap.org/data/2.5/weather?q=bageshwar,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hualmay. http://api.openweathermap.org/data/2.5/weather?q=hualmay,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Severodvinsk. http://api.openweathermap.org/data/2.5/weather?q=severodvinsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arandis. http://api.openweathermap.org/data/2.5/weather?q=arandis,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iskateley. http://api.openweathermap.org/data/2.5/weather?q=iskateley,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Opuwo. http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nioki. http://api.openweathermap.org/data/2.5/weather?q=nioki,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dudinka. http://api.openweathermap.org/data/2.5/weather?q=dudinka,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sept-Iles. http://api.openweathermap.org/data/2.5/weather?q=sept-iles,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Akdepe. http://api.openweathermap.org/data/2.5/weather?q=akdepe,tm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Concordia. http://api.openweathermap.org/data/2.5/weather?q=concordia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maragogi. http://api.openweathermap.org/data/2.5/weather?q=maragogi,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sarankhola. http://api.openweathermap.org/data/2.5/weather?q=sarankhola,bd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bonavista. http://api.openweathermap.org/data/2.5/weather?q=bonavista,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Khorixas. http://api.openweathermap.org/data/2.5/weather?q=khorixas,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bonfim. http://api.openweathermap.org/data/2.5/weather?q=bonfim,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hamilton. http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atasu. http://api.openweathermap.org/data/2.5/weather?q=atasu,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapais. http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gurgaon. http://api.openweathermap.org/data/2.5/weather?q=gurgaon,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dalbandin. http://api.openweathermap.org/data/2.5/weather?q=dalbandin,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sombrio. http://api.openweathermap.org/data/2.5/weather?q=sombrio,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muzaffargarh. http://api.openweathermap.org/data/2.5/weather?q=muzaffargarh,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Loum. http://api.openweathermap.org/data/2.5/weather?q=loum,cm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gloucester. http://api.openweathermap.org/data/2.5/weather?q=gloucester,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krasnovishersk. http://api.openweathermap.org/data/2.5/weather?q=krasnovishersk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kirovskiy. http://api.openweathermap.org/data/2.5/weather?q=kirovskiy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Trinidad. http://api.openweathermap.org/data/2.5/weather?q=trinidad,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Wattegama. http://api.openweathermap.org/data/2.5/weather?q=wattegama,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Arucas. http://api.openweathermap.org/data/2.5/weather?q=arucas,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vagur. http://api.openweathermap.org/data/2.5/weather?q=vagur,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bouna. http://api.openweathermap.org/data/2.5/weather?q=bouna,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Michel-des-Saints. http://api.openweathermap.org/data/2.5/weather?q=saint-michel-des-saints,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ewo. http://api.openweathermap.org/data/2.5/weather?q=ewo,cg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gazanjyk. http://api.openweathermap.org/data/2.5/weather?q=gazanjyk,tm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Baijiantan. http://api.openweathermap.org/data/2.5/weather?q=baijiantan,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nuuk. http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aasiaat. http://api.openweathermap.org/data/2.5/weather?q=aasiaat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Paul. http://api.openweathermap.org/data/2.5/weather?q=saint-paul,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luque. http://api.openweathermap.org/data/2.5/weather?q=luque,py&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Meteti. http://api.openweathermap.org/data/2.5/weather?q=meteti,pa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Warsaw. http://api.openweathermap.org/data/2.5/weather?q=warsaw,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Koungou. http://api.openweathermap.org/data/2.5/weather?q=koungou,yt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lahan. http://api.openweathermap.org/data/2.5/weather?q=lahan,np&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Xuddur. http://api.openweathermap.org/data/2.5/weather?q=xuddur,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Voslobeni. http://api.openweathermap.org/data/2.5/weather?q=voslobeni,ro&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iskateley. http://api.openweathermap.org/data/2.5/weather?q=iskateley,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Margate. http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Namibe. http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bilma. http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Osorno. http://api.openweathermap.org/data/2.5/weather?q=osorno,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Praia. http://api.openweathermap.org/data/2.5/weather?q=praia,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yerkoy. http://api.openweathermap.org/data/2.5/weather?q=yerkoy,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Uyo. http://api.openweathermap.org/data/2.5/weather?q=uyo,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sabha. http://api.openweathermap.org/data/2.5/weather?q=sabha,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oxilithos. http://api.openweathermap.org/data/2.5/weather?q=oxilithos,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zarasai. http://api.openweathermap.org/data/2.5/weather?q=zarasai,lt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Uyuni. http://api.openweathermap.org/data/2.5/weather?q=uyuni,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kulhudhuffushi. http://api.openweathermap.org/data/2.5/weather?q=kulhudhuffushi,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahibadhoo. http://api.openweathermap.org/data/2.5/weather?q=mahibadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Conde. http://api.openweathermap.org/data/2.5/weather?q=conde,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Afrikanda. http://api.openweathermap.org/data/2.5/weather?q=afrikanda,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nouakchott. http://api.openweathermap.org/data/2.5/weather?q=nouakchott,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gijon. http://api.openweathermap.org/data/2.5/weather?q=gijon,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Imbituba. http://api.openweathermap.org/data/2.5/weather?q=imbituba,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grindavik. http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Naryan-Mar. http://api.openweathermap.org/data/2.5/weather?q=naryan-mar,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yershov. http://api.openweathermap.org/data/2.5/weather?q=yershov,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nouadhibou. http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mazagao. http://api.openweathermap.org/data/2.5/weather?q=mazagao,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lixourion. http://api.openweathermap.org/data/2.5/weather?q=lixourion,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kavaratti. http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Damaturu. http://api.openweathermap.org/data/2.5/weather?q=damaturu,ng&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rusape. http://api.openweathermap.org/data/2.5/weather?q=rusape,zw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Denis. http://api.openweathermap.org/data/2.5/weather?q=saint-denis,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Xuddur. http://api.openweathermap.org/data/2.5/weather?q=xuddur,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mogadishu. http://api.openweathermap.org/data/2.5/weather?q=mogadishu,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cervo. http://api.openweathermap.org/data/2.5/weather?q=cervo,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Segovia. http://api.openweathermap.org/data/2.5/weather?q=segovia,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Norilsk. http://api.openweathermap.org/data/2.5/weather?q=norilsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grand-Santi. http://api.openweathermap.org/data/2.5/weather?q=grand-santi,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Babati. http://api.openweathermap.org/data/2.5/weather?q=babati,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Iraquara. http://api.openweathermap.org/data/2.5/weather?q=iraquara,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Benguela. http://api.openweathermap.org/data/2.5/weather?q=benguela,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Halifax. http://api.openweathermap.org/data/2.5/weather?q=halifax,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Monrovia. http://api.openweathermap.org/data/2.5/weather?q=monrovia,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paamiut. http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luba. http://api.openweathermap.org/data/2.5/weather?q=luba,gq&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gravdal. http://api.openweathermap.org/data/2.5/weather?q=gravdal,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maputo. http://api.openweathermap.org/data/2.5/weather?q=maputo,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ibirama. http://api.openweathermap.org/data/2.5/weather?q=ibirama,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Pierre. http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,pm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dinajpur. http://api.openweathermap.org/data/2.5/weather?q=dinajpur,bd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Akhtubinsk. http://api.openweathermap.org/data/2.5/weather?q=akhtubinsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Grand-Santi. http://api.openweathermap.org/data/2.5/weather?q=grand-santi,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kudahuvadhoo. http://api.openweathermap.org/data/2.5/weather?q=kudahuvadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bukama. http://api.openweathermap.org/data/2.5/weather?q=bukama,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaqortoq. http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Inhambane. http://api.openweathermap.org/data/2.5/weather?q=inhambane,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Guhagar. http://api.openweathermap.org/data/2.5/weather?q=guhagar,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Karoi. http://api.openweathermap.org/data/2.5/weather?q=karoi,zw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oristano. http://api.openweathermap.org/data/2.5/weather?q=oristano,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carballo. http://api.openweathermap.org/data/2.5/weather?q=carballo,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bealanana. http://api.openweathermap.org/data/2.5/weather?q=bealanana,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taoudenni. http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Beloha. http://api.openweathermap.org/data/2.5/weather?q=beloha,mg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yabrud. http://api.openweathermap.org/data/2.5/weather?q=yabrud,sy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hualmay. http://api.openweathermap.org/data/2.5/weather?q=hualmay,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Semey. http://api.openweathermap.org/data/2.5/weather?q=semey,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jawhar. http://api.openweathermap.org/data/2.5/weather?q=jawhar,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaqortoq. http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hornepayne. http://api.openweathermap.org/data/2.5/weather?q=hornepayne,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mokrous. http://api.openweathermap.org/data/2.5/weather?q=mokrous,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mocuba. http://api.openweathermap.org/data/2.5/weather?q=mocuba,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Anajatuba. http://api.openweathermap.org/data/2.5/weather?q=anajatuba,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Brae. http://api.openweathermap.org/data/2.5/weather?q=brae,gb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tshikapa. http://api.openweathermap.org/data/2.5/weather?q=tshikapa,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kargasok. http://api.openweathermap.org/data/2.5/weather?q=kargasok,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Beisfjord. http://api.openweathermap.org/data/2.5/weather?q=beisfjord,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalmunai. http://api.openweathermap.org/data/2.5/weather?q=kalmunai,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kavaratti. http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kavaratti. http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Soyo. http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Charagua. http://api.openweathermap.org/data/2.5/weather?q=charagua,bo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abha. http://api.openweathermap.org/data/2.5/weather?q=abha,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Natal. http://api.openweathermap.org/data/2.5/weather?q=natal,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kaspi. http://api.openweathermap.org/data/2.5/weather?q=kaspi,ge&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Constitucion. http://api.openweathermap.org/data/2.5/weather?q=constitucion,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kajaani. http://api.openweathermap.org/data/2.5/weather?q=kajaani,fi&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mogadishu. http://api.openweathermap.org/data/2.5/weather?q=mogadishu,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kedgwick. http://api.openweathermap.org/data/2.5/weather?q=kedgwick,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oranjemund. http://api.openweathermap.org/data/2.5/weather?q=oranjemund,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Necochea. http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ipixuna. http://api.openweathermap.org/data/2.5/weather?q=ipixuna,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Fougamou. http://api.openweathermap.org/data/2.5/weather?q=fougamou,ga&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hwange. http://api.openweathermap.org/data/2.5/weather?q=hwange,zw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Wattegama. http://api.openweathermap.org/data/2.5/weather?q=wattegama,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ngorongoro. http://api.openweathermap.org/data/2.5/weather?q=ngorongoro,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Willowmore. http://api.openweathermap.org/data/2.5/weather?q=willowmore,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mizdah. http://api.openweathermap.org/data/2.5/weather?q=mizdah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Praia. http://api.openweathermap.org/data/2.5/weather?q=praia,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Trapani. http://api.openweathermap.org/data/2.5/weather?q=trapani,it&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bridlington. http://api.openweathermap.org/data/2.5/weather?q=bridlington,gb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bartica. http://api.openweathermap.org/data/2.5/weather?q=bartica,gy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maragheh. http://api.openweathermap.org/data/2.5/weather?q=maragheh,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bambey. http://api.openweathermap.org/data/2.5/weather?q=bambey,sn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shakiso. http://api.openweathermap.org/data/2.5/weather?q=shakiso,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Matara. http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Roald. http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dovolnoye. http://api.openweathermap.org/data/2.5/weather?q=dovolnoye,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Marmarion. http://api.openweathermap.org/data/2.5/weather?q=marmarion,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Turayf. http://api.openweathermap.org/data/2.5/weather?q=turayf,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Borgarnes. http://api.openweathermap.org/data/2.5/weather?q=borgarnes,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yar-Sale. http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oranjestad. http://api.openweathermap.org/data/2.5/weather?q=oranjestad,aw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Gorom-Gorom. http://api.openweathermap.org/data/2.5/weather?q=gorom-gorom,bf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shalyhyne. http://api.openweathermap.org/data/2.5/weather?q=shalyhyne,ua&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carutapera. http://api.openweathermap.org/data/2.5/weather?q=carutapera,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nykoping. http://api.openweathermap.org/data/2.5/weather?q=nykoping,se&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Durban. http://api.openweathermap.org/data/2.5/weather?q=durban,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bobcaygeon. http://api.openweathermap.org/data/2.5/weather?q=bobcaygeon,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kapuskasing. http://api.openweathermap.org/data/2.5/weather?q=kapuskasing,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Opuwo. http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bongandanga. http://api.openweathermap.org/data/2.5/weather?q=bongandanga,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ardakan. http://api.openweathermap.org/data/2.5/weather?q=ardakan,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lakshettipet. http://api.openweathermap.org/data/2.5/weather?q=lakshettipet,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Inyonga. http://api.openweathermap.org/data/2.5/weather?q=inyonga,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Beitbridge. http://api.openweathermap.org/data/2.5/weather?q=beitbridge,zw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mamallapuram. http://api.openweathermap.org/data/2.5/weather?q=mamallapuram,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Augustin. http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Malanje. http://api.openweathermap.org/data/2.5/weather?q=malanje,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Itarema. http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Koulikoro. http://api.openweathermap.org/data/2.5/weather?q=koulikoro,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lokosovo. http://api.openweathermap.org/data/2.5/weather?q=lokosovo,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tabas. http://api.openweathermap.org/data/2.5/weather?q=tabas,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalmunai. http://api.openweathermap.org/data/2.5/weather?q=kalmunai,lk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Impfondo. http://api.openweathermap.org/data/2.5/weather?q=impfondo,cg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Benghazi. http://api.openweathermap.org/data/2.5/weather?q=benghazi,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sayat. http://api.openweathermap.org/data/2.5/weather?q=sayat,tm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Awjilah. http://api.openweathermap.org/data/2.5/weather?q=awjilah,ly&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Havre-Saint-Pierre. http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yazd. http://api.openweathermap.org/data/2.5/weather?q=yazd,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Permet. http://api.openweathermap.org/data/2.5/weather?q=permet,al&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapais. http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camacha. http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ulundi. http://api.openweathermap.org/data/2.5/weather?q=ulundi,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pangnirtung. http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mantes-la-Jolie. http://api.openweathermap.org/data/2.5/weather?q=mantes-la-jolie,fr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shahrud. http://api.openweathermap.org/data/2.5/weather?q=shahrud,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Huarmey. http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nantucket. http://api.openweathermap.org/data/2.5/weather?q=nantucket,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Putina. http://api.openweathermap.org/data/2.5/weather?q=putina,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dingle. http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Boende. http://api.openweathermap.org/data/2.5/weather?q=boende,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tarancon. http://api.openweathermap.org/data/2.5/weather?q=tarancon,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kalangala. http://api.openweathermap.org/data/2.5/weather?q=kalangala,ug&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kayerkan. http://api.openweathermap.org/data/2.5/weather?q=kayerkan,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Avallon. http://api.openweathermap.org/data/2.5/weather?q=avallon,fr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mecca. http://api.openweathermap.org/data/2.5/weather?q=mecca,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Broceni. http://api.openweathermap.org/data/2.5/weather?q=broceni,lv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Catio. http://api.openweathermap.org/data/2.5/weather?q=catio,gw&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Yaviza. http://api.openweathermap.org/data/2.5/weather?q=yaviza,pa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bhuj. http://api.openweathermap.org/data/2.5/weather?q=bhuj,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qasigiannguit. http://api.openweathermap.org/data/2.5/weather?q=qasigiannguit,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Suez. http://api.openweathermap.org/data/2.5/weather?q=suez,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Eyl. http://api.openweathermap.org/data/2.5/weather?q=eyl,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Rawson. http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Itarema. http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Novokuznetsk. http://api.openweathermap.org/data/2.5/weather?q=novokuznetsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salekhard. http://api.openweathermap.org/data/2.5/weather?q=salekhard,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paita. http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Buchanan. http://api.openweathermap.org/data/2.5/weather?q=buchanan,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kabalo. http://api.openweathermap.org/data/2.5/weather?q=kabalo,cd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aswan. http://api.openweathermap.org/data/2.5/weather?q=aswan,eg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Maceio. http://api.openweathermap.org/data/2.5/weather?q=maceio,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tabuk. http://api.openweathermap.org/data/2.5/weather?q=tabuk,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mumford. http://api.openweathermap.org/data/2.5/weather?q=mumford,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ziniare. http://api.openweathermap.org/data/2.5/weather?q=ziniare,bf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Havelock. http://api.openweathermap.org/data/2.5/weather?q=havelock,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Paamiut. http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mohgaon. http://api.openweathermap.org/data/2.5/weather?q=mohgaon,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Selb. http://api.openweathermap.org/data/2.5/weather?q=selb,de&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Krasnogvardeyets. http://api.openweathermap.org/data/2.5/weather?q=krasnogvardeyets,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Trairi. http://api.openweathermap.org/data/2.5/weather?q=trairi,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Waldshut-Tiengen. http://api.openweathermap.org/data/2.5/weather?q=waldshut-tiengen,de&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hamilton. http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Polyarnyy. http://api.openweathermap.org/data/2.5/weather?q=polyarnyy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mitu. http://api.openweathermap.org/data/2.5/weather?q=mitu,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Luanda. http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushtobe. http://api.openweathermap.org/data/2.5/weather?q=ushtobe,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chapais. http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mayumba. http://api.openweathermap.org/data/2.5/weather?q=mayumba,ga&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Semey. http://api.openweathermap.org/data/2.5/weather?q=semey,kz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Micheweni. http://api.openweathermap.org/data/2.5/weather?q=micheweni,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oistins. http://api.openweathermap.org/data/2.5/weather?q=oistins,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Susehri. http://api.openweathermap.org/data/2.5/weather?q=susehri,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pedernales. http://api.openweathermap.org/data/2.5/weather?q=pedernales,do&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hendek. http://api.openweathermap.org/data/2.5/weather?q=hendek,tr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Planadas. http://api.openweathermap.org/data/2.5/weather?q=planadas,co&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ashta. http://api.openweathermap.org/data/2.5/weather?q=ashta,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Uruacu. http://api.openweathermap.org/data/2.5/weather?q=uruacu,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ferrol. http://api.openweathermap.org/data/2.5/weather?q=ferrol,es&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sharjah. http://api.openweathermap.org/data/2.5/weather?q=sharjah,ae&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aksu. http://api.openweathermap.org/data/2.5/weather?q=aksu,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caravelas. http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ntungamo. http://api.openweathermap.org/data/2.5/weather?q=ntungamo,ug&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Methoni. http://api.openweathermap.org/data/2.5/weather?q=methoni,gr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Caraguatay. http://api.openweathermap.org/data/2.5/weather?q=caraguatay,py&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Muisne. http://api.openweathermap.org/data/2.5/weather?q=muisne,ec&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camacha. http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sur. http://api.openweathermap.org/data/2.5/weather?q=sur,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Onega. http://api.openweathermap.org/data/2.5/weather?q=onega,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Boddam. http://api.openweathermap.org/data/2.5/weather?q=boddam,gb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camacha. http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bezhetsk. http://api.openweathermap.org/data/2.5/weather?q=bezhetsk,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Monrovia. http://api.openweathermap.org/data/2.5/weather?q=monrovia,lr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jaisalmer. http://api.openweathermap.org/data/2.5/weather?q=jaisalmer,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Eidsvag. http://api.openweathermap.org/data/2.5/weather?q=eidsvag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sawakin. http://api.openweathermap.org/data/2.5/weather?q=sawakin,sd&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Islamkot. http://api.openweathermap.org/data/2.5/weather?q=islamkot,pk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Brigantine. http://api.openweathermap.org/data/2.5/weather?q=brigantine,us&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Nouakchott. http://api.openweathermap.org/data/2.5/weather?q=nouakchott,mr&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salinopolis. http://api.openweathermap.org/data/2.5/weather?q=salinopolis,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tabou. http://api.openweathermap.org/data/2.5/weather?q=tabou,ci&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Stornoway. http://api.openweathermap.org/data/2.5/weather?q=stornoway,gb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Garowe. http://api.openweathermap.org/data/2.5/weather?q=garowe,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Taoudenni. http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jaisalmer. http://api.openweathermap.org/data/2.5/weather?q=jaisalmer,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sorland. http://api.openweathermap.org/data/2.5/weather?q=sorland,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Araouane. http://api.openweathermap.org/data/2.5/weather?q=araouane,ml&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Urucara. http://api.openweathermap.org/data/2.5/weather?q=urucara,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Karpogory. http://api.openweathermap.org/data/2.5/weather?q=karpogory,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Havoysund. http://api.openweathermap.org/data/2.5/weather?q=havoysund,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hunucma. http://api.openweathermap.org/data/2.5/weather?q=hunucma,mx&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pendra. http://api.openweathermap.org/data/2.5/weather?q=pendra,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salinopolis. http://api.openweathermap.org/data/2.5/weather?q=salinopolis,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Brattvag. http://api.openweathermap.org/data/2.5/weather?q=brattvag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Shiraz. http://api.openweathermap.org/data/2.5/weather?q=shiraz,ir&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Purpe. http://api.openweathermap.org/data/2.5/weather?q=purpe,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Sisimiut. http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mogwase. http://api.openweathermap.org/data/2.5/weather?q=mogwase,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Inhambane. http://api.openweathermap.org/data/2.5/weather?q=inhambane,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Oranjemund. http://api.openweathermap.org/data/2.5/weather?q=oranjemund,na&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Katakwi. http://api.openweathermap.org/data/2.5/weather?q=katakwi,ug&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bridgetown. http://api.openweathermap.org/data/2.5/weather?q=bridgetown,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Amvrosiyivka. http://api.openweathermap.org/data/2.5/weather?q=amvrosiyivka,ua&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kautokeino. http://api.openweathermap.org/data/2.5/weather?q=kautokeino,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kemin. http://api.openweathermap.org/data/2.5/weather?q=kemin,kg&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mitsamiouli. http://api.openweathermap.org/data/2.5/weather?q=mitsamiouli,km&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mpanda. http://api.openweathermap.org/data/2.5/weather?q=mpanda,tz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kochi. http://api.openweathermap.org/data/2.5/weather?q=kochi,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Necochea. http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Talara. http://api.openweathermap.org/data/2.5/weather?q=talara,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Camocim. http://api.openweathermap.org/data/2.5/weather?q=camocim,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Honningsvag. http://api.openweathermap.org/data/2.5/weather?q=honningsvag,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Floro. http://api.openweathermap.org/data/2.5/weather?q=floro,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Goba. http://api.openweathermap.org/data/2.5/weather?q=goba,et&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pudozh. http://api.openweathermap.org/data/2.5/weather?q=pudozh,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Puri. http://api.openweathermap.org/data/2.5/weather?q=puri,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Mercedes. http://api.openweathermap.org/data/2.5/weather?q=mercedes,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aksu. http://api.openweathermap.org/data/2.5/weather?q=aksu,cn&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tignere. http://api.openweathermap.org/data/2.5/weather?q=tignere,cm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ouidah. http://api.openweathermap.org/data/2.5/weather?q=ouidah,bj&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kathmandu. http://api.openweathermap.org/data/2.5/weather?q=kathmandu,np&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Manica. http://api.openweathermap.org/data/2.5/weather?q=manica,mz&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dhidhdhoo. http://api.openweathermap.org/data/2.5/weather?q=dhidhdhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Colesberg. http://api.openweathermap.org/data/2.5/weather?q=colesberg,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Takoradi. http://api.openweathermap.org/data/2.5/weather?q=takoradi,gh&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Vicuna. http://api.openweathermap.org/data/2.5/weather?q=vicuna,cl&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Roald. http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Bandarbeyla. http://api.openweathermap.org/data/2.5/weather?q=bandarbeyla,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Qandala. http://api.openweathermap.org/data/2.5/weather?q=qandala,so&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Abha. http://api.openweathermap.org/data/2.5/weather?q=abha,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Aripuana. http://api.openweathermap.org/data/2.5/weather?q=aripuana,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Dasoguz. http://api.openweathermap.org/data/2.5/weather?q=dasoguz,tm&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Buraydah. http://api.openweathermap.org/data/2.5/weather?q=buraydah,sa&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kulhudhuffushi. http://api.openweathermap.org/data/2.5/weather?q=kulhudhuffushi,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kudahuvadhoo. http://api.openweathermap.org/data/2.5/weather?q=kudahuvadhoo,mv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Asnaes. http://api.openweathermap.org/data/2.5/weather?q=asnaes,dk&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Pitimbu. http://api.openweathermap.org/data/2.5/weather?q=pitimbu,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Zorritos. http://api.openweathermap.org/data/2.5/weather?q=zorritos,pe&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Neuquen. http://api.openweathermap.org/data/2.5/weather?q=neuquen,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Tarrafal. http://api.openweathermap.org/data/2.5/weather?q=tarrafal,cv&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Chatra. http://api.openweathermap.org/data/2.5/weather?q=chatra,in&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    City: Skjervoy. http://api.openweathermap.org/data/2.5/weather?q=skjervoy,no&units=imperial&APPID=067896fd7e9a52cfebc9a42c4b82e6c2
    


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
      <td>colombo</td>
      <td>lk</td>
      <td>6.75</td>
      <td>78.63</td>
      <td>6.93</td>
      <td>79.85</td>
      <td>77</td>
      <td>94</td>
      <td>40</td>
      <td>5.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lagoa</td>
      <td>pt</td>
      <td>44.99</td>
      <td>-27.55</td>
      <td>37.14</td>
      <td>-8.45</td>
      <td>71.6</td>
      <td>68</td>
      <td>0</td>
      <td>9.17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cidreira</td>
      <td>br</td>
      <td>-58.55</td>
      <td>-21.64</td>
      <td>-30.17</td>
      <td>-50.22</td>
      <td>46.39</td>
      <td>82</td>
      <td>0</td>
      <td>2.77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kikwit</td>
      <td>cd</td>
      <td>-6.28</td>
      <td>18.74</td>
      <td>-5.04</td>
      <td>18.82</td>
      <td>64.93</td>
      <td>90</td>
      <td>0</td>
      <td>4.68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>bilma</td>
      <td>ne</td>
      <td>20.13</td>
      <td>10.25</td>
      <td>18.69</td>
      <td>12.92</td>
      <td>82.3</td>
      <td>19</td>
      <td>76</td>
      <td>5.68</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv("WeatherPy.csv", encoding="utf-8", index=False)
```


```python
plt.scatter(df['Latitude'],df['Temp (F)'])
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")
plt.title("Temperature (F) vs. Latitude at 6/19/18")

plt.savefig("LatvsTemp.png")
```


![png](output_10_0.png)



```python
plt.scatter(df['Latitude'],df['Humidity (%)'])
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.title("Humidity (%) vs. Latitude at 6/19/18")

plt.savefig("LatvsHumidity.png")
```


![png](output_11_0.png)



```python
plt.scatter(df['Latitude'],df['Cloudiness (%)'])
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.title("Cloudiness (%) vs. Latitude at 6/19/18")

plt.savefig("LatvsCloudiness.png")
```


![png](output_12_0.png)



```python
plt.scatter(df['Latitude'],df['Wind Speed (mph)'])
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.title("Wind Speed (mph) vs. Latitude at 6/19/18")

plt.savefig("LatvsWind.png")
```


![png](output_13_0.png)

