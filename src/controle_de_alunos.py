from app import disciplina_dao, aluno_dao
from src.classes_base import Disciplina, Aluno
from src import menu_principal as menu
from src import utils




def MenuAluno():
    while True:
        print("""
            ---------------- Controle de Disciplinas ----------------
            \n  1 – Cadastrar Novo Aluno
            \n  2 – Atualizar Matricula
            \n  3 – Remover Aluno
            \n  4 – Listar Alunos
            \n  5 – Voltar Menu Principal
        """)
        
        comando = str(input("\nDigite sua opção:"))

        if comando == "1":
            cadastrar_aluno(aluno_dao) #feito
        elif comando == "2":
            atualizar_aluno(aluno_dao) #feito
        elif comando == "3":
            deletar_aluno(aluno_dao) #feito
        elif comando == "4":
            listar_alunos(aluno_dao) 
        elif comando == "5":
            menu.MenuPrincipal()

def cadastrar_aluno(aluno_dao):


    cpf = str(input('\n\n  cpf: '))
    if not cpf:
        print(" Insira um cpf válido:")
        cpf = str(input('  Insira o cpf: '))
        if not cpf:
            print(" Erro no cadastro!:")
            MenuAluno()
    while len(cpf) <11:
        print('\n\n  cpf invalido. ')
        cpf = (input('\n  cpf: '))
        if len(cpf) <11:
            MenuAluno()
    aluno_existente = aluno_dao.buscar_aluno(cpf)
       

    if aluno_existente is not None:
        print('\n    Aluno já cadastrado!')
        cpf = input('\n  Digite um novo cpf: ')
        aluno_existente = aluno_dao.buscar_aluno(cpf)
        if aluno_existente is not None:
            print('\n    cpf já cadastrado. Erro no cadastro!')
            MenuAluno()



    nome = input('  Insira o nome do aluno: ')
    if not nome:
        print(" Insira um nome válido:")
        nome = str(input('  Insira o nome do aluno: '))
        if not nome:
            print(" Erro no cadastro!:")
            MenuAluno()

    try:
        idade = int(input('  Idade: '))
        if not idade:
            print(" Insira uma idade válida:")
            idade = int(input('  Idade: '))
            if not idade:
                print(" Erro no cadastro!:")
                MenuAluno()
    except:
        print("Use apenas numeros inteiros na idade: ")
        try:
            idade = int(input('  Idade: '))
            if not idade:
                print(" Insira uma idade válida:")
                idade = int(input('  Idade: '))
                if not idade:
                    print(" Erro no cadastro!:")
                    MenuAluno()
        except: 
            MenuAluno()


    email = str(input('  Insira um email: '))
    if not '@' in email:
        email = str(input('  Insira um email válido: '))
        if not '@' in email:
            print(" Erro no cadastro!:")
            MenuAluno()
        
    cep = str(input("  Insira o CEP:"))

    try:
        endereco = utils.conferir_cep(cep)
    except:
        print("Não foi possível encontrar informações do CEP.")
        endereco_lista = obter_endereco_manualmente()
    else:
        endereco_lista = endereco

    aluno = Aluno(cpf, nome, idade, email, endereco_lista)

    aluno_dao.cadastrar_aluno(aluno)

    print('\n\n  Aluno cadastrado com sucesso!')


def obter_endereco_manualmente():
    rua = str(input(" Logradouro (Rua): "))
    bairro = str(input(" Bairro: "))
    cidade = str(input(" Cidade: "))
    estado = str(input(" Estado: "))

    return [rua, bairro, cidade, estado]


def atualizar_aluno(aluno_dao):
    cpf = str(input("    CPF do aluno:"))
    aluno_existente = aluno_dao.buscar_aluno(cpf)

    if aluno_existente is None:
        print('\n    Aluno não encontrado!')
        cpf = str(input("    CPF do aluno:"))
        aluno_existente = aluno_dao.buscar_aluno(cpf)
        if aluno_existente is None:
            print('\n    Aluno não encontrado!')
            MenuAluno(aluno_dao.db_path)

    print(f"""\n
        Dados do Aluno:\n
        CPF: {aluno_existente.cpf}
        Nome: {aluno_existente.nome}
        Idade: {aluno_existente.idade}
        Email: {aluno_existente.email}
        Endereço: {aluno_existente.endereco}\n
    """)

    nome_new = str(input("\n    Novo nome do aluno:"))
    idade_new = str(input("\n    Nova idade do aluno:"))
    email_new = str(input("\n    Novo email do aluno:"))

    cep = str(input("\n    Novo CEP do aluno:"))
    endereco_new = utils.conferir_cep(cep)

    if nome_new:
        aluno_existente.nome = nome_new

    if idade_new:
        try:
            idade_new = int(idade_new)
            aluno_existente.idade = idade_new
        except ValueError:
            print("A idade deve ser um número inteiro.")

    if email_new:
        aluno_existente.email = email_new

    if endereco_new:
        aluno_existente.endereco = endereco_new

    aluno_dao.atualizar_aluno(aluno_existente)
    print("Aluno atualizado com sucesso!")


def deletar_aluno(aluno_dao):
    cpf = str(input("    CPF:"))
    aluno_existente = aluno_dao.buscar_aluno(cpf)

    if aluno_existente is None:
        print('\n    Aluno não encontrado!')
        cpf = str(input("    CPF:"))
        aluno_existente = aluno_dao.buscar_aluno(cpf)
        if aluno_existente is None:
            print('\n    Aluno não encontrado!')
            MenuAluno(aluno_dao.db_path)

    resposta = str(input(f"Deseja excluir o aluno {aluno_existente.nome}? [y/n]"))
    if resposta.lower() == 'y':
        aluno_dao.excluir_aluno(aluno_existente)

def listar_alunos(aluno_dao):
    aluno_dao.listar_alunos()