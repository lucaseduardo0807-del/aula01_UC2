import pandas as pd

alunos = pd.Series(
    [8.5,7.0,9.5],
    index=["Ana","João","Maria"]
)

#print(alunos)
#print(alunos[["Ana","Maria"]])
#print(alunos[alunos >8])
#print(alunos[alunos <8])
#print(alunos + 1)
print(alunos.mean())