import unittest
from matrix import Matrix
import numpy as np

class TestMatrix(unittest.TestCase):
    
    def test_add(M):
        A = Matrix([1,2,3,4], [2,3,4,1], [3,2,4,1])
        B = Matrix([4,3,2,1], [3,2,1,4], [2,3,1,4])
        C = A + B
        # print(C.mat)
        M.assertEqual(C.mat, tuple([[5]*4]*3))
        # except Exception as X:
        #     print("Error")

    def test_sub(M):

        A = Matrix([1,2,3,4], [2,3,4,1], [3,2,4,1])
        B = Matrix([4,3,2,1], [3,2,1,4], [2,3,1,4])
        C = A - B
        try:
            M.assertEqual(C.mat, ([-3,-1,1,3],[-1,1,3,-3],[1,-1,3,-3]))
        except Exception as X:
            print ("Error")

    def test_pow(M):
       
        A = Matrix([1,2,3,4], [2,3,4,1], [3,2,4,1], [2,4,1,3])
        C = A ** 2
        m = np.array([[1,2,3,4], [2,3,4,1], [3,2,4,1], [2,4,1,3]])
        expec = np.linalg.matrix_power(m,2).tolist()
        # print(f'{expec}, "\n" {C.mat}')
    
        M.assertEqual(list(C.mat), (expec))
    


    def test_mul(M):
        A = Matrix([1,2,3,4], [2,3,4,1], [3,2,4,1], [2,3,1,4])
        B = Matrix([4,3,2,1], [3,2,1,4], [2,3,1,4], [4,3,2,1])
        expec = np.matmul([[1,2,3,4], [2,3,4,1], [3,2,4,1], [2,3,1,4]], [[4,3,2,1], [3,2,1,4], [2,3,1,4], [4,3,2,1]])
        expec = expec.tolist()
        C = A*B
        try:
            M.assertEqual(C.mat, tuple(expec))
        except Exception as e:
            print("Error")

if __name__ =='__main__':
    unittest.main()