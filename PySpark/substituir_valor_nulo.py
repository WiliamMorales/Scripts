#Importando bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, avg
import pandas as pd
import math

# Criando uma sessão spark e configurando o nível de log para ERROR
spark = SparkSession.builder.appName("Exemplo").config("spark.driver.log.level", "ERROR").getOrCreate()

# Ler o arquivo Excel usando o Pandas
pandas_df = pd.read_excel('dados.xlsx')

# Criar um DataFrame do PySpark a partir do Pandas DataFrame
df = spark.createDataFrame(pandas_df)
#df.show()

#Preencher valores nulos na coluna 'UnitPrice' com a média dos preços unitários
media_precounitario = pandas_df['UnitPrice'].mean()
pandas_df['UnitPrice'].fillna(media_precounitario, inplace=True)

# Criar um DataFrame do PySpark a partir do Pandas DataFrame com valores nulos preenchidos
df = spark.createDataFrame(pandas_df)
df.show()

######################################################
#
# RODAR: python3 substituir_valornulo.py
#
######################################################

