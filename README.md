# kmeanskmedians

The location.mat contains 1500 points in 2D. Each point represents a mouse's location. We are asked to put K mouse traps 
to catach the mice and we want the distances between trap and mice be the smallest.

We implemented two algorithms, one is K-means and one is K-medians.

For the function itself, we can specify the data X, number of K, number of iterations, and which algorithm to choose.
If we want the algorithm to converge by itself, we can put -1 in numOfIter argument. Otherwise we can put exact number
we want.
If we want to use K-means, we put 1 at k_means to indicate this flag is on. If we want to use K-medians, we put 0.

We also included the plot to help the user better visualize where the tracks are amond all the mice. The mice are in blue
dots and the tracks are in red dots.
