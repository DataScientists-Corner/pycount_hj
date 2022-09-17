from string import punctuation
from typing import Counter


def load_text(input_file):
    '''Load text file as a text and return a string'''
    with open(input_file, "r") as file:
        text = file.read()
    return text


def clean_text(text):
    '''Lower case and remove punctuation from string'''
    text = text.lower()
    for p in punctuation:
        text = text.replace(p,"")
    return text


def count_words(input_file):
    '''Count unique words in text file'''
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
