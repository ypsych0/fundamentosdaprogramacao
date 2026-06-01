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

—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# PROGRAMMING FUNDAMENTALS NOTES

## Data Types in Python
1. string
2. number int
3. number float
4. boolean

## Basic Mathematical Operators
+ -> addition
- -> subtraction
* -> multiplication
/ -> division

## Logical Operators
and -> If two conditions are true, the result is true.
or -> If at least one condition is true, the result is true.
not -> It changes the boolean value of the condition.

## Methods in Python
1. print() -> Displays information in the terminal.
2. input() -> Captures input from the terminal.
3. lower() -> Converts the entire string to lowercase.
4. upper() -> Converts the entire string to uppercase.
5. isdigit() -> Checks if the value contains a number.

## Format in Python

# Conditional Structure
1. `if` -> Checks if a condition is (true). If it is, it executes the code.
2. `elif (else if)` -> Used to test multiple conditions; it only executes if all previous conditions are false.
3. `else` -> Executes the code if the if condition is false.

## Type Conversion in Python
1. int() -> We specify which variable/data we want to convert to an integer.
2. float() -> We specify which variable/data we want to convert to a decimal number.
3. str() -> We specify which variable/data we want to convert to a string.

# Loops
A programming resource that allows executing a set of commands multiple times. Also called loops or iterations.
`FOR` -> Used when we know how many times we want to repeat something.
Syntax:
FOR variable in range(start, end):
    `commands`
[range()] -> Method that accepts number generation.
[start] -> Inclusive. It is the first number to be used.
[end] -> Exclusive. The number used is the one before this.

## Variable Scope
Local Scope -> The variable can only be accessed inside the structure where it was created.
Global Scope -> The variable can be accessed by everyone.

## Variable Variations
In-memory variable -> Declared when you do not intend to use that variable in other scenarios.
Counter variable -> Used for logic where the repetition will be incremented/changed.

`WHILE` -> Used when we do not know how many times the program will repeat. It repeats while a condition is true.
Syntax:
while condition:
    `commands`

## Best Practices
1. Any variable in Python uses the snake_case naming convention, or more recently camelCase.
2. If you see a structure like name(), there is a 90% chance it is a function.
3. Python does not have constants; however, we use the UPPERCASE convention to simulate that a variable cannot be changed.

## Functions in Python
`def` -> Defines that a function will be declared.
`parameter` -> An in-memory variable that will receive an argument.
`argument` -> The value that will fill the parameter's slot.

## Data Structures
`list` -> Stores individual values and can be heterogeneous or homogeneous. That is, it can hold values of the same type or different types.
Ex: list = []  # Empty list
list = ["Pedro", 20, 1.75]

`dict (dictionary)` -> Stores sets of values (key:value). Keys and values can be heterogeneous or homogeneous.
1. To get the value of an entry in a dict, you access it by its key.
Ex: user_data = {}  # Empty dictionary
user_data = {"name": "Pedro", "cpf": "121009774-34", "age": 20}
user_data["name"]  # Returns the value, which is "Pedro".
