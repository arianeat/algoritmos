"""
Implementação do algoritmo quick sort em python

Para rodar o doctest use o comando:
python -m doctest -v quick_sort.py
ou
python3 -m doctest -v quick_sort.py
Para o teste manual use:
python quick_sort.py
"""

def partition(ini,fim,A):
    pivo = A[ini]
    a = ini+1
    b = fim
    while (1):
        while A[b]>=pivo and b>=a:
            b -=1
        while a<=b and A[a]<=pivo:
            a +=1
        if (a<=b): 
            A[a],A[b]=A[b],A[a]
        else:
            A[ini],A[b]=A[b],A[ini]
            return b


def quick_sort(ini,fim,A):
    '''
    >>> quick_sort(0,6,[0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> quick_sort(0,0,[])
    []
    >>> quick_sort(0,3,[-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> quick_sort(0,10,[1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    '''
    if ini<fim:
        q = partition(ini,fim,A)
        quick_sort(ini,q-1,A)
        quick_sort(q+1,fim,A)

    return A

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(quick_sort(0,len(array)-1,array))


