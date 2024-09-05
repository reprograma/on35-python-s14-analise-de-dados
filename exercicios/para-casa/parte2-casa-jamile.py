# %%
# Parte 2: Olist

# Desafio: Criar um notebook de análise exploratória (como fizemos na nossa aula de hoje) com todas as etapas de coleta, limpeza, análise e visualização com base de dados da Olist.

# **Requisitos:**

# Formular no mínimo **2 perguntas** (caso queira se desafiar crie pelo menos mais perguntas além das 2 obrigatórias) para responder com suas análises;
# Utilizar pelo menos **3 bases de dados da Olist** (caso você deseje criar sua base do zero). Caso deseje continuar utilizando a que criamos em aula, é necessário incluir pelo menos mais **1 tabela** para enriquecer sua análise.

# Para responder as perguntas elaboradas usar:

# Criar pelo menos **2 gráficos**.
# Exporte sua base final em csv.
# Submeta uma pasta que contenha:
# o arquivo **seu_nome.ipynb** com sua análise exploratória;
# a base final criada por você no formato .csv;

# %%
# Formular no mínimo **2 perguntas** (caso queira se desafiar crie pelo menos mais perguntas além das 2 obrigatórias) para responder com suas análises;
# Qual o produto mais vendido?
import pandas as pd

df_produtos = pd.read_csv('../para-sala/dados/olist_products_dataset.csv')
df_produtos

# %%
# Qual o produto mais vendido?
df_produtos['product_category_name'].unique()
 
# %%
df_produtos.info()




 # %%
# Qual o meio de pagamento mais utilizado?

