def is_factorial(n):
    result = 1
    i = 1
    while result < n:
        i += 1
        result *= i
    if result == n:
        return True
    else:
        return False

number = int(input("enter number: "))
if is_factorial(number):
    print("yes")
else:
    print("no")