'''
Created on 7 de jun. de 2016

@author: Isabel Aguilar
'''

from HTMLCleaner import HTMLCleaner
from WordsPreprocessor import WordsPreprocessor
from collections import Counter

if __name__ == '__main__':

    words_list = HTMLCleaner().CleanHTMLFromURL("https://en.wikipedia.org/wiki/Glass")
    words_list_processed = WordsPreprocessor().DeleteWordsWithoutMeaning(words_list)

    #print words_list_processed

    #COUNT THE OCURRENCES OF EACH WORD
    doctionary_words = Counter(words_list_processed)

    print doctionary_words