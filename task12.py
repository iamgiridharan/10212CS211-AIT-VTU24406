import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Sample dataset (Day vs Temperature)
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7],
    'Temperature': [30, 32, 34, 33, 35, 36, 38]
}

df = pd.DataFrame(data)

# Step 2: Separate features and labels
X = df[['Day']]              # Independent variable
y = df['Temperature']        # Dependent variable

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict the temperature for test data
y_pred = model.predict(X_test)

# Step 6: Display results
print("Actual Temperatures:", list(y_test.values))
print("Predicted Temperatures:", [round(val, 2) for val in y_pred])

# Step 7: Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Weather Forecasting using Linear Regression")
plt.legend()
plt.show()
