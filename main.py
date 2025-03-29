from Classes.Node import Node
from Functions.work_with_tree import appropriate_descendants, read_file


def main():
    print("Данная программа находит длиннейший путь(пути),\nвдоль которого номера вершин упорядочены по возрастанию\n")
    file_name: str = input("Введите имя файла для считывания входных данных: ")


    tree: list[Node | None] = read_file(file_name)


    appropriate_descendants(tree)

    for index, node in enumerate(tree):
        if node is None:
            print(f"None")
            continue

        print(f"Вершина {node}. Левый потомок {node.left}, правый потомок {node.right}")


if __name__ == "__main__":
    main()
