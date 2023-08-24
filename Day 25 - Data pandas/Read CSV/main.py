# import csv
#
# with open("weather_data.csv") as data:
#     database = csv.reader(data)
#     temp =[]
#     for row in database:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data.temp.to_list()
print(temp_list)

print(data.temp.max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])


