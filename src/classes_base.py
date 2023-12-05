
class Disciplina():
    def __init__(self, codigo, nome, carga_h, nome_professor):
        self.codigo = codigo
        self.nome = nome
        self.carga_h = carga_h
        self.nome_professor = nome_professor

    def get_codigo(self):
        return self.codigo
    def set_codigo(self, new_codigo):
        self.codigo = new_codigo

    def get_nome(self):
        return self.nome
    def set_nome(self, new_nome):
        self.nome = new_nome
    
    def get_carga_h(self):
        return self.carga_h
    def set_carga_h(self, new_carga_h):
        self.carga_h = new_carga_h

    def get_nome_professor(self):
        return self.nome_professor
    def set_nome_professor(self, new_nome_professor):
        self.nome_professor = new_nome_professor


class Aluno():
    def __init__(self, cpf, nome, idade, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.endereco = endereco

    def get_nome(self):
        return self.nome
    def set_nome(self, new_nome):
        self.nome = new_nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, new_cpf):
        self.cpf = new_cpf

    def get_idade(self):
        return self.idade
    def set_idade(self, new_idade):
        self.idade = new_idade

    def get_email(self):
        return self.email
    def set_email(self, new_email):
        self.email = new_email

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, new_endereco):
        self.endereco = new_endereco



class Matricula():
    def __init__(self, cpf, codigo, data):
        self.cpf = cpf
        self.codigo = codigo
        self.data = data

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, new_cpf):
        self.cpf = new_cpf

    def get_codigo(self):
        return self.codigo
    def set_codigo(self, new_codigo):
        self.codigo = new_codigo

    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data