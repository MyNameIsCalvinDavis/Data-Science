# Overview

# About Dataset

https://www.kaggle.com/datasets/rohit265/credit-card-eligibility-data-determining-factors

The Credit Card Eligibility Dataset: Determining Factors is a comprehensive collection of variables aimed at understanding the factors that influence an individual's eligibility for a credit card. This dataset encompasses a wide range of demographic, financial, and personal attributes that are commonly considered by financial institutions when assessing an individual's suitability for credit.

Each row in the dataset represents a unique individual, identified by a unique ID, with associated attributes ranging from basic demographic information such as gender and age, to financial indicators like total income and employment status. Additionally, the dataset includes variables related to familial status, housing, education, and occupation, providing a holistic view of the individual's background and circumstances.

|Feature | Description |
| ---------- | ----------------------- |
|ID | An identifier for each individual (customer). |
|Gender | The gender of the individual. |
|Own_car | A binary feature indicating whether the individual owns a car. |
|Own_property | A binary feature indicating whether the individual owns a property. |
|Work_phone | A binary feature indicating whether the individual has a work phone. |
|Phone | A binary feature indicating whether the individual has a phone. |
|Email | A binary feature indicating whether the individual has provided an email address. |
|Unemployed | A binary feature indicating whether the individual is unemployed. |
|Num_children | The number of children the individual has. |
|Num_family | The total number of family members. |
|Account_length | The length of the individual's account with a bank or financial institution. |
|Total_income | The total income of the individual. |
|Age | The age of the individual. |
|Years_employed | The number of years the individual has been employed. |
|Income_type | The type of income (e.g., employed, self-employed, etc.). |
|Education_type | The education level of the individual. |
|Family_status | The family status of the individual. |
|Housing_type | The type of housing the individual lives in. |
|Occupation_type | The type of occupation the individual is engaged in. |
|Target | The target variable for the classification task, indicating whether the individual is eligible for a credit card or not (e.g., Yes/No, 1/0). |

# Lessons Learned
My variables are named poorly
feature importance on scaled data and not unscaled data
Once i started pivoting between SMOTE and other samplers and classifiers, I got disorganized
for SMOTE I didn't down the majority class as is recommended
ROS seems to downsample the majority class but I can't find documentation that says it should do this, I thought it would only randomly upsample the minority class
# Overview
## Process
## Analysis
## Meta Analysis




## Notes to be digested
SMOTE every iteration of feature importance, scale every feature
Got axis mixed up for plugging data into SMOTE, was thinking rows but its actually cols
Data not prepared in advance to handle easy representation of numerical / categorical data
Fit classifier with
    
- X: Train / SMOTE / Scaled / Top X features (multi col)
- Y: Train / SMOTE / (single col)
- Training data should be Training / Top features / SMOTE / scaled data
- It is generally unnecessary to scale the Target column

Score classifier with
- X: Test / Scaled / Top X
- Y: Test
- Test data should not apply SMOTE due to train/test leakage

In doing the permutation importance, I used scaled training data instead of raw training data, leading me to believe that the feature importance was being interpreted incorrectly since my permuted results labeled nearly all of the features as unimportant. Once I began implementing a soltution, I realized my error, but am including this information here because it's interesting.

    Although the impurity feature importance suggests a high importance for some features, the permutation-based feature importance does not. This phenomenon is described in greater detail here:

    https://scikit-learn.org/stable/modules/permutation_importance.html#misleading-values-on-strongly-correlated-features

    and it's deeper investigation of this topic, here

    https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-multicollinear-py

    Long story short, when a dataset has variables that "contains multicollinear features, the permutation importance shows that none of the features are important, in contradiction with the high test accuracy.". This issue can be rectified by "performing hierarchical clustering on the Spearman rank-order correlations, picking a threshold, and keeping a single feature from each cluster".


