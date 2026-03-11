##1.remove duplicates from a string:

text = input("enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result = result+ch
print("after removing duplicates:",result)


##2.remove duplicate words from string:

text = input("sentence: ")
words = text.split()
result = []
for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))


##3.sort leeter in a word:

word = input("Enter a word: ")

letters = list(word)
letters.sort()

print("".join(letters))


