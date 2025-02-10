import pandas as pd
import numpy as np

df = pd.read_csv("files/tr_metrics_dataframe_raw.csv")

df

pivot = df.pivot_table(
    df,
    index= ["dibs_U_id", "status"],
    columns= ["Year", "Month"],
    aggfunc={"status":['count']}, dropna= False, fill_value=0
)

# monthly_totals = pivot.sum()
# pivot.loc[('Total', 'All Status'), :] = monthly_totals

# monthly_totals

# pivot["status":['count'].count()]

dfsum = df.groupby('dibs_U_id', as_index=False).sum()
dfsum['status'] = 'Total'
dfsum

pivot = pivot._append(df)

pivot



# table = df.pivot_table(df, values=['SalesToday', 'SalesMTD','SalesYTD'],\
#                      rows=['State'], cols=['City'], aggfunc=np.sum, margins=True)



format = df.groupby("dibs_U_id").apply(lambda sub_df:
    sub_df.pivot_table(index=[ "status"], columns= ["Year", "Month"], aggfunc='count', margins=True, dropna= False, fill_value=0))

format

# df.groupby(['A', 'B', 'C']).apply(lambda sub_df:
#     sub_df.pivot_table(index=['D'], values=['E'], aggfunc='count', margins=True))











# Calculate sums
df_subtotal = df.groupby('dibs_U_id', as_index=False, dropna=True)[['status']].agg('count')
# Manipulate string Patient
# df_subtotal['dibs_U_id'] = df_subtotal['dibs_U_id'] + ' subtotal'
# Join dataframes
df_new = pd.concat([pivot, df_subtotal], axis=0, ignore_index=True)
# Sort
df_new = df_new.set_index('dibs_U_id').sort_values(['dibs_U_id'])

df_new