from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext
sqlc = SQLContext(sc)

# paths
path_didac = 'difernan/data'
path_jorge = 'josanche/data'
path_vik   = 'kamdar/data'
path_hdfs  = 'hdfs:///'
hdfs_didac = path_hdfs + 'user/' + path_didac
hdfs_jorge = path_hdfs + 'user/' + path_jorge
hdfs_vik   = path_hdfs + 'user/' + path_vik
path_dataset = 'hdfs:///datasets/reddit_data/'

# read data for January 2017
df = sqlc.read.json(path_dataset + '/2017/RC_2017-01.bz2')

#
df.write.mode('overwrite').parquet("/home/difernan/data/sample2017.parquet")
df.write.mode('overwrite').parquet("/home/kamdar/posts.parquet")
