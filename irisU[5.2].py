#Iris Flower Classification & Accuracy
# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()

# Input data
x = iris.data

# Output data
y = iris.target

# Split data into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(x_train, y_train)

# Test the model
accuracy = model.score(x_test, y_test)
print("Accuracy: ", accuracy)

# New flower input
new_flower = [[5.1, 3.5, 1.4, 0.2]]

# Predict Flower
prediction = model.predict(new_flower)
print("Predicted Class: ", prediction[0])
print("Flower name: ", iris.target_names[prediction[0]])
