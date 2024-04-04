with open("texto1.txt") as txt1, open("texto2.txt") as txt2, open("texto3.txt") as txt3, open("texto4.txt") as txt4, open("texto5.txt") as txt5:
    palavras = txt1.read().split() + txt2.read().split() + txt3.read().split() + txt4.read().split() + txt5.read().split()
    dicionario = {}
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    dicionario = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)
    for i in range(100):
        print(dicionario[i])
    print("Quantidade de palavras distintas: ", len(dicionario))
    print("Quantidade de palavras no texto: ", len(palavras))
    for i in range(100):
        print(dicionario[i][0], ":", dicionario[i][1]/len(palavras))
        