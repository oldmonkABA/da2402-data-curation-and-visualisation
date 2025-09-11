import numpy as np
import random
import pandas as pd
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://ecomuser:Ecomuser#123@localhost/ecom")
df = pd.read_sql("SELECT * FROM customers LIMIT 5", engine)
print(df)
sql="SELECT\
  p.product_id,\
  p.product_name,\
  SUM(p.price) AS revenue,\
  ROUND(100 * SUM(p.price) / NULLIF(SUM(SUM(p.price)) OVER (), 0), 2) AS pct_of_total \
FROM orders o \
JOIN products p ON p.product_id = o.product_id \
GROUP BY p.product_id, p.product_name \
ORDER BY revenue DESC, p.product_id;"
print(sql)
#exit()
df = pd.read_sql(sql, engine)
print(df)
