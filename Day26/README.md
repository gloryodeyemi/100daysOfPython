## Day 26 - List Comprehension and NATO Alphabet

**Stage:** Intermediate

**Project:** NATO Alphabet

**Topics:**
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