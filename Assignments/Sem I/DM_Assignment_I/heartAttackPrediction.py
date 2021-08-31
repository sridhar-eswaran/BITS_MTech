#%% Library import
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns

# Set image size for exporting
from matplotlib import rcParams
# figure size in inches
rcParams['figure.figsize'] = 11.7,8.27

#%% data import
raw_data = pd.read_csv(r'C:\Users\seswaran\OneDrive\OneDrive - JAGUAR LAND ROVER\02_Documents\02_Workspaces\11_Py_Workspace\Py_WorkingDirectory\BITS_MTech\Assignments\Sem I\DM_Assignment_I\Heart_Attack_Analysis_Data.csv')

#%% Data preprocessing
# null value check
null_entry = raw_data.isnull().sum()
if 1 in null_entry.values:
    print('Values missing in data_set; preprocessing required')
else:
    print('No Null Values found in data_set')

# #%% Descriptive Analysis
# raw_data_info = raw_data.info()# Check for name, data type & count
#
# raw_data_5point = raw_data.describe() # check for 5 point summary and distribution info
#
# raw_data_correlation = raw_data.corr()
#
# # Save correlation plot
# sns.heatmap(raw_data_correlation,annot=True,cmap='terrain')
# plt.savefig('correlationMap.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_pair = sns.pairplot(data = raw_data)
# plt.savefig('pairPlot.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_hist = raw_data.hist()
# plt.savefig('histogram.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_box = raw_data.plot(kind='box',subplots=True,layout=(5,3),figsize=(12,12))
# plt.savefig('boxPlot.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='Age',hue='Target')
# plt.savefig('catPlot_Age.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='CP_Type',hue='Target')
# plt.savefig('catPlot_CPType.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='BloodPressure',hue='Target')
# plt.savefig('catPlot_BP.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='Cholestrol',hue='Target')
# plt.savefig('catPlot_Cholestrol.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='BloodSugar',hue='Target')
# plt.savefig('catPlot_Sugar.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='ECG',hue='Target')
# plt.savefig('catPlot_ECG.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='MaxHeartRate',hue='Target')
# plt.savefig('catPlot_HR.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='ExerciseAngia',hue='Target')
# plt.savefig('catPlot_ExAngia.png',format='png',dpi=300)
# plt.clf()
#
# raw_data_cat = sns.catplot(data = raw_data,x='Sex',y='FamilyHistory',hue='Target')
# plt.savefig('catPlot_Family.png',format='png',dpi=300)
# plt.clf()
#
# sex_tab = pd.crosstab(raw_data['Sex'],raw_data['Target'],rownames=['Sex'],colnames=['Target'])
# print(sex_tab)
#
# Sugar_tab = pd.crosstab(raw_data['BloodSugar'],raw_data['Target'],rownames=['BloodSugar'],colnames=['Target'])
# print(Sugar_tab)
#
# Ecg_tab = pd.crosstab(raw_data['ECG'],raw_data['Target'],rownames=['ECG'],colnames=['Target'])
# print(Ecg_tab)
#
# ExAngia_tab = pd.crosstab(raw_data['ExerciseAngia'],raw_data['Target'],rownames=['ExerciseAngia'],colnames=['Target'])
# print(ExAngia_tab)
#
# Family_tab = pd.crosstab(raw_data['FamilyHistory'],raw_data['Target'],rownames=['FamilyHistory'],colnames=['Target'])
# print(Family_tab)

#%% Data Selection & Preparation
# Scaling the data
from sklearn.preprocessing import StandardScaler
StandardScaler = StandardScaler()
columnsToScale = ['Age','BloodPressure','Cholestrol','MaxHeartRate']
raw_data[columnsToScale] = StandardScaler.fit_transform(raw_data[columnsToScale])

#%%
# Train & Test data split
from sklearn.model_selection import train_test_split
X = raw_data.drop(columns='Target',axis=1)
Y = raw_data['Target']



# Prediction Model
#for i in np.linspace(1,100,100):
X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,stratify=Y,random_state=54)

# Decision Tree
decisionTree = tree.DecisionTreeClassifier()
decisionTreeModel = decisionTree.fit(X_train,Y_train)
decisionTreePredictionTest = decisionTreeModel.predict(X_test)
decisionTreePredictionTrain = decisionTreeModel.predict(X_train)

# Decision Tree: Check accuracy
from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,classification_report
decisionTreeConfusionMatrix = confusion_matrix(Y_test,decisionTreePredictionTest)
decisionTreeScoreTrain = accuracy_score(Y_train,decisionTreePredictionTrain)
decisionTreeScoreTest = accuracy_score(Y_test,decisionTreePredictionTest)
decisionTreeReport = classification_report(Y_test,decisionTreePredictionTest)

# Logistic Regression
logisticRegression = LogisticRegression(max_iter=2000)
logisticRegressionModel = logisticRegression.fit(X_train,Y_train)
logisticRegressionPredictionTest = logisticRegressionModel.predict(X_test)
logisticRegressionPredictionTrain = logisticRegressionModel.predict(X_train)

# Logistic Regression: Check Accuracy
logisticRegressionConfusionMatrix = confusion_matrix(Y_test, logisticRegressionPredictionTest)
logisticRegressionScoreTest = accuracy_score(Y_test, logisticRegressionPredictionTest)
logisticRegressionScoreTrain = accuracy_score(Y_train, logisticRegressionPredictionTrain)
logisticRegressionReport = classification_report(Y_test, logisticRegressionPredictionTest)

# if decisionTreeScoreTest > .75 or decisionTreeScoreTest > .75:
#     print(i ,'Decision Tree : Train ', decisionTreeScoreTrain,' Test ', decisionTreeScoreTest)
#     print(i, 'Logistic Regression : Train ', logisticRegressionScoreTrain, ' Test ', logisticRegressionScoreTest)

#%%
sample_data = (51,0,0,130,305,0,1,142,1,3)

sample_data_shaped = np.array(sample_data).reshape(1,-1)

# Prediction
predictionLR = logisticRegressionModel.predict(sample_data_shaped)
predictionDT = decisionTreeModel.predict(sample_data_shaped)

print(predictionLR)
print(predictionDT)