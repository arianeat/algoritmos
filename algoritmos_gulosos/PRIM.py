'''
Implementação do algoritmo de PRIM em python


Arquivo de entrada:
  n
  Wij (triângulo superior)

  onde: n = |V|
        Wij = função de pesos das arestas (triângulo superior da Matriz de Adjacência)

Arquivo exemplo:
  4
  23 17 19
  22 20
  25
'''

def Prim(arquivo):

    #criando a matriz de adjacencia do grafo
    matriz = criarMatrizAdj(arquivo)

    #criando a lista de adjacencia do grafo
    lista = criarListaAdj(matriz)

    #criando o vetor das arestas com os valores correspondentes de pai e chave
    V=[] 
    r = 0 # O vertice que vai inicializar a árvore

    for i in range(0,len(matriz[0])):
        v =[]
        v.append(i) #vertice
        v.append(0)  #pai
        v.append(float('inf'))  #chave
        V.append(v)  

    V[r][2] = 0 #Marcando o vertice que vai inicializar

    #Para acessar o vertice -> V[vertice][0]
    #Para acessar o pai do vertice-> V[vertice][1]
    #Para acessar a chave -> V[vertice][2]
    
    #vetor para marcar os vertices já  percorridos
    visitados = [False] * (len(matriz[0]))

    #iniciando as ligações das árvores
    Q = V.copy()
    
    while Q != []:
        u = build_min_heap(Q)
        min = u[0]
        visitados[min] = True
        for v in lista[min]:
            if visitados[v]== False and matriz[min][v]<V[v][2]:
                V[v][1]=min #pai
                V[v][2]=matriz[min][v] #chave
        Q.remove(u) 

    #somando o caminho
    soma = 0
    for i in V:
        soma += i[2]
    
    return soma

def criarListaAdj(matriz):
    lista = []
    for linha in matriz:
        y = []
        i=0
        for x in linha:
            if x != 0:
                y.append(i)
            i+=1
        lista.append(y)
    return lista
       

def criarMatrizAdj(arquivo):

    with open(arquivo) as f:
     
        n = int(f.readline())
        
        #criando a matriz
        matriz = []
        for i in range(n):
            matriz.append([0] * n)

        dados = f.readlines()
        
        #adicionando os numeros na matriz
        i = 0
        for linha in dados:
            valores = linha.split()
            k=0
            for j in range(i+1,n):
                matriz[i][j] = int(valores[k])
                matriz[j][i] = matriz[i][j] 
                k+=1
            i+=1

        return matriz


def min_heapify(A,i):
    l = 2*i+1
    r = 2*i+2
    if l <len(A) and A[l][2]<A[i][2]:
        menor = l
    else:
        menor = i
    if r < len(A) and A[r][2]<A[menor][2]:
        menor = r
    if menor!=i:
        A[i],A[menor] = A[menor], A[i]
        min_heapify(A,menor)

    else:
        return A

def build_min_heap(A):
    for i in range((len(A)//2)-1,-1,-1):
        min_heapify(A,i)
    return A[0]
