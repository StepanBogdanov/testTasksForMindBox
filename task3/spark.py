from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Products and Categories").getOrCreate()

products = spark.createDataFrame([
    (1, "product1"),
    (2, "product2"),
    (3, "product3"),
    (4, "product4")
], ["product_id", "product_name"])

categories = spark.createDataFrame([
    (1, "category1"),
    (2, "category2"),
    (3, "category3")
], ["category_id", "category_name"])

product_category = spark.createDataFrame([
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 1),
    (3, 3)
], ["product_id", "category_id"])

products.createOrReplaceTempView("products")
categories.createOrReplaceTempView("categories")
product_category.createOrReplaceTempView("product_category")

result = spark.sql(
    "SELECT p.product_name, c.category_name \
    FROM products p \
    LEFT JOIN product_category pc USING(product_id) \
    LEFT JOIN categories c USING(category_id)"
)

result.show()