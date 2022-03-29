"""
Implementação do algoritmo selection sort em python

Para rodar o doctest use o comando:
python -m doctest -v selection_sort.py
ou
python3 -m doctest -v selection_sort.py
Para o teste manual use:
python selection_sort.py
"""


def selection_sort(A):
    """
    >>> selection_sort([0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> selection_sort([ 1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    """

    for i in range(0,len(A)):
        i_min = i
        for j in range(i+1,len(A)):
            if A[j] < A[i_min]:
                i_min = j
        if A[i] != A[i_min]:
            A[i],A[i_min] = A[i_min],A[i]
            
    return A

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(selection_sort(array))
