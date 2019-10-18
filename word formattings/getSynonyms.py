import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet

# ------------word explaination-------------
syn = wordnet.synsets("can")
print(syn[0].definition())
print(syn[0].examples())

# ------------synonyms words-------------
# synonyms = []
# for syn in wordnet.synsets('talk'):
#     for lemma in syn.lemmas():
#         synonyms.append(lemma.name())
# print(synonyms)

# -----------antonyms words--------------
# antonyms = []
# for syn in wordnet.synsets("large"):
#     for l in syn.lemmas():
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
# print(antonyms)