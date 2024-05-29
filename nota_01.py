# sistema em que o usuário armazena 3 notas 
# de um aluno e no final é mostrado qual é a média que esse 
# aluno teve e se ele alcançar a média 7 está aprovado caso 
# o contrário está reprovado, utilizando dicionários:
cod_alunoD = {}
banco_notas = {}
lista_notas = []

cod_aluno = input("Digite um código numérico para um aluno: ")
nome_aluno = input("Digite o nome do aluno:")
nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))

lista_notas.append(nota1)
lista_notas.append(nota2)
lista_notas.append(nota3)

cod_alunoD[cod_aluno] = nome_aluno
banco_notas[cod_aluno] = lista_notas

print("O aluno cadastrado foi {} e as suas notas estão no sistema".format(nome_aluno))

media = banco_notas.get(cod_aluno)
media = sum(media)
media = media / 3

print(f"A média do aluno {nome_aluno} é: {media}")

if(media >= 7):
    print("O aluno", nome_aluno, "está aprovado!")
else:
    print("O aluno {} está reprovado".format(nome_aluno))