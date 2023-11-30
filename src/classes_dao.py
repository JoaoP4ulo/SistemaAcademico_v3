from src import utils
import sqlite3
from src.classes_base import Disciplina, Aluno
import csv
import json

class DisciplinaDAO():
    def __init__(self,db_path):
        self.db_path = db_path

    def buscar_disciplina(self, codigo):
        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Disciplina WHERE codigo = ?
        """
        
        cursor.execute(comando_sql, (codigo, ))

        disciplina_tupla = cursor.fetchone()

        conexao.close()

        if disciplina_tupla is None:
            return None
        
        disciplina = Disciplina(codigo=disciplina_tupla[0], nome=disciplina_tupla[1], \
            carga_h=disciplina_tupla[2], nome_professor=disciplina_tupla[3])


        return disciplina
    
    def cadastrar_disciplina(self, disciplina):
            
        conexao = sqlite3.Connection(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        INSERT INTO Disciplina (codigo,nome,carga_h,nome_professor) 
        VALUES (?, ?, ?, ?)
        """
        
        cursor.execute(comando_sql, \
            (disciplina.codigo, disciplina.nome, disciplina.carga_h, disciplina.nome_professor))

        conexao.commit()

        conexao.close()

    def atualizar_nome(self, disciplina, new):
        conexao = sqlite3.Connection(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        UPDATE Disciplina SET nome = ? WHERE codigo = ?
        """
        
        cursor.execute(comando_sql, (new, disciplina.codigo))

        conexao.commit()
        print("Nome da disciplina atualizado!")
        conexao.close()

    def atualizar_carga_h(self, disciplina, new):
        conexao = sqlite3.Connection(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        UPDATE Disciplina SET carga_h = ? WHERE codigo = ?
        """
        
        cursor.execute(comando_sql, (new, disciplina.codigo))

        conexao.commit()
        print("Carga horária da disciplina atualizada!")
        conexao.close()

    def atualizar_nome_professor(self, disciplina, new):
        conexao = sqlite3.Connection(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        UPDATE Disciplina SET nome_professor = ? WHERE codigo = ?
        """
        
        cursor.execute(comando_sql, (new, disciplina.codigo))

        conexao.commit()
        print("Nome do professor responsável atualizado!")
        conexao.close()

    def excluir_disciplina(self, disciplina_existente):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql_nome = """
            DELETE FROM Disciplina WHERE codigo = ?
            """
        
        cursor.execute(comando_sql_nome, (disciplina_existente.codigo,))

        conexao.commit()

        conexao.close()

    

    def listar_disciplinas(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Disciplina
        """

        cursor.execute(comando_sql)
        disciplinas = cursor.fetchall()

        conexao.close()

        if not disciplinas:
            print("Não há disciplinas cadastradas.")
        else:
            print("\nLista de Disciplinas:")
            print("Total de disciplinas cadastradas:", len(disciplinas))

            for disciplina in disciplinas:
                codigo, nome, carga_h, nome_professor = disciplina
                print("\nCódigo:", codigo)
                print("Nome:", nome)
                print("Carga Horária:", carga_h)
                print("Professor Responsável:", nome_professor)

            exportar_csv = input("\nDeseja exportar os dados para um arquivo CSV? (S/N): ").lower()

            if exportar_csv == 's':
                self.exportar_para_csv(disciplinas)

            

    def exportar_para_csv(self, disciplinas):
        nome_arquivo = input("Digite o nome do arquivo CSV (ou pressione Enter para o padrão 'disciplinas.csv'): ").strip()

        if not nome_arquivo:
            nome_arquivo = 'disciplinas.csv'

        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')
            # Escreve o cabeçalho
            escritor_csv.writerow(['Código', 'Nome', 'Carga Horária', 'Professor Responsável'])
            # Escreve os dados das disciplinas
            escritor_csv.writerows(disciplinas)

        print(f"Dados exportados para o arquivo CSV: {nome_arquivo}")





class AlunoDAO():
    def __init__(self,db_path):
        self.db_path = db_path

    def buscar_aluno(self, cpf):
        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Aluno WHERE cpf = ?
        """
        
        cursor.execute(comando_sql, (cpf, ))

        aluno_tupla = cursor.fetchone()

        conexao.close()

        if aluno_tupla is None:
            return None
        
        aluno = Aluno(cpf=aluno_tupla[0], nome=aluno_tupla[1], \
            idade=aluno_tupla[2], email=aluno_tupla[3], endereco=aluno_tupla[4])


        return aluno
    
    def cadastrar_aluno(self, aluno):
            
        conexao = sqlite3.Connection(self.db_path)

        cursor = conexao.cursor()

        lista_serializada = json.dumps(aluno.endereco)

        comando_sql = """
        INSERT INTO Aluno (cpf, nome, idade, email, endereco) 
        VALUES (?, ?, ?, ?, ?)
        """
        
        cursor.execute(comando_sql, \
            (aluno.cpf, aluno.nome, aluno.idade, aluno.email, lista_serializada))

        conexao.commit()

        conexao.close()

    def excluir_disciplina(self, disciplina_existente):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql_nome = """
            DELETE FROM Disciplina WHERE codigo = ?
            """
        
        cursor.execute(comando_sql_nome, (disciplina_existente.codigo,))

        conexao.commit()

        conexao.close()

    

    def listar_disciplinas(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Disciplina
        """

        cursor.execute(comando_sql)
        disciplinas = cursor.fetchall()

        conexao.close()

        if not disciplinas:
            print("Não há disciplinas cadastradas.")
        else:
            print("\nLista de Disciplinas:")
            print("Total de disciplinas cadastradas:", len(disciplinas))

            for disciplina in disciplinas:
                codigo, nome, carga_h, nome_professor = disciplina
                print("\nCódigo:", codigo)
                print("Nome:", nome)
                print("Carga Horária:", carga_h)
                print("Professor Responsável:", nome_professor)

            exportar_csv = input("\nDeseja exportar os dados para um arquivo CSV? (S/N): ").lower()

            if exportar_csv == 's':
                self.exportar_para_csv(disciplinas)

    def exportar_para_csv(self, disciplinas):
        nome_arquivo = input("Digite o nome do arquivo CSV (ou pressione Enter para o padrão 'disciplinas.csv'): ").strip()

        if not nome_arquivo:
            nome_arquivo = 'disciplinas.csv'

        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')
            # Escreve o cabeçalho
            escritor_csv.writerow(['Código', 'Nome', 'Carga Horária', 'Professor Responsável'])
            # Escreve os dados das disciplinas
            escritor_csv.writerows(disciplinas)

        print(f"Dados exportados para o arquivo CSV: {nome_arquivo}")
