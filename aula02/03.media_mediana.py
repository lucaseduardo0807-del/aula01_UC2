import pandas as pd
import numpy as np

ARQUIVO= '01.amazon_sales_dataset.csv'

try:
    df = pd.read_csv(ARQUIVO)
    print(df.head(10))
    print(30*'-')
    print(df.columns)
    print(60*'-')
    print(df.describe())

    total_vendas = np.array(df['total_sales'])

    media = np.mean(total_vendas)
    mediana = np.median(total_vendas)
    print(f'Media: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Media/Mediana: {(media/mediana)*100}%')
except Exception as e:
    print(f'Erro: {e}')