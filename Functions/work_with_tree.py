import pydot

import Classes


def read_file(file_name: str) -> list[Classes.Node | None]:
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

            node: Classes.Node = Classes.Node(int(node))
            tree.append(node)

    return tree


def appropriate_descendants(tree: list[Classes.Node | None]) -> None:
    """
    Присваивает вершинам соответствующих потомков.
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


def draw_tree(tree: list[Classes.Node | None], output_png: str = "./Images/tree.png") -> None:
    """
    Визуализирует бинарное дерево.
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
            picture.add_edge(pydot.Edge(str(index), right_index))

    picture.write(output_png, format="png")


def draw_path(tree: list[Classes.Node | None], path: list[Classes.Node], output_png: str = "./Images/paths.png") -> None:
    """
    Визуализирует бинарное дерево с выделенным путём
    :param tree: Список вершин бинарного дерева
    :param path: Путь, который нужно выделить
    :param output_png: Имя выходного файла
    :return: None
    """

    picture: pydot.Dot = pydot.Dot(graph_type="digraph")

    # Создаем словарь для быстрого поиска индекса узла в дереве
    node_indices: dict[Classes.Node, int] = {}
    for index, node in enumerate(tree):
        if node is not None:
            node_indices[node] = index

    # Формируем множество вершин, входящих в путь
    path_nodes: set = set(path)

    # Добавляем все вершины на граф
    for index, node in enumerate(tree):
        if node is None:
            continue

        # Если вершина входит в путь, выделяем ее цветом
        if node in path_nodes:
            pydot_node = pydot.Node(str(index), label=str(node.number), style="filled", fillcolor="lightblue")
        else:
            pydot_node = pydot.Node(str(index), label=str(node.number))

        picture.add_node(pydot_node)

    # Добавляем все ребра
    none_count: int = 0
    limit: int = len(tree)

    for index, node in enumerate(tree):
        if node is None:
            none_count += 2
            continue

        left_index: int = index * 2 + 1 - none_count
        right_index: int = index * 2 + 2 - none_count

        # Добавляем ребро к левому потомку
        if left_index < limit and tree[left_index] is not None:
            # Проверяем, является ли ребро частью пути
            is_path_edge: bool = (
                    node in path_nodes and tree[left_index] in path_nodes and
                    path.index(tree[left_index]) == path.index(node) + 1
            )

            if is_path_edge:
                picture.add_edge(pydot.Edge(str(index), str(left_index), color="blue", penwidth=2.0))
            else:
                picture.add_edge(pydot.Edge(str(index), str(left_index)))

        # Добавляем ребро к правому потомку
        if right_index < limit and tree[right_index] is not None:
            # Проверяем, является ли ребро частью пути
            is_path_edge: bool = (
                    node in path_nodes and tree[right_index] in path_nodes and
                    path.index(tree[right_index]) == path.index(node) + 1
            )

            if is_path_edge:
                picture.add_edge(pydot.Edge(str(index), str(right_index), color="blue", penwidth=2.0))
            else:
                picture.add_edge(pydot.Edge(str(index), str(right_index)))

    picture.write(output_png, format="png")


def find_longest_path(tree: list[Classes.Node | None]) -> list[list[Classes.Node]]:
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
    longest_path: dict[Classes.Node, list[list[Classes.Node]]] = {}
    max_length: int = 0

    # Рекурсивная функция для поиска путей
    def dfs(node: Classes.Node) -> list[list[Classes.Node]]:
        # Базовый случай
        if node in longest_path:
            return longest_path[node]

        paths: list[list[Classes.Node]] = [[node]]

        if node.left and node.left.number > node.number:
            left_path: list[list[Classes.Node]] = dfs(node.left)
            for path in left_path:
                paths.append([node] + path)

        if node.right and node.right.number > node.number:
            right_path: list[list[Classes.Node]] = dfs(node.right)
            for path in right_path:
                paths.append([node] + path)

        max_path_length: int = max(len(path) for path in paths)
        longest_path_from_node: list[list[Classes.Node]] = [path for path in paths if len(path) == max_path_length]

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

    result_paths: list[list[Classes.Node]] = []
    seen_paths: set = set()

    for path in all_longest_paths:
        if len(path) == max_length:
            path_tuple = tuple(node.number for node in path)
            if path_tuple not in seen_paths:
                seen_paths.add(path_tuple)
                result_paths.append(path)

    return result_paths
