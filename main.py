import csv
import os
livros = []

ARQUIVO = "livros.csv"

#Neste comando, estou pedindo para criar um arquivo "csv" caso não exista.
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Título", "Autor", "Ano", "ISBN", "Status"])

def cadastro_livro(livros):
    titulo = input('Título do livro: ')
    autor = input('Autor do livro: ')
    ano = int(input('Ano de publicação: '))
    isbn = input('Código ISBN do livro: ')
    status = 'Disponível'

    #Processo de pegar as informações e por na tabela
    livro = {
        'título': titulo ,
        'autor': autor,
        'ano': ano,
        'isbn': isbn,
        'status': status
    }
    livros.append(livro)
    return livros


def emprestimo(livros):
    isbn = input('Digite o ISBN do livro que gostaria de pegar emprestado: ')
    encontrado = False

    for livro in livros:
        if livros['isbn'] == isbn: # livro[3] é a posição do ISBN dentro da linha
            encontrado = True # marca que achamos o livro procurado

            if livro['status'] == "Disponível": # Verifica se o livro está disponível pra empréstimo
                livro['status'] = "Emprestado"
                print("Livro emprestado com sucesso!")
                return True
            else:
                print("Este livro já está emprestado.")
                return False

            # Independente de ser o livro procurado ou não,
            # adiciona a linha na lista para não perder nenhum registro
        livros.append(livro)

    if not encontrado:
        print("Livro não encontrado.")
        return False # sai da função sem reescrever o arquivo (não é necessário)

    # Reabre o arquivo, agora em modo escrita ("w"), o que apaga o conteúdo antigo
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        # Escreve todas as linhas de uma vez (cabeçalho + livros atualizados),
        # substituindo o arquivo antigo pelo novo, já com o status corrigido
        escritor.writerows(livros)


def devolver():
    isbn = input('Digite o ISBN do livro que gostaria de devolver: ')
    livros = []
    encontrado = False
    
    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        livros.append(cabecalho)
    
        for livro in leitor:
            if livro[3] == isbn:
                encontrado = True
    
                if livro[4] == "Emprestado":
                    livro[4] = "Disponível"
                    print("Livro devolvido com sucesso!")
                else:
                    print("Este livro não pode ser devolvido pois não está emprestado.")
    
            livros.append(livro)
    
    if not encontrado:
        print("Livro não encontrado.")
        return
    
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(livros)

def listar():
    #Coloca o arquivo livros.csv em modo de leitura, tranformando ele quase em uma lista
    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        print(f"{'Título':30} {'Autor':20} {'Ano':6} {'ISBN':15} {'Status'}") #Define as colunas e o tamanho delas
        print("-" * 90)

        for livro in leitor:
            print(f"{livro[0]:30} {livro[1]:20} {livro[2]:6} {livro[3]:15} {livro[4]}")#Print das informações dos livros

def buscar():
    busca = input('Digite o título ou o autor do livro que deseja pesquisar: ').strip().lower()
    encontrado = False

    with open(ARQUIVO, 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor) #Pula o cabeçalho

        for livro in leitor:
            if busca in livro[0].lower() or busca in livro[1].lower():
                encontrado = True

                print("\n===== LIVRO ENCONTRADO =====")
                print(f"Título: {livro[0]}")
                print(f"Autor: {livro[1]}")
                print(f"Ano: {livro[2]}")
                print(f"ISBN: {livro[3]}")
                print(f"Status: {livro[4]}")
                print("-" * 40)

        if not encontrado:
            print("Livro não encontrado.")


def ordenar():
    livros = []

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pula o cabeçalho

        for livro in leitor:
            livros.append(livro)

    print("\nComo deseja ordenar?")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livros.sort(key=lambda livro: livro[0].lower())

    elif opcao == "2":
        livros.sort(key=lambda livro: livro[1].lower())

    elif opcao == "3":
        livros.sort(key=lambda livro: int(livro[2]))
    else:
        print('OPÇÃO INVÁLIDA!')
        return

    for livro in livros:
        print(f"Título: {livro[0]}")
        print(f"Autor: {livro[1]}")
        print(f"Ano: {livro[2]}")
        print(f"ISBN: {livro[3]}")
        print(f"Status: {livro[4]}")
        print("-" * 40)


while True:
    print('----------|SISTEMA DE BIBLIOTECA|----------')
    print('1 - Cadastrar livro')
    print('2 - Pegar livro emprestado')
    print('3 - Devolver livro')
    print('4 - Listar livros em nossa biblioteca')
    print('5 - Buscar livros na biblioteca')
    print('6 - Ordenar livros')
    print('7 - Sair do Sistema')
    opcao = int(input('Qual a opção deseja escolher?: '))
    if opcao == 1:
        livros = cadastro_livro(livros)
    elif opcao == 2:
        emprestimo(livros)
    elif opcao == 3:
        devolver()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        buscar()
    elif opcao == 6:
        ordenar()
    elif opcao == 7:
        print('OBRIGADO POR UTILIZAR A BIBLIOTECA!')
        break
    else:
        print('OPÇÃO INVÁLIDA!')