import numpy as np

arr = np.random.randint(100, 500, size=12)
print(arr)

mat = arr.reshape(3, 4)
print(mat)

totalSemana = np.sum(mat, axis=1)
print(totalSemana)

mediaDiaria = np.mean(mat, axis=0)
print([f"{val:.2f}" for val in mediaDiaria])

acima400 = np.sum(mat>400)
print(acima400)