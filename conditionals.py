# Conditionals

# if statements
# condition = True
# condition_2 = False

if not (isinstance(2, int) or isinstance("Hello world", str)): # condition = predicate, boolean expression, evaluates to true or false
    print("2 is an int") # consequent, code to execute if predicate = True
else:
    print("condition was false") # alternate, code to execute if no predicates are true

## Boolean expressions
# Comparisons: == (equal), != (not equal), > (greater than), < (less than)
# >= (greater than or equal to), <= (less than or equal to), in, is
# boolean functions: many methods, isinstance(object, class)

# Truthiness
# Numerical: zero = false, non-zero = true
# Strings/collections: empty = false, non-empty = true

# Logical operations: and, or, not

# time = input("Enter the time: ")

# if time < "12:00":
#     print("Good morning")
# elif time > "12:00":
#     print("Good afternoon")
# else:
#     print("It's noon!")