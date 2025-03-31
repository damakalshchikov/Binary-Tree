import pydot

from Classes.Node import Node


def read_file(file_name: str) -> list[Node | None]:
    """
    Читает файл и преобразует строки в тип None или тип Node.
    :param file_name: Имя файла
    :return: Массив с элементами типа Node или None
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
    Данная функция присваивает вершинам соответствующих потомков.
    :param tree: Массив с вершинами
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
    Данная функция визуализирует бинарное дерево.
    :param tree: Массив со связанными вершинами дерева
    :param output_png: Имя выходного файла
    :return: None
    """

    picture: pydot.Dot = pydot.Dot(graph_type="digraph")

    for index, node in enumerate(tree):
        if node is None:
            continue

        pydot_node = pydot.Node(str(index), label=str(node.number))
        picture.add_node(pydot_node)

    none_count: int = 0
    limit: int = len(tree)

    for index, node in enumerate(tree):
        if node is None:
            none_count += 2
            continue

        left_index: int = index * 2 + 1 - none_count
        right_index: int = index * 2 + 2 - none_count

        if left_index < limit and tree[left_index] is not None:
            picture.add_edge(pydot.Edge(str(index), left_index))
        if right_index < limit and tree[right_index] is not None:
            graph.add_edge(pydot.Edge(str(index), right_index))
            picture.add_edge(pydot.Edge(str(index), right_index))

    picture.write(output_png, format="png")

    graph.write(output_png, format="png")


def find_longest_path(tree: list[Node | None]) -> list[list[Node]]:
    """
    Находит все длиннейшие пути в бинарном дереве,
    вдоль которых номера вершин упорядочены по возрастанию.
    :param tree: Список вершин бинарного дерева
    :return: Список путей
    """

    # Проверка на пустое дерево
    if not tree or tree[0] is None:
        return []

    # Словарь для хранения максимальной длины пути, начинающегося с каждой вершины
    longest_path: dict[Node, list[list[Node]]] = {}
    max_length: int = 0

    # Рекурсивная функция для поиска путей
    def dfs(node: Node) -> list[list[Node]]:
        # Базовый случай
        if node in longest_path:
            return longest_path[node]

        paths = [[node]]

        if node.left and node.left.number > node.number:
            left_path = dfs(node.left)
            for path in left_path:
                paths.append([node] + path)

        if node.right and node.right.number > node.number:
            right_path = dfs(node.right)
            for path in right_path:
                paths.append([node] + path)

        max_path_length: int = max(len(path) for path in paths)
        longest_path_from_node = [path for path in paths if len(path) == max_path_length]

        longest_path[node] = longest_path_from_node
        return longest_path[node]

    all_longest_paths = []
    for node in tree:
        if node is not None:
            node_paths = dfs(node)
            longest_from_node = max(len(path) for path in node_paths)

            if longest_from_node > max_length:
                max_length = longest_from_node
                all_longest_paths = node_paths
            elif longest_from_node == max_length:
                all_longest_paths.extend(node_paths)

    result_paths = []
    seen_paths = set()

    for path in all_longest_paths:
        if len(path) == max_length:
            path_tuple = tuple(node.number for node in path)
            if path_tuple not in seen_paths:
                seen_paths.add(path_tuple)
                result_paths.append(path)

    return result_paths
