import sys

# trying to really learn the merge sort

A = [2,4, 5, 7, 1, 2, 3 , 6]

print(len(A))

# p eh a pos mais esquerda
#q meio
#r pos mais a direita
L = []
R = []
def Merge(vector, p, q, r):
      n1 = q - p + 1 #n1 eh o indice do vetor Left
      n2 = r - p #n2 eh o indice do vetor Right



