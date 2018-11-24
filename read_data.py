
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)
#df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2017-01.bz2')

df = sqlc.read.parquet('hdfs:///user/difernan/data/*.parquet')#.sample(False,0.1)
df = df.sample(False,0.1)
df.write.mode('overwrite').parquet('/home/difernan/data/2012_2016_sampled.parquet')


#for i in range(2012,2017):
#    for j in range(1,13):
#        path = ""
#        #save_path=""
#        if j<10:
#            path = 'hdfs:///user/difernan/data/' + str(i) + '/RC_' + str(i) + '-0' + str(j) + '.bz2'
#            save_path = str(i) + '_RC_' + str(i) + '-0' + str(j)
#        else:
#            path = 'hdfs:///user/difernan/data/' + str(i) + '/RC_' + str(i) + '-' + str(j) + '.bz2'
#            save_path = str(i) + '_RC_' + str(i) + '-' + str(j)
#        df = sqlc.read.parquet(path)
        #df.write.mode('overwrite').parquet('data/' + save_path + '.parquet')
        #print('Year: ' + str(i) + '     ' + 'month: ' + str(j) + ' saved.')

#df.write.mode('overwrite').parquet("/home/difernan/data/sample2017.parquet")
#df.write.mode('overwrite').parquet("/home/kamdar/posts.parquet")
