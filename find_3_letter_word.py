
punctuation = ",.?!\""

def find_words(filename):
    #print 3 letter words satrting with b from a file
    with open(filename) as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0] in "bB":
                    print(word)

find_words("input.txt")

