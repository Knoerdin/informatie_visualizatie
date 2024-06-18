import pandas as pd

def files_ordered(file, output):
    x = pd.read_csv(file)
    date_format = "%Y-%m-%d %H:%M:%S"
    x['datetime'] = pd.to_datetime(x['datetime'],format=date_format, errors='coerce')
    new_data = x[(x['datetime'].dt.year == 2016) | (x['datetime'].dt.year == 2017)]
    new_data.to_csv(output, index=False)
#files_ordered('humidity.csv', 'WeatherHUM.csv')
#files_ordered('temperature.csv', 'WeatherTEMP.csv')
#files_ordered('wind_speed.csv','WeatherWIN.csv')


#goeie shit die niet files ordered:)
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)


df = pd.read_csv('city_attributes.csv')
pf = pd.read_csv('BubbleMapData.csv')
hf = pd.read_csv('humidity.csv')
wf = pd.read_csv('city_attributes.csv')

steden = []
weersteden = df['City'].tolist()
alle_steden = pf['City'].tolist()

for i in weersteden:
    if i in alle_steden:
        steden.append(i)

#Weather score sahbi's
gegevens_steden = []

hum = pd.read_csv('WeatherHUM.csv')
win = pd.read_csv('WeatherWIN.csv')
temp = pd.read_csv('WeatherTEMP.csv')

weights = {
    'humidity': 0.4,
    'temperature': 0.3,
    'wind_speed': 0.3
}

for city in steden:
    if city not in gegevens_steden:

        gem_hum = hum[city].mean()
        max_hum = hum[city].max()
        min_hum = hum[city].min()
        norm_hum = normalize(gem_hum, min_hum, max_hum)

        gem_win = win[city].mean()
        max_win = win[city].max()
        min_win = win[city].min()
        norm_win = normalize(gem_win, min_win, max_win)

        gem_temp = temp[city].mean()
        max_temp = temp[city].max()
        min_temp = temp[city].min()
        norm_temp = normalize(gem_temp, min_temp, max_temp)

        city_info = wf[wf['City'] == city].iloc[0]
        gegevens_steden.append({
            'city' : city,
            'score' : weights['humidity'] * norm_hum + weights['temperature'] * norm_temp + weights['wind_speed'] * norm_win,
            'lat': city_info['Latitude'],
            'lng': city_info['Longitude'],
        })


ongelukken_df = pd.DataFrame(gegevens_steden)
ongelukken_df.to_csv('WeatherBubbleData.csv', index=False)
#list dict ding naar nieuwe file

