# 🎓 Student Performance Prediction Using Machine Learning

## 📌 Project Overview

**Student Performance Prediction** is a Machine Learning project that predicts a student's final marks based on different academic factors.

The project uses **Supervised Machine Learning** and the **Linear Regression** algorithm to learn the relationship between student information and final marks.

The main purpose of this project is to demonstrate a complete Machine Learning workflow using Python.

---

## 🎯 Objective

The objective of this project is to predict the final marks of a student using:

* Study Hours
* Attendance Percentage
* Previous Marks
* Assignment Marks
* Internal Exam Marks

The trained Machine Learning model uses these features to predict the student's expected final marks.

---

## 🤖 Machine Learning Type

**Supervised Learning**

The model is trained using a dataset where the input features and the actual final marks are already available.

### Problem Type

**Regression**

Regression is used because the project predicts a continuous numerical value — the student's final marks.

---

## 🧠 Machine Learning Algorithm

### Linear Regression

Linear Regression is used to find the relationship between input features and the target value.

In this project:

**Input Features → Final Marks**

The model learns from existing student data and predicts the final marks of a new student.

---

## 📊 Features Used

| Feature            | Description                         |
| ------------------ | ----------------------------------- |
| `study_hours`      | Number of hours the student studies |
| `attendance`       | Student attendance percentage       |
| `previous_marks`   | Marks obtained previously           |
| `assignment_marks` | Assignment marks                    |
| `internal_marks`   | Internal examination marks          |
| `final_marks`      | Final marks to be predicted         |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**

---

## 📚 Libraries Used

### Pandas

Used for creating and handling the dataset using DataFrames.

### NumPy

Used for numerical calculations and processing prediction results.

### Matplotlib

Used to create graphs and visualize the data.

### Scikit-learn

Used for:

* Train-test splitting
* Linear Regression
* Model training
* Prediction
* Model evaluation

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Collection
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
New Student Prediction
```

---

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── student_performance.py
│
└── README.md
```

---

## ⚙️ Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## ▶️ How to Run the Project

### Step 1: Download or clone the project

Open the project folder in VS Code.

### Step 2: Install the required libraries

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Step 3: Run the Python file

```bash
python student_performance.py
```

### Step 4: Enter student information

The program will ask for:

```text
Enter study hours:
Enter attendance percentage:
Enter previous marks:
Enter assignment marks:
Enter internal marks:
```

### Step 5: View the prediction

The model will display the predicted final marks and performance category.

---

## 🧪 Example

### Input

```text
Study Hours: 7
Attendance: 85
Previous Marks: 75
Assignment Marks: 80
Internal Marks: 78
```

### Output

```text
Predicted Final Marks: XX.XX

Performance: Good
```

The exact predicted value may vary depending on the trained model and dataset.

---

## 📈 Data Visualization

The project creates graphs to understand the relationship between student performance and the input features.

### Graph 1: Study Hours vs Final Marks

This graph shows how study hours are related to final marks.

### Graph 2: Actual vs Predicted Marks

This graph compares the actual marks from the test dataset with the marks predicted by the Machine Learning model.

---

## 📏 Model Evaluation

The project evaluates the Machine Learning model using:

### Mean Absolute Error (MAE)

Measures the average difference between actual and predicted marks.

### Mean Squared Error (MSE)

Measures the squared difference between actual and predicted values.

### Root Mean Squared Error (RMSE)

Measures the square root of the Mean Squared Error.

### R² Score

Shows how well the model explains the relationship between the input features and final marks.

---

## 💡 Key Learning Outcomes

Through this project, I learned how to:

* Create a dataset using Pandas
* Work with DataFrames
* Check missing values
* Analyze data
* Select features and target variables
* Split data into training and testing sets
* Train a Machine Learning model
* Use Linear Regression
* Make predictions
* Evaluate a Machine Learning model
* Create data visualizations using Matplotlib
* Predict results for new data

---

## 🚀 Future Improvements

The project can be improved by:

* Using a larger real-world student dataset
* Adding more student features
* Trying different Machine Learning algorithms
* Adding a graphical user interface
* Creating a web-based prediction system
* Improving model accuracy
* Saving the trained model for future predictions

---

## 🎓 Project Type

**Final AI/ML Project**

This project demonstrates the application of Machine Learning to predict student academic performance using Python.

---

## 👩‍💻 Author

**Priyanshi Dangi**

BCA Student

---

## 📜 Conclusion

The **Student Performance Prediction** project demonstrates how Machine Learning can be used to analyze student-related data and predict final marks.

By using **Pandas, NumPy, Matplotlib, and Scikit-learn**, the project follows a complete Machine Learning workflow from data preparation to model training, evaluation, and prediction.
