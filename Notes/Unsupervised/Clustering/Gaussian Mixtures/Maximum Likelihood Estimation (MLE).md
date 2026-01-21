## Summary
Basically, given some dataset, there's a function or distribution that can be used to describe it. MLE is a method used to identify the parameters of this function, given the data but not the function.

Eg the probability of a coin flip being heads is generally considered to be 50%, but in our coin flipping test we got 60 heads and 40 tails. MLE describes our real data set with a coefficient of 0.6 despite the hidden 50% probability of having gotten that result.

Eg Here's an example [[Dirichlet Distribution]] for some shapes A,B,C
![[DirichletDistTriGraph.png]]
Some Dir(A,B,C) generated this distribution. We can use MLE to find those parameters, from the points in this dataset.


In this image the **MLE Estimate** under-estimated a fake dataset of 100 clicks where the probability of someone clicking on an ad is 60%. Even though the actual likelihood shifted higher (65% or so clicked on the ad), the MLE Estimate of the true probability used to generate this data (0.6) was identified by the algorithm.
![[MLE.png]]
## Limitations
- **Requires labeled data:** If some labels are missing, MLE cannot be directly applied (this is where **Expectation-Maximization (EM)** helps).
- **Sensitive to outliers:** Since MLE maximizes probability, extreme data points can distort estimates.
- **Assumes a correct distribution:** If the data does not follow the assumed distribution, MLE can produce biased results.

MLE (Maximum Likelihood Estimation) is a fundamental method in data science for estimating the parameters of a probability distribution that best explains the observed data. Instead of guessing the parameters, MLE finds the values that make the data **most probable** under a chosen model.

- Assume data follows some distribution (eg Normal, Poisson, Bernoulli)
- Assume each data point is independent
	- Likelihood function is a product of individual probabilities, see [[Log Likelihood]]
- Determine parameter values that maximize this LL function
- 
## On Maximum Likelihood Estimation (MLE) and EM
**MLE** is a direct optimization method that finds the parameters making the observed data most probable. If you have complete and labeled data, MLE is usually the preferred choice. It’s commonly used in **linear regression, logistic regression, and deep learning models**.

**EM**, on the other hand, is designed for situations where some data is **missing or hidden** (latent variables). Instead of solving for parameters directly, EM iteratively refines estimates, making it useful for **clustering (e.g., Gaussian Mixture Models), semi-supervised learning, and handling incomplete data**.

While MLE is a **direct method** that works with fully observed data, EM is an **iterative technique** that estimates parameters when some data is missing or hidden.

- **Use MLE when you have complete, labeled data.** Example: Predicting the probability of customer purchases.
- **Use EM when you have missing labels or hidden variables.** Example: Identifying customer segments without knowing them beforehand.

See [[Expectation Maximization (EM)]]

https://medium.com/data-scientists-handbook/mle-vs-em-in-data-science-the-how-why-and-when-a55b7a943071