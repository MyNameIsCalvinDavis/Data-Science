When doing an explained variance ratio as described in [[Principle Component Analysis (PCA)#Choosing the number of components]], for complex (likely nonlinear) data the number of components used to describe the data might be high like 100 components for 90% variance. This tells us that the data is intrinsically very high dimensional—it can’t be described linearly with just a few components. 

When this is the case, nonlinear manifold embeddings like LLE and Isomap can be
helpful.

![[Pasted image 20250905165059.png]]

The way this author describes Manifold Learning as a general rule is Isomap performs better than LLE for high-dimensional data from real world sources, but is really only useful as a visualization tool for said high dimensional data.