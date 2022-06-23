import mysql.connector #Faz acesso ao mysql
from mysql.connector import errorcode #Trata as execões que vão surgir

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user= 'root', password='', database='bdti13n')

        print('Conectado com SUCESSO!')
        return db_connection

    except mysql.connector.Error as erro: #Guardando as possiveis exceções na variavel
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso este banco de dados não exista
            print('Banco de dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Caso o usuario ou senha estejam errados
            print('Usuario ou senha não são validos!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close()
