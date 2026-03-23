
A = [[4, 7],
     [2, 6]]
B = [[1, 3],
     [5, 2]]


result = [[0, 0],
          [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

print("Resultant Matrix:")
for row in result:
    print(row)