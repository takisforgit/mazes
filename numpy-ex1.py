import numpy
from scipy import sparse
def buildSparseMatrix():
	''' Let's build a 100 x 100 matrix with around 10% filled with ones '''
	A = abs((numpy.random.random(1000 ** 2) - 0.4)).round()
	M = A.reshape(1000, 1000)
	S = sparse.csr_matrix(M)
	print(S)
##	S * S

	# print(__name__)

def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    import timeit
##    buildSparseMatrix()
##    print(timeit.timeit("test()", setup="from __main__ import test"))
    print(timeit.timeit("buildSparseMatrix()", setup="from __main__ import buildSparseMatrix", number=1))
