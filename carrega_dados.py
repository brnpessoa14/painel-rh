import pandas as pd

# caminho para o arquivo CSV
caminho_folha = "data/folha-de-pagamento.csv"
caminho_beneficios = "data/benificios.csv"
caminho_movimentacao = "data/movimentacoes.csv"


# leitura das plhanilhas 

try:
    df_folha = pd.read_csv(caminho_folha)
    df_folha = pd.read_csv(caminho_folha)
    print("Planilha de folha lida com sucesso:")
    print(df_folha.head())
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

