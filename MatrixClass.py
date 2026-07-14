# Matrix Class (Addition and Multiplication)
class Matrix:

    def add(self, A, B):
        result = []

        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])
            result.append(row)

        return result

    def multiply(self, A, B):

        result = []

        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                total = 0
                for k in range(len(B)):
                    total += A[i][k] * B[k][j]
                row.append(total)
            result.append(row)

        return result


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

m = Matrix()

print("Addition:")
print(m.add(A, B))

print("Multiplication:")
print(m.multiply(A, B))