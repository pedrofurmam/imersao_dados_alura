import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns   
import plotly.express as px

df = pd.read_csv("salaries.csv")
print(df.shape)

linhas, colunas = df.shape[0], df.shape[1]
print("Número de linhas:",linhas)
print("Número de colunas:",colunas)

print(df.columns)

# Renomeando as colunas do DataFrame
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'localizacao_empresa',
    'company_size': 'tamanho_empresa'
}

#Aplicando os novos nomes
df.rename(columns=novos_nomes, inplace=True)

#Verificando as colunas renomeadas
print(df.columns)

# Verifica quantas vezes cada nível de experiência aparece no DataFrame
print(df.nivel_experiencia.value_counts())

print(df.tipo_emprego.value_counts())

print(df.remoto.value_counts())

nivel_experiencia = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df['nivel_experiencia'] = df['nivel_experiencia'].replace(nivel_experiencia)
print(df['nivel_experiencia'].value_counts())

contrato={
    'FT': 'Integral',
    'PT': 'Parcial',
    'CT': 'Contrato',
    'FL': 'Freelancer'
}
df['tipo_emprego'] = df['tipo_emprego'].replace(contrato)
print(df['tipo_emprego'].value_counts())

tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Media',
    'L': 'Grande'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
print(df['tamanho_empresa'].value_counts())

remoto = {
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
}
df['remoto'] = df['remoto'].replace(remoto)
print(df['remoto'].value_counts())
print(df.head())
print(df.describe(include = 'object'))

print(df.isnull())


print(df['ano'].unique())

#Exibindo quais linhas estão com os anos nulos:
print(df.isnull().any(axis=1))

#Exemplo de preenchimento com média e mediana

#Criação de um DataFrame de exemplo
df_salarios = pd.DataFrame({

    'nome': ['João', 'Bruno', 'Pedro', 'Daniele', 'Maria'],
    'salario': [3000, np.nan, 5000, np.nan, 7000],
})

# Preenchendo valores nulos com a média do salário
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

# Preenchendo valores nulos com a mediana do salário
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

print(df_salarios)

# Exemplo de DataFrame com dados de temperatura
df_temperatura = pd.DataFrame({
    'dia_semana': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [25, 28, np.nan, 30, 27]
})  

# Preenchendo valores nulos com o método forward fill(responsável por preencher os valores nulos com o último valor válido)
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill()
print(df_temperatura)


df_cidades = pd.DataFrame({
    'nome': ['João', 'Bruno', 'Pedro', 'Daniele', 'Maria'],
    'cidade': ['São Paulo', np.nan, np.nan, 'Curitiba', 'Porto Alegre'],

})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não Informada')
print(df_cidades)

df_limpo = df.dropna()
print(df_limpo.isnull().sum())

print(df_limpo.head())

print(df_limpo.info())
"""
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.info())

df_limpo['nivel_experiencia'].value_counts().plot(kind='bar',title='Distribuição dos tipos de emprego')
plt.show()
"""
"""
sns.barplot(data=df_limpo, x='nivel_experiencia', y='usd')
plt.show()
"""
''' 
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='nivel_experiencia', y='usd')
plt.title("Salário médio por nível de experiência")
plt.xlabel("Nível de Experiência")
plt.ylabel("Salário médio anual em USD")
plt.show()
'''
#df_limpo.groupby('nivel_experiencia')['usd'].mean().sort_values(ascending=False)

ordem = df_limpo.groupby('nivel_experiencia')['usd'].mean().sort_values(ascending=False).index
"""
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='nivel_experiencia', y='usd', order=ordem)
plt.title("Salário médio por nível de experiência")
plt.xlabel("Nível de Experiência")
plt.ylabel("Salário médio anual em USD")
plt.show()
"""
"""
plt.figure(figsize=(8,50))
sns.histplot(df_limpo['usd'], bins=5, kde=True)
plt.title("Distribuição dos salários anuais")
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()
"""

""""
plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title("Boxplot dos salários anuais")        
plt.xlabel("Salário em USD")
plt.show()
""" 
"""
ordem_nivel_experiencia=['Junior','Pleno','Senior','Executivo']
plt.figure(figsize=(8,5))
sns.boxplot( x='nivel_experiencia', y='usd', data=df_limpo,order=ordem_nivel_experiencia, palette='Set2')
plt.title("Boxplot dos salários anuais por nível de experiência")
plt.show()
"""
"""
media_salario = df_limpo.groupby('nivel_experiencia')['usd'].mean().reset_index()

fig = px.bar(
    media_salario,
    x='nivel_experiencia',
    y='usd',
    title='Média salarial anual (USD) por nível de experiência',
    labels={'nivel_experiencia': 'Nível de Experiência', 'usd': 'Salário Médio (USD)'}
)
fig.show(renderer="browser")
"""
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Distribuição dos tipos de trabalho',
             hole=0.5
)
fig.update_traces( textinfo='percent+label')  
fig.show(renderer="browser")