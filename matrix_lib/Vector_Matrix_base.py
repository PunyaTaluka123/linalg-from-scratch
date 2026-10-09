#Build: add, scalar multiply, matmul, transpose, identity, dot product, norms (L1, L2, Frobenius), trace. Then a visualizer that applies a 2x2 matrix to a grid and plots the result (matplotlib).

class Matrix:
    def __init__(self, components):
        self.components = list(components)
        self.rows = len(self.components)
        self.cols = len(self.components[0]) if self.rows>0 else 0

    def __getitem__(self,index):
        return self.components[index]

    def __setitem__(self, index, value):
        self.components[index] = value
    
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError
            res = []
            for i in range(self.rows):
                r1 = []
                for j in range(other.cols):
                    total = 0
                    for k in range(other.rows):
                        total = total + self.components[i][k] * other.components[k][j]
                    r1.append(total)
                res.append(r1)
            return Matrix(res)
        elif isinstance(other, Vector):
            if self.cols != other.n:
                raise ValueError
            res = []
            for i in range(self.rows):
                total = 0
                for j in range(other.n):
                    total += self.components[i][j] * other[j]
                res.append(total)
            return Vector(res)

    def transpose(self):
        res = []
        for i in range(self.cols):
            res1 = []
            for j in range(self.rows):
                res1.append(self.components[j][i])
            res.append(res1)
        return Matrix(res)

    @classmethod
    def identity(cls, num):
        return cls([
            [1 if i==j else 0 for j in range(num)]
            for i in range(num)
        ])

    def Fnorm(self):
        total = 0
        for rows in self.components:
            for i in rows:
                total += i**2
        return total **0.5

    def trace(self):
        total = 0
        for i, rows in enumerate(self.components):
            total+=rows[i]
        return total

    def row_swap(self, i,j):
        if not (self.rows>i and self.rows>j):
            raise ValueError
        self.components[i], self.components[j] = self.components[j], self.components[i]

    def row_scale(self, i, scale):
        if not (self.rows>i):
            raise IndexError
        self[i] = [x*scale for x in self[i]]

    def row_add(self, i, j, scale = 1):
        self[i] = [self[i][k]+scale * self[j][k] for k in range(self.cols)]


    def ref(self):
        #Assuming no first cols are non-zero
        for i in range(min(self.rows, self.cols)):
            norm = self[i][i]
            self.row_scale(i, 1/norm)
            for j in range(i+1, self.rows):
                scale = self[j][i]
                self.row_add(j, i, -scale)
        return self



class Vector:
    def __init__(self, components: float):
        self.components = list(components)
        self.n = len(self.components)

    def __add__(self, vec):
        if self.n!= vec.n:
            raise ValueError
        return Vector(x+y for x,y in zip(self.components, vec.components))

    def __mul__(self, other):
        return Vector(x*other for x in self.components)

    def __rmul__(self, other):
        return self*other

    def __getitem__(self, index):
        return self.components[index]

    def dot(self, other):
        if self.n != other.n:
            raise ValueError

        total =0
        for i in range (len(self.components)):
            total += self.components[i] * other.components[i]
        return total    

    def L1_norm(self):
        total = 0
        for i in (self.components):
            total += abs(i)
        return total

    def L2norm(self):
        total = 0
        for i in (self.components):
            total += i**2
        return total**0.5

print((3*Vector([1, 2])).components)