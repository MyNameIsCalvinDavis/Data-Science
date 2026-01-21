## Coin Flip - Choosing Prior, Likelihood, Posterior
- Bayesian Analysis with Python P.30
- [[Vocab#Bayes Theorem]]
```python
n_trials = [0, 1, 2, 3, 4, 8, 16, 32, 50, 150]
n_heads = [0, 1, 1, 1, 1, 4, 6, 9, 13, 48]
beta_params = [(1, 1), (20, 20), (1, 4)]
x = np.linspace(0, 1, 2000)
for idx, N in enumerate(n_trials):
	y = n_heads[idx]
	for (𝛼_prior, 𝛽_prior) in beta_params:
		posterior = pz.Beta(𝛼_prior + y, 𝛽_prior + N - y).pdf(x)
```
![[Pasted image 20251129135031.png]]

- Uniform Prior (Black) - No info
- Gaussian Prior (Grey)
- Skewed Prior (Light Grey) - Tail heavy

## Reporting
- Bayesian Analysis with Python P.40