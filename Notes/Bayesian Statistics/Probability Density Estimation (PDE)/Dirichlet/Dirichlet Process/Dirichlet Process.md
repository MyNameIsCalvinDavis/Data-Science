The Dirichlet process is a stochastic proces used in Bayesian nonparametric
models of data, particularly in Dirichlet process mixture models (also known as
infinite mixture models). It is a distribution over distributions, i.e. each draw
from a Dirichlet process is itself a distribution. It is called a Dirichlet process be-
cause it has Dirichlet distributed finite dimensional marginal distributions, just
as the Gaussian process, another popular stochastic process used for Bayesian
nonparametric regression, has Gaussian distributed finite dimensional marginal
distributions. Distributions drawn from a Dirichlet process are discrete, but
cannot be described using a finite number of parameters, thus the classification
as a nonparametric model

A **Dirichlet Process** is a stochastic process that generates probability distributions over infinite categories. It enables clustering without specifying the number of clusters in advance.

The ****stick-breaking process**** is a method to generate cluster probabilities from a Dirichlet Process. The concept is shown in the image below:

![[Pasted image 20250831142057.png]]

A particularly important application of Dirichlet processes is as a [prior probability](https://en.wikipedia.org/wiki/Prior_probability "Prior probability") distribution in [infinite mixture models](https://en.wikipedia.org/wiki/Infinite_mixture_model "Infinite mixture model").

[[Teh2010a.pdf]]