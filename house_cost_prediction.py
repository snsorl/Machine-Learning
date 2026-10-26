from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[500], [1000], [1500], [2000], [2500]])
y= np.array([150, 250, 350, 450, 550])
model = LinearRegression()
model.fit(X, y)
predicted_price = model.predict([[1500]])
print(f"Predicted Price: ${predicted_price[0]:.0f},000")
