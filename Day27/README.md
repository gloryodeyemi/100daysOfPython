## Day 27 - TKinter, *args, **kwargs, and Creating GUI Programs

**Stage:** Intermediate

**Project:** Mile to Kilometers Converter (try [here](https://replit.com/@GloryOdeyemi/Miles-to-Km-Converter?v=1))

**Topics:**
* Default values for arguments
```
def func(a=1, b=2, c=3)
    do something with a
    do something with b
    do something with c
    
func()
```

* Unlimited positional arguments - *args
  - the asteriks is important 
  - the name (args) can be changed
  - *args is a tuple
```
def add(*args):
    for n in args:
        print(n)
```

* Unlimited keywords arguments - **kwargs
  - the asteriks are important 
  - the name (kwargs) can be changed
  - **kwargs is a dictionary
```
def func(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

* TKinters layout managers
  - pack()
    ```
      label.pack(side="left")
    ```
  - place() - precise positioning (works with coordinates).
    ```
      label.place(x=0, y=0)
    ```
  - grid()
    ```
      label.grid(column=0, row=0)
    ```