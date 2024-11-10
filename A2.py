import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

# Creating the dataset from the transcribed data
data = {
    "Outlook": ["sunny", "sunny", "overcast", "rainy", "rainy", "overcast", "sunny", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy"],
    "Temperature": ["hot", "hot", "hot", "cool", "cool", "cool", "mild", "cool", "mild", "mild", "mild", "hot", "mild"],
    "Humidity": ["high", "high", "high", "normal", "normal", "normal", "high", "normal", "normal", "normal", "high", "normal", "high"],
    "Windy": ["false", "true", "false", "false", "true", "true", "false", "false", "false", "true", "true", "false", "true"],
    "Play": ["no", "no", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encoding categorical features
df_encoded = pd.get_dummies(df[['Outlook', 'Temperature', 'Humidity', 'Windy']])
target = df['Play'].apply(lambda x: 1 if x == 'yes' else 0)  # Encode 'yes' as 1 and 'no' as 0

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_encoded, target, test_size=0.3, random_state=42)

# Initialize and train the Naive Bayes classifier
model = CategoricalNB()
model.fit(X_train, y_train)

# Make predictions and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Show the results
print("Accuracy:", accuracy)
print("Predicted Labels:", y_pred)
print("Actual Labels:", y_test.tolist())
