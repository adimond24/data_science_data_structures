import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')

df3.info()
df3.head()

df3.plot.scatter(x='a',y='b',s=50,c='red')

df3['a'].hist()

plt.style.use('gplot',alpha=0.5)

df3.[['a','b']].plot.box()

df3['d'].plot.kde(lw=5,ls='--')


f = plt.figure()
df3.ix[0:30].plotarea(alpha = 0.4)

plt.legend(loc='center left', bbox_to_anchor=(1.0,0.5))

plt.show()