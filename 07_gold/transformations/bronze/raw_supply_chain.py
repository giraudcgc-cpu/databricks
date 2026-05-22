from pyspark import pipelines as dp

BASE_DIR = "/Volumes/supply_chain_live2/default/raw"

schema = (spark.read.format("csv").options(header=True, inferSchema=True).load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv").schema)

# catalog.schema.volume
@dp.table(name="supply_chain_live2.bronze.raw_supply_chain", 
          comment="Raw supply chain live2 ", 
          table_properties={
              "delta.columnMapping.mode": "name",
              "delta.minReaderVersion": "2",
              "delta.minWriterVersion": "5"
          })
def raw_supply_chain():
    return spark.readStream.format("csv").options(header=True, encoding="latin1").schema(schema).load(f"{BASE_DIR}/data")

