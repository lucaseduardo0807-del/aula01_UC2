import pandas as pd

aluno = pd.Series(
    ["Clayton",49,"Python","Centro"],
    index=["Nome","Idade","Curso","Cidade"]
)

print(aluno)