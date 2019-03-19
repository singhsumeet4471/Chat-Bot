import nltk
import string

class lemitizer:

    lemmer = nltk.stem.WordNetLemmatizer()
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def lemToken(tokens):
        return [lemitizer.lemmer.lemmatize(token) for token in tokens]

    def LemNormalize(text):
        return lemitizer.lemToken(nltk.word_tokenize(text.lower().translate(lemitizer.remove_punct_dict)))
