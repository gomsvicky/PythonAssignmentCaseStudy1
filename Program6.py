word = input("Enter a word ")
print("Split the word and print each character")
for i in word:
    print(i)
print("slice the word and create new sub strings")
words = [word[0:2], word[2:5], word[0:4], word[3:6]]
print(words)
print("Multiply the string for 100 times")
print(word*100)
print("string 2 concatenate with 4th string")
print(words[1]+words[3])