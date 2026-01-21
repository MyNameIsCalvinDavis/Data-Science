- PreliZ [Icazatti et al., 2023] used for prior elicitation
```python
# Calculate real and empirical example beta distribution
plt.hist(pz.BetaBinomial(alpha=2, beta=5, n=5).rvs(1000))
pz.BetaBinomial(alpha=2, beta=5, n=5).plot_pdf();
```
```python
# Calculate a beta distribution prior with 90% of mass between 0.1 and 0.7
dist = pz.Beta()
2 pz.maxent(dist, 0.1, 0.7, 0.9)
```

- ArviZ used as exploratory analysis of Bayesian models, helps us summarize the posterior
```python
# Randomly sample a beta distribution
np.random.seed(1)
2 az.plot_posterior({'𝜃':pz.Beta(4, 12).rvs(1000)})
```
