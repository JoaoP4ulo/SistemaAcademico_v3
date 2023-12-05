from app import disciplina_dao, aluno_dao, matricula_dao
from src.classes_base import Disciplina, Aluno
from src import menu_principal as menu
from src import utils
from datetime import datetime
from src.classes_base import Matricula



def MenuMatricula():
    
    print("""
            ---------------- Controle de Disciplinas ----------------
            \n  1 – Matricular Aluno
            \n  2 – Cancelar Matricula
            \n  3 – Listar Matriculas
            \n  4 – Voltar Menu Principal
    """)
        
    comando = str(input("\nDigite sua opção:"))

    if comando == "1":
        matricular_aluno(aluno_dao, disciplina_dao, matricula_dao) 
    elif comando == "2":
        cancelar_matricula(aluno_dao, disciplina_dao, matricula_dao) 
    elif comando == "3":
        listar_matriculas(aluno_dao, disciplina_dao, matricula_dao) 
    elif comando == "4":
        menu.MenuPrincipal()


def matricular_aluno(aluno_dao, disciplina_dao, matricula_dao):
    
    codigo_disciplina = input("Digite o código da disciplina: ")
    disciplina = disciplina_dao.buscar_disciplina(codigo_disciplina)
    if disciplina is None:
        print("Disciplina não encontrada. Certifique-se de que a disciplina está cadastrada.")
        return

    cpf_aluno = input("Digite o CPF do aluno: ")
    aluno = aluno_dao.buscar_aluno(cpf_aluno)
    if aluno is None:
        print("Aluno não encontrado. Certifique-se de que o aluno está cadastrado.")
        return
    

    matricula_existente = matricula_dao.buscar_matricula(cpf_aluno, codigo_disciplina)
    if matricula_existente is not None:
        print("Este aluno já está matriculado nesta disciplina.")
        return

    data_matricula = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    matricula = Matricula(cpf_aluno, codigo_disciplina, data_matricula)

    matricula_dao.cadastrar_matricula(matricula)

    print(f"Aluno matriculado com sucesso na disciplina {disciplina.nome}.")

    MenuMatricula()



def cancelar_matricula(aluno_dao, disciplina_dao, matricula_dao):

    
    cpf_aluno = input("Digite o CPF do aluno: ")
    codigo_disciplina = input("Digite o código da disciplina: ")

    matricula = matricula_dao.buscar_matricula(cpf_aluno, codigo_disciplina)
    if matricula is None:
        print("Matrícula não encontrada.")
        return

    
    matricula_dao.cancelar_matricula(matricula)

    print("Matrícula cancelada com sucesso.")

    MenuMatricula()


def listar_matriculas(matricula_dao):
    
    matriculas = matricula_dao.listar_matriculas()

    
    if not matriculas:
        print("Não há matrículas cadastradas.")
        return

    
    for matricula in matriculas:
        print("\nCPF do Aluno:", matricula.cpf_aluno)
        print("Código da Disciplina:", matricula.codigo_disciplina)
        print("Data e Horário da Matrícula:", matricula.data_horario)

    
    exportar_csv = input("\nDeseja exportar os dados para um arquivo CSV? (S/N): ").lower()

    if exportar_csv == 's':
        matricula_dao.exportar_matriculas_para_csv(matriculas)

    MenuMatricula()