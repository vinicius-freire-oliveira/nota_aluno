# Crie um menu para os projetos anteriores que usaram processos de decisões
# Dicionário para armazenar os códigos e nomes dos alunos
cod_alunoD = {}

# Dicionário para armazenar as notas dos alunos
banco_notas = {}

# Lista temporária para armazenar as notas temporariamente
lista_notas = []

# Dicionário para armazenar as médias dos alunos
banco_medias = {}

# Loop principal do programa
while True:
    # Menu de opções
    print("0 - Cadastrar aluno \n1 - Mostrar cadastros \n2 - Mostrar nota")
    
    # Solicitação da escolha do usuário
    conf = int(input("Digite sua opção: "))
    
    # Opção para cadastrar um novo aluno
    if conf == 0:
        # Solicitação dos dados do aluno
        cod_aluno = input("Digite um código numérico para o aluno: ")
        nome_aluno = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite aqui a primeira nota: "))
        nota2 = float(input("Digite aqui a segunda nota: "))
        nota3 = float(input("Digite aqui a terceira nota: "))
        
        # Cálculo da média do aluno
        media = (nota1 + nota2 + nota3) / 3
        
        # Adiciona as notas à lista temporária
        lista_notas.append(nota1)
        lista_notas.append(nota2)
        lista_notas.append(nota3)
        
        # Armazena o código e o nome do aluno no dicionário
        cod_alunoD[cod_aluno] = nome_aluno
        
        # Armazena as notas do aluno no dicionário de notas
        banco_notas[cod_aluno] = lista_notas
        
        # Armazena a média do aluno no dicionário de médias
        banco_medias[cod_aluno] = media
        
        # Limpa a lista de notas para o próximo aluno
        lista_notas = []
        
        # Informa ao usuário que o aluno foi cadastrado
        print(f"O aluno cadastrado foi {nome_aluno} e suas notas estão no sistema")
    
    # Opção para mostrar a lista de alunos cadastrados
    elif conf == 1:
        print("Lista de alunos cadastrados: ")
        print("------------------------------")
        print(cod_alunoD)
    
    # Opção para mostrar as notas e média de um aluno específico
    elif conf == 2:
        Cod_Aluno = input("Digite o código de cadastro do aluno: ")
        # Obtém o nome do aluno correspondente ao código do aluno fornecido
        nome_aluno = cod_alunoD.get(Cod_Aluno)

        # Obtém as notas do aluno correspondente ao código do aluno fornecido
        notas = banco_notas.get(Cod_Aluno)

        # Obtém a média do aluno correspondente ao código do aluno fornecido
        media = banco_medias.get(Cod_Aluno)

        print("As notas do aluno {} são: {}".format(nome_aluno, notas))
        print("E sua média é: {}".format(media))
    
    # Solicitação para continuar ou sair do programa
    print("")
    print("===========") 
    print("0 para continuar | 1 para sair ")
    if int(input()) == 1:
        break  # Sai do loop principal e encerra o programa