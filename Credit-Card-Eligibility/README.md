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

# Process
# Analysis
# Meta Analysis / Lessons Learned

Like all projects, I learned a lot while going through and in hindsight, would have preferred to reorganize / redo the project in certain ways. In this section I explain those ways and have some feedback for myself in the next project.

### Scope the project better
This project started as a simple classification example with a RandomForestClassifier. I saw the data science competitions on Kaggle and wanted to reproduce / improve some of the datasets I saw. In doing so, I learned about SMOTE, and how SMOTE may actually be a bad way to organize or interpolate data. So then I expanded the project into a SMOTE decomposition, but then, maybe SMOTE works better or worse for certain classifiers? So now we're also doing GradientBoostClassifier. But is all sampling bad (or good), or is it just SMOTE? Now we're doing RandomOverSampling.

The worst part of all of this is, it's still a bad study. I should drill down and more specifically examine a single variable instead of multiple. For example, if I was interested in identifying the effectiveness of smote, I should do a full test on GradientBoostClassifier with/without SMOTE against multiple datasets, with multiple types of data, with lots of other variables modified & triggered, with intelligent design, hypothesis, and testing of PRO or ANTI SMOTE resources I found online. I should also understand the [original paper for SMOTE]([url](https://arxiv.org/pdf/1106.1813)) and SMOTENC, understand what it's describing and what problem it's trying to solve, and then identify if it actually solves that problem. However I'm not getting paid to do that and I have a full time job.

For example, there's a lot of literature that suggests SMOTE is just bad ML practice, and smarter people than I have done studies on it. See here: [Link1]([url](https://datascience.stackexchange.com/questions/106461/why-smote-is-not-used-in-prize-winning-kaggle-solutions)) / [Link2]([url](https://stats.stackexchange.com/questions/357466/are-unbalanced-datasets-problematic-and-how-does-oversampling-purport-to-he)) / [Link3]([url](https://arxiv.org/abs/2201.08528))

So maybe I shouldn't feel so bad. It looks like real scientists and not frauds (like myself) have identified this as a problem, and this was really just a fun side project anyway.

My variables are named poorly
feature importance on scaled data and not unscaled data
Once i started pivoting between SMOTE and other samplers and classifiers, I got disorganized
for SMOTE I didn't down the majority class as is recommended
ROS seems to downsample the majority class but I can't find documentation that says it should do this, I thought it would only randomly upsample the minority class


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


