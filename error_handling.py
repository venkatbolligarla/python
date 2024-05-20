# Interpting normal excution of the code is called error (or) Exception.
# We will handle by using error Handling.

try:
    for i in range(1,11):
        print(i,'x 2 =',i*2)
except:
    print("Error")
else:
    print("No error")
finally:
    print("always")