CREATE OR REFRESH STREAMING TABLE supply_chain_live2.bronze.metadata
COMMENT "Raw metadata - bronze layer" AS
SELECT *
FROM STREAM read_files("/Volumes/supply_chain_live2/default/raw/metadata",
format => "csv", 
header => true,
inferSchema => true
) 