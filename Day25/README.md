## Day 25 - Working with CSV Data and the Pandas Library

**Stage:** Intermediate

**Project:** U.S. States Game

**Topics:**
* **Reading CSV Data**
    ```
    import csv
    import pandas as pd

    # with csv
    with open("data.csv") as csv_file:
        data = csv.reader(csv_file)
  
    # with pandas
    data = pd.read_csv("data.csv")
    ```
  
* **DataFrames & Series**
  ```
  # convert dataframe to list
  data_dict = data.to_dict()
  
  # convert series to list
  data_series = data["column_name"]
  series_list = data_series.to_list()
  
  # create a dataframe
  data_dict = {
      "letters": ["A", "B", "C"],
      "numbers": [1, 2, 3]
  }
  data = pd.DataFrame(data_dict)
  
  # convert to csv
  data.to_csv("new_data.csv")
  ```
  