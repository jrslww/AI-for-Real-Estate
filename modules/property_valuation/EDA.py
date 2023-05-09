# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed data
df = pd.read_csv('data/property_data.csv')

# Print out a summary of the data
print(df.describe())

# Visualize the distribution of the target variable (sale_price_usd)
plt.figure(figsize=(10,6))
sns.histplot(df['sale_price_usd'], kde=True)
plt.title('Distribution of Sale Price')
plt.show()

# Visualize the correlation matrix
corr_matrix = df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Scatter plot of size vs sale_price_usd
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='size_sqft', y='sale_price_usd')
plt.title('Size vs Sale Price')
plt.show()

# Boxplot of condition vs sale_price_usd
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='condition', y='sale_price_usd')
plt.title('Condition vs Sale Price')
plt.show()

# And so on for other variables and combinations of variables...
