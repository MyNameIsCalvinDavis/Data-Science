## Summary
Iterative method to find estimates of local maxima of a probability distribution, where the model depends on unobserved latent variables. 

The EM iteration alternates between performing an expectation (E) step, which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters maximizing the expected log-likelihood found on the _E_ step. These parameter-estimates are then used to determine the distribution of the latent variables in the next E step. It can be used, for example, to estimate a mixture of Gaussian Mixtures, or to solve the multiple linear regression problem.

## Assumptions
- Maximum likelihood (wrt latent vars, unknown vals, params) solutions via derivation is impossible because there are too many variables & not enough actual data. Produces interlocking equations that can't solve one another
	- Pick a set of random vals for one equation(s), use to solve for the other. Use that output back into the original and approach a real solution (stochastic method)
## References
https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm
