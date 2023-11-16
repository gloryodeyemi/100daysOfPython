# unlimited positional arguments - *args is a tuple
def add(*args):
    result = 0
    for num in args:
        result += num
    return result


res1 = add(2, 5, 8, 9)
print(f"Result 1 = {res1}")

res2 = add(15, 3)
print(f"Result 2 = {res2}")


# unlimited positional arguments - *kwargs is a dictionary
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"n = {n}")


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan",  model="GT-R")
print(f"My car model = {my_car.model}\nMy car color = {my_car.color}")
