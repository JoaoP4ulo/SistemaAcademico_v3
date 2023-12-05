from src.controle_de_disciplina import MenuDisciplina
from src.controle_de_alunos import MenuAluno
from src.controle_de_matricula import MenuMatricula



def MenuPrincipal():
    
    print("""
            ---------------- Menu Principal ----------------
            \n  1 – Controle de Disciplinas
            \n  2 - Controle de Alunos(as)
            \n  3 – Controle de Matrículas
            \n  4 – Sair
    """)

    comando = input("\nDigite sua opção:")

    if comando == "1":
        MenuDisciplina()
    elif comando == "2":
        MenuAluno()
    elif comando == "3":
        MenuMatricula()
    elif comando == "4":
        print("Encerrando o programa. Até mais!")
        

if __name__ == '__main__':
    MenuPrincipal()
