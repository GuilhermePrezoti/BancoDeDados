import mysql.connector
import conexaoBD #Classe que faz a conexao com o banco de dados

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values ('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, tratarData(dataDeNascimento))
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print(con.rowcount, 'Inserido!')

    except Exception as erro:
        return erro

def tratarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano,mes,dia)

def consultar():
    try:
        sql = 'select * from pessoa'
        con.execute(sql)

        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            print('codigo: {}, nome: {}, telefone: {}, endereco: {}, dataDeNascimento: {}'. format(codigo, nome, telefone, endereco, dataDeNascimento))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update pessoa set {} = '{}' where cod = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

