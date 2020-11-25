import numpy as np

def diff(array = None):
    if array == None:
        return np.array(0)
    else:
         
    	print array

        return np.diff(np.array(array))


def diffN(array = None, N = None):
	##  Second order difference

	if array == None:
		return np.array(0)
	else:
		if N == None:
			return np.diff(np.array(array))
		else:
			return np.diff(np.array(array), n = N)


def perDiff(array = None):

	if array == None:
		return None
	else:

		#  Returns percent difference in decimal format which 
		#  is equal to (X2 - X1) / X1 
		return np.diff(np.array(array, dtype=float)) / array[:-1]


if __name__ == "__main__":
    print type(diff([1, 2, 3]))
    print diff([1,2,4,7,0])
    print diffN([1,2,4,7,0], 3)
    print perDiff([1,2,4,7,0])
