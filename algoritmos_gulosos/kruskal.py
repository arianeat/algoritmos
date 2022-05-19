'''
Implementação do algoritmo de Kruskal em python


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

def Kruskal(arquivo):

    #criando a matriz de adjacencia do grafo
    matriz = criarMatrizAdj(arquivo)

    A = []  #conjunto de arestas selecionadas
      
    #criando o conjunto de arestas com o seu peso
    arestas = []
    i=0
    for linha in matriz:
        j=0
        for w in linha:
            a = []
            a.append(i)
            a.append(j)
            a.append(w)
            arestas.append(a)
            j+=1
        i+=1
    
    #ordenando o conjunto de arestas
    arestas = sorted(arestas, key = lambda x: x[2])

    #vetor auxiliar 
    aux = []
    for i in range(len(matriz[0])):
        aux.append(i)

    #formando a árvore
    for aresta in arestas:
        if aux[aresta[0]]!=aux[aresta[1]]:

            A.append(aresta)

            if aux[aresta[0]]<aux[aresta[1]]:
                pivo = aux[aresta[1]]
                for i in range(0,len(aux)):
                    if aux[i]==pivo:
                        aux[i]=aux[aresta[0]]
            else:
                pivo = aux[aresta[0]]
                for i in range(0,len(aux)):
                    if aux[i]==pivo:
                        aux[i]=aux[aresta[1]]

    # somando o caminho
    soma = 0
    for i in A:
        soma += i[2] 
    
    return soma

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

