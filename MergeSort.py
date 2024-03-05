import sys
import random
# Ao longo do script, estou seguindo a notacao do livro

inf = sys.maxsize
# trying to really learn the merge sort

#p eh a pos mais esquerda
#q meio
#r pos mais a direita


#lista, inicio e fim
def MergeSort(vector, p = 0, r = None):

      if r is None:
            r = len(vector)
            print(r)
      #Mergesort(vector,inicio, fim)
      #condicao de parada:
      #se ainda tiver um item
      if (p < r - 1):
            q = (p + r) // 2 # meio recebe (meio + fim)/2
            MergeSort(vector,p,q) #mergesort(lista,inicio, meio)
            MergeSort(vector,q + 1,r) #mergesort(lista, item seguinte ao meio, fim)
            Merge(vector,p, q, r)



#The .extend() method allows you to add more items to the end of a list

def Merge(vector, p, q, r):
      R = []
      L = []
      q = len(vector) // 2 # meio do vetor
      p = vector[:q] #pos mais esquerda
      r = vector[q:] # +1 pq estou excluindo a pos do meio 
      n1 = len(vector[:q])
      n2 =  len(vector[q:])


      print("len p",len(p))
      print("len r",len(r))


      L = p.copy()
      R = r.copy()
      


      L.insert(len(L),inf)
      R.insert(len(R), inf)

      print("L", L)
      print("R", R)

      i = j = 0
      for k in range(len(p),len(r)): 
           if (L[i] <= R[j]):
                 vector[k] = L[i]
                 i += 1
           else:
                  vector[k] = R[j]
                  j += 1
      print("sorted vec", vector)


if __name__ == "__main__":
      #random_list = random.sample(range(1,1000), 8)
      A = [744, 591, 491, 452, 413, 775, 245, 141]
      
      print("Caso teste:", A)
      MergeSort(A)
      print("Caso teste ordenado",A)
