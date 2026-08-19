# =====================================================
# STUDENT PERFORMANCE PREDICTION
# USING MACHINE LEARNING
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =====================================================
# 1. CREATE DATASET
# =====================================================

data = {
    "study_hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 9, 10, 10, 11,
        2, 3, 4, 5, 6,
        7, 8, 9, 10
    ],

    "attendance": [
        55, 60, 62, 65, 68,
        70, 72, 75, 77, 80,
        82, 84, 86, 88, 90,
        92, 94, 95, 96, 97,
        58, 67, 73, 78, 83,
        87, 91, 93, 98
    ],

    "previous_marks": [
        40, 45, 42, 50, 52,
        55, 58, 60, 62, 65,
        67, 70, 72, 75, 77,
        80, 82, 85, 88, 90,
        43, 51, 57, 64, 69,
        74, 79, 84, 92
    ],

    "assignment_marks": [
        45, 50, 48, 55, 57,
        60, 62, 65, 67, 70,
        72, 75, 77, 80, 82,
        85, 87, 90, 92, 95,
        47, 56, 63, 68, 73,
        78, 83, 88, 96
    ],

    "internal_marks": [
        42, 46, 45, 51, 54,
        57, 60, 62, 65, 68,
        70, 73, 75, 78, 80,
        83, 85, 88, 91, 94,
        44, 52, 59, 65, 71,
        76, 81, 86, 95
    ],

    "final_marks": [
        42, 47, 45, 52, 54,
        57, 60, 63, 65, 69,
        71, 74, 76, 79, 81,
        84, 86, 89, 92, 95,
        44, 53, 60, 66, 71,
        77, 82, 87, 96
    ]
}


# Convert data into DataFrame

df = pd.DataFrame(data)


# =====================================================
# 2. DISPLAY DATASET
# =====================================================

print("\n===================================")
print("      STUDENT PERFORMANCE DATA")
print("===================================\n")

print(df.head(10))


# =====================================================
# 3. DATASET INFORMATION
# =====================================================

print("\n===================================")
print("       DATASET INFORMATION")
print("===================================\n")

print("Total students:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())


# =====================================================
# 4. BASIC STATISTICS
# =====================================================

print("\n===================================")
print("       BASIC STATISTICS")
print("===================================\n")

print(df.describe())


# =====================================================
# 5. SEPARATE FEATURES AND TARGET
# =====================================================

X = df[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_marks",
        "internal_marks"
    ]
]

y = df["final_marks"]


# =====================================================
# 6. SPLIT DATA INTO TRAINING AND TESTING
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\n===================================")
print("       TRAIN / TEST DATA")
print("===================================")

print("\nTraining students:", len(X_train))
print("Testing students:", len(X_test))


# =====================================================
# 7. CREATE MACHINE LEARNING MODEL
# =====================================================

model = LinearRegression()


# =====================================================
# 8. TRAIN THE MODEL
# =====================================================

model.fit(X_train, y_train)

print("\nModel training completed successfully!")


# =====================================================
# 9. PREDICT TEST DATA
# =====================================================

y_pred = model.predict(X_test)


# =====================================================
# 10. MODEL EVALUATION
# =====================================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


print("\n===================================")
print("        MODEL EVALUATION")
print("===================================")

print("\nMean Absolute Error:", round(mae, 2))

print("Mean Squared Error:", round(mse, 2))

print("Root Mean Squared Error:", round(rmse, 2))

print("R2 Score:", round(r2, 2))


# =====================================================
# 11. COMPARE ACTUAL AND PREDICTED MARKS
# =====================================================

comparison = pd.DataFrame({
    "Actual Marks": y_test.values,
    "Predicted Marks": np.round(y_pred, 2)
})

print("\n===================================")
print("     ACTUAL VS PREDICTED MARKS")
print("===================================\n")

print(comparison)


# =====================================================
# 12. PREDICT NEW STUDENT PERFORMANCE
# =====================================================

print("\n===================================")
print("     NEW STUDENT PREDICTION")
print("===================================")

study_hours = float(input("\nEnter study hours: "))

attendance = float(input("Enter attendance percentage: "))

previous_marks = float(input("Enter previous marks: "))

assignment_marks = float(input("Enter assignment marks: "))

internal_marks = float(input("Enter internal marks: "))


new_student = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_marks": [previous_marks],
    "assignment_marks": [assignment_marks],
    "internal_marks": [internal_marks]
})


prediction = model.predict(new_student)

predicted_marks = prediction[0]


# Keep marks between 0 and 100

predicted_marks = max(0, min(100, predicted_marks))


print("\n===================================")
print("       PREDICTION RESULT")
print("===================================")

print("\nPredicted Final Marks:",
      round(predicted_marks, 2))


# =====================================================
# 13. PERFORMANCE CATEGORY
# =====================================================

if predicted_marks >= 75:

    print("Performance: Excellent")

elif predicted_marks >= 60:

    print("Performance: Good")

elif predicted_marks >= 40:

    print("Performance: Average")

else:

    print("Performance: Needs Improvement")


# =====================================================
# 14. VISUALIZATION
# =====================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["study_hours"],
    df["final_marks"]
)

plt.xlabel("Study Hours")

plt.ylabel("Final Marks")

plt.title("Study Hours vs Final Marks")

plt.grid(True)

plt.show()


# =====================================================
# 15. ACTUAL VS PREDICTED GRAPH
# =====================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel("Actual Marks")

plt.ylabel("Predicted Marks")

plt.title("Actual vs Predicted Marks")

plt.grid(True)

plt.show()