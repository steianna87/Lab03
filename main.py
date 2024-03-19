import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        sc.addLingua('Italian')
        txtInStr = input()
        sc.handleSentence(txtInStr,"Italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        sc.addLingua('English')
        txtInStr = input()
        sc.handleSentence(txtInStr,"English")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        sc.addLingua('Spanish')
        txtInStr = input()
        sc.handleSentence(txtInStr,"Spanish")
        continue

    if int(txtIn) == 4:
        break


