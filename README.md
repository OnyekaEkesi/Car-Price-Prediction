# Project Name: Car Price Prediction

## Introduction

In the dynamic automotive market, determining the value of a car based on its features is crucial for buyers and sellers alike. Car Price Prediction leverages machine learning to provide accurate estimates of car prices, aiding informed decision-making for both parties.

**Detailed Report:** For an in-depth exploration of the project, read the detailed report on my Medium page: [Revving Up Insights: Predicting Car Prices with Regression Models and Model Interpretability](https://medium.com/@onyekaekesi/revving-up-insights-predicting-car-prices-with-regression-models-and-model-interpretability-2c4b86266a28).

### Table of Content

1. [Project Name](#project-name)
2. [Project Overview](#project-overview)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
   - [Data Processing for Machine Learning](#data-processing-for-machine-learning)
   - [Feature Engineering](#feature-engineering)
   - [Feature Selection and Dimensionality Reduction](#feature-selection-and-dimensionality-reduction)
   - [Model Building](#model-building)
   - [Model Evaluation and Analysis](#model-evaluation-and-analysis)
   - [Visualization](#visualization)
   - [Results and Potential Enhancements](#results-and-potential-enhancements)
   - [Deployment](#deployment)
   - [Benefits](#benefits)
   - [Contributors](#contributors)

## Project Overview

Car Price Prediction is a machine learning project designed to predict car prices based on features such as make, model year, mileage, condition, fuel type, and transmission type. The project provides insights into the key factors influencing car prices and applies advanced machine learning techniques to predict the market value of a car.

## Getting Started

These instructions will help you set up and run the project locally for development and testing.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- **Python:** The project is written in Python, so Python installation is essential. You can download Python from [python.org](https://www.python.org/) or use package managers like Anaconda or Miniconda.

## Setup Instructions

1. Clone the project repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended) to isolate dependencies.
4. Activate the virtual environment and install the project dependencies.

## Data Processing for Machine Learning

The data processing phase focuses on preparing the data for machine learning:

- **Noise Detection and Handling:** Identify and address noisy data points.
- **Handling Missing Values:** Use techniques such as imputation to handle missing data.
- **Outlier Detection and Removal:** Identify and remove outliers that may distort model predictions.
- **Categorical Encoding:** Convert categorical variables into numerical formats using encoding techniques.
- **Rescaling:** Standardize or normalize numerical data to ensure uniformity.
- **Data Splitting:** Divide the data into predictor variables (features) and target variables (car prices).
- **Train/Validation/Test Split:** Split the data into training, validation, and test folds for model evaluation.

## Feature Engineering

Feature engineering is the process of deriving new features based on domain knowledge to improve model performance:

- **Domain Knowledge Features:** Create new features based on insights from the automotive industry (e.g., age of the car, Standard Description etc).
- **Polynomial/Basis Functions:** Introduce polynomial features to capture non-linear relationships between variables.
- **Interaction Features:** Create interaction terms to model complex relationships between different features.

## Feature Selection and Dimensionality Reduction

In this step, we focus on selecting the most relevant features and reducing dimensionality:

- **Manual Feature Selection:** Use domain knowledge and exploratory data analysis (EDA) to manually select relevant features.
- **Automated Feature Selection:** Apply algorithms to automatically select the most impactful features.
- **Dimensionality Reduction:** Reduce the number of features using techniques like PCA (Principal Component Analysis) to avoid overfitting and improve model performance.

## Model Building

This phase focuses on selecting and tuning the right machine learning algorithms:

- **Algorithm Selection:** Choose suitable algorithms based on the nature of the problem (e.g., regression models, random forest etc).
- **Model Fitting and Tuning:** Fit the model and tune hyperparameters using techniques like grid search to optimize performance.
- **Model Ranking and Selection:** Rank models based on evaluation metrics (e.g., MSE, RMSE, MAE) and assess underfitting and overfitting.
- **Ensemble Models:** Combine the best-performing models into an ensemble to improve prediction accuracy.

## Model Evaluation and Analysis

Once models are trained, it's important to evaluate their performance:

- **Cross-Validation:** Evaluate models using k-fold cross-validation to ensure robustness and avoid overfitting.
- **True vs Predicted Plots:** Generate plots comparing true vs predicted values to visually assess model accuracy.
- **Feature Importance:** Analyze feature importance to identify which variables have the greatest impact on car price predictions, SHAP Plots, Partial Dependency Plots and Model Coefficient Plots were used in this project .

## Visualization

Visualization of the model performance and streamlit app prediction, other visuals are found in the detailed report on Medium, find the link above:

**MSE Comparison Plot**
<p align = 'center'> 
<img width='700' height='400' src = 'https://github.com/OnyekaEkesi/Car-Price-Prediction/blob/main/result.jpg?raw=true'>
</p>  <br>

**Streamlit App Prediction**
<p align = 'center'> 
<img width='700' height='400' src = 'https://github.com/OnyekaEkesi/Car-Price-Prediction/blob/main/appPic1.jpg?raw=true'>
</p>  <br>

<p align = 'center'> 
<img width='700' height='400' src = 'https://github.com/OnyekaEkesi/Car-Price-Prediction/blob/main/appPic2.jpg?raw=true'>
</p>  <br>

## Results and Potential Enhancements

This project uses a machine learning model to predict car prices based on input features. While the current implementation provides reliable predictions, there is room for improvement:

- **Hyperparameter Tuning:** Optimize the model for better accuracy.
- **Feature Engineering:** Add additional relevant features to help improve model performance.
- **Model Exploration:** Experiment with advanced models like neural networks.

## Deployment

The model is served through a **Streamlit** app, which allows users to input car features and get real-time price predictions. 

To run the app locally, follow these steps:

1. Install Streamlit: `pip install streamlit`
2. Run the app: `streamlit run app.py`
3. Open the app in your browser (default address: http://localhost:8501).

Further deployment to cloud platforms like AWS or Azure ensures scalability and accessibility to a wider audience.

## Benefits

- **Better Decision-Making:** Enables buyers and sellers to make informed decisions based on accurate price predictions.
- **Market Insights:** Helps car dealerships understand market trends and pricing strategies.
- **Efficiency:** Reduces the time and effort involved in manual price estimations.

## Contributors

This is an individual project carried out by Onyekachukwu Ekesi, showcasing expertise in machine learning and predictive analytics.

**Connect with me:**

- [LinkedIn](https://linkedin.com/in/onyekachukwu-ekesi/)
- [Medium Article](https://medium.com/@onyekaekesi/revving-up-insights-predicting-car-prices-with-regression-models-and-model-interpretability-2c4b86266a28)
