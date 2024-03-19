from time import *

from multiDictionary import *

class SpellChecker:

    def __init__(self):
        self.multiDict = MultiDictionary()

    def addLingua(self, lingua):
        self.multiDict.addDict(lingua)
    def handleSentence(self, txtIn, language):
        tc1 = time()
        resoconto = self.multiDict.searchWord(replaceChars(txtIn), language)
        errateC = [i for i in resoconto if i.corretta == False ]
        tc2 = time()

        tl1 = time()
        resoconto = self.multiDict.searchWordLinear(replaceChars(txtIn), language)
        errateL = [i for i in resoconto if i.corretta == False]
        tl2 = time()
        printWrong(errateC, 'contains', tc2-tc1)
        printWrong(errateL, 'Linear search', tl2 - tl1)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
def printWrong(wrong, tipologia, tempo):
    print('______________________________')
    print(f'Using {tipologia}')
    elenco = ''
    for parola in wrong:
        if elenco != '':
            elenco += '\n'
        elenco += parola.__str__()
    print(elenco)
    print(f'Time elapsed {tempo}')
    print('______________________________')