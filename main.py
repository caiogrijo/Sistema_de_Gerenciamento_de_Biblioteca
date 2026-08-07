import csv
import os

ARQUIVO = "livros.csv"

#Neste comando, estou pedindo para criar um arquivo "csv" caso não exista.
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Título", "Autor", "Ano", "ISBN", "Status"])


def carregar_livros():
    livros = []

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            livro = {
                "título": linha[0],
                "autor": linha[1],
                "ano": int(linha[2]),
                "isbn": linha[3],
                "status": linha[4]
            }

            livros.append(livro)

    return livros


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


def salvar_livros(livros):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Título", "Autor", "Ano", "ISBN", "Status"])

        for livro in livros:
            escritor.writerow([
                livro["título"],
                livro["autor"],
                livro["ano"],
                livro["isbn"],
                livro["status"]
            ])

    return True


def emprestimo(livros):
    isbn = input('Digite o ISBN do livro que gostaria de pegar emprestado: ')
    encontrado = False

    for livro in livros:
        if livro['isbn'] == isbn: # livro[3] é a posição do ISBN dentro da linha
            encontrado = True # marca que achamos o livro procurado

            if livro['status'] == "Disponível": # Verifica se o livro está disponível pra empréstimo
                livro['status'] = "Emprestado"
                print("Livro emprestado com sucesso!")
                return True
            else:
                print("Este livro já está emprestado.")
                return False

    if not encontrado:
        print("Livro não encontrado.")
        return False # sai da função sem reescrever o arquivo (não é necessário)
    

def devolver(livros):
    isbn = input('Digite o ISBN do livro que gostaria de devolver: ')
    encontrado = False
    
    for livro in livros:
        if livro['isbn'] == isbn:
            encontrado = True
    
            if livro['status'] == "Emprestado":
                livro['status'] = "Disponível"
                print("Livro devolvido com sucesso!")
                return True
            else:
                print("Este livro não pode ser devolvido pois não está emprestado.")
                return False
    
    if not encontrado:
        print("Livro não encontrado.")
        return False

def listar(livros):
    print(f"{'Título':30} {'Autor':20} {'Ano':6} {'ISBN':15} {'Status'}")
    print("-" * 90)

    for livro in livros:
        print(f"{livro['título']:30} {livro['autor']:20} {livro['ano']:6} {livro['isbn']:15} {livro['status']}")
    return True

def buscar(livros):
    busca = input('Digite o título ou o autor do livro que deseja pesquisar: ').strip().lower()
    encontrado = False

    for livro in livros:
        if busca in livro['título'].lower() or busca in livro['autor'].lower():
            encontrado = True

            print("\n===== LIVRO ENCONTRADO =====")
            print(f"Título: {livro['título']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Status: {livro['status']}")
            print("-" * 40)

    if encontrado:
        return True
    else:
        print("Livro não encontrado.")
        return False


def ordenar(livros):
    print("\nComo deseja ordenar?")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livros.sort(key=lambda livro: livro["título"].lower())

    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())

    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])

    else:
        print("OPÇÃO INVÁLIDA!")
        return False

    for livro in livros:
        print(f"Título: {livro['título']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("-" * 40)

    return True

livros = carregar_livros()

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
        salvar_livros(livros)
    elif opcao == 2:
        if emprestimo(livros):
            salvar_livros(livros)
    elif opcao == 3:
        if devolver(livros):
            salvar_livros(livros)
    elif opcao == 4:
        listar(livros)
    elif opcao == 5:
        buscar(livros)
    elif opcao == 6:
        ordenar(livros)
    elif opcao == 7:
        print('OBRIGADO POR UTILIZAR A BIBLIOTECA!')
        break
    else:
        print('OPÇÃO INVÁLIDA!')