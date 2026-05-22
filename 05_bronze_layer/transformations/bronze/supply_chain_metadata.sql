CREATE OR REFRESH STREAMING TABLE supply_chain_demo_cat.bronze.metadata
COMMENT "Raw metadate for DataCo" AS
SELECT *
FROM STREAM read_files("/Volumes/supply_chain_demo_cat/default/raw/metadata",
format => "csv", 
header => true,
inferSchema => true
) 