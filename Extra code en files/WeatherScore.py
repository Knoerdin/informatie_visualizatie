import pandas as pd

# Function to normalize a value
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

# Function to calculate weather score
def calculate_weather_score(humidity, temperature, wind_speed, weights):
    # Normalize humidity, temperature, and wind speed
    humidity_norm = normalize(humidity, min_humidity, max_humidity)
    temperature_norm = normalize(temperature, min_temperature, max_temperature)
    wind_speed_norm = normalize(wind_speed, min_wind_speed, max_wind_speed)
    
    # Calculate weather score
    score = weights['humidity'] * humidity_norm + weights['temperature'] * temperature_norm + weights['wind_speed'] * wind_speed_norm
    
    return score

# Example weights (summing up to 1)
weights = {
    'humidity': 0.4,
    'temperature': 0.3,
    'wind_speed': 0.3
}

# Example CSV file path (replace with your actual CSV file path)
csv_file = '../resources/mean_data_good.csv'

# Read data using pandas
df = pd.read_csv(csv_file)

# Extract min and max values for normalization
min_humidity = df['humidity'].min()
max_humidity = df['humidity'].max()
min_temperature = df['temperature'].min()
max_temperature = df['temperature'].max()
min_wind_speed = df['wind_speed'].min()
max_wind_speed = df['wind_speed'].max()

# Calculate weather scores
df['weather_score'] = df.apply(lambda row: calculate_weather_score(row['humidity'], row['temperature'], row['wind_speed'], weights), axis=1)

# Print results
print("Weather Scores:")
for index, row in df.iterrows():
    print(f"Humidity: {row['humidity']}%, Temperature: {row['temperature']}°C, Wind Speed: {row['wind_speed']} km/h -> Weather Score: {row['weather_score']:.4f}")