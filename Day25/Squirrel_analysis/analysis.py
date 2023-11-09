import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(f"{squirrel_data.head()}\n")

squirrel_columns = squirrel_data.columns
print(f"Columns in squirrel data:\n{squirrel_columns}\n")

# option 1
squirrel_color_count = (squirrel_data.groupby(["Primary Fur Color"])["Primary Fur Color"].count().
                        reset_index(name="count"))
print(f"Colors in squirrel data:\n{squirrel_color_count}\n")
squirrel_color_count.to_csv('squirrel_colors.csv', index=False)

# option 2
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

name_list = ['Gray', 'Black', 'Cinnamon']
count_list = [gray_count, black_count, cinnamon_count]

count_dict = {
    "colors": name_list,
    "count": count_list
}

count_df = pd.DataFrame(count_dict)
print(f"Colors in squirrel data:\n{count_df}\n")
count_df.to_csv("squirrel_colors2", index=False)
