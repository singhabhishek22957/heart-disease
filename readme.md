# ❤️ Heart Disease Prediction using K-Nearest Neighbors (KNN)

A Machine Learning web application built with **Streamlit** that predicts whether a patient is at risk of heart disease based on medical information.

The application uses a trained **K-Nearest Neighbors (KNN)** model and provides an easy-to-use interface with sliders and dropdown menus for patient data.

---

# 🚀 Features

* Predicts the risk of heart disease.
* User-friendly Streamlit interface.
* Numeric inputs using sliders.
* Categorical inputs using dropdown menus.
* Displays prediction confidence.
* Shows patient summary after prediction.
* Uses a trained KNN model with feature scaling.

---

# 📁 Project Structure

```text
HeartDiseasePrediction/
│
├── app.py                # Streamlit application
├── KNN_heart.pkl         # Trained KNN model
├── scaler.pkl            # StandardScaler used during training
├── columns.pkl           # Feature column names
├── requirements.txt      # Python dependencies
├── heart.csv             # Dataset (optional)
└── README.md
```

---

# 📊 Dataset

The dataset contains patient medical information such as:

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| Age            | Patient's age                                 |
| Sex            | Male or Female                                |
| ChestPainType  | Type of chest pain                            |
| RestingBP      | Resting blood pressure (mmHg)                 |
| Cholesterol    | Serum cholesterol (mg/dL)                     |
| FastingBS      | Fasting blood sugar (>120 mg/dL)              |
| RestingECG     | Resting ECG result                            |
| MaxHR          | Maximum heart rate achieved                   |
| ExerciseAngina | Exercise-induced angina                       |
| Oldpeak        | ST depression induced by exercise             |
| ST_Slope       | Slope of the peak exercise ST segment         |
| HeartDisease   | Target variable (0 = No Disease, 1 = Disease) |

---

# 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

# 📦 Installation

## Step 1: Clone the repository

```bash
git clone https://github.com/your-username/HeartDiseasePrediction.git
```

Move into the project folder:

```bash
cd HeartDiseasePrediction
```

---

## Step 2: Create a virtual environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Verify project files

Ensure these files exist in the project directory:

* `app.py`
* `KNN_heart.pkl`
* `scaler.pkl`
* `columns.pkl`

---

## Step 5: Run the application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

If it does not open automatically, visit:

```
http://localhost:8501
```

---

# 💻 How to Use

1. Launch the application using:

```bash
streamlit run app.py
```

2. Enter the patient's information.

3. Adjust the numeric values using the sliders.

4. Select the appropriate options from the dropdown menus.

5. Click the **Predict Heart Disease** button.

6. The application will display:

   * Prediction result
   * Confidence score
   * Patient summary
   * Class probabilities

---

# 📌 Input Features

### Numeric Features

* Age
* Resting Blood Pressure
* Cholesterol
* Maximum Heart Rate
* Old Peak

### Categorical Features

* Sex
* Chest Pain Type
* Fasting Blood Sugar
* Resting ECG
* Exercise Angina
* ST Slope

---

# 🤖 Machine Learning Model

This project uses the **K-Nearest Neighbors (KNN)** algorithm.

### Workflow

1. Load the trained model.
2. Load the scaler.
3. Load the feature columns.
4. Collect user input.
5. Convert categorical values into one-hot encoded features.
6. Scale the input using the saved scaler.
7. Predict the class using the trained KNN model.
8. Display the prediction and confidence.

---

# 📈 Prediction Output

The model predicts one of the following classes:

| Prediction | Meaning                    |
| ---------- | -------------------------- |
| 0          | Low risk of heart disease  |
| 1          | High risk of heart disease |

---

# 📋 Requirements

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🔄 Retraining the Model (Optional)

If you train a new model, save the required files:

```python
import joblib

joblib.dump(model, "KNN_heart.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")
```

**Important:** Use `X.columns.tolist()` with parentheses. Omitting `()` will save the method instead of the actual list of feature names.

---

# 📷 Screenshots

You can add screenshots of the application here.

Example:

```text
screenshots/
    home.png
    prediction.png
```

Then include them in the README:

```markdown
![Home Screen](screenshots/home.png)

![Prediction Result](screenshots/prediction.png)
```

---

# 📄 License

This project is intended for educational and learning purposes. Feel free to modify and improve it.

---

# 👨‍💻 Author

**Abhishek Singh**

If you found this project useful, consider giving it a ⭐ on GitHub.
