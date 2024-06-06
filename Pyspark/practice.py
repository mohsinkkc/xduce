# Import required modules
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("SplitRowsByDelimiter").getOrCreate()

# Create an RDD with sample data
rdd = spark.sparkContext.parallelize(["foo\tbar\tbaz","hello\tworld"])

# Define the delimiter
delimiter = "\t"

# Split the rows by the delimiter
split_data = rdd.map(lambda row: row.split(delimiter))

# Print the resulting RDD
for row in split_data.collect():
	print(row)
