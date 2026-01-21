Downsides
- In manifold learning, there is no good framework for handling missing data. In
contrast, there are straightforward iterative approaches for missing data in PCA.
- In manifold learning, the presence of noise in the data can “short-circuit” the
manifold and drastically change the embedding. In contrast, PCA naturally filters
noise from the most important components.
- The manifold embedding result is generally highly dependent on the number of
neighbors chosen, and there is generally no solid quantitative way to choose an
optimal number of neighbors. In contrast, PCA does not involve such a choice.
- In manifold learning, the globally optimal number of output dimensions is diffi‐
cult to determine. In contrast, PCA lets you find the output dimension based on
the explained variance.
- In manifold learning, the meaning of the embedded dimensions is not always
clear. In PCA, the principal components have a very clear meaning.
- In manifold learning the computational expense of manifold methods scales as
O[N2] or O[N3]. For PCA, there exist randomized approaches that are generally
much faster (though see the megaman package for some more scalable imple‐
mentations of manifold learning).

With all that on the table, the only clear advantage of manifold learning methods over PCA is their ability to preserve nonlinear relationships in the data; for that reason I tend to explore data with manifold methods only after first exploring them with PCA.

See other topics: Isomap / *t-distributed stochastic neighbor embedding*
