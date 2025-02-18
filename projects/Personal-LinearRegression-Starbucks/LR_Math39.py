import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# 1. Variables: Week, Temperature, Holiday Week, Daily Traffic, Sales
np.random.seed(42)  # function sets the seed for the NumPy random number generator.
Week = np.arange(1, 15)  # 14 weeks starting from November 7 (nov7 is starbucks' holiday launch)
Temperature = [63, 58, 57, 56, 55, 54, 53, 52, 52, 52, 53, 53, 54, 56]  # average San Jose temps (fahrenheit)
HolidayWeek = np.array([1, 0,0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0])  # Starbucks launch, Thanksgiving, Christmas, New Years
DailyTraffic = np.array([900, 700, 600, 850, 650, 680, 720, 1100, 1000, 640, 610, 610, 630, 580])  # estimated store traffic
WeekCoeff = np.where(Week <= 9, 5, -3)  # growth before Week 10, sales decline after week 9 (3rd week of jan)
WeekEffect = Week * WeekCoeff  #week contribution to sales
# calculating the dependent variable (Sales or y) with some noise
Sales = (WeekEffect + 2 * np.array(Temperature) + 
         50 * HolidayWeek + 0.1 * DailyTraffic + 
         np.random.normal(0, 10, size=14))  # adding randomness due to factors such as staffing, low ingredients etc.
# Sales consists of constants; helps create a realistic growth or decline in sales relative to temperature or a holiday week.
#  2. !!Matrix Formulation for Linear Regression!!      y = Xβ + ε
X = np.column_stack((np.ones(len(Week)), Week, Temperature, HolidayWeek, DailyTraffic))
y = Sales  # dependent variable vector
# 3. calculating regression coefficients using the normal equation:     β = (X^T X)^-1 X^T y
XT = X.T  # Transpose of X
beta = np.linalg.inv(XT @ X) @ XT @ y  # = regression coefficients  β
# 4. displaying the Results
print("Regression Coefficients (β):")
print(beta)
# 5. predicting Sales
yPrediction= X @ beta  # Predicted values

# 6. visualizing actual vs predicted sales
plt.figure(figsize=(12, 6))
plt.plot(Week, y, 'bo-', label="Actual Sales")  # actual sales
plt.plot(Week, yPrediction, 'r--', label="Predicted Sales")  # predicted sales
plt.xlabel("Week")
plt.ylabel("Sales")
plt.title("Actual vs Predicted Sales for Seasonal Drink")
plt.legend()
plt.grid(True)
plt.show()
#visualizing x. can be done just as a numpy array, but use DF as a readable matrix with labels.
columns = ["Bias", "Week", "Temperature", "HolidayWeek", "DailyTraffic"]
Xdf = pd.DataFrame(X, columns=columns)# var to set X as a dataframe
print("Matrix X (Independent Variables):")
print(Xdf)# visualize X as a matrix

print("Interpretation of Coefficients:")
print(f"Intercept (Bias): {beta[0]:.2f} (Baseline sales)")
print(f"Week Coefficient: {beta[1]:.2f} (Effect of week on sales)")
print(f"Temperature Coefficient: {beta[2]:.2f} (Effect of temperature on sales)")
print(f"HolidayWeek Coefficient: {beta[3]:.2f} (Effect of holidays on sales)")
print(f"DailyTraffic Coefficient: {beta[4]:.4f} (Effect of foot traffic on sales)")