for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print("")
print("=============================================") # #This all patterns are using Stars printed
for k in range(5):
    for s in range(k+1):
        print("*", end = " ")
    print(" ")
print("=============================================")
for k in range(6):
    for j in range(k):               #Revers triangle
        print(" ", end= " ")
    for s in range(6-k):
        print("  *", end = " ")
    print(" ")
print("=============================================")
for k in range(6):
    for j in range(6-k):               #normal triangle
        print(" ", end= "")
    for s in range(k+1):
        print("* ", end = "")
    print("")
print("=============================================")
for k in range(6):
    for j in range():               # triangle
        print(" ", end= " ")
    for s in range(k+1):
        print("* ", end = " ")
    print("")