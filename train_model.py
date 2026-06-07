import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load sample data
iris = load_iris()
X = iris.data
y = iris.target

# Train a simple model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")

