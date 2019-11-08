import re
import nltk
# to install contractions - pip install contractions
from contractions import contractions_dict

def expand_contractions(text, contractions_dict):
    contractions_pattern = re.compile('({})'.format('|'.join(contractions_dict.keys())))

    def expand_match(contraction):
        print(contraction)
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contractions_dict.get(match) \
            if contractions_dict.get(match) \
            else contractions_dict.get(match.lower())
        expanded_contraction = expanded_contraction
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    print(expanded_text)
    return expanded_text

def main():

#     text = """I’ve already talked about how crucial your writing quality will be to your success in
# your studies and in the workplace.
# I’m now going to talk about how central your choice of words will be to your writing
# quality. How word-aware are you?"""
    text = """I ain't going there. You won't have to go alone 'school'. """
    text = expand_contractions(text, contractions_dict)
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    print(tokenized_sentences)

# for the doc
    # with open('sample.txt', 'r') as file:
    #     data = file.read()
    # sentence = nltk.sent_tokenize(data)
    # tokenized_sentences = [nltk.word_tokenize(sentences) for sentences in sentence]
    #
    # print(tokenized_sentences)

if __name__ == '__main__':
    main()
