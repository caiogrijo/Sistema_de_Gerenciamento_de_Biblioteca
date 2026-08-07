# Sistema de Gerenciamento de Biblioteca

## Descrição

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python. 
O programa permite cadastrar livros e controlar seus empréstimos e devoluções, 
além de pesquisar, listar e ordenar os livros cadastrados.

## Como executar o programa

1. Tenha o Python instalado no computador.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no Visual Studio Code ou outro editor.
4. Execute o arquivo principal do programa pelo Python.

O programa utiliza apenas bibliotecas padrão do Python, portanto não é necessário instalar pacotes externos.

## Principais funcionalidades
- Cadastrar livros com:
  - Título
  - Autor
  - Ano de publicação
  - ISBN
  - Status
- Registrar empréstimos de livros.
- Registrar devoluções de livros.
- Listar todos os livros cadastrados.
- Buscar livros pelo título ou autor.
- Ordenar os livros por título, autor ou ano.
- Salvar os livros em um arquivo CSV.
- Carregar os livros do arquivo CSV ao iniciar o programa.

## Requisitos técnicos aplicados

- **Menu principal:** feito com `if/elif/else`, contendo as opções de cadastrar, emprestar, devolver, listar, buscar, ordenar e sair.
- **Estrutura de repetição:** utilização de `while` para manter o menu funcionando até o usuário escolher sair.
- **Funções próprias:** o programa possui funções para cadastrar, emprestar, devolver, listar, buscar, ordenar, carregar e salvar livros.
- **Parâmetros e retornos:** as funções recebem parâmetros quando necessário e utilizam `return` para retornar informações.
- **Lista de dicionários:** os livros são armazenados em uma lista, sendo cada livro representado por um dicionário com título, autor, ano, ISBN e status.
- **Persistência de dados:** os livros são salvos no arquivo `livros.csv` e carregados novamente quando o programa é iniciado.
- **Bibliotecas padrão:** foram utilizadas somente bibliotecas que já fazem parte do Python, como `csv` e `os`.