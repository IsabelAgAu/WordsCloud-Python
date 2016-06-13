'''
Created on 13 de jun. de 2016

@author: Isabel Aguilar
'''
import unittest
from WordsPreprocessor import WordsPreprocessor

class TestWordsPreprocessor(unittest.TestCase):

    def testDeleteWordsWithoutMeaning_WhenWordsListHasArticles_ShouldDeleteArticles(self):
        list_without_articles = WordsPreprocessor().DeleteWordsWithoutMeaning(["the", "dog", "cat"])
        self.assertEqual(["dog", "cat"], list_without_articles, "Articles should not appear")

    def testDeleteWordsWithoutMeaning_WhenWordsListHasPrepositions_ShouldDeletePrepositions(self):
        list_without_prepositions = WordsPreprocessor().DeleteWordsWithoutMeaning(["between", "dog", "cat", "like"])
        self.assertEqual(["dog", "cat"], list_without_prepositions, "Prepositions should not appear")

    def testDeleteWordsWithoutMeaning_WhenWordsListHasAdverbs_ShouldDeleteAdverbs(self):
        list_without_adverbs = WordsPreprocessor().DeleteWordsWithoutMeaning(["nowhere", "dog", "sometimes", "cat"])
        self.assertEqual(["dog", "cat"], list_without_adverbs, "Adverbs should not appear")

    def testDeleteWordsWithoutMeaning_WhenWordsListHasConjunctions_ShouldDeleteConjunctions(self):
        list_without_conjunctions = WordsPreprocessor().DeleteWordsWithoutMeaning(["while", "dog", "since", "cat"])
        self.assertEqual(["dog", "cat"], list_without_conjunctions, "Conjunctions should not appear")

    def testDeleteWordsWithoutMeaning_WhenWordsListHasOthersWordsWithoutMeaning_ShouldDeleteOthersWordsWithoutMeaning(self):
        list_without_others = WordsPreprocessor().DeleteWordsWithoutMeaning(["is", "dog", "th", "cat"])
        self.assertEqual(["dog", "cat"], list_without_others, "Others words without meaning should not appear")


if __name__ == "__main__":
    unittest.main()