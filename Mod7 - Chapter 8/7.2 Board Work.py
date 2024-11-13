import re

words = []

with open('words_alpha.txt', 'r') as wordText:
    for line in wordText:
        line = line.strip('\n')
        words.append(line)

acc = 0

print("\nStarting with st...\n")

for word in words:
    if re.match('st*', word):
        acc += 1
        print(word)

print("\nEnding with ...s\n")


for word in words:
    if re.match('[a-z]*s$', word):
        acc += 1
        print(word)

print("\nEnding with ...ing\n")


for word in words:
    if re.match('[a-z]*ing$', word):
        acc += 1
        print(word)

print("\ngg anywhere\n")


for word in words:
    if re.match('[a-z]*gg[a-z]*$', word):
        acc += 1
        print(word)

print("\nstarts and ends with a\n")


for word in words:
    if re.match('a[a-z]*a$', word):
        acc += 1
        print(word)


# make a list with 5 words

fiveWords = [word for word in words in len(word) == 5]
print(fiveWords)