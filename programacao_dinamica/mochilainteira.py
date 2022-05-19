'''
Implementação do algoritmo da Mochila Inteira em python


Arquivo de entrada:
  n M
  p1 v1
  p2 v2
  ...
  pn vn

  onde: n = |O
        M = capacidade da mochila
        pi = vetor dos pesos dos objetos
        vi = vetor dos valores dos objetos

Arquivo exemplo:
  4 30
  13 23
  23 29
  17 27
  19 25
'''

def mochilaInteira(arquivo):

    with open(arquivo) as f:
    
        n_m = f.readline().split()
        n = int(n_m[0])
        M = int(n_m[1])

        p = []
        v = []

        dados = f.readlines()
        
        i = 0
        for linha in dados:
            valores = linha.split()
            p.append(int(valores[0]))
            v.append(int(valores[1]))
    
        
    #criando tabela para armazenar os dados
    tabela = []
    for i in range(M+1):
        tabela.append([0] * (n+1))
    
    #inicialização
    for i in range(M+1):
        tabela[i][n] = [0]
    
    #preenchendo a tabela
    for i in range(n-1,-1,-1):  #coluna
        for y in range(0,M+1):    #linha
            valor1 = tabela[y][i+1][0]
            if y-p[i]<0:
                valor2 = 0
            else:
                valor2 = (tabela[y-p[i]][i+1][0] + v[i])
            if valor1>=valor2:
                tabela[y][i]=[valor1,0] 
            else:
                tabela[y][i]=[valor2,1]
        

    #vetor dos elementos presentes na mochila:
    X = []


    linha = M
    coluna = 0
    ganho = tabela[linha][coluna][0]

    i=0
    for x in range(len(tabela)-1,-1,-1):
        for y in range(n):
            if x==linha and y==coluna:
                if tabela[linha][coluna][1]==1:
                    X.append(i+1)
                    linha-=p[i]
                coluna+=1
                i+=1  

    return 'Ganho da mochila: ' + str(ganho) + '\nProdutos escolhidos: ' + str(X)[1:-1]

