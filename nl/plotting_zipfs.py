## plot Zipfs Law


from nltk.corpus import gutenberg
from nltk import FreqDist
from scipy.stats import lognorm
import matplotlib
import matplotlib.pyplot as plt


all_words = gutenberg.words()

some_words = gutenberg.words('austen-persuasion.txt')


fd = FreqDist(all_words)

## initialize 2 empty lists to hold our ranks and fequencies
ranks = []
freqs = []


for rank, freq in enumerate([freq for word,freq in fd.most_common()]):
    ranks.append(rank+1)
    freqs.append(freq)

    

# ## Plot Ranks vs frequency
plt.loglog(ranks,freqs)
plt.xlabel('frequency(f)', fontsize=14, fontweight='bold')
plt.ylabel('rank(r)', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()


## note: make a ranked word list like this:
lst = list([word for word,freq in fd.most_common()])
