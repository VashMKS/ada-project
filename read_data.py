
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)
df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2017-01.bz2')
df.write.mode('overwrite').parquet("/home/kamdar/posts.parquet")
