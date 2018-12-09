from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql import SparkSession
from pyspark import SparkContext
'''
Script functionality:
With this script we obtain a parquet file containing a sample (10% of the total)
of the 2016 data.
'''

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)
df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2016-*.bz2')

to_drop = ['author_flair_css_class','author_flair_text','distinguished','edited','retrieved_on','stickied','subreddit_id']

df_reduced = df.drop(*to_drop)
#df = df.sample(False,0.1)
df.write.mode('overwrite').parquet("full_reduced_dataet_2016.parquet")
