# %%
import nltk

nltk.download('wordnet')

from nltk.corpus import wordnet as wn

# %%
wn.synsets('people')
# %%
wn.synsets('people')[0].hypernyms()


# %%
def hypernyms(word):
    current_node = wn.synsets(word)[0]
    yield current_node

    while True:
        try:
            current_node = current_node.hypernyms()[0]
            yield current_node
        except IndexError:
            break

for h in hypernyms('policeman'):
    print(h)

# %%
[h for h in hypernyms('firefighter')]
# %%
[h for h in hypernyms('sheriff')]
# %%
[h for h in hypernyms('mailman')]

# %%
def distance(word1, word2):
    word1_hypernyms = [h for h in hypernyms(word1)]

    for i, word2_hypernym in enumerate(hypernyms(word2)):
        try:
            return i + word1_hypernyms.index(word2_hypernym)
        except ValueError:
            continue


distance('sheriff', 'student')

# %%
import numpy as np


def similarity(word1, word2):
    return -np.log(distance(word1, word2))


print(similarity('sheriff', 'student'))
print(similarity('sheriff', 'policeman'))