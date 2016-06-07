'''
Created on 7 de jun. de 2016

@author: Isabel Aguilar
'''

class WordsPreprocessor():
    
    def __init__(self):
        self.prepositions = ["aboard","about","above","across","after","against", "along","amid",
                "among", "anti","around","as","at","before","behind","below","beneath",
                "beside","besides","between","beyond","but", "by", "concerning", "considering", 
                "despite","down","during","except","excepting","excluding","following","for",
                "from","in","inside", "into", "like", "minus", "near", "of","off","on",
                "onto","other","opposite","outside","over","past","per","plus","regarding","round",
                "save","since","than","through","to","toward","towards","under","underneath",
                "unlike","until","up","upon","versus","via","with","within","without"]

        self.adverbs = ["yesterday","today","tomorrow","now","then","that","or","later","tonight","already","recently",
           "lately","soon","immediately","still","yet","ago","here","there","everywhere",
           "anywhere","nowhere","away","out","very","quite","pretty","really","well","hard",
           "quickly","slowly","carefully","hardly","barely","mostly","almost","absolutely",
           "together","always","frequently","usually","sometimes","occasionally","seldom",
           "rarely","never"]

        self.articles = ["the","a", "an", "one","some","few"]

        self.conjunctions = ["though","although","while","if","unless","until","lest","than","rather","whether",
                "whereas","after","before","once","since","till","when","whenever","while","because",
                "since","that","why","what","whatever","which","whichever","who","whoever","whom",
                "whomever","whose","how","where","wherever"]
        self.others = ["and", "is", "it", "are", "can", "also", "has", "th"]

    def DeleteWordsWithoutMeaning(self,words_list):
        return [item for item in words_list if item not in self.articles 
                      and item not in self.prepositions 
                      and item not in self.adverbs
                      and item not in self.conjunctions
                      and item not in self.others]
