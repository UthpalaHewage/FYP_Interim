# Import spaCy and load the language library
import spacy
#load small version of english library
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')
for sent in doc.sents:
    print(sent)

# # Print each token separately-parse the entire stream into seperate components
# Create a Doc object
# obj = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
# for token in obj:
#     print(token.text)