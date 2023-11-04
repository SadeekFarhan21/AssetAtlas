import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dhhagan/stocks/master/scripts/stock_info.csv')
df[df['Exchange'] == 'NYSE']
df[df['Exchange'] == 'NASDAQ']