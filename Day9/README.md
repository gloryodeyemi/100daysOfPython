## Day 9 - Dictionaries, Nesting, and the Secret Auction

**Stage:** Beginner

**Project:** Secret Auction

**Topics:**
* Dictionary
  ```
  dictionary = {
      key: value
  }
  ```
* Retrieving items from a dictionary
  ```
  dictionary[key]
  ```
* Empty dictionary
  ```
  empty_dictionary = {}
  ```
* Edit an item in a dictionary
  ```
  dictionary[key] = value
  ```
* Loop through a dictionary
  ```
  for key in dictionary:
    print(f"{key}: {dictionary[key]}")
  ```
* Nesting a list in a dictionary
  ```
  dictionary = {
      "key1": [list1],
      "key1": [list2],
  }
  ```
* Nesting a dictionary in a dictionary
  ```
  dictionary = {
      "key1": {
              "inner_key1": [list1],
              "inner_key2": value2
      },
      "key2": {
              "inner_key1": [list2],
              "inner_key2": value2
      },
  }
  ```
* Nesting a dictionary in a list
  ```
  list = [
    {
        "key1": "value1", 
        "key2": [value2], 
        "key3": value3
    },
    {
        "key1": "value1", 
        "key2": [value2], 
        "key3": value3
    },
  ]
  ```
