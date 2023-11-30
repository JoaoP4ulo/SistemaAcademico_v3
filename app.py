import os
import src.utils as utils
from src.classes_dao import DisciplinaDAO,AlunoDAO
from src import menu_principal as menu



#definição do caminho padrão do db
db_path = 'controle_academico.db'
#definição da senha padrão de recuperação de email
aluno_dao = AlunoDAO(db_path)
disciplina_dao = DisciplinaDAO(db_path)

if __name__ == '__main__':

    #verificar se o banco de dados existe
    if not os.path.exists(db_path):
        utils.criar_banco_de_dados(db_path)
        

    menu.MenuPrincipal()
        
            
    
        
            