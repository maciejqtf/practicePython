filePath = 'text.txt'

# Wypisanie wszystkich wierszy :

with open(filePath, 'r') as file:
    #line = file.readline() # niepotrzebne jeśli i tak pętlą for iterujemy po pliku
    for line in file:
        print(line)

# zadanie :

with open(filePath, "r") as file:
    all_text = file.read()
    names = all_text.split() # tworzymy listę imion
    namesDict = {} # tworzymy pusty słownik
    for i in set(names): # Set tworzy liste o unikalnych wartościach. Dla każdego imiona, które są 3
        n = 0 # ustawiamy licznik na 0
        for j in names: # dla każdego pola wśród listy imion ( których jest 100)
            if i == j: # jeśli imię z setu == imię z listy
                n+=1 # to zwiększ licznik o 1
                namesDict[i] = n # przyporządkuj do słownika klucz = i (imię) : wartość - n (liczbę powtórzeļ imienia)
    print(namesDict)
