import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


df = pd.read_csv("Task/files/qa.csv")
df.columns = df.columns.str.upper() 


connection = snowflake.connector.connect(
    user='project',
    password='Project@123456',
    account='NKXAMJR-FUB34596',
    warehouse='COMPUTE_WH',
    role='ACCOUNTADMIN'
)

c = connection.cursor()

c.execute("create database if not exists demo")
c.execute("use database demo")

c.execute("create schema if not exists demo_data")
c.execute("use schema demo_data")

c.execute('''
    create table if not exists DEMO_TABLE (
        CANCELED_YEAR STRING,
        CANCELED_MONTH STRING,
        HOLD_REASON STRING,
        CONFIRMED_FRAUD STRING,
        MISSING_ESCALATION STRING,
        PAYMENT_METHOD STRING,
        LATEST_BUYER_PRICE STRING
    )
''')

write_pandas(connection, df, table_name="DEMO_TABLE")
