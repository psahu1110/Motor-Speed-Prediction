# Motor Speed Prediction Project 
# Project Description

Dataset Import and Initial Analysis

1. Importing the Dataset -
The initial step involved importing the dataset provided in Excel file.

2. Exploratory Data Analysis (EDA) - 
Performed exploratory data analysis to understand the data better.
Utilized Pandas functions such as head, tail, and shape for initial insights.

3. Handling Missing Values - 
Identified and addressed missing values using the fill NA function.

4. Dropping Unnecessary Columns -
Removed columns deemed less important for analysis.

Feature Selection and Correlation Analysis

1. Correlation Analysis-
Investigated the correlation between features using statistical methods.
Visualized feature correlations using a heatmap for better understanding.

2. Feature Selection-
Choose features with a high correlation with the target output for model building.

Outlier Handling and Multicollinearity

1. Outlier Detection-
Checked for outliers in the dataset using boxplots for each feature.

2. Outlier Treatment-
Considered the impact of outliers on the dataset and decided to handle them using the interquartile range (IQR) method.

3. Multicollinearity Check-
Examined multicollinearity issues within the dataset.

4. Feature Removal to Address Multicollinearity-
Dropped features contribute to multicollinearity.

Model Training and Evaluation

1. Data Splitting - 
Split the dataset into training and testing sets for model evaluation.

2. Model Training-
Utilized the Random Forest algorithm for model training.

3. Evaluation Metrics-
Assessed model performance using mean squared error and R-squared (r2) score.

Deployment
1. Model Deployment-
Deployed the trained model using Streamlit for practical use.

![Result](https://github.com/psahu1110/Sentiment-Analysis-on-Financial-Statements/assets/114385902/3b1cbd79-200a-4d4f-b85c-a4b96fc79823)


# Conclusion

This project involved a comprehensive analysis of motor speed prediction, addressing issues such as missing values, outliers, and multicollinearity. The Random Forest algorithm was employed for accurate predictions, and the model was successfully deployed using Streamlit for real-world applications. The documentation provides an overview of the project's steps, from data import to model deployment, emphasizing the key decisions made throughout the process.
