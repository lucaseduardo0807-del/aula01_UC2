import pandas as pd
df = pd.read_csv("ex01.csv",sep=";")
print(df)

nome = input("Nome: ")
idade = int(input("Idade: "))
curso = input("Curso: ")
nova_linha={
    'Nome':nome,
    'Idade':idade,
    'Curso':curso
}

df.loc[len(df)] = nova_linha
print("\nData Frame atualizado:")
print(df)

df.to_csv("ex01.csv",sep=";",index=False)