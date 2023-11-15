## Day 26 - List Comprehension and NATO Alphabet

**Stage:** Intermediate

**Project:** NATO Alphabet

**Topics:**
* Python sequences - list, range, tuple, dictionary.

* List Comprehension

``
new_list = [new_item for item in list]
``

* Conditional List Comprehension

```new_list = [new_item for item in list if test]```

* Dictionary Comprehension

```
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dict.items()}
```

* Conditional Dictionary Comprehension
```
new_dict = {new_key:new_value for item in list if test}
new_dict = {new_key:new_value for (key,value) in dict.items() if test}
```

* Looping through a DataFrame
```
for (index, row) in df.iterrows():
    print(f"Index {index}:{row}")
```