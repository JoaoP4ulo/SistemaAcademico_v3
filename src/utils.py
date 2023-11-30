import sqlite3  as sqlite3
import os
import requests


def criar_banco_de_dados(db_path):   

    conexao = sqlite3.connect(db_path)

    cursor = conexao.cursor()

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
        cpf TEXT NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
    """

    comando_sql_Matricula = """
    CREATE TABLE Matricula (
        cpf TEXT NOT NULL,
        codigo INTEGER NOT NULL,
        data DATETIME NOT NULL
    )
    """

    cursor.execute(comando_sql_disciplina)
    cursor.execute(comando_sql_Aluno)
    cursor.execute(comando_sql_Matricula)

    conexao.commit()
    conexao.close()

    print('\n\n  Banco de Dados Criado com Sucesso!')


def conferir_cep(cep):
    cep = cep.strip()

    # Remover qualquer pontuação do CEP, mantendo apenas os números
    cep = ''.join(char for char in cep if char.isdigit())

    # Verificar se o CEP possui 8 dígitos
    if len(cep) != 8:
        print("Formato de CEP inválido. Certifique-se de fornecer exatamente 8 dígitos.")
        return None

    # Construir a URL para a consulta ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Inicializar a lista de endereço
    endereco = ["CEP não encontrado", "Logradouro não encontrado", "Bairro não encontrado", "Cidade não encontrada", "Estado não encontrado"]

    # Fazer a requisição HTTP
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar se houve algum erro na requisição
        endereco_info = response.json()

        # Atualizar a lista de endereço com as informações disponíveis
        endereco[0] = endereco_info.get('cep', 'CEP não encontrado')
        endereco[1] = endereco_info.get('logradouro', 'Logradouro não encontrado')
        endereco[2] = endereco_info.get('bairro', 'Bairro não encontrado')
        endereco[3] = endereco_info.get('localidade', 'Cidade não encontrada')
        endereco[4] = endereco_info.get('uf', 'Estado não encontrado')

        return endereco
    except requests.exceptions.HTTPError as err:
        print(f"Erro na requisição HTTP: {err}")
    except Exception as e:
        print(f"Erro: {e}")
