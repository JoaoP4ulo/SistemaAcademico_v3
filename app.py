import os
import src.utils as utils
from src.classes_dao import DisciplinaDAO,AlunoDAO,MatriculaDAO
from src import menu_principal as menu



#definição do caminho padrão do db
db_path = 'controle_academico.db'

aluno_dao = AlunoDAO(db_path)
disciplina_dao = DisciplinaDAO(db_path)
matricula_dao = MatriculaDAO(db_path)

if __name__ == '__main__':

    #verificar se o banco de dados existe
    if not os.path.exists(db_path):
        utils.criar_banco_de_dados(db_path)
        

    while True:
        
        menu.MenuPrincipal()
        

        # Dentro do loop, aguarde a entrada do usuário para decidir se deve continuar ou encerrar
        resposta = input("Deseja encerrar o programa? (S/N): ").strip().lower()
        if resposta == 's':
            break
            
    
        
            