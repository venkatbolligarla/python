# class Venkat:                                         #Create a class. Class name "Venkat"

#     print("This is the class method")                   #Print statement
#     def display(self):                                  # This Function is creating inside Class & written tTwo variables also
#         a = "A is a variable"
#         b = "B is a variable"
#         print(a,b)
# obj = Venkat()                                          #Create Object
# obj.display()                                           # call the function
# -----------------------------------------------------------------------------------------------------------------



# class Mobile:                                                   # Inside the __init method is used here.

#     def __init__(self, brand, battery, ram, price):             # Inside Function Arrguments are passed here.
#         self.Brand = brand                                      # Inslization of the self Keyword "brand to price" 
#         self.Battery= battery
#         self.ram = ram
#         self.price= price
#     def display(self):                                         #This is the normal funhction & Attached here self key word also.
#         print("Brand :",self.Brand)
#         print("Battery :",self.Battery)
#         print("Ram :",self.ram)
#         print("Price :",self.price)
#         print("====================")
# for i in range(3):                                             # Here iam using forloop Because one code use multiple times. 
#     obj = Mobile("Vivo", "5000mgh", "8GB", "20,000rs")         #The class was changed to "OBJECT"
#     obj.display()                                               # Call the Function.

#     obj1 = Mobile("Realme", "4300mgh", "4GB", "12,000rs")    # one class call multiple times And change the object name
#     obj1.display()
# -----------------------------------------------------------------------------------------------------------------


class Mobile:                                                     #I am already write in print label
    def __init__(self):
        print("This is the Automatic excution of the __init__ method")
    def display(self):
        print("This is the particlearly call the method")

obj = Mobile()
obj.display()