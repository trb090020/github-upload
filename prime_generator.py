#FILE: prime_generator.py
#AUTHOR: Thomas Bennett

x = int(input("Enter a positive number: "))
print("You gave me " + str(x))

if(x == 1):
    print("1 is not a prime number.")
elif(x <= 0):
    print("Invalid entry, 0 or negative number not allowed...")
elif(x > 1):
    i = 2
    j = 2
    a = 2
    b = 2
    c = 0
    p = 0
    while(i <= x):
        if(i % j == 0 and i != j):
            i += 1
            j = 2
        elif(i == j):
            print(i)
            
            #Twin Prime detector
            b = a
            a = i
            c = a - b
            
            if(c == 2):
                print("Twin Prime found!")
                p += 1
            i += 1
            j = 2
        else:
            j += 1
    print(str(p) + " Twin Primes in the set of all primes up to " + str(x))
        
else: print("Something went wrong...")
