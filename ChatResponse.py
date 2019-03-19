from sklearn.feature_extraction.text import TfidfVectorizer as tfvec
from sklearn.metrics.pairwise import cosine_similarity as cosim

import random
import nltk

from lemitizer import lemitizer

class ChatResponse:
    f = open('data.txt', 'r', errors='ignore')
    raw = f.read()
    raw = raw.lower()

    sent_token = nltk.sent_tokenize(raw)
    word_token = nltk.word_tokenize(raw)

    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

    def greeting(sentence):
        for word in sentence.split():
            if word.lower() in ChatResponse.GREETING_INPUTS:
                return random.choice(ChatResponse.GREETING_RESPONSES)

    def response(user_response):
        robo_response = ''
        ChatResponse.sent_token.append(user_response)
        TfidfVec = tfvec(tokenizer=lemitizer.LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(ChatResponse.sent_token)
        vals = cosim(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if (req_tfidf == 0):
            robo_response = robo_response + "I am sorry! I don't understand you"
            return robo_response
        else:
            robo_response = robo_response + ChatResponse.sent_token[idx]
            return robo_response