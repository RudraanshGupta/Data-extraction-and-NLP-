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

# Function to compute all required variables
def compute_variables(text):
    sentences = sent_tokenize(text)  # Tokenize text into sentences
    words = word_tokenize(text)  # Tokenize text into words
    
    # Clean words by removing stopwords
    cleaned_words = clean_text(text)
    
    # Sentiment Analysis: Positive/Negative Scores
    positive_score = sum(1 for word in cleaned_words if word.lower() in positive_words)
    negative_score = sum(1 for word in cleaned_words if word.lower() in negative_words)
    
    # Polarity and Subjectivity Scores
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_words) + 0.000001)
    
    # Average Sentence Length
    avg_sentence_length = len(cleaned_words) / len(sentences) if sentences else 0
