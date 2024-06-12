# Itera três vezes para coletar as notas e calcular a média de cada conjunto de notas
for contador in range(1, 4):
    # Solicita a primeira nota ao usuário
    nota_1 = float(input('Digite a 1° nota: '))
    # Solicita a segunda nota ao usuário
    nota_2 = float(input('Digite a 2° nota: '))

    # Calcula e imprime a média das duas notas
    print(f'Média: {(nota_1 + nota_2) / 2}')
