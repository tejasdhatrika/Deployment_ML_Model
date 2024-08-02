import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

st.title("Machine Learning Task Application")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    if st.checkbox("Specify columns"):
        columns = st.multiselect("Select columns to use for the model", data.columns.tolist())
        if columns:
            X = data[columns]
            y = data.iloc[:, -1]  # Assuming the target variable is the last column
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            st.write("Training the model...")
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            st.write(classification_report(y_test, y_pred))
            st.write("Model Training Results")
            st.write("Classification Report", classification_report(y_test, y_pred))

