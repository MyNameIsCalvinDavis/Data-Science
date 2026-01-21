It is a multivariate generalization of the [beta distribution](https://en.wikipedia.org/wiki/Beta_distribution "Beta distribution")

A particularly important application of Dirichlet processes is as a [prior probability](https://en.wikipedia.org/wiki/Prior_probability "Prior probability") distribution in [infinite mixture models](https://en.wikipedia.org/wiki/Infinite_mixture_model "Infinite mixture model").

https://www.andrewheiss.com/blog/2023/09/18/understanding-dirichlet-beta-intuition/

The Dirichlet distribution is one that has often been turned to in Bayesian
statistical inference as a convenient prior distribution to place over proportional
data

[[dirichlet.pdf]]

The Dirichlet process is, in some sense, an infinite dimen-
sional version of the Dirichlet distribution. This is a useful prior to put over mixing
weights of a Gaussian mixture model and is used for automatically picking out the
number of necessary clusters as opposed to the approach of trying to fit the data
several times to different numbers of clusters to find the best number [4].


As an example, a bag of 100 real-world dice is a _random [probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function "Probability mass function") (random pmf)_—to sample this random pmf you put your hand in the bag and draw out a die, that is, you draw a pmf. A bag of dice manufactured using a crude process 100 years ago will likely have probabilities that deviate wildly from the uniform pmf, whereas a bag of state-of-the-art dice used by Las Vegas casinos may have barely perceptible imperfections. We can model the randomness of pmfs with the Dirichlet distribution.[](https://en.wikipedia.org/wiki/Dirichlet_process#cite_note-1)

Dir(3,7,2) creates a \[0-1] centered probability distribution for, in this case, three variables, where *7* creates a higher gravity pull in the distribution. We can use [[Maximum Likelihood Estimation (MLE)]] to find the parameters of a distribution given a datset.
![[DirichletDistTriGraph.png]][src](https://www.andrewheiss.com/blog/2023/09/18/understanding-dirichlet-beta-intuition/)
