n = int(input("enter number: "))

number = [1, 1]
for i in range(2, n):
    number.append(number[i-1] + number[i-2])

print(f" {n}: {number}")