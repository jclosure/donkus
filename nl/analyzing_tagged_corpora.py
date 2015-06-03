

## • What is the most frequent tag ?
## • Which word has the most number of distinct tags ?
## • What is the ratio of masculine to feminine pronouns ?
## • How many words are ambiguous, in the sense that they appear with at least two tags ?


from nltk.corpus import brown
from nltk import FreqDist, ConditionalFreqDist

fd = FreqDist()
cfd = ConditionalFreqDist()

# for each tagged sentence in the corpus, get the (token, tag) pair and update
# both count(tag) and count(tag given token)



for sentence in brown.tagged_sents():
    for (token, tag) in sentence:
        fd[tag] += 1
        cfd[token][tag] += 1


#most frequent tag is 'NN
fd.max()

wordbins = [] # initialize a list to hold (numtags, word) tuple

# append each (number of unique tags for token, token) tuple to list
for token in cfd.conditions():
    wordbins.append((cfd[token].B(), token)) # e.g. (num of tags for token, token)

# sort tuples by the number of unique tags (higest first)
wordbins.sort(reverse=True)
print wordbins[0] # token with the max number of tags is ...
# (12, 'that') .. makes sense



male = ['he', 'his', 'him', 'himself'] # masculine pronouns
female = ['she', 'hers', 'her', 'herself'] # feminine pronouns

n_male, n_female = 0,0 # initialize counters

# total number of masculine samples
for m in male:
    n_male += cfd[m].N()

# total number of feminine samples
for f in female:
    n_female += cfd[f].N()

print float(n_male)/n_female # calculate ratio of male to female pronouns used



# calculate amgiguous tokens (more than one type of tag)
n_ambiguous = 0
for (ntags,token) in wordbins:
    if ntags>1:
        n_ambiguous += 1

n_ambiguous # number of tokens with more than a single POS tag 
# 8729
