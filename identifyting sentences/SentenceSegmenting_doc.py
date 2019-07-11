# Import spaCy and load the language library
import spacy
#load small version of english library
nlp = spacy.load('en_core_web_sm')

with open('sample1.txt', 'r') as file:

    data = file.read().replace('\n', ' ')
# print(data)

doc = nlp(data)
for sent in doc.sents:
    print(sent)