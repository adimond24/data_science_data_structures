from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import plotly as plt
import cufflinks as cf
sns.set_style('whitegrid')
cf.go_offline()

start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

BAC = data.DataReader('BAC','google',start,end)
C = data.DataReader('C','google',start,end)
GS = data.DataReader('GS','google',start,end)
JPM = data.DataReader('JPM','google',start,end)
MS = data.DataReader('MS','google',start,end)
WFC = data.DataReader('WFC','google',start,end)

tickers = ['BAC','C','GS','JPM','MS','WFC']

bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=tickers)

bank_stocks.columns.names= ['Bank Ticker', 'Stock Info']
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

#returns
returns = pd.DataFrame()
for tick in tickers:
    returns[tick+'Return'] = bank_stocks[tick]['Close'].pct_change()

sns.pairplot(returns[1:])

returns.idxmin()
returns.idxmax()

#standard deviation
returns.std()
returns.ix['2015-01-01':'2015-12-31'].std()

#distplot
sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=50)

sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'], color='red',bins=50)

#line plot
for tick in tickers:
    bank_stocks[tick]['Close'].plot(label=tick,figsize=(12,3))
plt.legend()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()

#moving averages
BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 day moving average')
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC Close')
plt.legend()

#heat map close prices
sns.heatmap(
bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
sns.clustermap(
bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

#final optional part

close_corr = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()

close_corr.iplot(kind='heatmap',colorscale='rdylbu')

bac15 = BAC[['Open','High','Low','Close']].ix['2015-01-01':'2016-01-01']
bac15.iplot(kind='candle')

#sma
MS['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,25,55])

BAC['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='boll')




