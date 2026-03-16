from typing import Sequence
from matplotlib.pylab import f
import numpy as np

tempmedia = np.random.randint(20, 27, size=7)
print(f"temp media {np.median(tempmedia)} e mais quente {np.max(tempmedia)}")

v = np.array([1,2,2,3,4,4,4,5])
print(f"valores únicos: {np.unique(v)}")

interp = np.linspace(0, 10, num=5)
print(f"interpolação: {interp}")

vendas = np.random.randint(50,200, size=(3,4))
print(f"media por produto: {np.median(vendas,axis=0)}")

m = np.array([[0.2, 0.3, 0.5],
              [80, 90, 70]])
print(f"media ponderada: {np.multiply(m[0], m[1]).sum()}")

testes = np.array([75, 88, 92, 65, 70, 80, 95, 60, 85, 78])
print(f"minino: {np.min(testes)}, maximo: {np.max(testes)}")

e = np.random.randint(1, 24, size=(2,3))
print(f"original {e}")
print(f"transposta: {e.T}")

b = np.array(np.where(np.random.rand(5)))
print(f"valores maiores que 0.7: {b[b>0.7]}")

invertereixos = np.array([[1,2,3],[4,5,6]])
print(f"original: {invertereixos}")
print(f"invertido: {np.flip(invertereixos)}")

acoes = np.array([120.50, 121.00, 119.80, 122.30, 120.00])
print(f"variação percentual: {np.diff(acoes)/acoes[:-1]*100/5}%")

a = np.array([1, 2, 3]) 
b = np.array([3, 2, 1])
print(f"iguais {np.array_equal(a, b)}")

print(f"identidade: {np.eye(4)}")

print(f"mascara booleana: {np.where(np.random.randint(0,100, size=10)>50)}")

print(f"zero: {np.zeros((3,3))}, um: {np.ones((2,5))}")

al = np.random.randint(1, 100, size=25)
print(f"reshape: {al.reshape(5,5)}")

print(f"contagem: {np.array([1, 7, 3, 7, 5, 7].count(7))}")

print(f"arreodndamento: {np.round(np.array([1.23, 2.78, 3.50, 4.11]), 0)}")

print(f"pares index booleano: {np.where(np.arange(10)%2==0)}")

print(f"combina 2d: {np.stack((np.array([1,2,3]), np.array([4,5,6])))}")

print(f"soma acumulada: {np.cumsum(np.array([1, 2, 3, 4, 5]))}")


