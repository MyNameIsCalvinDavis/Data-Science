In statistics, probability density estimation or simply density estimation is **the construction of an estimate, based on observed data, of an unobservable underlying probability density function**.

https://machinelearningmastery.com/probability-density-estimation/

In many methods, the data is modeled with a probability distribution that fully specifies the probability density/mass as a function of the parameters of that distribution. In essence, the only thing that stops us from knowing the precise density of a variable is knowledge of the parameters, and thus efforts focus on the estimation of those parameters. This approach is appropriately referred to as parametric, and is incredibly common in statistical inference.

As [Glen_b pointed out](https://stats.stackexchange.com/questions/268638/what-exactly-is-the-difference-between-a-parametric-and-non-parametric-model/268646#comment513816_268638), in parametric data generation model this distribution is defined by a fixed number of parameters. In nonparametric data generation model we don't have a distribution with a fixed number of parameters, we have milder assumptions about it, like continuity or symmetry.

In parametric hypothesis space (parametric model) every algorithm is uniquely defined by a fixed number of parameters (this number is the same for all algorithms from this space). Simple examples of parametric models are linear regression model: H={h(x;w,b)=⟨w,x⟩+b∣w∈Rd,b∈R}  
and linear (binary) classification model: H={h(x;w,b)=sign(⟨w,x⟩+b)∣w∈Rd,b∈R}.  
In non-parametric models we can't describe every algorithm with the vector of parameters of the same constant size for all algorithms. Usually the number of parameters grows with the size of a training set. For example in the case of decision trees H={T(x;Θ)∣Θ}, where Θ={J,{Rj,γj}Jj=1} is a vector of tree's parameters: J is a number of terminal nodes in the tree, Rj are subregions of the input space X corresponding to these nodes, and γj are the predictions in these nodes. Trees can have different number of leaves and different number of internal nodes, so the space of decision trees is non-parametric (dimension of Θ will be different for different trees, if we train them on the datasets generated from the same distribution, that is, with the same number of features d, but with different number of observations in each dataset).

![[ParamNonparam.png]]

Use parametric tests for normally distributed, interval/ratio data with a large sample size and homogeneous variance. Use nonparametric tests for non-normally distributed data, smaller sample sizes, ordinal data, or when data contains significant outliers. Nonparametric tests are generally less powerful but more robust to distributional issues and outliers.


Gaussians being non parametric
https://stats.stackexchange.com/questions/46588/why-are-gaussian-process-models-called-non-parametric