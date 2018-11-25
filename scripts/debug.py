from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext
sqlc = SQLContext(sc)
'''
Script functionality: Just checking we can use read parquet in the cluster. 
'''
# username
user = 'difernan'

# paths in the local file system of the cluster
path_local = '/home/' + user + '/'

# paths in the hadoop file system
hdfs  = 'hdfs:///'
path_hdfs = hdfs + 'user/' + username + '/'
path_dataset = hdfs + 'datasets/reddit_data/'

df = spark.read.parquet(path_hdfs + "sampled_dataset_2012_2016.parquet")
