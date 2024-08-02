# Deployment_ML_Model
## Machine Learning Application
This repository contains a Streamlit-based web application for performing machine learning tasks. The application allows users to upload data, specify the columns to be used for training a model, and view the results of the analysis.

## Features

Data Upload: Upload your dataset in CSV format.
Column Specification: Select which features to use for model training.
Model Training: Train a machine learning model on the selected features.
Results Viewing: Display the results of the analysis, including performance metrics.

## Instructions

Upload Data: Upload your dataset using the file uploader.
Select Columns: Choose the columns to be used for model training.
Train Model: Train the machine learning model and view the results.

## Docker Containerization

The application is containerized using Docker. Follow these steps to build and run the Docker container:

Build the Docker image:
bash
Copy code
docker build -t ml-app:latest .

Run the Docker container:
bash
Copy code
docker run -p 8501:8501 ml-app:latest

## Deployment

The application can be deployed using the Docker image available on Docker Hub.
