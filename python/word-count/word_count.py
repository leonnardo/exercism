from collections import Counter
import re

def word_count(text):
    text = text.lower()
    text = re.sub("[^a-z0-9]", " ", text)
    return Counter(text.split())

