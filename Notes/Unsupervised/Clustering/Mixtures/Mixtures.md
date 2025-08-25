![[MixtureComponents.png]]
## Summary
A **mixture model** is a [probabilistic model](https://en.wikipedia.org/wiki/Probabilistic_model "Probabilistic model") for representing the presence of [subpopulations](https://en.wikipedia.org/wiki/Subpopulation "Subpopulation") within an overall population, without requiring that an observed data set should identify the sub-population to which an individual observation belongs.

![[MixturePic.png]]

In addition, in a [Bayesian setting](https://en.wikipedia.org/wiki/Bayesian_inference "Bayesian inference"), the mixture weights and parameters will themselves be random variables, and [prior distributions](https://en.wikipedia.org/wiki/Prior_distribution "Prior distribution") will be placed over the variables. In such a case, the weights are typically viewed as a _K_-dimensional random vector drawn from a [Dirichlet distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution "Dirichlet distribution") (the [conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior "Conjugate prior") of the categorical distribution), and the parameters will be distributed according to their respective conjugate priors.

MMs are soft clustering methods compared to something like KMM which is a hard clustering method, GMMs define component populations with probability distributions instead of a definite value when describing data component participation. 

MMs generally follow Gaussian Distributions

## References
https://scikit-learn.org/stable/modules/mixture.html
https://en.wikipedia.org/wiki/Mixture_model
https://www.youtube.com/watch?v=qMTuMa86NzU