import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()

sns.jointplot(x='fare', y='age', data=titanic)
sns.distplot(titanic['fare'], kde=False,color='red',bins=30)

sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')

sns.countplot(x='sex',data=titanic)

sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')

g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist,'age')

