import nltk
from nltk.corpus import wordnet
from util.rule_based import contextHeavyWords
nltk.download('wordnet')
nltk.download('punkt')

def paraphrase(sentence):
    words = nltk.word_tokenize(sentence)
    paraphrase_words = []
    for word in words:
        # Check if word is a single-word, all-uppercase string
        if word in contextHeavyWords():
            paraphrase_words.append(word)
        else:
            synonyms = wordnet.synsets(word)
            if synonyms and synonyms[0].lemmas():
                synonym = synonyms[0].lemmas()[0].name()
                paraphrase_words.append(synonym)
            else:
                paraphrase_words.append(word)
    return " ".join(paraphrase_words)
