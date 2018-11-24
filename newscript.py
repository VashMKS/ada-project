
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext
sqlc = SQLContext(sc)

from pyspark.sql.types import *

cSchema = StructType([StructField("WordList", ArrayType(StringType()))])

# notice extra square brackets around each element of list
test_list = [['Hello', 'world']], [['I', 'am', 'fine']]

df = spark.createDataFrame(test_list,schema=cSchema)

#df = sqlc.read.json('hdfs:///datasets/reddit_data/2017/RC_2017-01.bz2')
#df_spark_slice = df_spark.sample(False,0.01)
df.write.mode('overwrite').parquet('2017_01.parquet')
