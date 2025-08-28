import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=customers.merge(
        right=orders,
        how='left',
        left_on='id',
        right_on='customerId'
    )
    df=df[df['customerId'].isna()][['name']].rename(columns={'name':'Customers'})
    return df
