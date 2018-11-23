#FOR ME
#import findspark
#findspark.init(r'C:\Users\jorge\Anaconda3\pkgs\pyspark-2.3.1-py36_1001\Lib\site-packages\pyspark')
#NEW
#findspark.init('/Users/vikalpkamdar/opt/spark')
#findspark.find()

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

#import pandas as pd

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)
#df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2017-01.bz2')
df_spark = sqlc.read.parquet("hdfs:///user/kamdar/posts.parquet")

df_spark_slice= df_spark.sample(False,0.1)

df_spark_slice.write.mode('overwrite').parquet("sliced_2017_posts.parquet")
