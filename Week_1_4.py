#Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

vowels_list = ["a", "e", "i", "o", "u"]
string = input("Enter a word\n")
input_word = string
count = 0
for i in input_word:
    if(i in vowels_list):
        count = count + 1
print(count)