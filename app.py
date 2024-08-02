import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

st.title("Machine Learning Task Application")

# Upload file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:", data.head())
    except Exception as e:
        st.error(f"Error loading file: {e}")
    
    # Select columns and target variable
    if st.checkbox("Specify columns"):
        columns = st.multiselect("Select features for the model", data.columns.tolist())
        target_column = st.selectbox("Select the target variable", data.columns.tolist())
        
        if columns and target_column:
            if target_column in columns:
                st.error("Target variable cannot be one of the feature columns.")
            else:
                X = data[columns]
                y = data[target_column]
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                
                st.write("Training the model...")
                
                # Train model
                model = RandomForestClassifier()
                model.fit(X_train, y_train)
                
                # Predict and display results
                y_pred = model.predict(X_test)
                
                st.write("Model Training Results:")
                st.write("Classification Report:")
                st.text(classification_report(y_test, y_pred))
        else:
            st.warning("Please select features and the target variable.")
