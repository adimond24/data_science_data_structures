import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
customers = pd.read_csv('Ecommerce Customers')

sns.jointplot(data=customers,x='Time on Website', y='Yearly Amount Spent')
sns.jointplot(data=customers, x='Time on App')

sns.jointplot(x='Time on App', y='Length of Membership',kind='hex',data=customers)
sns.pairplot(customers)

#length of membership
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)

y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website','Length of Membership' ]]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)
predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
plt.xlabel('Y Test (True Values)')
plt.ylabel('Predicted Values')

print('MAE', metrics.mean_absolute_error(y_test,predictions))
print('MSE', metrics.mean_squared_error(y_test,predictions))
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test,predictions)))

metrics.explained_variance_score(y_test,predictions)
sns.distplot((y_test-predictions), bins=50)

cdf = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])



