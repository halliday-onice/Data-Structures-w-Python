import sys

inf = sys.maxsize
# trying to really learn the merge sort

# p eh a pos mais esquerda
#q meio
#r pos mais a direita
L = []
R = []
#The .extend() method allows you to add more items to the end of a list
def Merge(vector, p, q, r):
      n1 = q - p + 1 #n1 eh o indice do vetor Left
      n2 = r - p #n2 eh o indice do vetor Right
      L = [None for i in range(n1 + 1)]
      
      print(len(L))
            


if __name__ == "__main__":
      A = [2, 4, 5, 7, 1, 2, 3 , 6]
      Merge(A,0,3,7)
