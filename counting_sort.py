"""
Implementação do algoritmo counting sort em python

Para rodar o doctest use o comando:
python -m doctest -v counting_sort.py
ou
python3 -m doctest -v counting_sort.py
Para o teste manual use:
python counting_sort.py
"""


def counting_sort(A):
    """
    >>> counting_sort([0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> counting_sort([ 1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    """
    
    min = 0
    for i in range(0,len(A)):
        if A[i]<min:
            min=A[i]

    if min<0:
        for i in range(0,len(A)):
            A[i] = A[i] + abs(min)

    k = 0
    for i in range(0,len(A)):
        if A[i]>k:
            k=A[i]
    
    B = [0] * len(A)

    C = [0] * (k+1)

    for i in range(0,len(A)):
        C[A[i]] += 1

    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]

    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]=C[A[i]]-1

    if min<0:
        for i in range(0,len(B)):
            B[i] = B[i] - abs(min)

    return B

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(counting_sort(array))
