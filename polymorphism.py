#The polymorphism is one of the opps concet in python. And it means multiple forms or many forms.
#1)Method over-loading 
#2)Method over-riding

#METHOD OVER-LOADING
# same class 
# same function or same method names
# defferent perameters

class Venkat:
    def display(self, a, b):
        return a + b
    def display(self, a, b, c=1):
        return a + b + c

obj = Venkat()
print(obj.display(1,2))

#METHOD OVER-RIDING
# different class 
# same function or same method names
# defferent perameters

class A:
    def display(self):
        print("This is class A function")
class B(A):
    def display(self):
        print("This is class B function")
        super().display()

obj = B()
obj.display()