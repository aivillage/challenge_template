import numpy as np
from scipy.stats import ortho_group

totalDim = 10
clusterCounts = [6,8,8,2,4]
numDataPerCluster = 200

# Generates a symetric matrix with a given set of eigenvalues, or random ones.
def generateCovariance(dim = 3, diag = None):
	if diag is None:
		diag = np.random.rand(dim)*4
	rand_orth = ortho_group.rvs(dim)

	return np.matmul(rand_orth.T * diag, rand_orth)

for j,c in enumerate(clusterCounts):
	dataset = []
	for i in range(c):
		cov = generateCovariance(totalDim)
		mean = 40*np.random.rand(totalDim) - 20

		centroid = np.random.multivariate_normal(mean, cov, numDataPerCluster)

		dataset.append(centroid)
	dataset = np.concatenate(dataset)
	np.random.shuffle(dataset)
	print(dataset)
	np.save("clusterCountDataset"+str(j),dataset)
