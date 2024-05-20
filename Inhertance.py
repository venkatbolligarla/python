# #single Level
# class parents:
#     def fun1(self):
#         print("This is the parent class")
# class child(parents):
#     def fun2(self):
#         print("This is the child class")
# obj = child()
# obj.fun1()
# obj.fun2()


# multi-Level 

# class parents:
#     def fun1(self):
#         print("This is the parent class")
# class child(parents):
#     def fun2(self):
#         print("This is the child class")
# class grandchild(child):
#     def fun3(self):
#         print("This is the grandchild class")

# obj = grandchild()
# obj.fun1()
# obj.fun2()
# obj.fun3()

#hirarichal inheritance
# class parents:
#     def fun1(self):
#         print("This is the parent class")
# class child1(parents): 
#     def fun2(self):
#         print("This is the child1 class")
# class child2(parents):
#     def fun3(self):
#         print("This is the child2 class")

# obj1 = child2()
# obj = child1()
# obj.fun1()
# obj.fun2()
# obj1.fun3()

# MULTIPLE INHERITANCE:
# class Father:
#     def fun1(self):
#         print("This is the parent class")
# class Mother: 
#     def fun2(self):
#         print("This is the Mother class")
# class child(Father, Mother):
#     def fun3(self):
#         print("This is the child class")

# obj = child()
# obj.fun1()
# obj.fun2()
# obj.fun3()



# USING "SUPPER KEY WORD:"

class A:
    def __init__(self):
        print("THis is used for super keyword A")
    def display(sefl):
        print("This is the self1 function")
class B(A):
    def __init__(self):
        print("THis is used for super keyword B")
        super().__init__()
    def display1(sefl):
        print("This is the self function")
obj = B()
obj.display()
obj.display1()