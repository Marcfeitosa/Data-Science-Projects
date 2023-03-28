from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Define a nossa aplicação Spark
spark = SparkSession \
    .builder \
    .appName("StructuredStreamingStackApp") \
    .getOrCreate()
    
# Nome do arquivo para schema
arquivo = "/Users/rodrigosantanaferreira/data/landing/2010-summary.json"

# Diretório com os arquivos jsons
diretorio = "/Users/rodrigosantanaferreira/data/landing"

# Ler o arquivo para definir o schema
df = spark.read.json(arquivo)
schema_df = df.schema

# Imprime o schema do dataframe
df.printSchema()

# Lendo os arquivos e cria o dataframe em streaming
df_streaming = spark.readStream \
    .schema(schema_df) \
    .option("maxFilesPerTrigger", "1") \
    .json(diretorio)

# Processa os dados em streaming
resultado = df_streaming.groupBy("ORIGIN_COUNTRY_NAME").sum("count")

# Escreve a saida do processamento para o console
saida = resultado.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()
    
# Imprime o resultado até que a aplicação seja encerrada
saida.awaitTermination()