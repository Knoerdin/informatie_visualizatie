
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('US_Accidents.csv')
pf = pd.read_csv('uscities.csv')

steden = df['City'].unique()
totaal_steden = pf['city'].unique()

ongelukken = df.groupby('City').size().to_dict()

data = []
for city in steden:
    if city in totaal_steden:
        city_info = pf[pf['city'] == city].iloc[0]
        data.append({
            'City': city,
            'ongelukken': ongelukken.get(city, 0),
            'lat': city_info['lat'],
            'lng': city_info['lng']
        })

ongelukken_df = pd.DataFrame(data)

ongelukken_df.to_csv('BubbleMapData.csv', index=False)
