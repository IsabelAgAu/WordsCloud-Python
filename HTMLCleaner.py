'''
Created on 7 de jun. de 2016

@author: Isabel Aguilar
'''

import urllib2
import re

class HTMLCleaner():

    def GetPageSource(self, url):
        response = urllib2.urlopen(url)
        return response.read()
    
    def DeleteHTMLTags(self, source):
        words = re.sub(re.compile('<script>.*?</script>',re.DOTALL), ' ', source) # Clean script tags and content
        words = re.sub(re.compile('<.*?>',re.DOTALL), ' ', words) # Clean html tags
        return re.sub(re.compile('<!--.*?-->',re.DOTALL), ' ', words) #Clean all the html comments
        

    def GetWordsFromSourceAsOrderedList(self,source):
        words_list = re.findall('[a-zA-Z_]{2,}', source)
        words_list = [x.lower() for x in words_list]
        return words_list.sort()


    def CleanHTMLFromURL(self,url):
        source = self.GetPageSource(url)
        words = self.DeleteHTMLTags(source)
        return self.GetWordsFromSourceAsOrderedList(words)
