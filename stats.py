from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min

from pyspark.sql import SparkSession
from pyspark import SparkContext

from pyspark.sql.functions import lit

import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

sqlc = SQLContext(sc)

df_spark = spark.read.parquet("sampled_reduced_col_2016.parquet")

#f = open('/home/kamdar/stats.txt','w+')

'''
total_n_comments = df_spark.count()
print("Total number of comments: {}".format(str(total_n_comments)))
f.write("Total number of comments: {} \n".format(str(total_n_comments)))

n_deleted_comments = df_spark.filter('body = "[deleted]"').count()
print("Number of deleted comments: {}".format(str(n_deleted_comments)))
f.write("Number of deleted comments: {} \n".format(str(n_deleted_comments)))

percentage_deleted_comments = 100 * n_deleted_comments  / total_n_comments
print("% of deleted comments: {}".format(str(percentage_deleted_comments)))
f.write("% of deleted comments: {} \n".format(str(percentage_deleted_comments)))

comments_by_removed_users = df_spark.filter('author = "[deleted]"').count()
print("Number of comments by removed users: {}".format(str(comments_by_removed_users)))
f.write("Number of comments by removed users: {} \n".format(str(comments_by_removed_users)))

percentage_by_dl_user = 100 * comments_by_removed_users / total_n_comments
print("% comments by deleted users: {}".format(str(percentage_by_dl_user)))
f.write("% comments by deleted users: {} \n".format(str(percentage_by_dl_user)))

n_controversial_comments = df_spark.filter('controversiality = 1').count()
print("Number of controversial comments: {}".format(str(n_controversial_comments)))
f.write("Number of controversial comments: {} \n".format(str(n_controversial_comments)))

perc_controversial_comments = 100 * n_controversial_comments / total_n_comments
print("% of controversial comments: {}".format(str(perc_controversial_comments)))
f.write("% of controversial comments: {} \n".format(str(perc_controversial_comments)))


total_n_subreddits = df_spark[['subreddit']].distinct().count()
print("Number of subreddits: {}".format(str(total_n_subreddits)))
f.write("Number of subreddits: {}".format(str(total_n_subreddits)))

df_subreddit_count = df_spark.groupBy('subreddit').agg(count('*')).select('*',F.col('count(1)').alias('Number of comments')).drop('count(1)')#.withColumnRenamed('count(1)', 'Number of comments')
df_subreddit_count.write.mode("overwrite").parquet("df_subreddit_count.parquet")


df_controversial_per_subr_count = df_spark.filter('controversiality = 1').groupBy('subreddit').agg(count('*')).select('*',F.col('count(1)').alias('N_controversial_comments')).drop('count(1)')#.withColumnRenamed('count(1)', 'N controversial comments')
df_controversial_per_subr_count.write.mode("overwrite").parquet("df_controversial_per_subr_count.parquet")
'''

df_created_utc = df_spark[['created_utc']].orderBy(asc('created_utc'))
df_created_utc.write.mode("overwrite").parquet("df_created_utc.parquet")


#f.close()
