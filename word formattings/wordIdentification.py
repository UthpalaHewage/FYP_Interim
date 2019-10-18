#####SEPERATE WORDS AND DEFINE WHETHER THEY ARE STOP WORDS OR NOT######

# Import spaCy and load the language library
import spacy

nlp = spacy.load('en_core_web_sm')

# Create a string that includes opening and closing quotation marks
# myString = '"We\'re moving to L.A.!"'
myString = "'Hi, I'm Uthpala, an undergraduate from faculty of Information Technology'"

print(myString)

# Create a Doc object and explore tokens
doc = nlp(myString)
for token in doc:
    # print(token.text)
    print(token.text, '\t\t\t', token.pos_, '\t\t\t\t', token.is_stop)
    # for token in doc1:
    #     print(token.text, '\t', token.pos_, '\t', token.lemma, '\t\t', token.lemma_)
