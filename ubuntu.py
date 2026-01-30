print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("hello 1,2,3,4")
num1 = 18
num2 = 7
sum = num1 + num2
print(f"Sum of {num1} and {num2} is {sum}")
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1)

num = 6
print("Factorial of", num, "is", factorial(num))

