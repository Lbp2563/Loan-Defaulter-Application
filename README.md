# Loan Defaulter Application

![Loan-Defaulter-Application](https://socialify.git.ci/Lbp2563/Loan-Defaulter-Application/image?language=1&owner=1&name=1&stargazers=1&theme=Light)

## Introduction
The Loan Defaulter Application is a machine learning project aimed at predicting whether a bank loan applicant will default on their loan. The application uses a pre-trained model to make predictions based on various input features such as applicant income, loan amount, loan duration, credit history, and more.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)

## Installation
To run this application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Lbp2563/Loan-Defaulter-Application.git
    cd Loan-Defaulter-Application
    ```
    
2. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage
To use the Loan Defaulter Application, follow these steps:

1. Enter the required information such as Full Name, Account Number, Gender, Marital Status, Dependents, Education, Employment Status, Monthly Income, Loan Amount, Loan Duration, Credit History, and Property Area.

2. Click on the "Submit" button to get the prediction.

3. The application will display whether the applicant is eligible for the loan based on the prediction model.

## Features
- User-friendly interface for inputting applicant details.
- Predicts loan eligibility based on the input features.
- Displays prediction results in a clear and concise manner.

## Dependencies
- Streamlit
- Pillow 
- Pickle
- Scikit-learn

## Configuration
The model for prediction is stored in a pickle file (`model.pkl`). Ensure this file is present in the root directory of the project.

## Documentation
For detailed documentation, please refer to the Jupyter notebook `loan_prediction.ipynb` provided in the repository. This notebook contains the data preprocessing steps, model training, and evaluation processes.

## Examples
Here is an example of how to use the application:

1. Run the application:
    ```bash
    streamlit run app.py
    ```

2. Enter the applicant details:
    - Full Name: John Doe
    - Account Number: 123456789
    - Gender: Male
    - Marital Status: Yes
    - Dependents: 2
    - Education: Graduate
    - Employment Status: No
    - Applicant's Monthly Income: 5000
    - Co-Applicant's Monthly Income: 2000
    - Loan Amount: 150000
    - Loan Duration: 360
    - Credit History: 1
    - Property Area: Urban

3. Click "Submit" to get the prediction.

## Troubleshooting
- Ensure that all required dependencies are installed.
- Verify that the `model.pkl` file is present in the root directory.
- Check the console for any error messages if the application does not run as expected.

## Contributors
- [Lakshin Pathak](https://github.com/Lbp2563)

