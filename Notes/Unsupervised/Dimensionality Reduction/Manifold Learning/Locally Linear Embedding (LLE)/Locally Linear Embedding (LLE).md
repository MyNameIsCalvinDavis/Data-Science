Using MDS on the *HELLO* data as described in [[Multidimensional Scaling (MDS)]]] gives us the following:
![[Pasted image 20250905115208.png]]

This is because MDS creates a distance matrix for all points; LLE instead creates a distance matrix for local (close) points.

![[Pasted image 20250905115326.png]]

We could imagine unrolling the data in a way that keeps the lengths of the lines approximately the same. This is precisely what LLE does, through a global optimization of a cost function reflecting this logic.
