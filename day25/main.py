# This is a sample Python script.
# from typing import type_check_only

import csv
#
#
# with open("weather_data.csv") as file:
#     all_weather_data = csv.reader(file)
#     temperatures = []
#     for row in all_weather_data:
#         if not row[1] == 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#
#     print(temperatures)
#

# import pandas as pd
#
# data = pd.read_csv('weather_data.csv')
#
# monday_row = data[data.day == 'Monday']
# print(monday_row)
#
# monday_temp_fahrenheite = monday_row['temp'] * 9/5 + 32
#
# print("temperature into fahrenheit:", monday_temp_fahrenheite)

#Gray
#Cinnamon
#black
import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# gray_color = data[data['Primary Fur Color'] == 'Gray'].count()

colors = data['Primary Fur Color'].value_counts()


print("cinnamon color: ", colors)
