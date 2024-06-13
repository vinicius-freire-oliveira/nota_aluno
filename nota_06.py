# declarando a lista de notas
notas = []
# laço for para pedir as 5 notas e armazená-las na lista notas
for i in range(1,6):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

# Função para remover a maior e menor nota e retornar a média das notas restantes
def media(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  return sum(lista) / len(lista)

# Chamando a função e imprimindo a média
media = media(notas)
print(f"A média foi: {round(media, 1)}") 
