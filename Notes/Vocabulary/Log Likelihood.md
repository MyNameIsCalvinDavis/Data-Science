Log likelihood is simply the log of the likelihood. If p is the likelihood, log likelihood is log(p).

The likelihood is just another word for probability, they likelihood of some observation is the probability of that observation.

Log likelihood is used because the independent events is a common assumption, and the likelihood of independent events is the multiplication product of the likelihoods of each event. When you take the log of products, it becomes the sum of the logs. log(x * y) = log(x) + log(y), and **sums are a lot simpler to manipulate mathematically, especially for taking derivatives.**

Now usually we can’t just change a value to make it easier to work with. But in the context of log likelihoods, the goal is to find the maximum likelihood. The log function is always increasing, this means that **log(x) > log(y) implies x > y**, then a function will achieve its maximum value at exactly the same point the log of the function achieves its maximum value.

https://en.wikipedia.org/wiki/Likelihood_function