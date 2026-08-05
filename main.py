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
    livros = []
    encontrado = False

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        livros.append(cabecalho)

        for livro in leitor:
            if livro[3] == isbn:
                encontrado = True

                if livro[4] == "Disponível":
                    livro[4] = "Emprestado"
                    print("Livro emprestado com sucesso!")
                else:
                    print("Este livro já está emprestado.")

            livros.append(livro)

    if not encontrado:
        print("Livro não encontrado.")
        return

    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
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