'''
Created on 2 de jul. de 2016

@author: Isabel Aguilar
'''
import unittest
from HTMLGenerator import HTMLGenerator

class TestHTMLGenerator(unittest.TestCase):

    def testGenerateHTMLDoctypeDeclaration (self):
        html = HTMLGenerator().GenerateHTMLDoctypeDeclaration()
        self.assertEqual("<!DOCTYPE html>", html, "")

    def testGenerateHTMLHeader(self):
        html = HTMLGenerator().GenerateHTMLHeader("This is a test")
        print html
        self.assertEqual("<HEAD><TITLE>This is a test</TITLE></HEAD>", html, "")
        
    def testGenerateHTMLBody(self):
        html = HTMLGenerator().GenerateHTMLBody(({'dog': 10, 'cat': 5}))
        expected_html = "<body><font size=\"10\"> dog </font><font size=\"5\"> cat </font></body>"
        self.assertEqual(expected_html, html, "")
        
    def testGenerateFinalHTML(self):
        html = HTMLGenerator().GenerateFinalHTML(({'dog': 10, 'cat': 5}), "Testing")
        expected_html = "<!DOCTYPE html><html><HEAD><TITLE>Testing</TITLE></HEAD>"
        expected_html +="<body><font size=\"10\"> dog </font><font size=\"5\"> cat </font></body></html>" 
        self.assertEqual(expected_html, html, "")

if __name__ == "__main__":
    unittest.main()