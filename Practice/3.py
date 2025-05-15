import pandas as pd
import numpy as np
df = pd.read_csv('employee_performance.csv')

# print(df)

# print(type(df['joining_date']))

df['joining_date'] = pd.to_datetime(df['joining_date'])

y = df['joining_date'].dt.year
m = df['joining_date'].dt.month
print(y)
print(m)

mean_sal=df.groupby('department')['salary'].mean()
mean_per_rating=df.groupby('department')['performance_rating'].mean()
mean_leaves=df.groupby('department')['leaves_taken'].sum()

print(mean_sal)
print(mean_per_rating)
print(mean_leaves)

a = df[df['joining_date'].dt.year < 2020]
b = df[df['performance_rating'] >= 4]
c = df[(df['department'] == 'IT') & (df['salary'] > 55000)]
print(a)
print(b)
print(c)

# df['bonus'] =  df.apply(lambda r : r['salary'] * 0.10 if [df['performance_rating'] >= 4 ] 
#                         else r['salary'] * 0.05 , axis=1)

#or 

df['bonus'] = np.where(df['performance_rating'] >= 4,
                       df['salary'] * 0.10,
                       df['salary'] * 0.05)

print(df)

sorted_df = df.sort_values(by=['performance_rating', 'leaves_taken'],
                           ascending=[False, True])

print(sorted_df)
# for i in range(0,len(df['emp_id'])):
#     if df['joining_date'].dt.year < 2020:
#         print(df['name'])
