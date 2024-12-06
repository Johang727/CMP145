wordList = ['you', 'i', 'it']
wordDict = {}
with open('wap.txt', 'r') as wap:
    ono = wap.read().split()
    for word in ono:
        if word in wordList:
            wordDict[word] = wordDict.get(word, 0) + 1


for i in wordDict.items():
    print(f"{i[0]} {i[1]}")

