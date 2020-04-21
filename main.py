#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


df = black_friday
df.head(5)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[30]:


def q1():
    return df.shape
pass
    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[33]:


def q2():
    #aux = df.drop_duplicates('User_ID')
    return len(df.query('(Gender == "F") & (Age == "26-35")'))
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[36]:


def q3():
    aux = df.drop_duplicates('User_ID')
    return len(aux)
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    return df.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[50]:


def q5():
    return float((((df.isna().sum(axis=1)) != 0).sum())/df.shape[0])
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    aux = pd.DataFrame({'colunas': df.columns,'faltantes': df.isna().sum()})
    return int(aux['faltantes'].max())
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[57]:


def q7():
    return float(df['Product_Category_3'].mode())
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[62]:


def q8():
    aux = (df['Purchase'] - df['Purchase'].min())/(df['Purchase'].max()-df['Purchase'].min())
    return float(aux.mean())
    pass


# In[63]:


#aux = (df['Purchase'] - df['Purchase'].min())/(df['Purchase'].max()-df['Purchase'].min())
#float(aux.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[66]:


def q9():
    aux = (df['Purchase'] - df['Purchase'].mean())/df['Purchase'].std()
    return aux[(aux > -1) & ( aux <= 1 )].shape[0]
    pass


# In[65]:


#aux = (df['Purchase'] - df['Purchase'].mean())/df['Purchase'].std()
#aux[(aux > -1) & ( aux <= 1 )].shape[0]


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[107]:


def q10():
    df = black_friday[['Product_Category_2', 'Product_Category_3']]
    df = df[df['Product_Category_2'].isna()]
    return df['Product_Category_2'].equals(df['Product_Category_3'])

