"""
Implementação do algoritmo max heapify em python

Para rodar o doctest use o comando:
python -m doctest -v max_heap.py
ou
python3 -m doctest -v max_heap.py
Para o teste manual use:
python max_heap.py
"""


def max_heapify(A,i):
    l = 2*i+1
    r = 2*i+2
    if l <len(A) and A[l]>A[i]:
        maior = l
    else:
        maior = i
    if r < len(A) and A[r]>A[maior]:
        maior = r
    if maior!=i:
        A[i],A[maior] = A[maior], A[i]
        max_heapify(A,maior)

    else:
        return(A)

def build_max_heap(A):
    '''
    >>> build_max_heap([27, 17, 3, 16, 13, 10, 15, 7, 12, 4, 8, 9, 0])
    [27, 17, 15, 16, 13, 10, 3, 7, 12, 4, 8, 9, 0]
    >>> build_max_heap([])
    []
    >>> build_max_heap([-2, -5, -8, -1, -45])
    [-1, -2, -8, -5, -45]
    >>> build_max_heap([1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [5, 4, 2, 3, 2, 1, -2, -5, -3, -45, 0]
    '''
    for i in range((len(A)//2)-1,-1,-1):
        max_heapify(A,i)
    return(A)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(build_max_heap(array))
