import numpy as np 
from scipy.stats import ortho_group
from sklearn.decomposition import PCA

totalDim = 20
dimensions = [3,4,8,12,1]
numData = 1000

def getDimensionality(singVals,tau = 2):
	# assumes this isn't 0 dim
	diff = 0
	dim = 0
	while diff < tau:
		diff = singVals[dim] / singVals[dim+1]
		dim += 1 
	return dim

for i,dim in enumerate(dimensions):

	# Generate data that varies only in the first dim directions
	data = np.concatenate([
		2*np.random.rand(numData,dim)-1,
		np.zeros([numData,totalDim-dim])],
		axis=1)

	# Perturb the data to hid the dimensionality
	rand_orth = ortho_group.rvs(dim=20)
	data = np.matmul(data,rand_orth)

	pca = PCA()
	pca.fit(data)
	print(pca.explained_variance_ratio_)
	print(pca.singular_values_)
	print(pca.n_components_)
	print(getDimensionality(pca.singular_values_))
	

	# Offset the data to be no where near the origin
	mean = 20*np.random.rand(totalDim) - 10
	data = data + mean


	np.save("dimensionalityDataset_"+str(i),data)