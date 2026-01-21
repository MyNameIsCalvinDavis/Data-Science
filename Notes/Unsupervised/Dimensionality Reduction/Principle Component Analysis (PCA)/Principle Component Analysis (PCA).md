![[Pasted image 20250905105236.png]]
In principal component analysis, one quantifies this relationship by finding a list of the principal axes in the data, and using those axes to describe the dataset; *components* and *explained variance*

These vectors represent the principal axes of the data, and the length shown is an indication of how “important” that axis is in describing the distribution of the data—more precisely, it is a measure of the variance of the data when projected onto that axis. The projection of each data point onto the principal axes are the “principal components” of the data.

This transformation from data axes to principal axes is as an **affine transformation**, which basically means it is composed of a translation, rotation, and uniform scaling.

## Dimensionality Reduction
Using PCA for dimensionality reduction involves zeroing out one or more of the smallest principal components, resulting in a lower-dimensional projection of the data that preserves the maximal data variance. The fraction of variance that is cut out is roughly a measure of how much “information” is discarded in this reduction of dimensionality.

For the handwritten digits dataset; 8x8 pixel images reduced to two dimensions:
![[Pasted image 20250905110059.png]]
Recall what these components mean: the full data is a 64-dimensional point cloud, and these points are the projection of each data point along the directions with the largest variance. Essentially, we have found the optimal stretch and rotation in 64-dimensional space that allows us to see the layout of the digits in two dimensions, and have done this in an unsupervised manner—that is, without reference to the labels.

For example, this is a per-pixel basis of the first 8 pixels. It's not a very efficient function to apply to the whole 8x8 matrix because it only extracts information from one pixel at a time, though it will eventually reconstruct the whole image.
![[Pasted image 20250905110715.png]]
For vector *x = {x1, x2, ... x64}* representing these pixels, the basis for this might be described as:

*image x = x1 · (pixel 1) + x2 · (pixel 2) + x3 · (pixel 3) ⋯x64 · (pixel 64)*

But the pixel-wise representation is not the only choice of basis. We can also use other basis functions, which each contain some predefined contribution from each pixel, and write something like:

*image x = mean + x1 · (basis 1) + x2 · (basis 2) + x3 · (basis 3) ⋯*

PCA can be thought of as a process of choosing optimal basis functions, such thatadding together just the first few of them is enough to suitably reconstruct the bulk of the elements in the dataset. The principal components, which act as the low-
dimensional representation of our data, are simply the coefficients that multiply each
of the elements in this series. Using 8 components:

![[Pasted image 20250905111142.png]]

## Choosing the number of components
A vital part of using PCA in practice is the ability to estimate how many components
are needed to describe the data. We can determine this by looking at the cumulative
explained variance ratio as a function of the number of components

```python
pca = PCA().fit(digits.data)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');
```

![[Pasted image 20250905111333.png]]

PCA's main weakness is that it tends to be affected by outliers, and does not perform well with nonlinear relationships within the data.
## Resources
Python Data Science Handbook P. 434