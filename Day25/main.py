import csv
import pandas as pd

# with csv
with open("weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
    temperature = []
    index = 0
    for row in data:
        if index > 0:
            temperature.append(int(row[1]))
        print(row)
        index += 1

print(f"Temperature:\n{temperature}\n")

# with pandas - get data from column
data = pd.read_csv("weather_data.csv")
temp_data = data['temp']
print(f"Temperature:\n{temp_data}\n")

condition_data = data.condition
print(f"Condition:\n{condition_data}\n")

# convert dataframe to list
data_dict = data.to_dict()
print(f"Data dictionary:\n{data_dict}\n")

# convert series to list
temp_list = temp_data.to_list()
print(f"Temperature list:\n{temp_list}\n")

avg_temp = temp_data.mean()
print(f"Average temperature = {avg_temp:.2f}")
print(f"Maximum temperature = {temp_data.max()}\n")

# get data from row
monday_row = data[data.day == "Monday"]
print(f"Monday row:\n{monday_row}\n")

# row with the highest temp
highest_temp = data[data.temp == max(data.temp)]
print(f"Highest temperature row:\n{highest_temp}\n")

monday_condition = monday_row.condition
print(f"Monday's condition:\n{monday_condition}\n")

monday_temp = (monday_row['temp'] * 1.8) + 32
print(f"Monday's temperature in Fahrenheit:\n{monday_temp}\n")

# create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# option 1
data = pd.DataFrame(data_dict)
print(f"Dataframe:\n{data}\n")

# convert to csv
data.to_csv("new_data.csv")
