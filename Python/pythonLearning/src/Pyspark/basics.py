from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("PySparkTutorial").getOrCreate()

data = [("James", "", "Smith", "36636", "M", 3000),
        ("Michael", "Rose", "", "40288", "M", 4000),
        ("Robert", "", "Williams", "42114", "M", 4000),
        ("Maria", "Anne", "Jones", "39192", "F", 4000),
        ("Jen", "Mary", "Brown", "", "F", -1)
       ]

columns = ["first_name", "middle_name", "last_name", "dob", "gender", "salary"]
df = spark.createDataFrame(data, columns)

# Display the DataFrame and its schema
df.show()
df.printSchema()