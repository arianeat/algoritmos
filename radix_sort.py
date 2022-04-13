"""
Implementação do algoritmo radix sort em python

Para rodar o doctest use o comando:
python -m doctest -v radix_sort.py
ou
python3 -m doctest -v radix_sort.py
Para o teste manual use:
python radix_sort.py
"""


def counting_sort(A,exp1):
        
        k = 0
        for i in range(0,len(A)):
            if int((A[i]/exp1)%10)>k:
                k = int((A[i]/exp1)%10)

        B = [0] * len(A)

        C = [0] * (k+1)

        for i in range(0,len(A)):
            C[int((A[i]/exp1)%10)] += 1

        for i in range(1,k+1):
            C[i] = C[i] + C[i-1]

        for i in range(len(A)-1,-1,-1):
            B[C[int((A[i]/exp1)%10)]-1]=A[i]
            C[int((A[i]/exp1)%10)]-=1
    
        i = 0
        for i in range(0,len(A)): 
            A[i] = B[i] 
        
        return A


def radix_sort(A):
    """
    >>> radix_sort([0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> radix_sort([])
    []
    >>> radix_sort([-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> radix_sort([ 1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    """
    min = 0
    for i in range(0,len(A)):
        if A[i]<min:
            min=A[i]

    if min<0:
        for i in range(0,len(A)):
            A[i] = A[i] - min

    max1 = 0
    for i in range(0,len(A)):
        if A[i]>max1:
            max1=A[i]

    exp=1
    while max1/exp>1:
        counting_sort(A,exp)
        exp *=10

    if min<0:
        for i in range(0,len(A)):
            A[i] = A[i] + min
    
    return A


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    #array = [ 170, 45, 75, 90, 802, 24, 2, 66]

    print(radix_sort(array))

