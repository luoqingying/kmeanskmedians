import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import statistics
import copy

%matplotlib inline

tmp = sio.loadmat("location.mat")

tracks = {} # dictionary 30*50
for trackno in range(30):
    tracks[trackno] = tmp["num%d"%(trackno)]
    
plt.close("all")
for trackno in range(30):
    plt.plot(tracks[(trackno)][:,0],tracks[(trackno)][:,1],'.')
plt.axis("square")
plt.xlabel("meters")
plt.ylabel("meters")
plt.show()

# X (1500,2) 1500 data points
# K: number of cluster
# numOfIter: -1 when the user want the convergence, otherwise specify a number
# kmeans: 1 when we want the k means algo, 0 when we want the k median algo

def kmeans(X,K,numOfIter,k_means):  
    # method can be kmeans or kmedians
    
    # randomly initialize cluster centers
    C = np.zeros([5,2])
    for k in range(K):
        C[k] = X[k] # the first K points in X
    # should use deep copy for numpy array
    C_new = copy.deepcopy(C)  
    if numOfIter == -1:
        iteration = 0
        # if there is any change, keep updating until convergence
        while True:
            iteration += 1
            print (iteration)
            bins = {}
            for k in range(K):
                bins[k] = []
            # for each point in X, find the cluster that is nearest
            for pt in X:
                dist = np.zeros(K)
                for k in range(K):
                    dist[k] = np.sqrt(np.power(pt[0]-C_new[k][0],2) + np.power(pt[1]-C_new[k][1],2))
                idx = np.argmin(dist)
                bins[idx].append(pt)
            for k in range(K):
                # cluster center update
                m_x = []
                m_y = []
                length = len(bins[k])
                for l in range(length):
                    m_x.append(bins[k][l][0])
                    m_y.append(bins[k][l][1])
                if k_means == 1:
                    C_new[k] = np.array([statistics.mean(m_x), statistics.mean(m_y)])
                elif k_means == 0:
                    C_new[k] = np.array([statistics.median(m_x), statistics.median(m_y)]) 
            if C_new.all == C.all:
                print ("number of iteration:", iteration)
                return C_new
            else:
                C = copy.deepcopy(C_new)
                
    
    # when the user limit the number of iteration
    for iter in range(numOfIter):
        bins = {}
        for k in range(K):
            bins[k] = []
        for pt in X:
            dist = np.zeros(K)
            for k in range(K):
                dist[k] = np.sqrt(np.power(pt[0]-C[k][0],2) + np.power(pt[1]-C[k][1],2))
            idx = np.argmin(dist)
            bins[idx].append(pt)
        for k in range(K):
            # cluster center update
            m_x = []
            m_y = []
            length = len(bins[k])
            for l in range(length):
                m_x.append(bins[k][l][0])
                m_y.append(bins[k][l][1])
            if k_means == 1:
                C[k] = np.array([statistics.mean(m_x), statistics.mean(m_y)])
            elif k_means == 0:
                C[k] = np.array([statistics.median(m_x), statistics.median(m_y)])      
    return C

C = kmeans(X,K=5,numOfIter=100, k_means=1)
C

X = np.zeros([30*50,2])

for trackno in range(30):
    X[(trackno*50):((trackno+1)*50),:] = tracks[trackno]
    
plt.close("all")
plt.plot(X[:,0],X[:,1],'.')
plt.plot(C[:,0],C[:,1],'ro')
plt.axis("square")
plt.xlabel("meters")
plt.ylabel("meters")
plt.show()

