import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the CSV file
df = pd.read_csv('StudentData.csv')

# Ensure the data has the expected columns
if 'Hours_Studied' not in df.columns or 'Exam_Score' not in df.columns:
    raise ValueError("The dataset must contain 'Hours_Studied' and 'Exam_Score' columns.")

# Define the features (X) and target (y)
X = df[['Hours_Studied']]  # Independent variable
y = df['Exam_Score']  # Dependent variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Extract slope and intercept
slope = model.coef_[0]  # Coefficient of the linear regression
intercept = model.intercept_  # Intercept of the linear regression

# Print the equation of the regression line
print(f"Slope (m): {slope}")
print(f"Intercept (b): {intercept}")
print(f"Equation of the regression line: Exam_Score = {slope:.2f} * Hours_Studied + {intercept:.2f}")

# Predict the test set results
y_test_pred = model.predict(X_test)

# Calculate and print the Mean Squared Error
mse = mean_squared_error(y_test, y_test_pred)
print(f"Mean Squared Error (MSE) on Test Data: {mse:.2f}")

# Predict for new data (e.g., 6 hours studied)
new_data = pd.DataFrame({'Hours_Studied': [6]})
predicted_score = model.predict(new_data)[0]
print(f"Predicted exam score for 6 hours studied: {predicted_score:.2f}")
