import csv
import os

ARQUIVO = "livros.csv"

# Neste comando, estou pedindo para criar um arquivo "csv" caso não exista.
# Isso evita erro na primeira vez que o programa roda, quando o arquivo
# livros.csv ainda não existe no computador.
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        # Escreve a primeira linha do CSV com o nome de cada coluna
        escritor.writerow(["Título", "Autor", "Ano", "ISBN", "Status"])


def carregar_livros():
    """
    Lê o arquivo CSV do início ao fim e transforma cada linha em um
    dicionário, guardando tudo numa lista. Essa lista é a 'biblioteca'
    que vai ficar em memória durante toda a execução do programa.

    Parâmetro: nenhum
    Retorno: list -> lista de dicionários (cada dicionário é um livro)
    """
    livros = []

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        # Pula a primeira linha do arquivo, que é o cabeçalho
        # (Título, Autor, Ano, ISBN, Status) e não é um livro de verdade
        next(leitor)

        # Cada 'linha' aqui é uma lista, por exemplo:
        # ['Dom Casmurro', 'Machado de Assis', '1899', '123', 'Disponível']
        for linha in leitor:
            # Transformo a linha (lista) em um dicionário com nomes de
            # chave, pra facilitar o acesso depois (livro["isbn"] em vez
            # de precisar lembrar que o ISBN é a posição 3)
            livro = {
                "título": linha[0],
                "autor": linha[1],
                "ano": int(linha[2]),  # convertido pra int pra poder ordenar por ano depois
                "isbn": linha[3],
                "status": linha[4]
            }

            livros.append(livro)

    return livros


def cadastro_livro(livros):
    """
    Pede os dados de um novo livro ao usuário e adiciona ele na lista
    'livros' recebida por parâmetro.

    Parâmetro: livros (list) -> a lista de livros já existente
    Retorno: list -> a mesma lista, já com o novo livro adicionado
    """
    titulo = input('Título do livro: ')
    autor = input('Autor do livro: ')
    ano = int(input('Ano de publicação: '))
    isbn = input('Código ISBN do livro: ')
    status = 'Disponível'  # todo livro novo começa como disponível

    # Processo de pegar as informações e por na tabela
    livro = {
        'título': titulo,
        'autor': autor,
        'ano': ano,
        'isbn': isbn,
        'status': status
    }

    # .append() adiciona o dicionário 'livro' no final da lista 'livros'.
    # Como listas são mutáveis, isso já altera a lista original que foi
    # passada por parâmetro (o return abaixo é mais uma formalidade).
    livros.append(livro)
    return livros


def salvar_livros(livros):
    """
    Recebe a lista de livros (em memória) e reescreve o arquivo CSV do
    zero com os dados atualizados. É chamada sempre que algo muda
    (cadastro, empréstimo, devolução).

    Parâmetro: livros (list)
    Retorno: bool -> True, indicando que o arquivo foi salvo com sucesso
    """
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        # Reescreve o cabeçalho, já que o modo "w" apaga o conteúdo
        # anterior do arquivo inteiro
        escritor.writerow(["Título", "Autor", "Ano", "ISBN", "Status"])

        # Percorre cada dicionário da lista e escreve uma linha no CSV
        # correspondente a ele, na mesma ordem das colunas do cabeçalho
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
    """
    Procura um livro pelo ISBN e, se ele estiver disponível, muda o
    status dele para 'Emprestado'.

    Parâmetro: livros (list)
    Retorno: bool -> True se o empréstimo foi feito com sucesso,
             False se o livro não existe ou já está emprestado
    """
    isbn = input('Digite o ISBN do livro que gostaria de pegar emprestado: ')
    encontrado = False

    for livro in livros:
        if livro['isbn'] == isbn:  # livro[3] é a posição do ISBN dentro da linha
            encontrado = True  # marca que achamos o livro procurado

            if livro['status'] == "Disponível":  # Verifica se o livro está disponível pra empréstimo
                livro['status'] = "Emprestado"
                print("Livro emprestado com sucesso!")
                return True  # sai da função aqui, já que o objetivo foi cumprido
            else:
                print("Este livro já está emprestado.")
                return False  # livro existe, mas não pôde ser emprestado

    if not encontrado:
        print("Livro não encontrado.")
        return False  # sai da função sem reescrever o arquivo (não é necessário)


def devolver(livros):
    """
    Procura um livro pelo ISBN e, se ele estiver emprestado, muda o
    status dele de volta para 'Disponível'.

    Parâmetro: livros (list)
    Retorno: bool -> True se a devolução foi feita com sucesso,
             False se o livro não existe ou já estava disponível
    """
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
    """
    Imprime todos os livros da lista em formato de tabela, alinhando
    as colunas por largura fixa.

    Parâmetro: livros (list)
    Retorno: bool -> True, indicando que a listagem foi exibida
    """
    # Define o cabeçalho da tabela e o tamanho (em caracteres) de cada coluna
    print(f"{'Título':30} {'Autor':20} {'Ano':6} {'ISBN':15} {'Status'}")
    print("-" * 90)

    # Print das informações de cada livro, respeitando o mesmo alinhamento do cabeçalho
    for livro in livros:
        print(f"{livro['título']:30} {livro['autor']:20} {livro['ano']:6} {livro['isbn']:15} {livro['status']}")
    return True


def buscar(livros):
    """
    Pede um termo de busca ao usuário e procura livros cujo título ou
    autor contenham esse termo (não precisa ser igual, só conter).

    Parâmetro: livros (list)
    Retorno: bool -> True se encontrou ao menos um livro, False caso contrário
    """
    # .strip() remove espaços em branco extras no início/fim
    # .lower() deixa tudo minúsculo, pra busca não diferenciar maiúscula de minúscula
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
    """
    Pergunta ao usuário o critério de ordenação (título, autor ou ano)
    e ordena a lista de livros de acordo com a escolha.

    Parâmetro: livros (list)
    Retorno: bool -> True se ordenou e exibiu a lista com sucesso,
             False se a opção escolhida foi inválida
    """
    print("\nComo deseja ordenar?")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Escolha uma opção: ")

    # livros.sort() ordena a lista original 'no lugar' (não cria uma
    # lista nova), usando como critério o valor retornado pela lambda
    # pra cada livro da lista
    if opcao == "1":
        livros.sort(key=lambda livro: livro["título"].lower())

    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())

    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])

    else:
        print("OPÇÃO INVÁLIDA!")
        return False

    # Depois de ordenada, percorre a lista e imprime cada livro
    for livro in livros:
        print(f"Título: {livro['título']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("-" * 40)

    return True


# Carrega a biblioteca do arquivo UMA ÚNICA VEZ, logo no início do
# programa. A partir daqui, 'livros' é a lista que vive em memória
# enquanto o programa estiver rodando.
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
        salvar_livros(livros)  # sempre salva após cadastrar, já que um livro novo foi adicionado

    elif opcao == 2:
        # Só salva o arquivo se emprestimo() retornar True, ou seja,
        # se o empréstimo realmente aconteceu (evita gravação desnecessária)
        if emprestimo(livros):
            salvar_livros(livros)

    elif opcao == 3:
        # Mesma lógica do empréstimo: só salva se a devolução deu certo
        if devolver(livros):
            salvar_livros(livros)

    elif opcao == 4:
        listar(livros)  # só exibe os dados, não precisa salvar nada

    elif opcao == 5:
        buscar(livros)  # só exibe os dados, não precisa salvar nada

    elif opcao == 6:
        ordenar(livros)  # reordena a lista em memória e exibe (não é salva no arquivo)

    elif opcao == 7:
        print('OBRIGADO POR UTILIZAR A BIBLIOTECA!')
        break  # encerra o loop 'while True' e finaliza o programa

    else:
        print('OPÇÃO INVÁLIDA!')