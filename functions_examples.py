# function: takes in arguments, returns a value
def square_and_increment(i = 1, x = 0):
    x **= 2
    x += i
    return x

# procedure: may take arguments, may do input/print, doesn't return value
def greet(): # pragma: no cover
    name = input("Enter your name: ")
    print("Hello,", name)

def sum_of_squares(*args): # **kwargs allows arbitrary keyword arguments
    sum = 0
    for i in args:
        sum += i ** 2
    return sum

...

# print(square_and_increment(x = 3))
# greet()
print(sum_of_squares)
