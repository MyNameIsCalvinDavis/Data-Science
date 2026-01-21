https://www.geeksforgeeks.org/machine-learning/dirichlet-process-mixture-models-dpmms/

+
Prior / Posterior likelihood identifies k components
Prior influences cluster params (https://stats.stackexchange.com/questions/256908/check-on-intuition-behind-infinite-mixture-models-for-clustering)

It is often used in [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference "Bayesian inference") to describe the [prior](https://en.wikipedia.org/wiki/Prior_probability "Prior probability") knowledge about the distribution of [random variables](https://en.wikipedia.org/wiki/Random_variable "Random variable")—how likely it is that the random variables are distributed according to one or another particular distribution.

[[Infinite Mixture Model]]

The model automatically determines the optimal number of clusters based on the data. [src](https://www.geeksforgeeks.org/machine-learning/dirichlet-process-mixture-models-dpmms/)
```python
dpmm = BayesianGaussianMixture(
	n_components=10, covariance_type='full',
	weight_concentration_prior_type='dirichlet_process',     
	weight_concentration_prior=1e-2,
	random_state=42 )
dpmm.fit(X)
labels = dpmm.predict(X)
```

![[Pasted image 20250831143006.png]]
