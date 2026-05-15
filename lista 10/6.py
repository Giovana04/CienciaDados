from sklearn.preprocessing import StandardScaler
import numpy as np

dados = np.array([[1.70, 70], [1.80, 80], [1.60, 60]]) 
dados_normalizados = StandardScaler().fit_transform(dados)
print(dados_normalizados)