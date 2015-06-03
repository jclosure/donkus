
# The task of free word association is a very common one when it comes to
# psycholinguistics, especially in the context of lexical retrieval - human subjects
# respond more readily to a word if it follows another highly associated
# word as opposed to a completely unrelated word. The instructions for performing
# the association are fairly straightforward - the subject is asked for
# the word that immediately comes to mind upon hearing a particular word.
# Task: Use a large POS-tagged text corpus to perform free word association.
# You may ignore function words and assume that the words to be associated
# are always nouns.
# For this task, we will use the concept of word co-occurrences, i.e., counting
# the number of times words occur in close proximity with each other and
# then using these counts to estimate the degree of association. For each token
# in each sentence, we will look at all following tokens that lie within
# a fixed window and count their occurrences in this context using a conditional
# frequency distribution. Listing 4 shows how we accomplish this
# using Python and NLTK with a window size of 5 and the POS-tagged version
# of the Brown corpus.

