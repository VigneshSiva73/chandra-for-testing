
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

txt = input("Enter a string: ")
if txt == txt[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

while True:
    print("Hello world")

word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

