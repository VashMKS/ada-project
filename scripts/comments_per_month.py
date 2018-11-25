# Imports working with the cluster
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

from pyspark.sql.functions import lit

import pyspark.sql.functions as F

# Spark configurations
spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)

df_spark = spark.read.parquet("sampled_reduced_col_2016.parquet")

to_drop = ['author','body','created_utc','gilded','id','link_id','parent_id','score','subreddit']

df_spark_reduced = df_spark.drop()
