# Aula 1 - Exercício 1
print(len(file_amostra.readlines()))

# Aula 1 - Exercício 2
if int(vec[2]) == 1:
    masculino = masculino + 1
elif int(vec[2]) == 2:
    feminino = feminino + 1

# Aula 1 - Exercício 3
if int(vec[11]) in faixa_salario_regiao[int(vec[1])]:
    faixa_salario_regiao[int(vec[1])][int(vec[11])] = faixa_salario_regiao[int(vec[1])][int(vec[11])] + 1
else:
    faixa_salario_regiao[int(vec[1])][int(vec[11])] = 1

# Aula 1 - Exercício 4
if int(vec[12]) in situacao:
    situacao[int(vec[12])] = situacao[int(vec[12])] + 1
else:
    situacao[int(vec[12])] = 1

# Aula 1 - Exercício 5  
for regiao in regioes:
    print(regiao, regioes[regiao])


#------------------------------------------------------------------------------------------------------------------

# Aula 2 - Exercício 1
notas = [10.6, 12.5, 13.4, 18.6, 9.8, 7.25, 17.10, 16, 48]


media = sum(notas) / len(notas)
print(media)

notas_menores = []
for nota in notas:
    if nota < media:
        notas_menores.append(nota)

print(notas_menores)

# Aula 2 - Exercício 2
notas = [10.6, 12.5, 13.4, 18.6, 9.8, 7.25, 17.10, 16, 48]

for nota in notas:
    if nota < 30:
        print("Reprovado")
    elif nota >= 60:
        print("Aprovado")
    else:
        print("Prova Final")

# mesmo exercicio usando list comprehension
notas = [10.6, 12.5, 13.4, 18.6, 9.8, 7.25, 17.10, 16, 48]
notas = ["Reprovado" if nota < 30 else "Aprovado" if nota >= 60 else "Prova Final" for nota in notas]
print(notas)

# Aula 2 - Exercício Lambda
notas = [10.6, 12.5, 13.4, 18.6, 9.8, 7.25, 17.10, 16, 48]
notas_menores = list(filter(lambda nota: nota < sum(notas) / len(notas), notas))
print(notas_menores)