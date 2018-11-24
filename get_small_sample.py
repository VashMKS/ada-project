from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext
sqlc = SQLContext(sc)

# WARNING: make sure that your usernam,e is correct befire running the script

# username
user = 'difernan'

# paths in the local file system of the cluster
path_local = '/home/' + user + '/'

# paths in the hadoop file system
hdfs  = 'hdfs:///'
path_hdfs = hdfs + 'user/' + username + '/'
path_dataset = hdfs + 'datasets/reddit_data/'

# read data for January 2017 into a spark dataframe
df = sqlc.read.json(path_dataset + '/2017/RC_2017-01.bz2')

# sample 10% of the data
df_spark_slice = df_spark.sample(False,0.01)

# create a parquet file with the sample on the user's hdfs
df.write.mode('overwrite').parquet("data_2017_01.parquet")
