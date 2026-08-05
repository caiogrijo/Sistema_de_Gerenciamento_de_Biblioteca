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
