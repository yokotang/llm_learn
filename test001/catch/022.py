import pandas as pd
import numpy as np

data = {
    'OrderID': ['ORD-1001', 'ORD-1002', 'ORD-1003', 'ORD-1003', 'ORD-1005', 'ORD-1006', np.nan, 'ORD-1008', 'ORD-1009'],
    'Customer_Name': [' Alice Smith ', 'Bob Jones', 'Charlie', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry_W'],
    'Age': [25, 34, -5, -5, 120, 29, 45, np.nan, 200],
    'Signup_Date': ['2023-01-01', '01/02/2023', '2023.01.03', '2023.01.03', 'Not Date', '2023-01-06', '2023-01-07', '2023-01-08', '2023/01/09'],
    'Product_Price': ['$100.50', '200.00', 'USD 150', 'USD 150', '300.5', '$50.00', '120', None, '1,000.00'],
    'Category': ['Electronics', 'Home', 'Electronics', 'Electronics', 'Unknown', 'home', 'Garden', 'Garden', 'Books']
}

df = pd.DataFrame(data)
print("=== 原始脏数据预览 ===")
print(df)
print(f"清洗前总行数: {len(df)}")
# 删除完全重复的行，保留第一次出现的
df_cleaned = df.drop_duplicates(keep='first')
# 基于OrderID进行去重，假设订单ID应唯一
df_cleaned = df_cleaned.drop_duplicates(subset=['OrderID'], keep='first')
print(f"去重后行数: {len(df_cleaned)}")
print(df_cleaned)