# Take user's name as input
name = input("Enter your name: ")

# Print a customized greeting
print(f"Hello, {name}! Welcome to Python programming.")

def find_factorial(n):
    # Base cases: factorial of 0 or 1 is always 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * find_factorial(n - 1)

num = int(input("Enter a positive integer: "))

if num < 0:
    print("Factorials are not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {find_factorial(num)}")

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

# Receive and convert user input into decimal numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add the numbers together
result = num1 + num2

# Display the sum
print(f"The sum of {num1} and {num2} is: {result}")


txt = input("Enter a string: ")
if txt == txt[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

num = int(input("Enter an integer: "))

# Check if the remainder is 0 when divided by 2
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")


while True:
    print("Hello world")

number = int(input("Display multiplication table for: "))

# Loop 10 times from 1 to 10
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

text = input("Enter a word to check: ").lower()

# Reverse the string using slicing syntax
reversed_text = text[::-1]

if text == reversed_text:
    print("Yes, this word is a palindrome!")
else:
    print("No, this word is not a palindrome.")


word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

