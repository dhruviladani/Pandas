import pandas as pd
from datetime import datetime
import numpy as np

df = pd.read_json('users.json')

# print(df)

# df = pd.json_normalize(df.to_dict(orient='records'))

df[['last_login', 'hours_used']] = df['usage'].apply(pd.Series)

df.drop(columns='usage', inplace=True)

print(df)

print('---------------------')

df['last_login'] = pd.to_datetime(df['last_login'])

df['signup_date'] = pd.to_datetime(df['signup_date'])

# df = np.count_nonzero(df['signup_date'] > currunt_date )

df['account_age_days'] = (datetime.today() - df['signup_date']).dt.days

df = df[(df['is_active'] == True) & (df['hours_used'] > 50)]
print(df)

df.to_parquet('active_users.parquet', index=False)
