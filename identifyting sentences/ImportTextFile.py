import spacy
nlp = spacy.load('en_core_web_sm')

with open('original.txt', 'r') as file:
# with open('sample.txt', 'r') as file:

    data = file.read().replace('\n', ' ')
# print(data)

doc = nlp(data)
for sent in doc.sents:
    print(sent)


# file = open('original.txt')
# file.seek(0)
# print(file)
# print(file.read())
# file.close()

