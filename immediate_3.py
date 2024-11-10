from sklearn.tree import DecisionTreeClassifier

# Directly assigning numerical values based on the table
# "Outlook": sunny = 0, overcast = 1, rainy = 2
# "Temperature": hot = 0, mild = 1, cool = 2
# "Humidity": high = 0, normal = 1
# "Windy": False = 0, True = 1
# "Play": no = 0, yes = 1

X = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 2, 1, 0],
    [2, 2, 1, 1],
    [1, 2, 1, 1],
    [0, 1, 0, 0],
    [0, 2, 1, 0],
    [2, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [2, 1, 0, 1]
]

y = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]

# Train the Decision Tree model
def decision_tree_train(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf

model = decision_tree_train(X, y)

# Testing with new cases
test_cases = [
    [0, 2, 0, 1],  # sunny, cool, high, windy=True
    [1, 1, 1, 0],  # overcast, mild, normal, windy=False
    [2, 0, 1, 1]   # rainy, hot, normal, windy=True
]

# Predicting and displaying results
predictions = model.predict(test_cases)
print("Predictions:", ["yes" if pred == 1 else "no" for pred in predictions])
