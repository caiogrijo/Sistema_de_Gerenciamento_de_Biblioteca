import csv
import os

ARQUIVO = "livros.csv"

#Neste comando, estou pedindo para criar um arquivo "csv" caso não exista.
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Título", "Autor", "Ano", "ISBN", "Status"])

def cadastro_livro():
    titulo = input('Título do livro: ')
    autor = input('Autor do livro: ')
    ano = int(input('Ano de publicação: '))
    isbn = input('Código ISBN do livro: ')
    status = 'Disponível'

    #Processo de pegar as informações e por na tabela
    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([titulo, autor, ano, isbn, status])
        print('Livro cadastrado com sucesso!')


def emprestimo():
    isbn = input('Digite o ISBN do livro que gostaria de pegar emprestado: ')
    livros = [] # Lista que vai guardar TODOS os livros (incluindo o cabeçalho)
    encontrado = False

    # Abre o arquivo em modo leitura ("r") para ler os dados atuais
    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor) # Lê a primeira linha do CSV (o cabeçalho: Título, Autor, Ano, ISBN, Status)
        livros.append(cabecalho) # Adiciona o cabeçalho na lista, pois ele também precisa ser gravado para não perdermos os nomes das colunas

        for livro in leitor:
            if livro[3] == isbn: # livro[3] é a posição do ISBN dentro da linha
                encontrado = True # marca que achamos o livro procurado

                if livro[4] == "Disponível": # Verifica se o livro está disponível pra empréstimo
                    livro[4] = "Emprestado"
                    print("Livro emprestado com sucesso!")
                else:
                    print("Este livro já está emprestado.")

            # Independente de ser o livro procurado ou não,
            # adiciona a linha na lista para não perder nenhum registro
            livros.append(livro)

    if not encontrado:
        print("Livro não encontrado.")
        return  # sai da função sem reescrever o arquivo (não é necessário)

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

    def titulo(livro):
        return livro[0].lower
    def autor(livro):
        return livro[1].lower
    def ano(livro):
        return int(livro[2])

    print("\nComo deseja ordenar?")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livros.sort(key=titulo)

    elif opcao == "2":
        livros.sort(key=autor)

    elif opcao == "3":
        livros.sort(key=ano)

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
        cadastro_livro()
    elif opcao == 2:
        emprestimo()
    elif opcao == 3:
        devolver()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        buscar()
    elif opcao == 6:
        ordenar()
    elif opcao == 7:
        sair()
    else:
        print('OPÇÃO INVÁLIDA!')
