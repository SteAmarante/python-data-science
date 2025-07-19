#vetor

import numpy as np

#cria um vetor com numpy
print("------------------------")
print("---------VETOR----------")
print("------------------------")
meu_vetor = np.array([10, 11, 13, 11, 14, 15])
print(meu_vetor)
print("\n")


print("------------------------")
print("---------MATRIX---------")
print("------------------------")

#matriz
#cria uma matriz 2 x 3 
minha_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(minha_matrix.shape) #resultado: (2,3)
print("\n")
print(minha_matrix) #resultado: (2,3)


print("------------------------")
print("---------TENSOR---------")
print("------------------------")
#tensor
#cria um tensor 3, 2, 3
meu_tensor = np.array([
    [
        [0,1,0], [1,0,1]
    ],
    [
        [0,1,0], [1,0,1]
    ],
    [
        [0,1,0], [1,0,1]
    ]
])
print(meu_tensor.shape)
print("\n")
print(meu_tensor)
