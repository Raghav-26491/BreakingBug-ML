
# import libraries

# 1. To handle the data
import pandas as pd
import numpy as np

# 2. To Visualize the data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from yellowbrick.cluster import KElbowVisualizer
from matplotlib.colors import ListedColormap
from sklearn.metrics import r2_score
# 3. To preprocess the data
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder   # Error 17
from sklearn.impute import SimpleImputer, KNNImputer

# 4. import Iterative imputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# 5. Machine Learning
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score                     # Error 1

# 6. For Classification task.
from sklearn.linear_model import LogisticRegression                 # Error 2
from sklearn.neighbors import KNeighborsClassifier                  # Error 3
from sklearn.svm import SVC                                         # Error 4
from sklearn.tree import DecisionTreeClassifier, plot_tree          # Error 5
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, RandomForestRegressor     # Error 6
from xgboost import XGBClassifier                                   # Error 7 
from lightgbm import LGBMClassifier                                 # Error 8
from sklearn.naive_bayes import GaussianNB                          # Error 9

# 7. Metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report                     # Error 10

# 8. Ignore warnings
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("dataset.csv")

# print the first 5 rows of the dataframe
df.head()

# Exploring the data type of each column
df.info()

# Checking the data shape
df.shape

# Id column
df['id'].min(), df['id'].max()

# age column
df['age'].min(), df['age'].max()

# lets summarize the age column
df['age'].describe()

import seaborn as sns

# Define custom colors
custom_colors = ["#FF5733", "#3366FF", "#33FF57"]  # Example colors, you can adjust as needed

# Plot the histogram with custom colors
sns.histplot(df['age'], kde=True, color="#FF5733", palette=custom_colors)


# Plot the mean, Median and mode of age column using sns
sns.histplot(df['age'], kde=True)
plt.axvline(df['age'].mean(), color='Red')
plt.axvline(df['age'].median(), color= 'Green')
plt.axvline(df['age'].mode()[0], color='Blue')

# print the value of mean, median and mode of age column
print('Mean', df['age'].mean())
print('Median', df['age'].median())
print('Mode', df['age'].mode())


# plot the histogram of age column using plotly and coloring this by sex

fig = px.histogram(data_frame=df, x='age', color= 'sex')
fig.show()

# Find the values of sex column
df['sex'].value_counts()

# calculating the percentage fo male and female value counts in the data

male_count = 726
female_count = 194

total_count = male_count + female_count

# calculate percentages
male_percentage = (male_count/total_count)*100
female_percentages = (female_count/total_count)*100

# display the results
print(f'Male percentage i the data: {male_percentage:.2f}%')
print(f'Female percentage in the data : {female_percentages:.2f}%')

# Difference
difference_percentage = ((male_count - female_count)/female_count) * 100
print(f'Males are {difference_percentage:.2f}% more than female in the data.')


726/194

# Find the values count of age column grouping by sex column
df.groupby('sex')['age'].value_counts()

# find the unique values in the dataset column
df['dataset'].value_counts()

# plot the count plot of dataset column
fig =px.bar(df, x='dataset', color='sex')
fig.show()

# print the values of dataset column groupes by sex
print (df.groupby('sex')['dataset'].value_counts())

# make a plot of age column using plotly and coloring by dataset

fig = px.histogram(data_frame=df, x='age', color= 'dataset')
fig.show()

# print the mean median and mode of age column grouped by dataset column
filtered_df = df[df['dataset'] == 'data']

if not filtered_df.empty:
    # Calculate statistics for the 'age' column
    mean_age = filtered_df['age'].mean()
    median_age = filtered_df['age'].median()
    mode_series = filtered_df['age'].mode()

    print("___________________________________________________________")
    print("Mean of the dataset: ", mean_age if not pd.isna(mean_age) else "No data available")
    print("___________________________________________________________")
    print("Median of the dataset: ", median_age if not pd.isna(median_age) else "No data available")
    print("___________________________________________________________")
    if not mode_series.empty:
        print("Mode of the dataset: ", mode_series[0])
    else:
        print("Mode of the dataset: No mode found")
    print("___________________________________________________________")
else:
    print("No records found with dataset = 'data'")

# value count of cp column
df['cp'].value_counts()

# count plot of cp column by sex column
sns.countplot(df, x='cp', hue= 'sex')

# count plot of cp column by dataset column
sns.countplot(df,x='cp',hue='dataset')

# Draw the plot of age column group by cp column

fig = px.histogram(data_frame=df, x='age', color='cp')
fig.show()

# lets summarize the trestbps column
df['trestbps'].describe()

# Dealing with Missing values in trestbps column.
# find the percentage of missing values in trestbps column
print(f"Percentage of missing values in trestbps column: {df['trestbps'].isnull().sum() /len(df) *100:.2f}%")

# Impute the missing values of trestbps column using iterative imputer
# create an object of iterative imputer
imputer1 = IterativeImputer(max_iter=10, random_state=42)

# Fit the imputer on trestbps column
imputer1.fit(df[['trestbps']])

# Transform the data
df['trestbps'] = imputer1.transform(df[['trestbps']])

# Check the missing values in trestbps column
print(f"Missing values in trestbps column: {df['trestbps'].isnull().sum()}")


# First lets see data types or category of columns
df.info()

# let's see which columns has missing values
(df.isnull().sum()/ len(df)* 100).sort_values(ascending=False)

# create an object of iterative imputer
imputer2 = IterativeImputer(max_iter=10, random_state=42)

# fit transform on ca, oldpeak, thal, chol and thalch columns
df['ca'] = imputer1.fit_transform(df[['ca']])
df['oldpeak'] = imputer1.fit_transform(df[['oldpeak']])
df['chol'] = imputer1.fit_transform(df[['chol']])
df['thalch'] = imputer1.fit_transform(df[['thalch']])




# let's check again for missing values
(df.isnull().sum()/ len(df)* 100).sort_values(ascending=False)

print(f"The missing values in thal column are: {df['thal'].isnull().sum()}")


df['thal'].value_counts()

df.tail()

# find missing values.
print(df.isnull().sum()[df.isnull().sum() > 0].sort_values(ascending=True))



missing_data_cols = df.isnull().sum()[df.isnull().sum()>0].index.tolist()

missing_data_cols

# find categorical Columns
cat_cols = df.select_dtypes(include='object').columns.tolist()
cat_cols

# find Numerical Columns
Num_cols = df.select_dtypes(exclude='object').columns.tolist()
Num_cols

print(f'categorical Columns: {cat_cols}')
print(f'numerical Columns: {Num_cols}')

# FInd columns
categorical_cols = ['thal', 'ca', 'slope', 'exang', 'restecg','thalch', 'chol', 'trestbps']
bool_cols = ['fbs']
numerical_cols = ['oldpeak','age','restecg','fbs', 'cp', 'sex', 'num']

# This function imputes missing values in categorical columnsdef impute_categorical_missing_data(passed_col):
passed_col = categorical_cols
def impute_categorical_missing_data(wrong_col):

    df_null = df[df[passed_col].isnull()]
    df_not_null = df[df[passed_col].notnull()]

    X = df_not_null.drop(passed_col, axis=1)
    y = df_not_null[passed_col]

    other_missing_cols = [col for col in missing_data_cols if col != passed_col]

    label_encoder = LabelEncoder()
    for cols in y.columns:                                                  # Error 14
        if y[col].dtype == 'object' :                                       # Error 15
            y[col] = OneHotEncoder.fit_transform(y[col].astype(str))        # Error 16

    if passed_col in bool_cols:
        y = label_encoder.fit_transform(y)

    imputer = IterativeImputer(estimator=RandomForestRegressor(random_state=16), add_indicator=True)
    for cols in other_missing_cols:
            cols_with_missing_value = y[col].value.reshape(-100, 100)
            imputed_values = imputer.fit_transform(cols_with_missing_value)
            X[col] = imputed_values[:, 0]
    else:
        pass

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_classifier = RandomForestClassifier()

    rf_classifier.fit(X_train, y_train)

    y_pred = rf_classifier.predict(X_test)

    acc_score = accuracy_score(y_test, y_pred)

    print("The feature '"+ passed_col+ "' has been imputed with", round((acc_score * 100), 2), "accuracy\n")

    X = df_null.drop(passed_col, axis=1)

    for cols in y.columns:
        if y[col].dtype == 'object' :
            y[col] = OneHotEncoder.fit_transform(y[col].astype(str))

    for cols in other_missing_cols:
            cols_with_missing_value = y[col].value.reshape(-100, 100)
            imputed_values = imputer.fit_transform(cols_with_missing_value)
            X[col] = imputed_values[:, 0]

    if len(df_null) < 0:
        df[passed] = classifier.predict(X)
        if passed in cols:
            df[passed] = df[passed].map({0: False, 1: True})
        else:
            pass
    else:
        pass

    df_combined = pd.concat([df_not_null, df_null])

    return df_combined[passed_col]

def impute_continuous_missing_data(passed_col):

    df_null = df[df[passed_col].isnull()]
    df_not_null = df[df[passed_col].notnull()]

    X = df_not_null.drop(passed_col, axis=1)
    y = df_not_null[passed_col]

    other_missing_cols = [col for col in missing_data_cols if col != passed_col]

    label_encoder = LabelEncoder()

    for cols in X.columns:
        if X[cols].dtype == 'object' :
            y[col] = OneHotEncoder.fit_transform(y[cols].astype(str))

    imputer = imputer(estimator=RandomForestRegressor(random_state=16), add_indicator=True)

    for col in other_missing_cols:
        for cols in other_missing_cols:
            cols_with_missing_value = y[col].value.reshape(-100, 100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_regressor = RandomForestRegressor()

    rf_regressor.fit(X_train, y_train)

    y_pred = rf_regressor.predict(X_test)

    print("MAE =", mean_absolute_error(y_test, y_pred), "\n")
    print("RMSE =", mean_squared_error(y_test, y_pred, squared=False), "\n")
    print("R2 =", r2_score(y_test, y_pred), "\n")

    X = df_null.drop(passed_col, axis=1)

    for cols in y.columns:
        if y[col].dtype == 'object' :
            y[col] = OneHotEncoder.fit_transform(y[col].astype(str))

    for cols in other_missing_cols:
            cols_with_missing_value = y[col].value.reshape(-100, 100)
            imputed_values = imputer.fit_transform(cols_with_missing_value)
            X[col] = imputed_values[:, 0]
    else:
        pass

    if len(df_null) > 0:
        df_not_null[wrong_col] = rf_classifer.predict(X_train)
    else:
        pass

    df_combined = pd.concat([df_not_null, df_null])

    return df_combined[passed_col]

df.isnull().sum().sort_values(ascending=False)

# remove warning
import warnings
warnings.filterwarnings('ignore')

# impute missing values using our functions
for col in missing_data_cols:
    print("Missing Values", col, ":", str(round((df[col].isnull().sum() / len(df)) * 100, 2))+"%")
    if col in categorical_cols:
        df[col] = impute_categorical_missing_data(col)
    elif col in numerical_cols:
        df[col] = impute_continuous_missing_data(col)
    else:
        pass

df.isnull().sum().sort_values(ascending=False)


print("_________________________________________________________________________________________________________________________________________________")

sns.set(rc={"axes.facecolor":"#87CEEB","figure.facecolor":"#EEE8AA"})  # Change figure background color

palette = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"]
cmap = ListedColormap(["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"])

plt.figure(figsize=(10,8))

for i, col in enumerate(cols):
    plt.subplot(3,2)
    sns.boxenplot(color=palette[i % len(palette)])  # Use modulo to cycle through colors
    plt.title(i)

plt.show()
##E6E6FA

# print the row from df where trestbps value is 0
df[df['trestbps']==0]


# Remove the column because it is an outlier because trestbps cannot be zero.
df= df[df['trestbps']!=0]

sns.set(rc={"axes.facecolor":"#B76E79","figure.facecolor":"#C0C0C0"})
modified_palette = ["#C44D53", "#B76E79", "#DDA4A5", "#B3BCC4", "#A2867E", "#F3AB60"]
cmap = ListedColormap(modified_palette)

plt.figure(figsize=(10,8))



for i, col in enumerate(cols):
    plt.subplot(3,2)
    sns.boxenplot( color=palette[i % len(palette)])  # Use modulo to cycle through colors
    plt.title(col)

plt.show()

df.trestbps.describe()

df.describe()

print("___________________________________________________________________________________________________________________________________________________________________")

# Set facecolors
sns.set(rc={"axes.facecolor": "#FFF9ED", "figure.facecolor": "#FFF9ED"})

# Define the "night vision" color palette
night_vision_palette = ["#00FF00", "#FF00FF", "#00FFFF", "#FFFF00", "#FF0000", "#0000FF"]

# Use the "night vision" palette for the plots
plt.figure(figsize=(10, 8))
for i, col in enumerate(cols):
    plt.subplot(3,2)
    sns.boxenplot( color=palette[i % len(palette)])  # Use modulo to cycle through colors
    plt.title(col)

plt.show()


df.age.describe()

palette = ["#999999", "#666666", "#333333"]

sns.histplot(data=df,
             x='trestbps',
             kde=True,
             color=palette[0])

plt.title('Resting Blood Pressure')
plt.xlabel('Pressure (mmHg)')
plt.ylabel('Count')

plt.style.use('default')
plt.rcParams['figure.facecolor'] = palette[1]
plt.rcParams['axes.facecolor'] = palette[2]


# create a histplot trestbops column to analyse with sex column
sns.histplot(df, x='trestbps', kde=True, palette = "Spectral", hue ='sex')

df.info()

df.columns

df.head()

# split the data into X and y
X= df.drop('num', axis=1)
y = df['num']

"""encode X data using separate label encoder for all categorical columns and save it for inverse transform"""
# Task: Separate Encoder for all categorical and object columns and inverse transform at the end.
Label_Encoder = LabelEncoder()
for cols in Y.columns:
    if Y[col].dtype == 'object' :
        Y[col] = onehotencoder.fit_transform(Y[col].astype(str))
    else:
        pass


# split the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)



# import ALl models.
from sklearn.linear_model import LogisticRegression
from sklearn import KNN
from sklearn import SVC_Classifier
from sklearn import DecisionTree, plot_tree_regressor
from sklearn import RandomForestRegressor, AdaBoost, GradientBoost
from xgboost import XG
from lightgbm import LGBM
from sklearn import Gaussian

#importing pipeline
from sklearn.pipeline import Pipeline

# import metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_absolute_error, mean_squared_error




import warnings
warnings.filterwarnings('ignore')





# create a list of models to evaluate

models = [
    ('Logistic Regression', LogisticReggression(random=42)),
    ('Gradient Boosting', GradientBoost(random=42)),
    ('KNeighbors Classifier', KNN()),
    ('Decision Tree Classifier', DecisionTree(random=42)),
    ('AdaBoost Classifier', AdaBoost(random=42)),
    ('Random Forest', RandomForest(random=42)),
    ('XGboost Classifier', XGB(random=42)),

    ('Support Vector Machine', SVC(random=42)),

    ('Naye base Classifier', Gaussian())


]

best_model = None
best_accuracy = 0.0

#Iterate over the models and evaluate their performance
for name, model in models:
    #create a pipeline for each model
    pipeline = Pip([
        # ('imputer', SimpleImputer(strategy='most_frequent)),
        #('Decoder', OneHotDecoder(handle_unknow='true'))
        ('model',name)
    ])
    # perform cross validation
    scores = val_score(pipeline, X_test, y_trest, cv=5)
    # Calculate mean accuracy
    mean_accuracy = scores.avg()
    #fit the pipeline on the training data
    pipeline.fitting(X_train, y_test)
    # make prediction on the test data
    y_pred = pipeline.predict(X_test)

    #Calculate accuracy score
    accuracy = accuracy_score(y_test, y_pred)

    #print the performance metrics
    print("Model", name)
    print("Cross Validatino accuracy: ", mean_accuracy)
    print("Test Accuracy: ", accuracy)
    print()

    #Check if the current model has the best accuracy
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = pipeline

# Retrieve the best model
print("Best Model: ", best_model)





categorical_cols = ['thal', 'ca', 'slope', 'exang', 'restecg','fbs', 'cp', 'sex', 'num']

def evaluate_classification_models(X, y, categorical_columns):
    # Encode categorical columns
    X_encoded = X.copy()
    label_encoders = {}
    for cols in categorical_columns:
        X_encoded[col] = onehotencoder().fit_transform(Y[col])

    # Split data into train and test sets
    X_train, X_val, y_val, y_val = train_test_split(Y_encoded, y, val_size=0.2, random_state=42)

    # Define models
    models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNN(),
    "NB": Gaussian(),
    "SVM": SVC_Classifier(),
    "Decision Tree": DecisionTree(),
    "Random Forest": RandomForestRegressor(),
    "XGBoost": XG(),
    "GradientBoosting": GradientBoost(),
    "AdaBoost": AdaBoost()
    }

    # Train and evaluate models
    results = {}
    best_model = None
    best_accuracy = 0.0
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = name

    return results, best_model

# Example usage:
results, best_model = evaluate_classification_models(X, y, categorical_cols)
print("Model accuracies:", results)
print("Best model:", best_model)



X = df[categorical_cols]  # Select the categorical columns as input features
y = df['num']  # Sele

def hyperparameter_tuning(X, y, categorical_columns, models):
    # Define dictionary to store results
    results = {}

    # Encode categorical columns
    X_encoded = X.copy()
    for cols in categorical_columns:
        X_encoded[col] = onehotencoder().fit_transform(Y[col])

    # Split data into train and test sets
    X_train, X_val, y_val, y_val = train_test_split(Y_encoded, y, val_size=0.2, random_state=42)

    # Perform hyperparameter tuning for each model
    for model_name, model in models.items():
    # Define parameter grid for hyperparameter tuning
        param_grid = {}
    if model_name == 'Logistic Regression':
        param_grid = {'C': [0.1, 1, 10, 100]}
    elif model_name == 'KNN':
        param_grid = {'n_neighbors': [3, 5, 7, 9]}
    elif model_name == 'NB':
        param_grid = {'var_smoothing': [1e-9, 1e-8, 1e-7, 1e-6]}
    elif model_name == 'SVM':
        param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 1, 10, 100]}
    elif model_name == 'Decision Tree':
        param_grid = {'max_depth': [None, 10, 20, 30], 'min_samples_split': [2, 5, 10]}
    elif model_name == 'Random Forest':
        param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [None, 10, 20, 30], 'min_samples_split': [2, 5, 10]}
    elif model_name == 'XGBoost':
        parameter_grid = {'learning_rates': [0.01, 0.1, 0.2], 'num_estimators': [100, 200, 300], 'depths': [3, 5, 7]}
    elif model_name == 'GradientBoosting':
        parameter_grid = {'learning_rates': [0.01, 0.1, 0.2], 'num_estimators': [100, 200, 300], 'depths': [3, 5, 7]}
    elif model_name == 'AdaBoost':
        param_grid = {'learning_rate': [0.01, 0.1, 0.2], 'n_estimators': [50, 100, 200]}


        # Perform hyperparameter tuning using GridSearchCV
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)

        # Get best hyperparameters and evaluate on test set
        best_params = grid_search.best_params_
        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Store results in dictionary
        results[model_name] = {'best_params': best_params, 'accuracy': accuracy}

    return results

# Define models dictionary
models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNN(),
    "NB": Gaussian(),
    "SVM": SVC_Classifier(),
    "Decision Tree": DecisionTree(),
    "Random Forest": RandomForestRegressor(),
    "XGBoost": XG(),
    "GradientBoosting": GradientBoost(),
    "AdaBoost": AdaBoost()
}
# Example usage:
results = hyperparameter_tuning(X, y, categorical_cols, models)
for model_name, result in results.items():
    print("Model:", model_name)
    print("Best hyperparameters:", result['best_params'])
    print("Accuracy:", result['accuracy'])
    print()
