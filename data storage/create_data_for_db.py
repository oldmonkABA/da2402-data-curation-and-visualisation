import numpy as np
import random
import pandas as pd
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://ecomuser:Ecomuser%23123@localhost/ecom")
n=100
m=50
k=4000
locations=['Delhi','Mumbai','Chennai','KolKata','Bangalore']

customers=[i for i in range(1,n+1)]
products=[i for i in range(1,m+1)]
orders=[i for i in range(1,k+1)]

customer_data = {
    'customer_id':customers,
    'name': [f'Customer_{i}' for i in range(1, n+1)],
    'email':[f'c_{i}@gmail.com' for i in range(1,n+1)],
     'place':np.random.choice(locations,n,replace=True)
}
df_customer=pd.DataFrame(customer_data)
'''
df_customer.to_sql(
    "customers",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000,
    method="multi"     # efficient executemany
)
'''
#exit()
product_type=['Snacks','Sweets','Cold Drinks','Hot Drinks']
product_data = {
    'product_id':products,
    'product_name': [f'P_{i}' for i in range(1, m+1)],
    'price':np.random.normal(1000, 50, m),
    'description':np.random.choice(product_type, m,replace=True)
}
#print(product_data)
df_product=pd.DataFrame(product_data)
'''
df_product.to_sql(
    "products",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000,
    method="multi"     # efficient executemany
)
'''

#print(df_product)
base_dates = pd.date_range("2020-01-01", periods=365, freq="D")
order_dates = np.tile(base_dates, k // len(base_dates) + 1)[:k]
order_data={
    
    'customer_id':np.random.choice(customers,k,replace=True),
    'product_id':np.random.choice(products,k,replace=True),
    'order_date':order_dates
}
#print(orders)
df_orders=pd.DataFrame(order_data)
df_orders.to_sql(
    "orders",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000,
    method="multi"     # efficient executemany
)

