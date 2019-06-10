# import pdf and undergo sentence segmenting - effective on a single page only

import PyPDF2
import spacy
nlp = spacy.load('en_core_web_sm')

# Notice we read it as a binary with 'rb'
f = open('sample.pdf', 'rb')
# f = open('pdf-test.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)


page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
# print(page_one_text)

doc = nlp(page_one_text)
for sent in doc.sents:
    print(sent)