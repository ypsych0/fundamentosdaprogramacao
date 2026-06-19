from pessoa import Pessoa
# NOME, CPF, DATA DE NASCIMENTO, ANO DE INGRESSO, NOTAS, MATRICULA E SE ESTAR ATIVO OU NÃO
class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nasc: str, ano_ingresso: int, matricula: str, ativo: bool):
        super().__init__(nome, cpf, data_nasc)
        self.ano_ingresso = ano_ingresso
        self.matricula = matricula
        self.ativo = True
        self.notas = []