import pandas as pd
import datetime
df = pd.read_csv('Practice/attendance.csv')

print(df)

df = df.drop_duplicates()

df = df.dropna(subset=['emp_id', 'status'])

df['status'] = df['status'].str.lower()

df['date'] = pd.to_datetime(df['date'])

df = df.dropna(subset=['date'])

print(df)
pivot = df.pivot_table(index=['emp_id','name'],
                       columns='status',
                       aggfunc='size',
                       fill_value=0).reset_index()

pivot['total_days'] = pivot[['present', 'absent']].sum(axis=1)

print(pivot)
