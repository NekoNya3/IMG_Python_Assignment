import copy

class Matrix:
    def __init__(M, *args):
        try:
            l1=len(args[0])
            for i in args:
                l=len(i)
                if l>l1:
                    l1=l
                elif l<l1:
                    while l<l1:
                        i.append(0)
                        l+=1
            M.mat=args
        except(IndexError, ValueError):
            M.mat=[]

    def __add__(M, N):
        r1=len(M.mat)
        r2=len(N.mat)
        A=Matrix()
        if r1==r2:
            c1=len(M.mat[0])
            c2=len(N.mat[0])
            if c1==c2:
                for i in range(r1):
                    R=[]
                    for j in range(c1):
                        R.append(M.mat[i][j]+N.mat[i][j])
                    A.mat.append(R)
                A.mat=tuple(A.mat)
                return A
            else:
                raise ValueError('Invalid Input')
        else:
            raise ValueError('Invalid Input')
    
    def __sub__(M, N):
        r1=len(M.mat)
        r2=len(N.mat)
        A=Matrix()
        if r1==r2:
            c1=len(M.mat[0])
            c2=len(N.mat[0])
            if c1==c2:
                for i in range(r1):
                    R=[]
                    for j in range(c1):
                        R.append(M.mat[i][j]-N.mat[i][j])
                    A.mat.append(R)
                A.mat=tuple(A.mat)
                return A
            else:
                raise ValueError('Invalid Input')
        else:
            raise ValueError('Invalid Input')

    def __mul__(M, N):
        A=Matrix()
        if len(M.mat[0])==len(N.mat):
            for i in range(len(M.mat)):
                R=[]
                for j in range(len(N.mat[0])):
                    counter=0
                    for k in range(len(N.mat)):
                        counter+=M.mat[i][k]*N.mat[k][j]
                    R.append(counter)
                A.mat.append(R)
        A.mat=tuple(A.mat)
        return A

    def sqMatrix(M):
        return len(M.mat)==len(M.mat[0])

    def I(M):
        if not Matrix.sqMatrix(M):
            raise ValueError('Invalid Error')
        else:
            A=Matrix()
            for i in range(len(M.mat)):
                R=[0]*len(M.mat)
                R[i]=1
                A.mat.append(R)
            return A

    def __pow__(M, n):
        if(n==0):
            return Matrix.I(M)
        E=Matrix.I(M)
        errorTerm=1e-5
        while(n>errorTerm):
            if n%2 == 1:
                E=E*M
            n=int(n/2)
            M=M*M
        return E

    def cof(M, mat, temp, p, q, n):
        i=0
        j=0
        for row in range(n):
            for col in range(n):
                if(row!=p)and(col!=q):
                    temp[i][j]=mat[row][col]
                    j+=1
                    if j==n-1:
                        j=0
                        i+=1
        return temp

    def determinant(M, mat, n):
        if len(mat)==len(mat[0]):
            if n==1:
                return mat[0][0]
            elif n==2:
                return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
            else:
                determinant=0
                sign=1
                X=[[0]*n for i in range(n)]
                for i in range(n):
                    X=Matrix.cof(M, mat, X, 0, i, n)
                    determinant+=sign*int(mat[0][i]*Matrix.determinant(M, X, n-1))
                    sign = -sign
                return determinant
        else:
            raise ValueError('Invalid Input')

#Driver's code 

r1=[1,2,3]
r2=[2,3,4]
r3=[1,4,3]
r4=[1,2,3]
r5=[1,3,4]
r6=[1,2,5]
r7=[1,2,6]

A=Matrix(r1,r2,r3)
B=Matrix(r4,r5,r6)

print(A.mat)
print(B.mat)

try:
    C= A+B
    D= A-B
    E= (A**2)*A
    F= A**3
    print(A.determinant(A.mat, len(A.mat)))
    print(F.determinant(F.mat, len(F.mat)))
    print(C.mat)
    print(D.mat)
    print(E.mat)
    print(F.mat)
except ValueError as m:
    print(m)