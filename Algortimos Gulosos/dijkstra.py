'''
Implementação do algoritmo de Dijkstra em python


Arquivo de entrada:
  n
  dij (triângulo superior)

  onde: n = |V|
        dij = função de distâncias das arestas (triângulo superior da Matriz de Adjacência)

Arquivo exemplo:
  4
  23 17 19
  22 20
  25
'''

def Dijkstra(arquivo):

    #criando a matriz de adjacencia do grafo
    matriz = criarMatrizAdj(arquivo)

    #criando a lista de adjacencia do grafo
    lista = criarListaAdj(matriz)

    ini = 0
    fim = len(matriz)-1

    #criando o vetor das arestas com os valores correspondentes de pai e chave
    V=[] 
   
    #INICIALIZA-SINGLE-SOURCE
    for i in range(0,len(matriz[0])):
        v =[]
        v.append(i) #vertice
        v.append(0)  #pai
        v.append(float('inf'))  #chave
        V.append(v)  

    V[ini][2] = 0 #Marcando o vertice que vai inicializar

    #Para acessar o vertice -> V[vertice][0]
    #Para acessar o pai do vertice-> V[vertice][1]
    #Para acessar a chave -> V[vertice][2]

    #vetor para marcar os vertices já  percorridos
    visitados = [False] * (len(matriz[0]))

    #iniciando as ligações das árvores
    Q = V.copy()
    
    while Q != []:
        u = build_min_heap(Q)
        visitados[u[0]] = True
        for v in lista[u[0]]:
            #RELAX
            if visitados[v]== False and V[v][2]> V[u[0]][2] + matriz[u[0]][v]:
                V[v][1]= u[0]
                V[v][2]= (V[V[v][1]][2] + matriz[u[0]][v]) 
        Q.remove(u)
        
  
    #valor do caminho minimo
    for v in V:
        if v[0]==fim:
            s = v[2]

    #trajeto do caminho
    caminho = []
    aux=fim
    caminho.append(aux)
    while caminho[-1]!=ini:
        for v in V:
            if v[0]==aux:
                caminho.append(v[1])
                aux=v[1]
    caminho = [num for num in reversed(caminho)]

    return s

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

