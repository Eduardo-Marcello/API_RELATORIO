import pandas as pd

dados_departamentos = pd.read_csv('departamentos.csv',
                                  delimiter=',',
                                  encoding='utf-8',
                                  index_col=None)

for dados in dados_departamentos:
  print(dados)
