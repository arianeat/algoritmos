"""
Implementação do algoritmo insertion sort em python

Para rodar o doctest use o comando:
python -m doctest -v insertion_sort.py
ou
python3 -m doctest -v insertion_sort.py
Para o teste manual use:
python insertion_sort.py
"""


def insertion_sort(A):
    """
    >>> insertion_sort([0, 1, 4, 5, 3, 2, 2])
    [0, 1, 2, 2, 3, 4, 5]
    >>> insertion_sort([])
    []
    >>> insertion_sort([-2, -5, -3, -45])
    [-45, -5, -3, -2]
    >>> insertion_sort([ 1, 4, 5, 3, 2, 2, -2, -5, -3, -45, 0])
    [-45, -5, -3, -2, 0, 1, 2, 2, 3, 4, 5]
    """

    for i in range(1,len(A)):
        pivo = A[i]
        while i>0 and A[i-1]> pivo:
            A[i] = A[i-1]
            i -= 1
        A[i] = pivo
    return A

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    numbers = input("Entre com os números separados por vírgula:\n").strip()
    array = [int(item) for item in numbers.split(",")]
    print(insertion_sort(array))
