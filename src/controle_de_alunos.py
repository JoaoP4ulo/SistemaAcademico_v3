from app import disciplina_dao, aluno_dao
from src.classes_base import Disciplina, Aluno
from src import menu_principal as menu
from src import utils




def MenuAluno():
    while True:
        print("""
            ---------------- Controle de Disciplinas ----------------
            \n  1 – Cadastrar Nova Disciplina
            \n  2 – Atualizar Disciplina
            \n  3 – Remover Disciplina
            \n  4 – Listar Disciplinas
            \n  5 – Voltar Menu Principal
        """)
        
        comando = str(input("\nDigite sua opção:"))

        if comando == "1":
            cadastrar_aluno(aluno_dao) 
        elif comando == "2":
            atualizar_aluno(aluno_dao) 
        elif comando == "3":
            deletar_aluno(aluno_dao) 
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
        
    endereco = str(input("  Insira o CEP:"))
    utils.conferir_cep(endereco)
        

    aluno = Aluno(cpf, nome, idade, email, endereco)

    disciplina_dao.cadastrar_disciplina(disciplina)

    print('\n\n  Disciplina cadastrada com sucesso!')

def atualizar_aluno(aluno_dao):
    pass

def deletar_aluno(aluno_dao):
    pass

def listar_alunos(aluno_dao):
    pass