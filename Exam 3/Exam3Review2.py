wordList = ['you', 'i', 'it']
wordDict = {}
newList = []
with open('wap.txt', 'r') as wap:
    ono = wap.read().split()
    for word in ono:
        if word in wordList:
            wordDict[word] = wordDict.get(word, 0) + 1


for i in wordDict.items():
    newList.append(i)


def getFreq(i):
    return i[1]

newList.sort(key=getFreq, reverse=True)

for i in newList:
    print(f"{i[0]} {i[1]}")