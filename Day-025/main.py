"""
Day 25 - [Project Name]
100 Days of Code - Python
Angela Yu's Python Bootcamp

Description:
[Brief description of what this program does]

Author: [Your Name]
Date: [Date]
Course: Udemy - 100 Days of Code: The Complete Python Pro Bootcamp
"""


import csv
"""This is opening CSV files using regular methods and the CSV library"""
# with open("Day-025/resources/weather_data.csv") as file:
#     # data = file.readlines()
#     # print(data)
#     data = csv.reader(file)
#     # print(data) #this prints a reader object that can be loop
#     temperature = []
#     """This is my way"""
#     # for row in data:
#     #     if row[1] == 'temp':
#     #         continue
#     #     else:
#     #         temperature.append(int(row[1]))
#         # print(row[1])
#     """This is Angela's way"""
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

data = pd.read_csv("Day-025/resources/weather_data.csv")
# # print(data)
# temp = data['temp']
# suma = 0
# ave = 0
# for i in temp:
#     suma = suma + i
# ave = suma/len(temp)
# print(ave)
# print(suma)
# print(temp)

# print(data[data['day'] == "Monday"])
"""This gets the entire row"""
# print(data[data['temp'] == data['temp'].max()])

"""This will convert Monday's temp from C to F"""
# temp = data[data['temp'] == data['temp'].max()]
temp = data[data['temp'] == data['temp'].min()]
cel = temp['temp']
fah = (cel * (9/5)) + 32
print(fah)


