import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# data import
raw_data = pd.read_csv(r'C:\Users\seswaran\OneDrive\OneDrive - JAGUAR LAND ROVER\02_Documents\02_Workspaces\11_Py_Workspace\Py_WorkingDirectory\BITS_MTech\Assignments\Sem I\DM_Assignment_I\Heart_Attack_Analysis_Data.csv')

#%% data pre-processing

#for i in np.linspace(1,100,100):

# Features and Target split
X = raw_data.drop(columns='Target',axis=1)
Y = raw_data['Target']

# Split Training and Test data
X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=61)

# Model training
# Logistic Regression
model = LogisticRegression(max_iter=2000)

# Train LR model
model.fit(X_train,Y_train)

# Model evaluation using accuracy score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)



X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

    #if training_data_accuracy > .8 and test_data_accuracy > .8:
        #print(i ,' ', training_data_accuracy,' ', test_data_accuracy)

sample_data = (34,0,1,118,210,0,1,192,0,2)

sample_data_shaped = np.array(sample_data).reshape(1,-1)

# Prediction
prediction = model.predict(sample_data_shaped)

