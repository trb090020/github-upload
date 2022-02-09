#use def to define functions (methods)

def fibonacci(n):
    #the first statement of the method body may be a string literal
    """defDemo docstring: This program demonstrates using def to create a method.

    The method will compute a Fibonacci sequence with terms not exceeding the input, n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

#call the method
fibonacci(1000)

#use a similar method to return a list rather than directly printing the values

def fibonacci_1(n):
    """This method returns a list containing a Fibonacci sequence of values
    not exceeding the value of n."""
    a, b = 0, 1
    fibList = []
    while a < n:
        fibList.append(a)
        a, b = b, a+b
    return fibList

#call the method as input to a print() statement
print(fibonacci_1(1000))
