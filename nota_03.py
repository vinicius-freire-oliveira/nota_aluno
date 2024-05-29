# Inicializa a variável soma_notas para armazenar a soma das notas
soma_notas = 0
# Define a quantidade de notas a serem inseridas
quantidade_notas = 3

# Loop para solicitar as notas ao usuário
for i in range(quantidade_notas):
    # Solicita a nota ao usuário e converte para float
    nota = float(input("Digite a {}ª nota: ".format(i + 1)))
    # Adiciona a nota à soma das notas
    soma_notas += nota
    
# Calcula a média das notas
media = soma_notas / quantidade_notas

# Imprime a média
print("A média do aluno é:", media)

# Verifica se o aluno está aprovado ou reprovado e imprime o resultado
if media >= 7:
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")