from app import disciplina_dao, aluno_dao
from src.classes_base import Disciplina, Aluno
from src import menu_principal as menu




def MenuDisciplina():
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
            cadastrar_disciplina(disciplina_dao) #feito
        elif comando == "2":
            atualizar_disciplina(disciplina_dao) #feito
        elif comando == "3":
            deletar_disciplina(disciplina_dao) #feito
        elif comando == "4":
            listar_disciplinas(disciplina_dao) #feito
        elif comando == "5":
            menu.MenuPrincipal()
        

def cadastrar_disciplina(disciplina_dao): #feito

    codigo = str(input('\n\n  Codigo: '))
    if not codigo:
        print(" Insira um codigo válido:")
        codigo = str(input('  Insira o codigo da disciplina: '))
        if not codigo:
            print(" Erro no cadastro!:")
            MenuDisciplina()
    while len(codigo) <4:
        print('\n\n  codigo muito pequeno, insira um codigo com mais de 4 caracteres. ')
        codigo = (input('\n  Codigo: '))
        if len(codigo) <4:
            MenuDisciplina()
    disciplina_existente = disciplina_dao.buscar_disciplina(codigo)
       

    if disciplina_existente is not None:
        print('\n    Disciplina já cadastrado!')
        codigo = input('\n  Digite um novo codigo: ')
        disciplina_existente = disciplina_dao.buscar_disciplina(codigo)
        if disciplina_existente is not None:
            print('\n    Codigo já cadastrado. Erro no cadastro!')
            MenuDisciplina()



    nome = input('  Insira o nome da disciplina: ')
    if not nome:
        print(" Insira um nome válido:")
        nome = str(input('  Insira o nome da disciplina: '))
        if not nome:
            print(" Erro no cadastro!:")
            MenuDisciplina()

    try:
        carga_h = int(input('  Carga horária: '))
        if not carga_h:
            print(" Insira uma carga horária válida:")
            carga_h = int(input('  Carga horária: '))
            if not carga_h:
                print(" Erro no cadastro!:")
                MenuDisciplina()
    except:
        print("Use apenas numeros inteiros na carga horária: ")
        try:
            carga_h = int(input('  Carga horária: '))
            if not carga_h:
                print(" Insira uma carga horária válida:")
                carga_h = int(input('  Carga horária: '))
                if not carga_h:
                    print(" Erro no cadastro!:")
                    MenuDisciplina()
        except: 
            MenuDisciplina()


    nome_professor = input('  Insira o nome do professor responsável: ')

    disciplina = Disciplina(codigo, nome, carga_h, nome_professor)

    disciplina_dao.cadastrar_disciplina(disciplina)

    print('\n\n  Disciplina cadastrada com sucesso!')


def atualizar_disciplina(disciplina_dao):
    codigo = str(input("    Codigo:"))
    disciplina_existente = disciplina_dao.buscar_disciplina(codigo)

    if disciplina_existente is None:
        print('\n    Disciplina não encontrada!')
        codigo = str(input("    Codigo:"))
        disciplina_existente = disciplina_dao.buscar_disciplina(codigo)
        if disciplina_existente is None:
            print('\n    Disciplina não encontrada!')
            MenuDisciplina(disciplina_dao.db_path)

    print(f"""\n
        Dados da Disciplina:\n
        Codigo: {disciplina_existente.codigo}
        Nome: {disciplina_existente.nome}
        Carga: {disciplina_existente.carga_h}
        Professor responsavel: {disciplina_existente.nome_professor}\n
    """)

    new_nome = str(input("\n    Novo nome da disciplina:"))
    new_carga_h = str(input("\n    Nova carga horária da disciplina:"))
    new_nome_professor = str(input("\n    Novo professor responsável:"))

    disciplina_dao.atualizar_disciplina(disciplina_existente, new_nome, new_carga_h, new_nome_professor)
    print("Disciplina atualizada com sucesso!")
    
        
def deletar_disciplina(disciplina_dao): #feito

    codigo = str(input("    Codigo:"))
    disciplina_existente = disciplina_dao.buscar_disciplina(codigo)

    if disciplina_existente is None:
        print('\n    Codigo não existente!')
        codigo = str(input("    Codigo:"))
        disciplina_existente = disciplina_dao.buscar_disciplina(codigo)
        if disciplina_existente is None:
            print('\n    Codigo não existente!')
            MenuDisciplina(disciplina_dao.db_path)

    resposta = str(input(f"Deseja excluir a disciplina {disciplina_existente.nome}?  [y/n]"))
    if resposta == 'y' or resposta =='Y':
        disciplina_dao.excluir_disciplina(disciplina_existente)

def listar_disciplinas(disciplina_dao):

    disciplina_dao.listar_disciplinas()