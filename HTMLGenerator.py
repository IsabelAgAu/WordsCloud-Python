'''
Created on 2 de jul. de 2016

@author: Tenar
'''

class HTMLGenerator(object):
    
    def GenerateHTMLDoctypeDeclaration(self):
        return "<!DOCTYPE html>"

    def GenerateHTMLHeader(self, title):
        return "<HEAD><TITLE>%s</TITLE></HEAD>" % title
    
    def GenerateHTMLBody(self, dictionary_words):
        html = "<body>"
        for key in dictionary_words.keys():
            html += "<font size=\"%s\">%s</font>" % (dictionary_words[key], key) 
        html += "</body>" 
        return html
    
    def GenerateFinalHTML (self,dictionary_words, title):
        html = self.GenerateHTMLDoctypeDeclaration()
        html += "<html>"
        html += self.GenerateHTMLHeader(title)
        html += self.GenerateHTMLBody(dictionary_words)
        html += "</html>"
        
        return html