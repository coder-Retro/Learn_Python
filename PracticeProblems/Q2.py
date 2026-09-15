# Write a program to take a string from user then count vowels and consonants

sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0

for letter in sentence:
    if letter in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1

print(f"There are {vowels} vowels in this sentence")
print(f"There are {consonants} consonants in this sentence")