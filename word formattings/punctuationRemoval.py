import spacy

nlp = spacy.load('en_core_web_sm')

from string import punctuation

def remove_punct(text):
    """
    take string input and clean string without punctuations.
    use regex to remove the punctuations.
    """
    return ''.join(c for c in text if c not in punctuation)


def main():
    with open('sample.txt', 'r') as file:
        data = file.read()

    punct_removed = remove_punct(data)
    print(punct_removed)


if __name__ == '__main__':
    main()
