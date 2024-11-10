from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Dataset
data = {
    'Outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'Temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'Humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'Windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'Play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

# Convert Dataset to DataFrame
df = pd.DataFrame(data)

# Encode Categorical Data
df = pd.get_dummies(df, columns=['Outlook', 'Temperature', 'Humidity', 'Windy'], drop_first=True)
X = df.drop('Play', axis=1)
y = df['Play']

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Define the new case
new_case = pd.DataFrame({
    'Outlook_sunny': [0],
    'Outlook_overcast': [1],
    'Outlook_rainy': [0],
    'Temperature_mild': [1],
    'Temperature_hot': [0],
    'Humidity_normal': [0],
    'Windy_True': [0]
})

# Ensure the new case has the same columns as the training data
new_case = new_case.reindex(columns=X.columns, fill_value=0)

# Predict the outcome for the new case
prediction = clf.predict(new_case)
print("Prediction for new case:", prediction)
