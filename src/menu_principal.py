# from src.controle_de_alunos import MenuAluno
from src.controle_de_disciplina import MenuDisciplina
# from src.controle_de_matricula import MenuMatricula





def MenuPrincipal():
    while True:
        print("""
            ---------------- Menu Principal ----------------
            \n  1 – Controle de Disciplinas
            \n  2 - Controle de Alunos(as)
            \n  3 – Controle de Matrículas
            \n  4 – Sair
        """)
        
        comando = str(input("\nDigite sua opção:"))

        if comando == "1":
            MenuDisciplina()
        elif comando == "2":
            None
        elif comando == "3":
            None
        elif comando == "4":
            break
    