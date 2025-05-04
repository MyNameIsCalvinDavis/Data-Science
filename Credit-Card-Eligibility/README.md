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

### 1. Scope the project better
This project started as a simple classification example with a RandomForestClassifier. I saw the data science competitions on Kaggle and wanted to reproduce / improve some of the datasets I saw. In doing so, I learned about SMOTE, and how SMOTE may actually be a bad way to organize or interpolate data. So then I expanded the project into a SMOTE decomposition, but then, maybe SMOTE works better or worse for certain classifiers? So now we're also doing GradientBoostClassifier. But is all sampling bad (or good), or is it just SMOTE? Now we're doing RandomOverSampling.

The worst part of all of this is, it's still a bad study. I should drill down and more specifically examine a single variable instead of multiple. For example, if I was interested in identifying the effectiveness of smote, I should do a full test on GradientBoostClassifier with/without SMOTE against multiple datasets, with multiple types of data, with lots of other variables modified & triggered, with intelligent design, hypothesis, and testing of PRO or ANTI SMOTE resources I found online. I should also understand the [original paper for SMOTE]([url](https://arxiv.org/pdf/1106.1813)) and SMOTENC, understand what it's describing and what problem it's trying to solve, and then identify if it actually solves that problem. However I'm not getting paid to do that and I have a full time job.

For example, there's a lot of literature that suggests SMOTE is just bad ML practice, and smarter people than I have done studies on it. See here: [Link1]([url](https://datascience.stackexchange.com/questions/106461/why-smote-is-not-used-in-prize-winning-kaggle-solutions)) / [Link2]([url](https://stats.stackexchange.com/questions/357466/are-unbalanced-datasets-problematic-and-how-does-oversampling-purport-to-he)) / [Link3]([url](https://arxiv.org/abs/2201.08528))

So maybe I shouldn't feel so bad. It looks like real scientists and not frauds (like myself) have identified this as a problem, and this was really just a fun side project anyway.

### 2. Organize my code / Make a plan
Unlike traditional software engineering, exploratory data science has been more difficult to effectively organize, because you don't know what you don't know. If I had known in advance I was doing two classifiers, three oversampling techniques, and varied data mangling, I would have described an object to the effect of:

```python

class Experiment:
    def __init__(self, classifier, sampler=None, data):
        ...
    def preprocessor(self):
        # Data processing based on passed in instance vars
        # One-hot encoding, etc
    def train(self, data):
        # Train a classifier with data
    def SMOTE(self, dataset):
        # return SMOTE-ified dataset
    def SMOTENC(self,dataset):
        # return SMOTENC-ified dataset
```

Or something. Not perfect, but a lot better than the copy-paste hell my code looks like right now. Iterative design is ugly.

### 3. Technical Errors:
- #### Do feature importance on scaled data and not unscaled data
Really this is a misunderstanding of process. Feature importance measures happen after training, and you need to train on scaled or normalized data. Training on unscaled or non-normalized data produces inaccurate results.

- #### For SMOTE I didn't explitly downsample the majority class as is recommended
For some reason the sklearn developers have decided to implement SMOTE against default recommendations in the paper. Parameters default to 'auto' which default to **'not majority': resample all classes but the majority class**.

I was just lazy, and I could still fix it, I just don't care to. Personal project, I'm allowed to cut corners if I feel like it.

- #### RandomOverSampler seems to downsample the majority class but I can't find documentation that says it should do this, I thought it would only randomly upsample the minority class
Unlike SMOTE, I found that the majority class was downsampled in the RandomOverSampler class, but no documentation describes either WHY they have chosen to do so (perhaps because of the aforementioned SMOTE paper) or how to disable or change this feature.

I wish the class had more granularity in describing what to resample. [RandomOverSampler]([url](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html)) uses the same paramaters as SMOTE for sampling technique, but for example describes "**not majority**" as the "_resampling of all non-majority classes_", but resample in which direction? Downsample? Upsample? There's no way to tell, maybe it does both depending on the context.

- #### SMOTE every iteration of feature importance, scale every feature
Originally I didn't realize SMOTE is for continuous (numerical) data only. Other versions are SMOTE-N & SMOTE-NC which have to be one-hot-encoded with any categorical data. I forget what I did originally, but I didn't realize this and had to rewrite the code to do it correctly. It threw no errors, it just gave me bad results. 

## Notes to be digested

Fit classifier with
    
- X: Train / SMOTE / Scaled / Top X features (multi col)
- Y: Train / SMOTE / (single col)
- Training data should be Training / Top features / SMOTE / scaled data
- It is generally unnecessary to scale the Target column

Score classifier with
- X: Test / Scaled / Top X
- Y: Test
- Test data should not apply SMOTE due to train/test leakage


