import sys

inf = sys.maxsize
# trying to really learn the merge sort

#p eh a pos mais esquerda
#q meio
#r pos mais a direita
L = []
R = []
vector = []

#The .extend() method allows you to add more items to the end of a list
def Merge(vector, p, q, r):
      q = len(vector) // 2 # meio do vetor
      p = vector[:q] #pos mais esquerda
      r = vector[q:] # +1 pq estou excluindo a pos do meio 
      print("p", p)
      print("q", q)
      print("r", r)
      
      #n2 eh o indice do vetor Right
      n2 =  len(vector[q:])#n2 eh basicamente o ultimo elemento ate a metade
      L = p.copy()
      print("L", L)
      R = r.copy()
      print("R", R) 

      L.insert(len(L),inf)
      R.insert(len(R), inf)

      print("L", L)
      print("R", R)

      i = j = 0
      for k in range(len(vector)): 
           if (L[i] <= R[j]):
                 A[k] = L[i]
                 i += 1
           else:
                  A[k] = R[j]
                  j += 1
      print("sorted vec", vector)




            


if __name__ == "__main__":
      A = [2, 4, 5, 7, 1, 2, 3 , 6]
      Merge(A,0,3,7)
