import spacy

nlp = spacy.load('en_core_web_sm')

from string import punctuation

def remove_punct(text):
    return ''.join(c for c in text if c not in punctuation)

def main():
    # with open('sample2.txt', 'r') as file:
    #     data = file.read()

    text = """Harry Potter (the hero), is the most miserable, lonely boy you can imagine. He’s shunned by his relatives, the Dursley’s, that have raised him since he was an infant. He’s forced to live in the cupboard under the stairs, forced to wear his cousin Dudley’s hand-me-down clothes, and forced to go to his neighbour’s house - "Malin" when the rest of the family is doing something fun. Yes, he’s just about as miserable as you can get."""
    punct_removed = remove_punct(text)

    # punct_removed = remove_punct(data)
    print(punct_removed)

if __name__ == '__main__':
    main()
