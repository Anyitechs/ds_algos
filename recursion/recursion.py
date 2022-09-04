# Recursion implementation
def countdown(numb):
    print(numb)
    if numb <= 1:
        return 
    else:
        countdown(numb-1)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))