# P-1: Add two 3D arrays
# Write a Python function that takes two three-dimensional numeric data sets and adds them componentwise. 

A = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

B = [
    [[1, 1], [1, 1]],
    [[2, 2], [2, 2]]
]

result = []

for i in range(len(A)):
    layer = []
    for j in range(len(A[i])):
        row = []
        for k in range(len(A[i][j])):
            row.append(A[i][j][k] + B[i][j][k])
        layer.append(row)
    result.append(layer)

print("Result:")
print(result)