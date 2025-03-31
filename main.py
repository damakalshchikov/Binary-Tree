from Classes.Node import Node
from Functions.work_with_tree import appropriate_descendants, read_file, draw_tree, find_longest_path, draw_path


def main():

    # Печать приветственной информации и ввод источника данных
    print("Данная программа находит длиннейший путь(пути),\nвдоль которого номера вершин упорядочены по возрастанию\n")
    file_name: str = input("Введите имя файла для считывания входных данных: ")

    # Вызов ф-ии, которая преобразует текстовый файл в массив с вершинами дерева
    tree: list[Node | None] = read_file(file_name)

    # Вызов ф-ии, которая устанавливает связь между вершинами в соответствии с исходными данными
    appropriate_descendants(tree)

    # Отладочная печать
    # for index, node in enumerate(tree):
    #     if node is None:
    #         print(f"None")
    #         continue
    #
    #     print(f"Вершина {node}. Левый потомок {node.left}, правый потомок {node.right}")

    # Вызов ф-ии, которая создаёт изображение бинарного дерева
    draw_tree(tree)

    # Вызов ф-ии поиска длиннейших возрастающих путей
    longest_paths = find_longest_path(tree)

    # Вывод найденных путей
    if not longest_paths:
        print("\nВ данном дереве нет возрастающих путей.")
    else:
        print(f"\nНайдено {len(longest_paths)} длиннейших возрастающих путей:")

        for i, path in enumerate(longest_paths, 1):
            path_str = " -> ".join(str(node.number) for node in path)
            print(f"Путь {i}: {path_str} (длина: {len(path)})")
            # Вызов ф-ии, которая визуализирует найденные пути
            draw_path(tree, path, output_png=f"./Images/path{i}.png")


if __name__ == "__main__":
    main()
