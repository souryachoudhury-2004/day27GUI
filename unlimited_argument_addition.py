
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5, 6, 7))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="GTR")
print(my_car.model)
