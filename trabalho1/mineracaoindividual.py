arq = open("texto1.txt","r+", encoding="utf-8") # Abre um arquivo texto1.txt

palavras = arq.read().split() #read() retorna uma string com o conteúdo do arquivo e split() retorna uma lista com as palavras do arquivo

dicionario = {}  #cria um dicionário vazio
for palavra in palavras: #para cada palavra na lista palavras
    if palavra in dicionario: #se a palavra já está no dicionário
        dicionario[palavra] += 1 #incrementa o valor da palavra no dicionário
    else: #se a palavra não está no dicionário
        dicionario[palavra] = 1 #adiciona a palavra no dicionário com valor 1

# ordena o dicionario em ordem decrescente
dicionario = sorted(dicionario.items(), key=lambda x: x[1], reverse=True) #sorted() retorna uma lista ordenada

# imprime as 100 palavras mais frequentes
for i in range(100): #para cada palavra na lista dicionario
    print(dicionario[i]) #imprime a palavra e a frequência

print("Quantidade de palavras distintas: ", len(dicionario)) #imprime a quantidade de palavras distintas

print("Quantidade de palavras no texto: ", len(palavras)) #imprime a quantidade de palavras no texto

for i in range(100):  #para cada palavra na lista dicionario
    print(dicionario[i][0], ":", dicionario[i][1]/len(palavras))  #imprime a palavra e a frequência relativa

arq.close() #fecha o arquivo



