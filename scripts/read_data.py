from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SQLContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)

df = spark.read.parquet("hdfs:///user/kamdar/data/sample2016.parquet")
df = df.sample(False,0.1)
df.write.mode("overwrite").parquet("sample2016_1.parquet")
