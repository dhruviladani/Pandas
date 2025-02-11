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

# dfsum = df.groupby('dibs_U_id', as_index=False).sum()
# dfsum['status'] = 'Total'
# dfsum

# pivot = pivot._append(df)

pivot



# table = df.pivot_table(df, values=['SalesToday', 'SalesMTD','SalesYTD'],\
#                      rows=['State'], cols=['City'], aggfunc=np.sum, margins=True)



# format = df.groupby("dibs_U_id").apply(lambda sub_df:
#     sub_df.pivot_table(index=[ "status"], columns= ["Year", "Month"], aggfunc='count', margins=True, dropna= False, fill_value=0))

# format

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



#########################


pivot = df.pivot_table(
    df,
    index= ["dibs_U_id", "status"],
    columns= ["Year", "Month"],
    aggfunc={"status":['count']}, dropna= False, fill_value=0
)

pivot



sub_total = pd.concat([
    df._append( df.sum().rename((k, 'Total')))
    for k, df in pivot.groupby(level=0)
])._append(pivot.sum().rename(('Grand', 'Total')))

sub_total

# grand_total = pd.concat([
    
# ])

# grand_total

approved_total = pivot.xs('Approved', level=1).sum().rename(('Approved Total', ''))
canceled_total = pivot.xs('Canceled', level=1).sum().rename(('Canceled Total', ''))
rejected_total = pivot.xs('Rejected', level=1).sum().rename(('Rejected Total', ''))

# Compute Grand Total
grand_total = pivot.sum().rename(('Grand', 'Total')).to_frame().T

grand_total


summary_rows = pd.concat([
    approved_total.to_frame().T,
    canceled_total.to_frame().T,
    rejected_total.to_frame().T
])


# Final table with summary rows and Grand Total
final_table = pd.concat([sub_total, summary_rows, grand_total])


final_table



# total_per_user = pd.concat([
#     pd.concat([df, df.sum().to_frame().T.assign(dibs_U_id=k, status='Total')])
#     for k, df in pivot.groupby(level=0)
# ])

# total_per_user
