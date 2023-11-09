# data = []
with open("weather_data.csv") as csv_file:
    data = csv_file.readlines()

print(data)
