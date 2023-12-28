def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print(f"k.m.m:{num1} , {num2} is: {lcm(num1, num2)}")