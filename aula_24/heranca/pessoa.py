# Precisamos crirar um molde de uma pessoa.
# Características -> atributos -> variáveis
# Ações -> métodos -> funções

class Pessoa:
    # Constructor
    def __init__(self, nome: str, cpf: str, data_nasc: str):
        self.nome = nome # Atributo público
        self._cpf = cpf # Atributo privado
        self.data_nasc = data_nasc # Atributo público

    # Método de apresentação
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}"


pessoa1 = Pessoa("João", "123.456.789-00")
pessoa2 = Pessoa("Maria", "987.654.321-00")

print(pessoa1.apresentar())
print(pessoa2.apresentar())