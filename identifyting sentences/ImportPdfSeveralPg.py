

########NOT YET CORRECTED##########


# import pdf with several pages and undergo sentence segmenting
import PyPDF2
import spacy
nlp = spacy.load('en_core_web_sm')

# Notice we read it as a binary with 'rb'
f = open('sample.pdf', 'rb')
# f = open('pdf-test.pdf', 'rb')

pdf_text = [0]

pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

# with several pages

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    print(page.extractText())
    # pdf_text.append(page.extractText())
f.close()
print(pdf_text)
# page_one = pdf_reader.getPage(0)
# page_one_text = page_one.extractText()
# print(page_one_text)

# doc = nlp()
# for sent in doc.sents:
#     print(sent)

# first_page = pdf_document.getPage(0)
# print(first_page.extractText())






# # with several pages
# page_one = [0]
# for p in range(pdf_reader.numPages):
#     page_one_text = pdf_reader.getPage(p)
#     page_one.append(page_one_text.extractText())
# f.close()
#
# # page_one = pdf_reader.getPage(0)
# # page_one_text = page_one.extractText()
# # print(page_one_text)
#
# doc = nlp(page_one)
# for sent in doc.sents:
#     print(sent)