from src import utils
import sqlite3
from src.classes_base import Disciplina, Aluno, Matricula
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

    def atualizar_disciplina(self, disciplina_existente, new_nome=None, new_carga_h=None, new_nome_professor=None):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        # Construir a parte da query que será dinâmica com base nos parâmetros fornecidos
        query_partes = []
        valores = []

        if new_nome is not None:
            query_partes.append("nome = ?")
            valores.append(new_nome)

        if new_carga_h is not None:
            query_partes.append("carga_h = ?")
            valores.append(new_carga_h)

        if new_nome_professor is not None:
            query_partes.append("nome_professor = ?")
            valores.append(new_nome_professor)

        # Montar a query final
        query_final = f"UPDATE Disciplina SET {', '.join(query_partes)} WHERE codigo = ?"
        valores.append(disciplina_existente.codigo)

        # Executar a query
        cursor.execute(query_final, valores)

        conexao.commit()
        print("Dados da disciplina atualizados!")
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

    def atualizar_aluno(self, aluno_existente):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        UPDATE Aluno SET nome = ?, idade = ?, email = ?, endereco = ? WHERE cpf = ?
        """
        
        lista_serializada = json.dumps(aluno_existente.endereco)

        cursor.execute(comando_sql, (aluno_existente.nome, aluno_existente.idade,
                                     aluno_existente.email, lista_serializada, aluno_existente.cpf))

        conexao.commit()
        print("Dados do aluno atualizados!")
        conexao.close()

    def excluir_aluno(self, aluno_existente):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql_cpf = """
            DELETE FROM Aluno WHERE cpf = ?
        """
        
        cursor.execute(comando_sql_cpf, (aluno_existente.cpf,))

        conexao.commit()
        print("Aluno excluído com sucesso!")

        conexao.close()

    def listar_alunos(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Aluno
        """

        cursor.execute(comando_sql)
        alunos = cursor.fetchall()

        conexao.close()

        if not alunos:
            print("Não há alunos cadastrados.")
        else:
            print("\nLista de Alunos:")
            print("Total de alunos cadastrados:", len(alunos))

            for aluno in alunos:
                cpf, nome, idade, email, endereco_serializado = aluno
                endereco = json.loads(endereco_serializado)
                print("\nCPF:", cpf)
                print("Nome:", nome)
                print("Idade:", idade)
                print("Email:", email)
                print("Endereço:", endereco)

            exportar_csv = input("\nDeseja exportar os dados para um arquivo CSV? (S/N): ").lower()

            if exportar_csv == 's':
                self.exportar_para_csv(alunos)


    def exportar_para_csv(self, alunos):
        nome_arquivo = input("Digite o nome do arquivo CSV (ou pressione Enter para o padrão 'alunos.csv'): ").strip()

        if not nome_arquivo:
            nome_arquivo = 'alunos.csv'

        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')
            # Escreve o cabeçalho
            escritor_csv.writerow(['CPF', 'Nome', 'Idade', 'Email', 'Endereço'])
            # Escreve os dados dos alunos
            for aluno in alunos:
                cpf, nome, idade, email, endereco_serializado = aluno
                endereco = json.loads(endereco_serializado)
                escritor_csv.writerow([cpf, nome, idade, email, endereco])

        print(f"Dados exportados para o arquivo CSV: {nome_arquivo}")


class MatriculaDAO():
    def __init__(self,db_path):
        self.db_path = db_path

    def cadastrar_matricula(self, matricula):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        INSERT INTO Matricula (cpf, codigo, data) 
        VALUES (?, ?, ?)
        """

        cursor.execute(comando_sql, (matricula.cpf, matricula.codigo, matricula.data))

        conexao.commit()
        conexao.close()

    def buscar_matricula(self, cpf_aluno, codigo_disciplina):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Matricula WHERE cpf = ? AND codigo = ?
        """

        cursor.execute(comando_sql, (cpf_aluno, codigo_disciplina))
        matricula_tupla = cursor.fetchone()

        conexao.close()

        if matricula_tupla is None:
            return None

        matricula = Matricula(cpf=matricula_tupla[0], codigo=matricula_tupla[1], data=matricula_tupla[2])

        return matricula
    
    def cancelar_matricula(self, matricula):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        DELETE FROM Matricula WHERE cpf = ? AND codigo = ?
        """

        cursor.execute(comando_sql, (matricula.cpf, matricula.codigo))

        conexao.commit()
        conexao.close()

    def listar_matriculas(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM Matricula
        """

        cursor.execute(comando_sql)
        matriculas = cursor.fetchall()

        conexao.close()

        return matriculas


    def exportar_matriculas_para_csv(self, matriculas):
        nome_arquivo = input("Digite o nome do arquivo CSV (ou pressione Enter para o padrão 'matriculas.csv'): ").strip()

        if not nome_arquivo:
            nome_arquivo = 'matriculas.csv'

        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')
            # Escreve o cabeçalho
            escritor_csv.writerow(['CPF do Aluno', 'Código da Disciplina', 'Data e Horário da Matrícula'])
            # Escreve os dados das matrículas
            for matricula in matriculas:
                escritor_csv.writerow([matricula.cpf_aluno, matricula.codigo_disciplina, matricula.data_horario])

        print(f"Dados exportados para o arquivo CSV: {nome_arquivo}")