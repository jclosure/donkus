import nltk


## REF:
## http://www.nltk.org/book/ch01.html
## old nlp ref: http://desilinguist.org/pdf/crossroads.pdf


from nltk.corpus import gutenberg

print(gutenberg.fileids())


from nltk import FreqDist

words = gutenberg.words('austen-persuasion.txt')

## compute total words in corpus
total_words = len(words)

## compute total unique words in corpus
total_uniqu_words = len(set(words))


fd = FreqDist(words)

## the frequency distribution also holds this kind of information
len(fd)


#first 10
#for word in list(fd)[:10]:
#    print(word, fd[word]


print(fd.most_common(10))


