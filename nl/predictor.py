
from nltk.corpus import gutenberg
from nltk import ConditionalFreqDist
from random import choice

#create the distribution object
cfd = ConditionalFreqDist()

## for each token count the current word given the previous word
prev_word = None
for word in gutenberg.words('austen-persuasion.txt'):
    cfd[prev_word][word] += 1
    prev_word = word

## start predicting at given word, say "therefore"
word = "therefore"
i = 1

## find all words that can follow the given word and choose one at random
while i<20:
    print word,
    lwords = cfd.get(word).keys()
    follower = choice(lwords)
    word = follower
    i += 1
    

