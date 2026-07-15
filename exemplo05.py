import pandas as pd

df = pd.read_csv("ex02.csv",sep=";")

print(df)
print("Soma das quantidades:")
print(df["Quantidade"].sum())

print("Menor Preço:")
print(df["Preço"].min())

print("Contagem:")
print(df["Preço"].count())

print("Média:")
print(df["Preço"].mean())

print("informação única:")
print(df["Preço"].unique())

#max(maior) min(menor) count(contagem) mean(média) unique(informação única)

#Maior Preço
#Menor Preço
#Quantidade de Produtos = Produto
#Média de Preço
#Informação Única com o campo Produto