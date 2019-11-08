# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
# Import the displacy library
# from spacy import displacy

# Create a simple Doc object
# doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")
#doc = nlp(u"We are team Aztec. The undergraduates of faculty of Information of Technology.")

# load a text file
with open('sample.txt', 'r') as file:

    data = file.read().replace('\n', ' ')
# print(data)

doc = nlp(data)

# for sent in doc.sents:
#     print(sent)

for token in doc:
    print(f'{token.text:{10}} {token.pos_:{7}} {token.dep_:{7}} {spacy.explain(token.dep_)}')
