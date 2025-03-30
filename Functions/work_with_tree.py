import pydot

from Classes.Node import Node


def read_file(file_name: str) -> list[Node | None]:
    """
    Читает файл и преобразует строки в тип None или тип Node
    :param file_name: имя файла
    :return: массив с элементами типа Node или None
    """

    tree: list = []

    with open(file_name) as file:
        for node in file:
            node: str = node.strip()

            if node == "None":
                tree.append(None)
                continue

            node: Node = Node(int(node))
            tree.append(node)

    return tree


def appropriate_descendants(tree: list[Node | None]) -> None:
    """
    Данная функция присваивает вершинам соответствующих потомков
    :param tree: массив с вершинами
    :return: None
    """

    none_count: int = 0
    limit: int = len(tree)

    for index, node in enumerate(tree):

        if node is None:
            none_count += 2
            continue

        left_index: int = index * 2 + 1 - none_count
        right_index: int = index * 2 + 2 - none_count

        if left_index < limit:
            node.left = tree[left_index]
        if right_index < limit:
            node.right = tree[right_index]


def draw_tree(tree: list[Node | None], output_png: str = "./Images/tree.png") -> None:
    """
    Данная функция визуализирует бинарное дерево
    :param tree: массив со связанными вершинами дерева
    :param output_png: имя выходного файла
    :return: None
    """

    graph: pydot.Dot = pydot.Dot(graph_type="digraph")

    for index, node in enumerate(tree):
        if node is None:
            continue

        pydot_node = pydot.Node(str(index), label=str(node.number))
        graph.add_node(pydot_node)

    none_count: int = 0
    limit: int = len(tree)

    for index, node in enumerate(tree):
        if node is None:
            none_count += 2
            continue

        left_index: int = index * 2 + 1 - none_count
        right_index: int = index * 2 + 2 - none_count

        if left_index < limit and tree[left_index] is not None:
            graph.add_edge(pydot.Edge(str(index), left_index))
        if right_index < limit and tree[right_index] is not None:
            graph.add_edge(pydot.Edge(str(index), right_index))

    graph.write(output_png, format="png")
