import nltk


## REF:
## http://www.nltk.org/book/ch01.html
## old nlp ref: http://desilinguist.org/pdf/crossroads.pdf


from nltk.corpus import gutenberg

print(gutenberg.fileids())


from nltk import FreqDist

fd = FreqDist(gutenberg.words('austen-persuasion.txt'))



#first 10
#for word in list(fd)[:10]:
#    print(word, fd[word]


print(fd.most_common(10))


