https://stats.stackexchange.com/questions/357466/are-unbalanced-datasets-problematic-and-how-does-oversampling-purport-to-he
https://arxiv.org/abs/2201.08528
https://stats.stackexchange.com/questions/285231/what-problem-does-oversampling-undersampling-and-smote-solve
https://stats.stackexchange.com/q/283170/1352
https://stats.stackexchange.com/questions/283170/when-is-unbalanced-data-really-a-problem-in-machine-learning

From [the first link](https://stats.stackexchange.com/questions/357466/are-unbalanced-datasets-problematic-and-how-does-oversampling-purport-to-he):
There _is_ a class imbalance problem, but it is not caused by the imbalance _per se_, but because there are too few examples of the minority class to adequately describe it's statistical distribution. As mentioned in the question, this means that the parameter estimates can have high variance, which is true, but that can give rise to a bias in favour of the majority class (rather than affecting both classes equally). In the case of logistic regression, this is discussed by King and Zeng,

[3](https://j.mp/2oSEnmf) Gary King and Langche Zeng. 2001. “Logistic Regression in Rare Events Data.” Political Analysis, 9, Pp. 137–163. [https://j.mp/2oSEnmf](https://j.mp/2oSEnmf)

In my experiments I have found that sometimes there can be a bias in favour of the minority class, but that is caused by wild over-fitting where the class-overlap dissapears due to random sampling, so that doesn't really count and (Bayesian) regularisation ought to fix that

The good thing is that MLE is asymptotically unbiased, so we can expect this bias against the minority class to go away as the overall size of the dataset increases, _regardless_ of the imbalance.

As this is an estimation problem, anything that makes estimation more difficult (e.g. high dimensionality) seems likely to make the class imbalance problem worse.

Note that probabilistic classifiers (such as logistic regression) and proper scoring rules will not solve this problem as "popular statistical procedures, such as logistic regression, can sharply underestimate the probability of rare events" [3](https://j.mp/2oSEnmf). This means that your probability estimates will not be well calibrated, so you will have to do things like adjust the threshold (which is equivalent to re-sampling or re-weighting the data).

---
One common real world reason you want to up-sample rare outcomes: limited data capacity.

Suppose you have an outcome that only happen with p=10−3

. If you have 1000 columns of features available, note that if you _don't_ upweight your positive results, then you need to sample 106 rows of data (which is 109

values, likely to strain most desktops) in order to get 1 positive outcome for every column. With this amount of data, you are very likely to be excessively overfit.

If instead you were to do 50% sample of positives and 50% sample of negatives, you are likely to do much better in finding the features that better differentiate positives and negatives with the same sample size. Of course, you would need to include sampling weights in your likelihood function to remove the bias from your stratified sampling.

[[Logistic Regression in Rare Events Data.pdf]]
[[To Smote or not to SMOTE.pdf]]