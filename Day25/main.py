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

print(f"{temperature}\n")

# with pandas
data = pd.read_csv("weather_data.csv")
print(data['temp'])
