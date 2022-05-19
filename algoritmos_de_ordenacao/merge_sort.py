"""
Implementação do algoritmo merge sort em python

Para rodar o doctest use o comando:
python -m doctest -v merge_sort.py
ou
python3 -m doctest -v merge_sort.py
Para o teste manual use:
python merge_sort.py
"""

def merge(ini,meio,fim,A):
    
    W=[0] * (fim-ini)
  
    i=ini
    j=meio
    k=0
    while i<meio and j<fim:
        if A[i]<=A[j]:
            W[k]=A[i]
            k+=1
            i+=1
        else:
            W[k]=A[j]
            k+=1
            j+=1
    while i<meio:
        W[k]=A[i]
        k+=1
        i+=1
    while j<fim:
        W[k]=A[j]
        k+=1
        j+=1
    for x in range(ini,fim):
        A[x]=W[x-ini]
    return A


def merge_sort(ini,fim,A):
    '''
    >>> merge_sort(0,7,[0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> merge_sort(0,1,[])
    []
    >>> merge_sort(0,4,[-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> merge_sort(0,11,[1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    '''
    if ini<(fim-1):
        meio = (ini+fim)//2
        merge_sort(ini,meio,A)
        merge_sort(meio,fim,A)
        merge(ini,meio,fim,A)

    return A

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(merge_sort(0,len(array),array))

