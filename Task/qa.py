import pandas as pd

df = pd.read_csv("files/qa.csv")

df

# grouping = df.groupby(['hold_reason', 'confirmed_fraud']).agg(
#     fraud_count = ('confirmed_fraud','count'),
#     latest_buyer_price = ('latest_buyer_price', 'sum')
# )

# grouping

pivot = df.pivot_table(
    df,
    index=["hold_reason", "confirmed_fraud"], 
    columns=["canceled_year","canceled_month"], 
    # values=["confirmed_fraud","latest_buyer_price"] ,
    aggfunc= {"confirmed_fraud":"count","latest_buyer_price" : "sum"}, dropna=False, fill_value=0 )

pivot = pivot.rename(columns={"confirmed_fraud":"fraud_count"})

pivot
