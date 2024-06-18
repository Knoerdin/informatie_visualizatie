import pandas as pd

#Alleen van 2016 en 2017
def code(file_path, output):
    df = pd.read_csv(file_path)

    us_accidents_vars = ['Severity', 'Start_Time', 'End_Time', 'Distance(mi)', 'City','Start_Lat','Start_Lng']

    date_format = "%Y-%m-%d %H:%M:%S"
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], format=date_format, errors='coerce')

    new_data = df[(df['Start_Time'].dt.year == 2016) | (df['Start_Time'].dt.year == 2017)]
    new_data = new_data[us_accidents_vars]

    new_data.to_csv(output, index=False)


code('US_Accidents_March23.csv','C:\\Users\\gijsv\\Desktop\\code\\outputcode.csv')


#'C:\\Users\\gijsv\\Desktop\\code\\outputcode.csv'

