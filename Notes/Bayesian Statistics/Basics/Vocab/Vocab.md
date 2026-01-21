### Probability Mass Function
- A probability mass function (PMF) is a function that gives the probability of a **[discrete random variable](https://www.google.com/search?q=discrete+random+variable&client=ubuntu-sn&hs=FvU&sca_esv=93a27070e35a51f2&channel=fs&sxsrf=AE3TifOHwNyPZGE158hrehBJVhhp5nNN2Q%3A1764442197622&ei=VUAraZumJMq2qtsP9NWs2QU&oq=what+is+a+probability&gs_lp=Egxnd3Mtd2l6LXNlcnAiFXdoYXQgaXMgYSBwcm9iYWJpbGl0eSoCCAAyCxAAGIAEGJECGIoFMgsQABiABBiRAhiKBTIFEAAYgAQyCxAAGIAEGJECGIoFMgsQABiABBiRAhiKBTIFEAAYgAQyBRAAGIAEMgoQABiABBgUGIcCMgUQABiABDIFEAAYgARI_xlQugZYgxJwAXgBkAEAmAGQBKAB7hiqAQswLjIuMy4xLjIuMrgBA8gBAPgBAZgCC6AC3hnCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAjGIAEGCcYigXCAgoQABiABBhDGIoFwgIIEAAYgAQYsQPCAg4QABiABBixAxiDARiKBZgDAIgGAZAGCpIHCTEuMi4zLjEuNKAHyj6yBwkwLjIuMy4xLjS4B8wZwgcFMi04LjPIB04&sclient=gws-wiz-serp&ved=2ahUKEwiuoP-1g5iRAxXhkyYFHXKMD7gQgK4QegYIAQgAEAg)** taking on a specific value. It is used for variables with a finite or countable number of outcomes, like the number of heads in three coin flips or the result of rolling a die.
- pmf(𝑥) = 𝑃(𝑋 = 𝑥) // Probability that a random variable is part of a discrete set *x*

![[Pasted image 20250908023439.png]]
	Figure 1.4: The gray dots represent the pmf of the BetaBinomial sample. In light gray, a histogram of 1,000 draws from that distribution

### Probability Distribution
- *List of probabilities* for all answers in *S* / all possible numbers from a die
### Empirical Distribution
 - Roll a die a few times, tabulate how often we get each number. Data-driven observational distribution, not theoretical
### Probability Density Function (PDF)
- PMF but for a continuous variable(s). *Thus, for a Gaussian, the probability of getting exactly the number -2, i.e. the number -2 followed by an infinite number of zeros after the decimal point, is 0. But the probability of getting a number between -2 and 0 is some number larger than 0 and smaller than 1.*

 ![[Pasted image 20251129120126.png]]
### Cumulative Distribution Function
- CDF a random variable 𝑋 is the function 𝐹x given by 𝐹x (𝑥) = 𝑃(𝑋 ≤ 𝑥). In other words, the cdf is the answer to the question: what is the probability of getting a number lower than or equal to 𝑥?

![[Pasted image 20251129121140.png]]

### Bayes Theorem
- **Prior Distribution** should reflect what we know about the value of hypothesis 𝜃 before seeing the data *Y*
- **Likelihood** is how we introduce data. It's an expression of the plausibility of our data given the parameters 
- **Posterior Distribution** is the result of the analysis, reflects all that we know about a problem. It's a probability distribution for parameters in our model and NOT a value.
- **Marginal Likelihood (evidence)** is the probability of observing the data averaged over all the possible values the parameters can take, described by the prior. Think of it as a normalization factor that ensures the posterior
is a proper pmf or pdf 

![[Pasted image 20251129122459.png]]

### Binomial Distribution
- Coin toss with 𝜃 as 0.5 (fair coin, bias). Discrete distribution returning the probability of getting *y* heads out of *N* coin tosses given a fixed value (bias), 𝜃.
- https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_(Shafer_and_Zhang)/04%3A_Discrete_Random_Variables/4.03%3A_The_Binomial_Distribution

![[Pasted image 20251129124754.png]]

### Beta Distribution
- In general, we use the Beta distribution when we want to model the proportions of a Binomial variable. Another reason is its versatility. As we can see in Figure 1.11, the distribution adopts several shapes (all restricted to the [0, 1] interval), including a Uniform distribution, Gaussian-like distributions, and U-like distributions.

![[Pasted image 20251129130214.png]]

### Conjugate Prior
- CP of a likelihood is a prior that, when used in combination with a given likelihood, returns a posterior with the same functional form as the prior.
- Conjugacy ensures mathematical tractability of the posterior, which is important given that a common problem in Bayesian statistics ends up with a posterior we cannot solve analytically.
- No longer a restriction with modern computational methods

### Maximum Likelihood
- Estimate the parameters of a distribution

### Highest Density Interval (HDI)
- Shortest interval containing some portion of a probability density. Eg. 95% HDI within [2,5]

Student’s t-distribution
- Location parameter 𝜇, a scale parameter 𝜎, and a normality parameter 𝜈
- The lower this number, the heavier their tails
![[Pasted image 20251228142457.png]]