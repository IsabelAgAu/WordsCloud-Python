'''
Created on 7 de jun. de 2016

@author: Isabel Aguilar
'''

from HTMLCleaner import HTMLCleaner
from WordsPreprocessor import WordsPreprocessor
from HTMLGenerator import HTMLGenerator
from collections import Counter

if __name__ == '__main__':

    words_list = HTMLCleaner().CleanHTMLFromURL("https://en.wikipedia.org/wiki/Glass")
    words_list_processed = WordsPreprocessor().DeleteWordsWithoutMeaning(words_list)

    #COUNT THE OCURRENCES OF EACH WORD
    dictionary_words = Counter(words_list_processed)
    
    html = HTMLGenerator().GenerateFinalHTML(dictionary_words, "WORD CLOUD")

    html_file = open('word_cloud.html', 'w+')
    html_file.write(html)
    html_file.close()