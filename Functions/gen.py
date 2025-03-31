import random

import Classes


def gen_tree(values: list[int]) -> Classes.Node | None:
    """
    Создаёт вершину бинарного дерева или None
    :param values: Числовые значения вершин
    :return: Classes.Node | None
    """

    if not values:
        return None

    root: Classes.Node = Classes.Node(values[0])

    if len(values) == 1:
        return root

    # Определяем случайное число вершин для левого поддерева
    left_count = random.randint(0, len(values) - 1)

    left_values = values[1:1 + left_count]
    right_values = values[1 + left_count:]

    root.left = gen_tree(left_values)
    root.right = gen_tree(right_values)

    return root


def get_txt_tree(root: Classes.Node) -> list[str]:
    """
    Собирает в один массив строковые литералы
     сгенерированных вершин или None
    :param root: Вершина, или None
    :return: Массив строковых литералов вершин и None
    """

    if not root:
        return []

    result: list[str] = []
    queue: list[Classes.Node] = [root]

    while queue:
        node: Classes.Node = queue.pop(0)
        if node:
            result.append(str(node.number))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("None")

    while result and result[-1] == "None":
        result.pop()

    return result


def gen_test_file(filename: str, n: int) -> None:
    """
    Записывает массив в текстовый файл
    :param filename: Имя выходного файла
    :param n: Количество вершин
    :return: None
    """

    values: list[int] = list(range(1, n + 1))
    random.shuffle(values)

    tree: Classes.Node | None = gen_tree(values)
    strings: list[str] = get_txt_tree(tree)

    with open(filename, "w") as file:
        for string in strings:
            file.write(string + "\n")
