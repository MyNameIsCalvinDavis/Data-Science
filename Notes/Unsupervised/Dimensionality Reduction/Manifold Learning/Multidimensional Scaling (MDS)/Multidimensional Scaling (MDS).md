Our discussion so far has considered linear embeddings, which essentially consist of
rotations, translations, and scalings of data into higher-dimensional spaces. Where
MDS breaks down is when the embedding is nonlinear—that is, when it goes beyond
this simple set of operations.

Consider a dataset with a nonlinear relationship:
![[Pasted image 20250905113858.png]]

We see that rotating, shrinking, transforming the data doesn't really affect our understanding. X & Y are not fundamental to the description of this dataset. What *is* fundamental, is the distance matrix between points. For *n=1000* a distance matrix of 1000x1000 is created:

![[Pasted image 20250905114028.png]]

MDS aims to transform a given distance matrix between points, and recover a D-dimensional coordinate representation of the data.

Here is one of two approximations:
![[Pasted image 20250905114623.png]]