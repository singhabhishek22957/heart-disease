import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background:#f8fafc;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#e63946;
    text-align:center;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.block-container{
    padding-top:2rem;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:20px;
    background:#e63946;
    color:white;
    border-radius:10px;
    border:none;
}

.stButton>button:hover{
    background:#c1121f;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='title'>❤️ Heart Disease Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Predict heart disease using Machine Learning (KNN)</div>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns(2)

# -----------------------------
# Left Column
# -----------------------------
with left:

    st.subheader("🩺 Patient Details")

    age = st.slider(
        "Age",
        18,
        100,
        40
    )

    resting_bp = st.slider(
        "Resting Blood Pressure",
        80,
        220,
        120
    )

    cholesterol = st.slider(
        "Cholesterol",
        0,
        700,
        200
    )

    max_hr = st.slider(
        "Maximum Heart Rate",
        60,
        220,
        150
    )

    oldpeak = st.slider(
        "Old Peak",
        0.0,
        6.5,
        1.0,
        step=0.1
    )

# -----------------------------
# Right Column
# -----------------------------
with right:

    st.subheader("📋 Medical Information")

    sex = st.selectbox(
        "Sex",
        ["Male","Female"]
    )

    chest = st.selectbox(
        "Chest Pain Type",
        [
            "ATA",
            "NAP",
            "ASY",
            "TA"
        ]
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar >120",
        [0,1]
    )

    ecg = st.selectbox(
        "Resting ECG",
        [
            "Normal",
            "ST",
            "LVH"
        ]
    )

    exercise = st.selectbox(
        "Exercise Angina",
        [
            "No",
            "Yes"
        ]
    )

    slope = st.selectbox(
        "ST Slope",
        [
            "Up",
            "Flat",
            "Down"
        ]
    )

st.divider()

# -----------------------------
# Predict Button
# -----------------------------
predict = st.button("❤️ Predict Heart Disease")

# -----------------------------
# Prediction
# -----------------------------
if predict:

    data = dict.fromkeys(columns, 0)

    data["Age"] = age
    data["RestingBP"] = resting_bp
    data["Cholesterol"] = cholesterol
    data["FastingBS"] = fasting_bs
    data["MaxHR"] = max_hr
    data["Oldpeak"] = oldpeak

    # Sex
    if sex == "Male":
        data["Sex_M"] = 1

    # Chest Pain
    if chest == "ATA":
        data["ChestPainType_ATA"] = 1
    elif chest == "NAP":
        data["ChestPainType_NAP"] = 1
    elif chest == "TA":
        data["ChestPainType_TA"] = 1

    # ECG
    if ecg == "Normal":
        data["RestingECG_Normal"] = 1
    elif ecg == "ST":
        data["RestingECG_ST"] = 1

    # Exercise
    if exercise == "Yes":
        data["ExerciseAngina_Y"] = 1

    # ST Slope
    if slope == "Flat":
        data["ST_Slope_Flat"] = 1
    elif slope == "Up":
        data["ST_Slope_Up"] = 1

    df = pd.DataFrame([data])

    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]

    probability = model.predict_proba(scaled)[0]

    confidence = probability[prediction]

    st.divider()

    st.header("Prediction Result")

    if prediction == 1:

        st.error("⚠️ High Risk of Heart Disease")

    else:

        st.success("✅ Low Risk of Heart Disease")

    st.write("### Confidence")

    st.progress(float(confidence))

    st.write(f"**Model Confidence:** {confidence*100:.2f}%")

    st.divider()

    st.subheader("Patient Summary")

    summary = pd.DataFrame({

        "Feature":[
            "Age",
            "Sex",
            "Chest Pain",
            "Resting BP",
            "Cholesterol",
            "Fasting BS",
            "Resting ECG",
            "Max HR",
            "Exercise Angina",
            "Old Peak",
            "ST Slope"
        ],

        "Value":[
            age,
            sex,
            chest,
            resting_bp,
            cholesterol,
            fasting_bs,
            ecg,
            max_hr,
            exercise,
            oldpeak,
            slope
        ]

    })

    st.table(summary)

    st.divider()

    st.write("### Prediction Probabilities")

    st.write(
        pd.DataFrame({
            "Class":["No Disease","Heart Disease"],
            "Probability":[
                probability[0],
                probability[1]
            ]
        })
    )