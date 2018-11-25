
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)

df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2017-01.bz2').withColumn('year',df.created_utc*0 + 2017).withColumn('month',df.created_utc*0 + 1)
df = df.sample(False,0.1)


for i in range(2012,2017):
    for j in range(1,13):
        path = ""
        #save_path=""
        if j<10:
            path = 'hdfs:///user/difernan/data/' + str(i) + '_RC_' + str(i) + '-0' + str(j) + '.parquet'
            #save_path = str(i) + '_RC_' + str(i) + '-0' + str(j)
        else:
            path = 'hdfs:///user/difernan/data/' + str(i) + '_RC_' + str(i) + '-' + str(j) + '.parquet'
            #save_path = str(i) + '_RC_' + str(i) + '-' + str(j)
        df_new = sqlc.read.parquet(path)
        df_new = df_new.withColumn('year',df_new.created_utc*0 + i).withColumn('month',df_new.created_utc*0 + j)
        df_new = df_new.sample(False,0.1)
        df = df.union(df_new)

df.write.mode('overwrite').parquet('2012_2016_sampled.parquet')
