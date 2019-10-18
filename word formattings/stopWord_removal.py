import spacy

nlp = spacy.load('en_core_web_sm')

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# declare a single stopword - declaration  must be done with correct case also
stop_words.add('Harry')

# list of new stopwords

# new_stop_words = ['Potter', 'Dursley', 'cousin']-for given text
new_stop_words_doc = ['Karen', 'Vampire']
stop_word_list = stop_words.union(new_stop_words_doc)


def remove_stopwords(sentence):
    """
    removes all the stop words like "is,the,a, etc."
    5 lines of code can be written in one line as:
        return ' '.join([w for w in word_tokenize(sentence) if not w in stop_words])
    """
    clean_sent = []
    for w in word_tokenize(sentence):
        if not w in stop_word_list:
            clean_sent.append(w)
    return " ".join(clean_sent)


def main():
    with open('sample.txt', 'r') as file:
        data = file.read()

    # for given text
    # text = """Harry Potter is the most miserable, lonely boy you can imagine. He’s shunned by his relatives, the Dursley’s, that have raised him since he was an infant. He’s forced to live in the cupboard under the stairs, forced to wear his cousin Dudley’s hand-me-down clothes, and forced to go to his neighbour’s house when the rest of the family is doing something fun. Yes, he’s just about as miserable as you can get."""
    cleaned_text = remove_stopwords(data)
    print(cleaned_text)


if __name__ == '__main__':
    main()
