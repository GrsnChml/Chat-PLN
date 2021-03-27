import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize (sentence):
    return nltk.word_tokenize(sentence);

def stem (word):
    return stemmer.stem(word.lower())

def bag_of_words (tokenized_token, all_words):
    '''
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool" ]
    bog = [0, 1, 0, 1, 0, 0, 0]
    '''
    pass


# a = "How long does shipping take?"
#
# print(a)
# a=tokenize(a)
# print(a)

# words = ["Organize", "organizes", "organizing"]
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)