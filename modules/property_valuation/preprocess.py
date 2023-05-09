## Import required libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

## Load the data
df = pd.read_csv('data/property_data.csv')

## Handle missing values - this dataset doesn't have any missing values,
## but if it did, you could fill them in with df.fillna(),
## drop them with df.dropna(), or use some imputation method
## For simplicity, let's assume there are no missing values in our data

## Handle outliers - this depends heavily on the data and the domain
## For simplicity, let's assume there are no significant outliers in our data

## Encode categorical data
categorical_features = ['location', 'condition']
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)])

## Fit and transform the data
df = preprocessor.fit_transform(df)

## Save the preprocessed data
pd.DataFrame(df).to_csv('data/preprocessed_data.csv', index=False)
