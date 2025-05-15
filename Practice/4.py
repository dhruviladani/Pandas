import pandas as pd
import numpy as np 
df = pd.read_csv('employee_extended.csv')
print(df)

unique = df['department'].unique()
print(unique)

df['department'] = df['department'].str.lower()

df['department'] = df['department'].str.strip()

newunique = df['department'].unique()
print(newunique)

# # df['salary'] = df['salary'].fillna(df['salary'].mean())

# df['joining_date'] = pd.to_datetime(df['joining_date'])
# emp_before2020 = df[df['joining_date'].dt.year < 2020]

# print(df)
# print(emp_before2020)

# shorted_df = df.sort_values(by=['training_score', 'leaves_taken'],
#                            ascending=[False, True])
# # shorted_df = df.sort_values(by = ['leaves_taken'], ascending=[True])
# print(shorted_df)

##########



# missing_cnts = df.isnull().sum()

# print(missing_cnts)



# missing_cnts_per = (df.isnull().mean() * 100).round(2)

# print(missing_cnts_per)

# missing_summary = pd.DataFrame({
#     'missing values' : missing_cnts,
#     'missing % ' : missing_cnts_per
# })

# print(missing_summary)


# df['salary_category'] = np.where(df['salary'] < 55000,
#                                 'Low') or np.where(55000 < df['salary'] < 60000,
#                                                    'Medium') or np.where(df['salary'] > 60000,
#                                                                          'High')

# print(df)

conditions = [
    df['salary'] < 55000,
    (df['salary'] >= 55000) & (df['salary'] <= 60000),
    df['salary'] > 60000
]

choices = ['Low', 'Medium', 'High']

df['salary_category'] = np.select(conditions, choices, default='Unknown')



df['joining_date'] = pd.to_datetime(df['joining_date'])

df['years_in_company'] = ((pd.to_datetime('2025-05-11') - df['joining_date']).dt.days / 365).round(2)
df['years_in_company'] = (2025 - df['joining_date'].dt.year )


a = df[df['years_in_company']>3]
print(a)
pd.set_option('display.max_columns', None)

filtered_df = df.query(
                "(gender == 'M') and (department in ['it', 'hr']) and (training_score > 80) and (salary_category == 'High')"
)

print(filtered_df)
