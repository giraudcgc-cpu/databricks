from pyspark import pipelines as dp 
from pyspark.sql.functions import coalesce, lit, when, col, to_timestamp
from utils.utils import rename_columns_to_snake_case

@dp.table(
    name="supply_chain_live2.silver.supply_chain_obt",
    comment= "Cleaned supply chain live2 data",
    table_properties={
    "delta.columnMapping.mode": "name",
    "delta.minReaderVersion":"2",
    "delta.minWriterVersion":"5"   
    }
)

def cleaned_supply_chain():
    df = spark.sql("FROM STREAM supply_chain_live2.bronze.raw_supply_chain")
    df = rename_columns_to_snake_case(df)

    return (
        df.withColumn(
            "shipping_date", to_timestamp("shipping_date_(dateorders)", "M/d/yyyy H:mm")
        )
        .withColumn(
            "order_zipcode",
            coalesce(col("order_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "customer_zipcode",
            coalesce(col("customer_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "customer_country",
            when(col("customer_country") == "EE. UU.", "United States").otherwise(
                col("customer_country")
            ),
        )
        .withColumn(
            "order_date",
            to_timestamp("order_date_(dateorders)", "M/d/yyyy H:mm"),
        )
    ).drop(
        "customer_email",
        "customer_password",
        "product_description",
        "shipping_date_(dateorders)",
        "order_date_(dateorders)",
    )
