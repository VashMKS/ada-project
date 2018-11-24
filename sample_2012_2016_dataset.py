from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext
sqlc = SQLContext(sc)

df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2017-01.bz2').withColumn('year',2017).withColumn('month',1)
df = df.sample(False,0.1)

# sample 10% data for each month from 2012 to 2016 (both included)
for i in range(2012,2017):
    for j in range(1,13):
        path = ""
        if j<10:
            path = 'hdfs:///user/difernan/data/' + str(i) + '_RC_' + str(i) + '-0' + str(j) + '.parquet'
        else:
            path = 'hdfs:///user/difernan/data/' + str(i) + '_RC_' + str(i) + '-' + str(j) + '.parquet'
        df_new = sqlc.read.parquet(path).withColumn('year',i).withColumn('month',j)
        df_new = df_new.sample(False,0.1)
        df = df.union(df_new)

# store all the sampled data in a parquet file
df.write.mode('overwrite').parquet('/home/difernan/sample_2012_2016.parquet')
