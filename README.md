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

## Métodos em python
1. print() -> Exibe informações no terminal.

## Format em python

# Estrutura de condicional
1. ``if (se)`` -> Verifica se uma condição é (verdadeira). Se for, ele executa o código.
2. ``elif (senão se)`` -> é usado para testar várias condições ele só executa se todas as condições anteriores forem falsas.
3. ``else (senão)`` -> Executa o código se a condição if for false (falsa).

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