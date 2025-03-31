from Classes.Node import Node
from Functions.work_with_tree import appropriate_descendants, read_file, draw_tree, find_longest_path


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


if __name__ == "__main__":
    main()
