from Classes.Node import Node


def read_file(file_name: str) -> list[Node or None]:
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


def appropriate_descendants(tree: list[Node or None]) -> None:
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
