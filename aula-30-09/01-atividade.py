import pandas as pd

# 1. Criar o nome ou o caminho completo do arquivo .xls
caminho_arquivo_xls = "estimativa_dou_2026.xls"

# 2. Lê a planilha
tabela = pd.read_excel(caminho_arquivo_xls)

# 3.Mostra as primeiras linhas no terminal
print(tabela.head())

# 4. Ler o arquivo Excel original (.xls ou .xlsx)
caminho_excel = caminho_arquivo_xls
tabela = pd.read_excel(caminho_excel)

# 5. Salvar como arquivo .csv
# 5.1 'index=False' impede que o Python crie uma coluna extra com números de linhas
# 5.2 'encoding="utf-8-sig"' garante que acentos e caracteres especiais não fiquem bugados
tabela.to_csv("convertido_arquivo.csv", index=False, encoding="utf-8-sig")

print("Arquivo convertido com sucesso para CSV!")