#Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a, b):
    sum = a + b
    print("Sum = ", sum)

value_a = int(input("Enter the first number:"))
value_b = int(input("Enter the second number:"))

sum_of_integers(value_a, value_b)