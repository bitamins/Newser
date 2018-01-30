import sys
import logging
import random

class Gister:
    def __init__(self):
        pass

    def get_sentiment(self,article):
        avg = 0 #0 = neutral, 1 = positive, -1 = negative
        total = 0
        art_list = article.split()
        for word in art_list:
            total = total + random.randint(1,100)
        avg = total/len(art_list)
        return avg
