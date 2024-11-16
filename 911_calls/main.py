import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
df.info()
df.head()
df['zip'].value_counts().head(5)
df['twp'].value_counts().head(5)
df['title'].nunique()
x = df['title'].iloc[0]
x.split(':')[0]
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

df['Reason'].value_counts()
sns.countplot(x='Reason',data=df,palette='virdius')


df['timeStamp'] = pd.to_datetime(df['timeStamp'])
time = df['timeStamp'].iloc[0]

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

sns.countplot(x='Day of Week', data=df,hue='Reason',palette='viridis')
byMonth = df.groupby('Month').count()
byMonth.head()
byMonth['lat'].plot()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

t = df['timeStamp'].iloc[0]
df['Date'] = df['timeStamp'].apply(lambda t:t.date())
df.groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.show()

df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.tight_layout()

df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.tight_layout()

df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.tight_layout()

dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
sns.heatmap(dayHour,cmap='viridis')

sns.clustermap(dayHour,cmap='viridis')


