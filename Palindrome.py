# str = input("Enter String ")

# if str == str[::-1]:                            #The palindrome meaning is reverse string
#     print(str,",This is a palindrome")           #And here using conditional statement and "SLICING OPERATER"
# else:
#     print(str,"This is not a palindrome")           --------->    # METHOD-1





str = input("Enter String: ")
rev_str =""

for char in str:
    rev_str = char + rev_str
                                                                #method-2 PALINDROME
if str == rev_str:
    print(str,"This is a PALINDROME")
else:
    print(str,"This is not a PALINDROME")

    