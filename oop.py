# object oriented programming

class Cars:
    # constructor method
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    # a_method_function
def myfunc(make,model,year):
    print(f"My dream car is {make},specifically the{model} from {year}")

# creating an object or instances of a class
c1 = Cars("Mercedes","S-Class",2015)
myfunc(c1.make,c1.model,c1.year)
c2 = Cars("BMW","7 Series",2022)
myfunc(c2.make,c2.model,c2.year)
c3 = Cars("Porsche", "Cayenne",2002)
myfunc(c3.make,c3.model,c3.year)
