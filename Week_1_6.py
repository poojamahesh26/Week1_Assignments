#Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for i in range(1,21):
    if i % 2 == 0:
        print(f"{i} is EVEN")
    else:
        print(f"{i} is ODD")