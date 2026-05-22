CREATE OR REFRESH MATERIALIZED VIEW supply_chain_live2.gold.dim_customer
COMMENT "dim customer  duplicated - gold layer" AS
SELECT 
    customer_id,
    MAX_BY(customer_fname, order_date) AS first_name,
    MAX_BY(customer_lname, order_date) AS last_name,
    MAX_BY(customer_country, order_date) AS country
FROM 
    supply_chain_live2.silver.supply_chain_obt
GROUP BY
    customer_id
ORDER BY
    customer_id;
