"""
wrapping of variables and methods in single unit is called encapsulation
public
private
protected
"""
class Venkat:
    def __init__(self, a, b):
        self.__a = a   #private date is can't access 
        self._b  = b   #proctected data is access
class Prasad(Venkat):
    def display(self):
        print(self._b)
obj = Prasad(5, 6)
obj.display()




#ABSTRACTION:  Hiding of information is called a data abstraction
