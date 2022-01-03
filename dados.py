import pandas as pd
from IPython.display import display

tabela = pd.read_excel("Vendas.xlsx")
print("Tabela De Vendas")
display(tabela)


# Pegar um Panorama geral sobre a sua base de Dados

faturamento_total = tabela["Valor Final"].sum()
print("Panorama Geral Base de dados")
print(faturamento_total)


#Faturamento POr LOja
faturamento_por_loja = tabela[["ID Loja" ,"Valor Final"]].groupby("ID Loja").sum()

print("Faturamento Por Loja")
display(faturamento_por_loja)

#Faturamento por produto
faturamento_por_produto = tabela[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print("Faturamento por loja e Produto")
display(faturamento_por_produto)