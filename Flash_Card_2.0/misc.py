import pandas as pd

txt_file = "data/fr_50k.txt"
csv_file = "data/french.csv"

data = pd.read_csv(txt_file, sep=' ')
print(data.head())
data.head(10000).to_csv(csv_file, index=False)
