# PythonSql
Conjunto de funções para simplificar o uso de banco de dados com python

# No momento, só foi feito para mysql. 


Codigo autoexplicativo!


Lista de funções:

conectar(): # Conecta ao banco de dados

executar(sql): # Executa uma query

criar_banco(nome_banco): # Cria um banco de dados

deletar_banco(conexao, nome_banco): # Deleta um banco de dados

criar_tabela(nome_tabela, colunas): # Cria uma tabela

deletar_tabela(nome_tabela): # Deleta uma tabela

inserir(nome_tabela, colunas, valores): # Insere dados em uma tabela

selecionar(nome_tabela, colunas, condicao=None): # Seleciona dados de uma tabela

deletar(nome_tabela, condicao): # Deleta dados de uma tabela

atualizar(nome_tabela, colunas, valores, condicao): # Atualiza dados de uma tabela

db_para_df(nome_tabela, colunas, condicao=None): # Transforma uma tabela em um dataframe

db_para_csv(nome_arquivo, nome_tabela, colunas, condicao=None): # Transforma uma tabela em um csv

colunas(nome_coluna, tipo, tamanho=None, auto_incremento=False, chave_primaria=False, nao_nulo=False): # Cria uma coluna

condicao(nome_coluna, operador, valor): # Cria uma condicao

condicao_mas(condicao1, condicao2): # Cria uma condicao AND

condicao_ou(condicao1, condicao2): # Cria uma condicao OR

condicao_negacao(condicao): # Cria uma condicao NOT

condicao_multiplas_where(condicao1, condicao2): # Cria uma condicao IN

condicao_entre(condicao1, condicao2, condicao3): # Cria uma condicao BETWEEN

**FUNÇÕES SENDO REVISADAS**
