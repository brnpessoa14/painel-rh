import pandas as pd
import psycopg2

# Dados de conexão com o PostgreSQL
db_host = "localhost"
db_port = "5432"
db_name = "painel_rh_db"
db_user = "admin"
db_password = "admin"

# Caminhos para os arquivos CSV
caminho_folha = "data/folha-de-pagamento.csv"
caminho_beneficios = "data/benificios.csv"
caminho_movimentacao = "data/movimentacoes.csv"

def criar_tabela_folha():
    conn = None
    try:
        conn = psycopg2.connect(host=db_host, port=db_port, database=db_name, user=db_user, password=db_password)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS folha_pagamento (
                funcionario_id INT,
                nome VARCHAR(255),
                salario_bruto DECIMAL(10, 2),
                mes_ano DATE
            );
        """)
        conn.commit()
        print("Tabela folha_pagamento criada com sucesso (ou já existia).")
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela folha_pagamento: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def inserir_dados_folha(df):
    conn = None
    try:
        conn = psycopg2.connect(host=db_host, port=db_port, database=db_name, user=db_user, password=db_password)
        cur = conn.cursor()
        for index, row in df.iterrows():
            sql = """
                INSERT INTO folha_pagamento (funcionario_id, nome, salario_bruto, mes_ano)
                VALUES (%s, %s, %s, %s);
            """
            cur.execute(sql, (row['Funcionário ID'], row['Nome'], row['Salário Bruto'], row['Mês/Ano']))
        conn.commit()
        print(f"{len(df)} registros inseridos na tabela folha_pagamento.")
    except psycopg2.Error as e:
        print(f"Erro ao inserir dados na tabela folha_pagamento: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

# Cria a tabela de folha
criar_tabela_folha()

# leitura da planilha de folha
try:
    df_folha = pd.read_csv(caminho_folha)
    print("Planilha de folha lida com sucesso:")
    print(df_folha.head())
    # Insere os dados da folha no banco de dados
    inserir_dados_folha(df_folha)
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_folha}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler a planilha de folha: {e}")

#separador
print("\n" + "="*30 + "\n")

# leitura da planilha de benefícios
try:
    df_beneficios = pd.read_csv(caminho_beneficios)
    print("Planilha de benefícios lida com sucesso:")
    print(df_beneficios.head())
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_beneficios}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler a planilha de benefícios: {e}")

#separador
print("\n" + "="*30 + "\n")

#leitura da planilha de movimentação
try:
    df_movimentacao = pd.read_csv(caminho_movimentacao)
    print("Planilha de movimentação lida com sucesso:")
    print(df_movimentacao.head())
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_movimentacao}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler a planilha de movimentação: {e}")