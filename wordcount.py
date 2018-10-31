import operator

def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news


textfile = 'TrumpWord.txt'

file = open(textfile)
buffer = file.read()
wordsDict = {}
for words in clean(buffer).split():
    wordsDict[words] = wordsDict.get(words, 0) + 1

sortedWords = sorted(wordsDict.items(), key=operator.itemgetter(1))

for words in sortedWords:
    print("{}: {}".format(words[0], words[1]))


