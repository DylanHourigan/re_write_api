import random
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from util.rule_based import contextHeavyWords

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_wordnet_pos(nltk_pos):
    tag = nltk_pos[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def paraphrase(sentence):
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    
    paraphrase_words = []
    for word, nltk_pos in tagged_tokens:
        wordnet_pos = get_wordnet_pos(nltk_pos)  # Convert NLTK POS to WordNet POS
        
        # Check if word is a single-word, all-uppercase string
        if word in contextHeavyWords():
            paraphrase_words.append(word)
        else:
            synonyms = wordnet.synsets(word, pos=wordnet_pos)  # Use the POS info
            if synonyms:
                chosen_synonym = random.choice(synonyms)
                if chosen_synonym.lemmas():
                    synonym = random.choice(chosen_synonym.lemmas()).name()
                    paraphrase_words.append(synonym)
                else:
                    paraphrase_words.append(word)
            else:
                paraphrase_words.append(word)
    return " ".join(paraphrase_words)
