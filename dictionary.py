from dataclasses import *




class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path, 'r', encoding='utf-8') as file:
            for righe in file:
                dati = righe.rstrip()
                self._dict.append(dati)

        return self._dict

    def printAll(self):
        elenco = ''
        for parola in self._dict:
            if elenco != '':
                elenco += '\n'
            elenco += parola

        return elenco

    def __repr__(self):
        elenco = ''
        for parola in self._dict:
            if elenco != '':
                elenco += '\n'
            elenco += parola

        return elenco
    @property
    def dict(self):
        return self._dict

def test():
    d = Dictionary()
    d.loadDictionary('resources/Italian.txt')
    print(d.printAll())

if __name__ == '__main__':
    test()
