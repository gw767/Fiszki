def fiszki():
    print("            WORDS TRANSLATOR V.1.0")
    print("Translate word from english language to polish.\nIf translate is correct, you get 1 point.\n")
    eng = ['cat', 'cow', 'dog', 'goat', 'parrot']
    pol = ['kot', 'krowa', 'pies', 'owca', 'papuga']
    punkty = 0
    for i in range(5):
        slowo = str(input(print(eng[i]+":")))
        if slowo == pol[i]:
            print("Brawo! Zdobywasz punkt.")
            punkty = punkty+1
        else:
            print("Źle!")
    print("Koniec! Zdobyłeś %i punktów." % punkty)


fiszki()
