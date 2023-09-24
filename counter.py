#Open file
infile = open("book of John text.txt", "r")

#Create dictionary
word_count = {

    "Father": 0,
    "God": 0,
    "Christ": 0,
    "Spirit": 0,
    "spirit": 0,
    "man": 0
}

#Count words
for line in infile:
    words = line.split()
    for word in words:
        #Remove punctuation
        word = word.strip(".,?")
        if word:
            #check for case sensitive
            if word in ["Father", "God", "Christ", "Spirit", "spirit", "man"]:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

#print counts
for word, count in word_count.items():
    print(f"{word}: {count}")

#close the file
infile.close()