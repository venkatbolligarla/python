count = 0                                    # The count is Zero
n = int(input("Enter Number "))              # This line Write by input box
for i in range(1,n+1):                       # The range is increasing 1 to n+1. Because N value we donot know
    if n % i == 0:                           # module by given number by same number
        count+=1                             # increasing by count value
if count == 2:                               # Using if condition conformation prime number or not 
    print("This is PRIME NUMBER")
else:
    print("NOT PRIME NUMBER")