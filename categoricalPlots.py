import seaborn as sns
import numpy as np
tips = sns.load_dataset('tips')
tips.head()

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

sns.countplot(x='sex',data=tips)

sns.boxplot(x='day', y='total_bill', data=tips)

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)

sns.stripplot(x='day', y='total-bill',data=tips,jitter=True,hue='sex',split=True)

sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
sns.violinplot(x='day',y='total_bill',data=tips)



