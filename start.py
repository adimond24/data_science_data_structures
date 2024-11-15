import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()

sns.distplot(tips['total_bill'], kde=False, bins=30)

sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde')

sns.pairplot(tips,hue='sex',palette='coolwarm')

sns.rugplot(tips['total_bill'])

sns.distplot(tips['total_bill'], kde=False)