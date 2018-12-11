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

import numpy as np
import pandas as pd

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)

df_spark = spark.read.parquet('hdfs:///user/kamdar/full_reduced_sentiment_dataset_2017.parquet')

df_subreddit_users = df_spark.select('subreddit','author','id').groupby('subreddit') \
                                .agg(collect_set('author').alias('users'),count('id').alias('number_of_posts')) \
                                .filter('number_of_posts > 1000')
                                .orderBy(asc('subreddit'))

df = df_subreddit_users.toPandas()

adjacency_matrix = np.zeros([df.shape[0],df.shape[0]])

for i in range(df.shape[0]):
    for j in range(df.shape[0]):
        if i == j:
            adjacency_matrix[i,j] = 0
        else:
            subb1_users = set(df.iloc[i]['users'])
            subb2_users = set(df.iloc[j]['users'])
            n_common_users = len(subb1_users.intersection(subb2_users))
            adjacency_matrix[i,j] = n_common_users

df_adj = pd.DataFrame(adjacency_matrix)
df_adj.to_csv('/home/kamdar/adjacency_matrix_2017.csv')
