import os
import re
import pandas as pd
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt_tab', force=True) # For sentence tokenization
nltk.download('stopwords', force=True) # For stopwords filtering

stop_words = set(stopwords.words('english'))

# Loading positive/negative word dictionaries
positive_words = set(open(r"C:\Users\RUDRAANSH GUPTA\Downloads\20211030 Test Assignment\MasterDictionary\positive-words.txt").read().split())
negative_words = set(open(r"C:\Users\RUDRAANSH GUPTA\Downloads\20211030 Test Assignment\MasterDictionary\negative-words.txt").read().split())

# Function to clean text using stopwords
def clean_text(text):
    words = word_tokenize(text)
    cleaned_words = [word for word in words if word.isalpha() and word.lower() not in stop_words]
    return cleaned_words

# Function to compute syllables in a word

def syllable_count(word):

    word = word.lower()
    syllable_count = len(re.findall(r'[aeiouy]+', word))  # Count vowels
    if word.endswith(('es', 'ed')):
        syllable_count = max(1, syllable_count - 1)
    return syllable_count

