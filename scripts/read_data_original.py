from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql import SparkSession
from pyspark import SparkContext
'''
Script functionality:
With this script we obtain a parquet file containing a sample (10% of the total)
of the 2016 data.
'''

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)
df = sqlc.read.json('hdfs:///datasets/reddit_data/2016/RC_2016-*.bz2')
df = df.sample(False,0.1)
df.write.mode('overwrite').parquet("sample2016.parquet")
