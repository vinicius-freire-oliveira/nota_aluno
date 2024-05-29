# Inicializa a variável soma_notas para armazenar a soma das notas
listas_notas = []
nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))

listas_notas.append(nota1)
listas_notas.append(nota2)
listas_notas.append(nota3)

# Calcula a média utilizando a lista
soma_notas = sum(listas_notas)
media = soma_notas / len(listas_notas)

print("A média do aluno é:", media)

if media >= 7:
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")