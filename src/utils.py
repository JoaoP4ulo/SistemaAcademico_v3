import sqlite3  as sqlite3
import os
import requests


def criar_banco_de_dados(db_path):   

    conexao = sqlite3.connect(db_path)

    comando_sql_disciplina = """
    CREATE TABLE Disciplina (
        codigo TEXT NOT NULL,
        nome TEXT NOT NULL,
        carga_h INTEGER NOT NULL,
        nome_professor TEXT NOT NULL
    )
    """

    comando_sql_Aluno = """
    CREATE TABLE Aluno (
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL,
    )
    """

    comando_sql_Matricula = """
    CREATE TABLE Matricula (
        cpf TEXT NOT NULL,
        codigo INTEGER NOT NULL,
        data DATETIME NOT NULL,
    )
    """

    cursor = conexao.cursor()

    cursor.execute(comando_sql_disciplina)

    cursor.execute(comando_sql_Aluno)

    cursor.execute(comando_sql_Matricula)

    conexao.close()

    print('\n\n  Banco de Dados Criado com Sucesso!')


def conferir_cep(cep):
    cep = cep.strip()

    # Remover qualquer pontuação do CEP, mantendo apenas os números
    cep = ''.join(char for char in cep if char.isdigit())

    # Verificar se o CEP possui 8 dígitos
    if len(cep) != 8:
        print("Formato de CEP inválido. Certifique-se de fornecer exatamente 8 dígitos.")
        return

    # Construir a URL para a consulta ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Fazer a requisição HTTP
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar se houve algum erro na requisição
        endereco_info = response.json()

        # Exibir informações do endereço
        print("\nInformações do Endereço:")
        print("CEP:", endereco_info.get('cep', 'Não encontrado'))
        print("Logradouro (Rua):", endereco_info.get('logradouro', 'Não encontrado'))
        print("Bairro:", endereco_info.get('bairro', 'Não encontrado'))
        print("Cidade:", endereco_info.get('localidade', 'Não encontrada'))
        print("Estado:", endereco_info.get('uf', 'Não encontrado'))
    except requests.exceptions.HTTPError as err:
        print(f"Erro na requisição HTTP: {err}")
    except Exception as e:
        print(f"Erro: {e}")