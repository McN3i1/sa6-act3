sum_of_digits = lambda num: sum(int(digit) for digit in str(num))

num = int(input("Enter a number: "))

x = sum_of_digits(num)

print(f"The sum of digits is: {x}")