from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql import SparkSession
from pyspark import SparkContext
'''
Script functionality:
With this script we obtain a parquet file containing the sample that we are
using locally. We sample the 10% of the original data in "posts.parquet" (which
was obtained previously).
'''

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext
sqlc = SQLContext(sc)

# WARNING: make sure that your username is correct before running the script

# username
user = 'difernan'

# paths in the local file system of the cluster
path_local = 'home/' + user + '/'

# paths in the hadoop file system
hdfs  = 'hdfs:///'
path_hdfs = hdfs + 'user/' + username + '/'
hdfs_dataset = hdfs + 'datasets/reddit_data/'

# read the parquet file
df_spark = sqlc.read.parquet(path_hdfs + "posts.parquet")

# sample 10% of the data
df_spark_slice = df_spark.sample(False,0.1)

# save the sample as another parquet file
df_spark_slice.write.mode('overwrite').parquet("sample_2017_01.parquet")
