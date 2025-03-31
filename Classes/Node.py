class Node:
    """
    Класс, который представляет вершину бинарного дерева
    """

    def __init__(self, number) -> None:
        self.number = number
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.number)
