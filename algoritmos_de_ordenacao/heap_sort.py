"""
Implementação do algoritmo heap sort em python

Para rodar o doctest use o comando:
python -m doctest -v heap_sort.py
ou
python3 -m doctest -v heap_sort.py
Para o teste manual use:
python heap_sort.py
"""


def max_heapify(A,i,tamanho_heap):
    l = 2*i+1
    r = 2*i+2
    if l <tamanho_heap and A[l]>A[i]:
        maior = l
    else:
        maior = i
    if r < tamanho_heap and A[r]>A[maior]:
        maior = r
    if maior!=i:
        A[i],A[maior] = A[maior], A[i]
        max_heapify(A,maior,tamanho_heap)

    else:
        return(A)


def build_max_heap(A,tamanho_heap):
    for i in range((len(A)//2)-1,-1,-1):
        max_heapify(A,i,tamanho_heap)
    return(A)
        

def heap_sort(A):
    '''
    >>> heap_sort([0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> heap_sort([1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    '''
    tamanho_heap = len(A)
    build_max_heap(A,tamanho_heap)
    for i in range(len(A)-1,-1,-1):
        A[0],A[i] = A[i],A[0]
        tamanho_heap -=1
        max_heapify(A,0,tamanho_heap)
    
    return A

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(heap_sort(array))


  
