import pandas as pd
import plotly.express as px

df = pd.read_csv('telecom_users.csv')

# LIMPANDO O CÓDIGO
# o segundo parâmetro(axis) indica se é linha(0) ou coluna(x)
df = df.drop(["Unnamed: 0"], axis=1)
# print(df) - imprime df
# print(df.info()) - imprime as informações sobre df
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
df = df.dropna(how="all", axis=1)
# é a mesma coisa que df = df.dropna() pq how="any", axis=0 são valores padrões
df = df.dropna(how="any", axis=0)

# ANALISANDO O CÓDIGO
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

print(df.info())
for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color="Churn")
        fig.show()
        print(df.pivot_table(index="Churn", columns=coluna,
              aggfunc='count')["IDCliente"])  # cria tabela com os dados do gráfico
