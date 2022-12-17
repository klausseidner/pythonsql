##############################################################################################################
#
#  Descrição: Biblioteca responsável por manipular o banco de dados em mysql
#  Autor: Klaus Seidner
#  Versão: 1.0
#  Licença: GNU General Public License v3.0
#
#  Observações:
#  - Para instalar a biblioteca mysql.connector: pip install mysql-connector-python
#  - Para instalar a biblioteca pandas: pip install pandas
#
##############################################################################################################

import mysql.connector # Biblioteca responsavel pela conexao mysql
from mysql.connector import Error # Biblioteca responavel para tratamentos de erros com mysql
import includes.functions.config as config # Importa as configuracoes do sistema
import pandas as pd # Biblioteca responsavel por manipular dados

host_name , user_name , user_password, db_name = config.get('Mysql') # Pega as configuracoes do mysql

def conectar(): # Conecta ao banco de dados
    conexao = None # Inicializa a variavel conexao
    try: # Tenta conectar ao banco de dados
        conexao = mysql.connector.connect( # Conecta ao banco de dados
            host=host_name, # Define o servidor
            user=user_name, # Define o usuario
            passwd=user_password, # Define a senha
            db=db_name # Define o banco de dados
        )
        print("MySQL Conectado com sucesso!") # Imprime mensagem de sucesso
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
    return conexao # Retorna a conexao

def executar(sql): # Executa uma query
    conexao = conexao() # Conecta ao banco de dados
    cursor = conexao.cursor() # Cria um cursor
    try: # Tenta executar a query
        cursor.execute(sql) # Executa a query
        conexao.commit() # Confirma a query
        print("Query successful") # Imprime mensagem de sucesso
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def criar_banco(nome_banco): # Cria um banco de dados
    try: # Tenta criar o banco de dados
        sql = f"CREATE DATABASE IF NOT EXISTS {nome_banco};" # Cria a query
        executar(sql) # Executa a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def deletar_banco(conexao, nome_banco): # Deleta um banco de dados
    try: # Tenta deletar o banco de dados
        sql = f"DROP DATABASE IF EXISTS {nome_banco};" # Cria a query
        executar(sql) # Executa a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def criar_tabela(nome_tabela, colunas): # Cria uma tabela
    '''
    CREATE TABLE IF NOT EXISTS professor (
    professor_id INT NOT NULL AUTO_INCREMENT,
    primeiro_nome VARCHAR(45) NOT NULL,
    segundo_nome VARCHAR(45) NOT NULL,
    linguagem_1 VARCHAR(45) NOT NULL,
    linguagem_2 VARCHAR(45),
    data_n DATE NOT NULL,
    taxa_id INT NOT NULL,
    num_telefone VARCHAR(45) NOT NULL,
    PRIMARY KEY (professor_id)
    );
    '''
    try: # Tenta criar a tabela
        sql = f"""CREATE TABLE IF NOT EXISTS {nome_tabela} ( """ # Cria a query
        for coluna in colunas: # Para cada coluna
            sql += f"{coluna}, " # Adiciona a coluna na query
        sql = sql[:-2] # Remove a ultima virgula
        sql += ");" # Fecha a query
        executar(sql) # Executa a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def deletar_tabela(nome_tabela): # Deleta uma tabela
    try: # Tenta deletar a tabela
        sql = f"DROP TABLE IF EXISTS {nome_tabela};" # Cria a query
        executar(sql) # Executa a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
        
def inserir(nome_tabela, colunas, valores): # Insere dados em uma tabela
    '''
    INSERT INTO professor (professor_id, primeiro_nome, segundo_nome, linguagem_1, linguagem_2, data_n, taxa_id, num_telefone) 
    VALUES (1, 'Joaquim', 'das Couve', 'c++', NULL, '1991-12-23', 11111, '+21 9 9999-9999');
    '''
    try: # Tenta inserir os dados
        sql = f"""INSERT INTO {nome_tabela} (""" # Cria a query
        for coluna in colunas: # Para cada coluna
            sql += f"{coluna}, " # Adiciona a coluna na query
        sql = sql[:-2] # Remove a ultima virgula
        sql += ") VALUES (" # Fecha a query
        for valor in valores: # Para cada valor
            sql += f"'{valor}', " # Adiciona o valor na query
        sql = sql[:-2] # Remove a ultima virgula
        sql += ");" # Fecha a query
        executar(sql) # Executa a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
    
def selecionar(nome_tabela, colunas, condicao=None): # Seleciona dados de uma tabela
    '''
    SELECT curso.curso_id, curso.curso_nome, curso.linguagem, cliente.cliente_nome, cliente.indereco
    FROM curso
    JOIN cliente
    ON curso.cliente = cliente.cliente_id
    WHERE curso.em_andamento = FALSE;
    '''
    conexao = conectar() # Conecta ao banco de dados
    try: # Tenta selecionar os dados
        sql = f"""SELECT """ # Cria a query
        for coluna in colunas: # Para cada coluna
            sql += f"{coluna}, " # Adiciona a coluna na query
        sql = sql[:-2] # Remove a ultima virgula
        sql += f""" FROM {nome_tabela} """ # Fecha a query
        if condicao != None: # Se a condicao for diferente de None
            sql += f""" WHERE {condicao} """ # Adiciona a condicao na query
        sql += ";" # Fecha a query
        #cursor = conexao.cursor() # Cria um cursor
        cursor = conexao.cursor(dictionary=True) # Cria um cursor
        cursor.execute(sql) # Executa a query
        resultado = cursor.fetchall() # Retorna os resultados
        return resultado # Retorna os resultados
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def deletar(nome_tabela, condicao): # Deleta dados de uma tabela
    try: # Tenta deletar os dados
        sql = f"""DELETE FROM {nome_tabela} WHERE {condicao}""" # Cria a query
        executar(sql)  # Executa a query
    except Error as err:
        print(f"Error: '{err}'") # Imprime mensagem de erro
    
def atualizar(nome_tabela, colunas, valores, condicao): # Atualiza dados de uma tabela
    try: # Tenta atualizar os dados
        sql = f"""UPDATE {nome_tabela} SET """ # Cria a query
        for i in range(len(colunas)): # Para cada coluna
            sql += f"{colunas[i]} = '{valores[i]}', " # Adiciona a coluna na query
        sql = sql[:-2] # Remove a ultima virgula
        sql += f""" WHERE {condicao} """ # Fecha a query
        executar(sql) # Executa a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def db_para_df(nome_tabela, colunas, condicao=None): # Transforma uma tabela em um dataframe
    try: # Tenta transformar em um dataframe
        resultado = selecionar(nome_tabela, colunas, condicao) # Seleciona os dados
        dataframe = pd.DataFrame(resultado, columns=colunas) # Transforma em um dataframe
        return dataframe # Retorna o dataframe
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def db_para_csv(nome_arquivo, nome_tabela, colunas, condicao=None): # Transforma uma tabela em um csv
    try: # Tenta transformar em um csv
        dataframe = db_para_df(nome_tabela, colunas, condicao) # Transforma em um dataframe
        dataframe.to_csv(nome_arquivo, index=False) # Transforma em um csv
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
    
def colunas(nome_coluna, tipo, tamanho=None, auto_incremento=False, chave_primaria=False, nao_nulo=False): # Cria uma coluna
    try: # Tenta criar a coluna
            sql = f"{nome_coluna} {tipo}" # Cria a query
            if tamanho != None: # Se o tamanho for diferente de None
                sql += f"({tamanho})" # Adiciona o tamanho na query
            if auto_incremento: # Se o auto_increment for True
                sql += " AUTO_INCREMENT" # Adiciona o auto_increment na query
            if chave_primaria: # Se o primary_key for True
                sql += " PRIMARY KEY" # Adiciona o primary_key na query
            if nao_nulo: # Se o not_null for True
                sql += " NOT NULL" # Adiciona o not_null na query
            return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def condicao(nome_coluna, operador, valor): # Cria uma condicao
    operadores = ["=", "!=", ">", "<", ">=", "<=", "LIKE", "NOT LIKE", "IN", "NOT IN", "BETWEEN", "NOT BETWEEN", "IS NULL", "IS NOT NULL"] # Lista de operadores
    if operador not in operadores: # Se o operador nao estiver na lista de operadores
        print(f"Error: Operador '{operador}' invalido") # Imprime mensagem de erro
    try: # Tenta criar a condicao
        sql = f"{nome_coluna} {operador} '{valor}'" # Cria a query
        return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
        
def condicao_mas(condicao1, condicao2): # Cria uma condicao AND
    try: # Tenta criar a condicao
        sql = f"{condicao1} AND {condicao2}" # Cria a query
        return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
        
def condicao_ou(condicao1, condicao2): # Cria uma condicao OR
    try: # Tenta criar a condicao
        sql = f"{condicao1} OR {condicao2}" # Cria a query
        return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def condicao_negacao(condicao): # Cria uma condicao NOT
    try: # Tenta criar a condicao
        sql = f"NOT {condicao}" # Cria a query
        return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
        
def condicao_multiplas_where(condicao1, condicao2): # Cria uma condicao IN
    try: # Tenta criar a condicao
        sql = f"{condicao1} IN {condicao2}" # Cria a query
        return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro

def condicao_entre(condicao1, condicao2, condicao3): # Cria uma condicao BETWEEN
    try: # Tenta criar a condicao
        sql = f"{condicao1} BETWEEN {condicao2} AND {condicao3}" # Cria a query
        return sql # Retorna a query
    except Error as err: # Caso ocorra um erro
        print(f"Error: '{err}'") # Imprime mensagem de erro
