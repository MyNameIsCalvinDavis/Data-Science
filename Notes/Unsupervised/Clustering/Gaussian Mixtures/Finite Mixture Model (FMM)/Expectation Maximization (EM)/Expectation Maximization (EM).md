## Summary
Iterative method to find estimates of local maxima of a probability distribution, where the model depends on unobserved latent variables, or we don't have all of the parameters for the model figured out.

The EM iteration alternates between performing an expectation (E) step, which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters maximizing the expected log-likelihood found on the _E_ step. These parameter-estimates are then used to determine the distribution of the latent variables in the next E step. It can be used, for example, to estimate a mixture of Gaussian Mixtures, or to solve the multiple linear regression problem.

## Example
Imagine we are an **e-commerce company** trying to segment customers into different buying behavior groups, but we **don’t know their true segment labels**. We only have data like:
- Total purchase amount
- Number of visits per month
- Average cart size
Since we don’t know which class a customer belongs to, **we treat the class as a hidden variable** and use EM to estimate both the **class probabilities** and the **mean spending behavior of each group**.

- Assume a gaussian mixture model / customer belongs to one of K segments with normal distribution of spending behavior, 3 classes (low / mid / high spending but we dont know that)

![[EMEstimation.png]]
## Assumptions
- Maximum likelihood (wrt latent vars, unknown vals, params) solutions via derivation is impossible because there are too many variables & not enough actual data. Produces interlocking equations that can't solve one another
	- Pick a set of random vals for one equation(s), use to solve for the other. Use that output back into the original and approach a real solution (stochastic method)

See [[Maximum Likelihood Estimation (MLE)#On Maximum Likelihood Estimation (MLE) and EM]]
https://medium.com/data-scientists-handbook/mle-vs-em-in-data-science-the-how-why-and-when-a55b7a943071
## References
https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm
