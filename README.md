# kmeanskmedians

The location.mat contains 1500 points in 2D. Each point represents a mouse's location. My task was to put K mouse traps 
to catch the mice and distances between trap and mice should be the smallest.

I implemented two clustering algorithms, one is K-means and one is K-medians.

For the function itself, it takes three arguments, input data X, number of K, number of iterations, and which algorithm 
to choose.
If we want the algorithm to converge by itself, we can put -1 in numOfIter argument. Otherwise we can put exact number
we want.
If we want to use K-means, we put 1 at k_means to indicate this flag is on. If we want to use K-medians, we put 0.

The starting centers are ramdonly chosen from the data set, although the final centers may be outside of the data set. 
The starting centers must be different, otherwise it is impossible to calculate the mean of a cluster for the repeating 
centers, cause all points relative to that center may go into only one bin and leave the rest repeating bins empty.

I also included the plot to help the user better visualize where the tracks are among all the mice. The mice are in blue
dots and the tracks are in red dots. It is obvious that K-means has no unique solution, although the positions are roughly 
the same. In the function I wrote, I shuffled the data set every time we initialized the starting centers. The way in which 
the data is ordered affects the final results of the data set.

K-medians here performed similarly as K-means. I didn't include many outliers here, if we had, we should see that the K-medians will be more robust to outliers and noises than K-menas, which means the plots will be more different also.

K-means pros:
1. easy to implement and understand
2. more suitable for large datasets than for small ones

K-means cons:
1. require the data set to be in hyper-spherical shape to a certain degree (visualize the data before applying the algo)
2. sensitive to scale (normalization, standardization)
3. have to predefine the number of clusters used
4. can only handle numerical data

