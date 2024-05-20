"""DSCRIPTION:-The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
usually starting with 0 and 1. So, the sequence typically goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
To generate the Fibonacci sequence, you start with 0 and 1, and then add the two previous numbers to get the next number."""
x = 0
y = 1
n = int(input("Enter Number: "))
for i in range(n):
    z = x + y
    x = y
    y = z
    print(z)