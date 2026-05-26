# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## Tipos de dados em python
1. string
2. number int
3. number float
4. boolean

## Operadores matemáticos - básicos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão

## Operadores lógicos
and -> e -> Se duas condições forem verdadeiras, o resultado é verdadeiro.
or -> ou -> Ser pelo menos uma condição for verdadeira, o resultado é verdadeiro.
not -> Ele altera o valor booleano da condição.

## Métodos em python
1. print() -> Exibe informações no terminal.
2. input() -> Capturar uma informação no terminal.
3. lower() -> Converte toda a string em minúscula.
4. upper() -> Converte toda a string em maiúscula.
5. isdigit() -> Verifica se o valor contém número.

## Format em python

# Estrutura de condicional
1. ``if (se)`` -> Verifica se uma condição é (verdadeira). Se for, ele executa o código.
2. ``elif (senão se)`` -> é usado para testar várias condições ele só executa se todas as condições anteriores forem falsas.
3. ``else (senão)`` -> Executa o código se a condição if for false (falsa).

 ## Conversão de tipos em Python
 1. int() -> Vamos incluir qual variável/dado que queremos converter para número inteiro.
 2. float() -> Vamos incluir qual variável/dado que queremos converter para número decimal.
 3. str() -> Vamos incluir qual variável/dado que queremos converter para texto.

# Laços de repetição
É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop, laços de repetição ou iteração.
`FOR` -> Utilizamos quando sabemos quantas vezes queremos repetir algo.
Sintax:
FOR variavel in rage(inicio,fim):
    ``comandos``
[range()] -> Método que aceita geração de números
[inicio] -> É inclusivo. É o primeiro número a ser usado. 
[fim] -> É exclusivo. O número utilizado é o anterior a esse.

## Escopo das Variáveis
Escopo Local -> A variável ela só é acessadaa dentro da estrutura que ela foi criada.
Escopo Global -> A variável pode ser acessada por todo mundo.

## Variações de variáveis
Variável em memória -> É declarada quando você não pretende utilizadr essa variável em outros cénarios.
Variável contadora -> É utilizada para uma lógica onde a repetição irá ser alterada.

``WHILE`` -> É utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
Sintax:
while condicao:
    ``Comandos``
## Boas Prátricas
1. Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o cammelCase.
2. Se você observar alguma estrutura tipo nome(), 90% de chance de ser uma função.
3. Python não tem constante porém, utilizamos o padrão case UPPERCASE,para simular que aquela variável não pode ser alterada.

## Funções em Python
`def` -> Difine que uma função será declarada;
`propriedade` -> Variável em memória que irá receber um argumento.
`argumento` -> Valor que irá preencher o espaço da propriedade.

## Estruturas de Dados
``lsit ou lista` -> Armazena valores avulsos e podem ser heterogenia ou homogenia. Ou seja, pode guardar valores de um mesmo tipo ou de diferentes tipo.
Ex: lsit = [] //Lista vazia
list = ["Pedro", 20, 1.75]

`dict ou dicionário` -> Armazena conjuntos de valores (chave:valor). As chaves e valores podem ser heterogenia ou homogenia.
1. Para obter o valor de um conjunto em dict, você acessa pela chave.
Ex: dados_usuario = {} // Dicionário Vazio
dados_usuario = {"nome": "Pedro", "cpf": 121009774-34, "idade": 20}
dados_usuario["nome"] => Devolve o valor, que é "Pedro".