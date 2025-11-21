import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("iris.csv")

# Use sepal_length to predict petal_length (simple linear regression)
X = df[['sepal_length']]
y = df['petal_length']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("=== MODEL RESULTS ===")
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("MSE:", mse)
print("R² Score:", r2)
