import pandas as pd
import numpy as np
import re

df = pd.read_csv('csv/location.csv')

df['lat_lon'] = df['location'].apply(lambda x : re.findall('(\d{2}.\d{10}),(\d{2}.\d{10})',x,re.DOTALL))

print(type(df['lat_lon'][0][0]))

df.drop(686, axis=0, inplace=True)

df['lat'] =  [x[0][0] for x in df['lat_lon']]
df['lon'] =  [x[0][1] for x in df['lat_lon']]


print(df.info())

df= df[['names','location', 'lat', 'lon']]

df.to_csv('csv/lat_lon.csv', index=False)




