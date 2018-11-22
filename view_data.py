#FOR ME
import findspark
#findspark.init(r'C:\Users\jorge\Anaconda3\pkgs\pyspark-2.3.1-py36_1001\Lib\site-packages\pyspark')
#NEW
findspark.init('/Users/vikalpkamdar/opt/spark')
findspark.find()

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
#df.write.mode('overwrite').parquet("posts.parquet")
data = sqlContext.read.parquet("posts.parquet")

print(data.first())
