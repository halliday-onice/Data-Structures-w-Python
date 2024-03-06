import sys
import random
# Ao longo do script, estou seguindo a notacao do livro


# trying to really learn the merge sort

#p eh a pos mais esquerda
#q meio
#r pos mais a direita
#lista, inicio e fim
def MergeSort(vector, p, r):

      #Mergesort(vector,inicio, fim)
      #condicao de parada:
      #se ainda tiver um item
      if (p < r):
            q = (p + r) // 2 # meio recebe (meio + fim)/2
            MergeSort(vector,p,q) #mergesort(lista,inicio, meio)
            MergeSort(vector, q + 1, r) #mergesort(lista, item seguinte ao meio, fim)
            Merge(vector,p, q, r)
            print("L",vector[p: q + 1], "and", vector[q + 1: r + 1])




#The .extend() method allows you to add more items to the end of a list

def Merge(vector, p, q, r):
 
      n1 = q - p + 1 # +1 pq o q tá dentro do n1
      n2 =  r - q


      L = [0] * n1
      R = [0] * n2

      for i in range(0, n1):
            L[i] = vector[p + i]

      for j in range(0, n2):
            R[j] = vector[q + 1 + j]
      
      print("N1",n1)
      print("N2",n2)
      i = 0
      j  = 0
      k = p
      while i < n1 and j < n2:
            if L[i] <= R[j]:
                  vector[k] = L[i]
                  print("L[I]",L[i])
                  i += 1
            else:
                  vector[k] = R[j]
                  print("R[I]", R[j])
                  j += 1
            k += 1
            
            
            print("vector", vector[k])
      #print("i,j", i,j)
      #preciso copiar algum elemento de L[] restante se houver
      while i < n1:
            vector[k] = L[i]
            i += 1
            k += 1
      while j < n2:
            vector[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
      #random_list = random.sample(range(1,1000), 8)
      A = [744, 591, 491, 452, 413, 775, 245]
      tamA = len(A)
      print("Caso teste:", A)
      MergeSort(A,0,tamA - 1)
      print("Caso teste ordenado",A)
