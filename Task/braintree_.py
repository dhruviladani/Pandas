import pandas as pd
import numpy as np

df = pd.read_csv("files/braintree_.csv")

# df.insert(column= "Country", )

country = ['US','IntI']
df["Country"] = np.random.choice(country, size=len(df))

df

data = df[df['Month'] == 1]

pivot = df.pivot_table(
    data,
    
    index= ["Country", "Response"],
    columns= ['Year', 'Month'],
    aggfunc= {'Response': ['count']}
)

pivot


sub_total = pd.concat([
    df._append( df.sum().rename((k, 'Total')))
    for k, df in pivot.groupby(level=0)
])

sub_total


approved_total = pivot.xs('Approved', level=1).sum().rename(('','Approved Total'))
declined_total = pivot.xs('Declined', level=1).sum().rename(('','declined Total'))

grand_total = pivot.sum().rename(('Grand Total', 'Grand Total')).to_frame().T

grand_total

summary_rows = pd.concat([
    approved_total.to_frame().T,
    declined_total.to_frame().T,
    
])

summary_rows

final_table = pd.concat([sub_total, summary_rows, grand_total])

final_table

##
declined_ratio = (declined_total / (approved_total + declined_total) * 100).rename(('Declined Ratio', ''))

sub_total = pd.concat([
    pd.concat([
        df,
        df.sum().rename((k, 'Total')).to_frame().T,
        (df.xs('Declined', level=1).sum() / df.sum() * 100).rename((k, 'Decline Ratio')).to_frame().T 
    ])
    for k, df in pivot.groupby(level=0)
])

# sub_total.index = pd.MultiIndex.from_tuples(sub_total.index)

sub_total

grand_declined_ratio = (declined_total.sum() / grand_total.sum() * 100).rename(('Grand', 'Declined Ratio')).to_frame().T

final_table = pd.concat([sub_total, summary_rows, grand_total, grand_declined_ratio])

final_table
