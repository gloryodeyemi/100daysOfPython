## Day 12 - Scope

**Stage:** Beginner

**Project:** Number Guessing Game (play [here](https://replit.com/@GloryOdeyemi/NumberGuesser?v=1))

**Topics:**
* **Local scope:** accessible only inside a function.
  
* **Global scope:** accessible everywhere in the code.
  
* **Modifying global variable** (not advisable in a local scope)
  ```
  variable = 1
  
  def function():
      global variable
      variable = 2
      print(f"variable inside function: {variable}")
  
  function()
  print(f"variable outside function: {variable}")
  ```
* **Constants** - use uppercase letters

  ```PI = 3.142```
