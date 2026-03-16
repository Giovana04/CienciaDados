import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

mat = np.bool(arr%0==0)
print(mat)

impar = np.extract(arr%2==1, arr)
print(impar)

arr = np.where(arr%2==1, -1, arr)
print(arr)

matrizAle = np.random.randint(1, 100, size=(5,5))
print(matrizAle)

somaCol = np.sum(matrizAle, axis=0)
print(somaCol)

maxLinha = np.max(matrizAle, axis=1)
print(maxLinha)

a = np.array([1, 2, 3, 4, 5])
for x in range(3,8,2): 
    a = np.insert(a, x, 2)
print(a)

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))

inv = np.array([10,20,30,40])
print(inv[::-1])