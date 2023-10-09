# Heritage Housing Prediction

Live Site: [Live Site](https://github.com/USERNAME/REPOSITORY/blob/main/README.md)

Link to Repository: [Repository](https://github.com/YourUsername/YourRepository/blob/main/README.md)

## Table of Content

- [Heritage Housing Prediction](#heritage-housing-prediction)
  - [Table of Content](#table-of-content)
  - [Introduction](#introduction)
  - [CRISP-DM Workflow](#crisp-dm-workflow)
    - [Epic 1: Business Understanding](#epic-1-business-understanding)
    - [Epic 2: Data Understanding](#epic-2-data-understanding)
    - [Epic 3: Data Preparation](#epic-3-data-preparation)
    - [Epic 4: Modeling \& Evaluation](#epic-4-modeling--evaluation)
    - [Epic 5: Deployment](#epic-5-deployment)
  - [Business Requirements](#business-requirements)
    - [Project Objectives](#project-objectives)
    - [User Stories](#user-stories)
  - [Dataset Content](#dataset-content)
  - [Hypothesis, Proposed Validation, and Actual Validation](#hypothesis-proposed-validation-and-actual-validation)
  - [Mapping the Business Requirements to Data Visualizations and ML Tasks](#mapping-the-business-requirements-to-data-visualizations-and-ml-tasks)
    - [Business Requirement 1: Data Exploration and Correlation Analysis](#business-requirement-1-data-exploration-and-correlation-analysis)
    - [Business Requirement 2: Predictive Modeling and Data Analysis](#business-requirement-2-predictive-modeling-and-data-analysis)
    - [Business Requirement 3: User-Friendly Online App and Deployment](#business-requirement-3-user-friendly-online-app-and-deployment)
  - [Business Requirement 2](#business-requirement-2)
    - [ML model](#ml-model)
  - [Business Requirement 3](#business-requirement-3)
    - [Dashboard Design](#dashboard-design)
    - [Page 1: Project Summary](#page-1-project-summary)
    - [Page 2: Sale Price Study](#page-2-sale-price-study)
    - [Page 3: Sale Price Prediction](#page-3-sale-price-prediction)
    - [Page 4: Hypothesis and Validation](#page-4-hypothesis-and-validation)
    - [Page 5: Machine Learning Model](#page-5-machine-learning-model)
  - [Unfixed Bugs](#unfixed-bugs)
  - [PEP8 Compliance Testing](#pep8-compliance-testing)
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
  - [Technologies](#technologies)
    - [Development and Deployment](#development-and-deployment)
    - [Main Data Analysis and Machine Learning](#main-data-analysis-and-machine-learning)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Introduction

This Machine Learning Project was developed as the fifth portfolio project during the Code Institute's Diploma in Full Stack Development. It covers the Predictive Analytics specialization.

The Machine Learning, Data Analysis toolkit & neural networks are applied to a real estate dataset with the specific purpose of allowing a user to predict the sale value of a property based on certain features of the home. It also allows the user to see how certain features of a home correlate with the sale price of the home.

## CRISP-DM Workflow

The project was developed using the Cross Industry Standard Process for Data Mining. This follows several iterations over well-defined steps:

### Epic 1: Business Understanding

- This initial phase revolves around comprehending the business problem at hand. It involves defining the objectives of the data mining project, understanding what the business hopes to achieve, and establishing success criteria. In this epic, you aim to align data analysis with the specific goals and requirements of the business.

### Epic 2: Data Understanding

- Once the business objectives are clear, the focus shifts to acquiring the relevant data. This stage involves gathering data from various sources and getting familiar with its structure and quality. Data exploration and initial insights help ensure that the collected data is suitable for analysis.

### Epic 3: Data Preparation

- This epic revolves around the transformation and preparation of the data for modeling. It includes tasks such as data cleaning, feature engineering, and handling missing values. The goal is to create a well-structured dataset that can be used effectively by machine learning algorithms.

### Epic 4: Modeling & Evaluation

- In this stage, the actual modeling takes place. It involves selecting appropriate machine learning algorithms, training models, and assessing their performance. Evaluation metrics are used to determine how well the models align with the business objectives. Iterative experimentation is often part of this phase.

### Epic 5: Deployment

- Once a satisfactory model is built, it needs to be deployed in a real-world context. This phase includes implementing the model into operational systems and continuously monitoring its performance. Ongoing maintenance and retraining are essential to ensure that the model remains effective and aligned with the evolving business goals.
- Develop the Streamlit app that will satisfy the business requirements determined in collaboration with the client and deploy the app online. The app is deployed on Heroku, and the process is described in the Deployment section below.

These steps can be matched up nicely to 6 Epics in the Agile development process. As we move along the pipeline of the development process, we may flow back and forth between stages/epics as we learn new insights and have to revisit previous steps to refine the development while ultimately moving towards the final delivery of a product that satisfies the user's/client's requirements.

## Business Requirements

A client who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, has requested help in maximizing the sales price for the inherited properties.

### Project Objectives

**Objective 1: Correlation Analysis**
- Discover how various attributes of homes correlate with their sale prices in Ames, Iowa.
- Identify which attributes have the most significant impact on the sale price.
- Provide data visualizations to illustrate these correlations.

**Objective 2: Price Prediction**
- Develop a predictive model for estimating house sale prices in Ames, Iowa.
- Ensure the model achieves an R2 value of 0.8 or higher for accurate predictions.

**Objective 3: Deployed User-Friendly App**
- Create a user-friendly and easily accessible online app.
- Enable users to explore correlations between home features and sale prices.
- Allow users to predict the sale price of any home based on specific features.

### User Stories

**User Story 1: Understanding Correlations**
- As an end user, I want to explore how different features of a home are related to its sale price.
- This will help me understand the importance of various home attributes in determining the sale price.

**User Story 2: Price Estimation**
- As an end user, I want the ability to estimate the likely sale price of a home based on its specific features.
- This feature will provide valuable insights into the potential value of a home in the Ames, Iowa area.

**User Story 3: User-Friendly Access**
- As an end user, I want easy online access to the necessary information.
- This includes user-friendly access to data visualizations and a prediction tool that can be used at any time.


## Dataset Content

The dataset used in this project is sourced from Kaggle and comprises approximately 1.5 thousand rows of housing records from Ames, Iowa. It provides comprehensive information on various attributes of these houses, including features related to floor area, basements, garages, kitchens, lots, porches, wood decks, year built, and more. Additionally, the dataset includes the respective sale prices of these houses. Notably, the houses in the dataset were built between the years 1872 and 2010.




| Variable       | Meaning                                                         | Units           |
|----------------|-----------------------------------------------------------------|-----------------|
| 1stFlrSF       | First Floor square feet                                         | 334 - 4692      |
| 2ndFlrSF       | Second-floor square feet                                       | 0 - 2065        |
| BedroomAbvGr  | Bedrooms above grade (does NOT include basement bedrooms)     | 0 - 8           |
| BsmtExposure  | Refers to walkout or garden level walls                         | Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement |
| BsmtFinType1  | Rating of basement finished area                               | GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement |
| BsmtFinSF1    | Type 1 finished square feet                                    | 0 - 5644        |
| BsmtUnfSF     | Unfinished square feet of basement area                        | 0 - 2336        |
| TotalBsmtSF   | Total square feet of basement area                             | 0 - 6110        |
| GarageArea    | Size of garage in square feet                                  | 0 - 1418        |
| GarageFinish  | Interior finish of the garage                                  | Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage |
| GarageYrBlt   | Year garage was built                                           | 1900 - 2010     |
| GrLivArea     | Above grade (ground) living area square feet                   | 334 - 5642      |
| KitchenQual   | Kitchen quality                                                | Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor |
| LotArea       | Lot size in square feet                                        | 1300 - 215245    |
| LotFrontage   | Linear feet of street connected to property                     | 21 - 313       |
| MasVnrArea    | Masonry veneer area in square feet                              | 0 - 1600        |
| EnclosedPorch | Enclosed porch area in square feet                             | 0 - 286         |
| OpenPorchSF   | Open porch area in square feet                                | 0 - 547         |
| OverallCond   | Rates the overall condition of the house                       | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor |
| OverallQual   | Rates the overall material and finish of the house             | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor |
| WoodDeckSF    | Wood deck area in square feet                                  | 0 - 736         |
| YearBuilt     | Original construction date                                      | 1872 - 2010     |
| YearRemodAdd  | Remodel date (same as construction date if no remodeling or additions) | 1950 - 2010  |
| SalePrice     | Sale Price                                                     | 34900 - 755000  |

## Hypothesis, Proposed Validation, and Actual Validation

In order to fulfill the business requirements and in discussion with the client, the following hypotheses have been developed:

In order to meet the project's business requirements and following discussions with the client, several hypotheses were formulated and subsequently validated:

**Hypothesis 1: Correlation with Sale Price**

- **Hypothesis:** We hypothesized that a property's sale price correlates strongly with a subset of features in the dataset.
- **Validation:** This hypothesis was confirmed through an extensive correlation study conducted on the dataset. The results were presented in the app, demonstrating significant correlations between specific features and the sale price.

**Hypothesis 2: Strongest Correlation Features**

- **Hypothesis:** We postulated that the correlation between sale price and home features is most prominent with common attributes, such as total square footage, overall condition, and overall quality.
- **Validation:** The extensive correlation study corroborated this hypothesis, identifying the five features with the strongest correlation to Sale Price. These key features were found to be 'OverallQual,' 'GrLivArea,' 'GarageArea & year built,' which are prevalent in the majority of homes.

**Hypothesis 3: Predictive Model Accuracy**

- **Hypothesis:** We proposed that it is feasible to predict a property's sale price with an R2 value of at least 0.8.
- **Validation:** To validate this hypothesis, we developed a predictive model and optimized it using data modeling tools. Subsequently, we evaluated the model's performance against the required criteria. The model surpassed expectations, achieving R2 values of 0.835 or higher for both the test and training datasets.

These hypotheses and their validation provide a strong foundation for the project's approach and demonstrate the successful achievement of critical project objectives.


## Mapping the Business Requirements to Data Visualizations and ML Tasks

### Business Requirement 1: Data Exploration and Correlation Analysis

**Objective:** Uncover insights into the factors influencing property sale prices in Ames, Iowa through data exploration and correlation analysis.

- **Data Exploration:** Investigate the dataset to understand the relationships between various property attributes and sale prices in the Ames area.
- **Correlation Analysis:** Conduct correlation studies, including Pearson and Spearman methods, to reveal connections between dataset variables and sale prices.
- **Data Visualization:** Create data visualizations to effectively represent the most relevant insights related to sale prices.

### Business Requirement 2: Predictive Modeling and Data Analysis

**Objective:** Develop a predictive model for property sale prices in Ames, Iowa.

- **Regression Modeling:** Construct a regression model with the sale price as the target variable to predict property sale prices.
- **Optimization and Evaluation:** Optimize the regression model through a series of techniques and evaluations to achieve a minimum R2 value of 0.8, ensuring accurate predictions.

### Business Requirement 3: User-Friendly Online App and Deployment

**Objective:** Create an intuitive and accessible online application for data analysis and price predictions.

- **App Development:** Build an interactive application using Streamlit, providing the client with features for data analysis and visualization.
- **Prediction Feature:** Implement a feature that enables the client to predict property sale prices for her inherited properties and other properties in Ames, Iowa, based on essential features.
- **Deployment:** Deploy the application using Heroku, making it readily available online for users.

These business requirements outline the core objectives of the project, encompassing data exploration, predictive modeling, and the development of a user-friendly online application.
.

## Business Requirement 2
### ML model

**Objective:** Develop a machine learning model to predict the sale price, in dollars, for residential properties in Ames, Iowa. The target variable is continuous and unidimensional, making it a regression task.

- **Client's Need:** Our primary goal is to provide the client with a robust tool for accurately estimating the sale prices of homes in Ames, Iowa. This is especially crucial for her inherited properties, which are of particular concern.

**Model Success Metrics:**

- **R2 Score:** The model's success will be measured by its R2 score, with a minimum threshold of 0.8 on both the training and test datasets.
- **Failure Criteria:** If, after 12 months of usage, the model's predictions deviate by more than 50% from the actual sale prices more than 30% of the time, or if the R2 score falls below 0.8, the model will be considered a failure.

**Output Format:** The model provides a continuous sale price value in dollars, offering flexibility for private homeowners and clients to utilize the online app. Real estate agents can also benefit by using the app to quickly estimate sale prices during live communication with prospective clients.

**Training Data Source:** The model is trained on a publicly available dataset, comprising approximately 1,500 property sales records. The dataset features a single target variable, sale price, while the remaining 23 variables are considered features.

This machine learning business case outlines the objectives, success criteria, and applications of the model in predicting property sale prices, serving the client's needs effectively.

## Business Requirement 3
### Dashboard Design

The project is developed as a Streamlit dashboard, catering to the third Business Requirement. It comprises several pages, each designed to serve specific purposes:

### Page 1: Project Summary

- **Objective:** This page provides a high-level overview of the project, serving as a central hub for users to understand the project's purpose and key details.
- **Content:**
  - Project's purpose statement.
  - Explanation of project terms and jargon.
  - A brief description of the dataset.
  - Statement of business requirements.
  - Links to additional information.
- **Screenshot:** ![summary](/assets/images/summary.png)

### Page 2: Sale Price Study

- **Objective:** This page fulfills the first Business Requirement, enabling users to explore correlations between property features and sale prices in Ames, Iowa.
- **Content:**
  - Option to display:
    - A sample of data from the dataset.
    - Pearson and Spearman correlation plots between features and sale prices.
    - Histograms and scatterplots of the most influential predictive features.
    - Predictive Power Score analysis.
- **Screenshot:** ![Study](/assets/images/study.png)

### Page 3: Sale Price Prediction

- **Objective:** This page satisfies the second Business Requirement, offering users the capability to predict property sale prices.
- **Content:**
  - Feature input for property attributes to generate sale price predictions.
  - Display of the predicted sale price.
  - Feature for predicting sale prices for the client's specific properties, including inherited properties.
- **Screenshot:** ![predict](/assets/images/predict.png)


### Page 4: Hypothesis and Validation

- **Objective:** This page includes a comprehensive list of project hypotheses and how they were validated.
- **Content:**
  - List of project hypotheses and their validation outcomes.
- **Screenshot:** [hypothesis](/assets/images/hyptothesis.png)

### Page 5: Machine Learning Model

- **Objective:** This page provides insights into the machine learning pipeline used for model training.
- **Content:**
  - Information about the ML pipeline, including training details.
  - Demonstration of feature importance.
  - Review of the pipeline's performance.
- **Screenshot:** [ml](/assets/images/ml.png)

This structured approach ensures that users can easily navigate and engage with the project, exploring its various facets and capabilities.
## Unfixed Bugs




## PEP8 Compliance Testing


## Deployment

### Heroku Deployment




## Technologies

### Development and Deployment


### Main Data Analysis and Machine Learning



- **GradientBoostedRegressor:**

## Credits


## Media

- all images were taken from shutterstock


## Acknowledgements

