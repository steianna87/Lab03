from dictionary import *
from richWord import *
from dataclasses import *

class MultiDictionary:
    def __init__(self):
        self.dizionari = {}

    def addDict(self, lingua):
        dizionario = Dictionary()
        path = 'resources/' + lingua + '.txt'
        dizionario.loadDictionary(path)
        self.dizionari[lingua] = dizionario

    def printDic(self, language):
        dizionario = self.dizionari[language]
        return dizionario.printAll()
    def searchWord(self, words, language):
        resoconto = []
        for word in words.strip().split(' '):
            if self.dizionari[language]._dict.__contains__(word.lower()):
                rw = RichWord(word)
                rw.corretta = True
                resoconto.append(rw)
            else:
                rw = RichWord(word)
                rw.corretta = False
                resoconto.append(rw)
        return resoconto

    def searchWordLinear(self, words, language):
        resoconto = []
        for word in words.strip().split(' '):
            trovata = False
            for parola in self.dizionari[language]._dict:
                if parola == word.lower():
                    rw = RichWord(word)
                    rw.corretta = True
                    resoconto.append(rw)
                    trovata = True
                    break
            if trovata == False:
                rw = RichWord(word)
                rw.corretta = False
                resoconto.append(rw)
        return resoconto

def test():
    md = MultiDictionary()
    md.addDict('Italian')
    print(md.searchWord('casa dolcw mario e serpenti', 'Italian'))
if __name__ == '__main__':
    test()