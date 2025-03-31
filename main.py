import Classes
import Functions


def main(prog_mode: int, file: str, strings_count: int = 0) -> None:
    if prog_mode == 2:
        # Генерируем файл со структурой бинарного дерева
        Functions.gen_test_file(file, strings_count)

    # Чтение файла структуры бинарного дерева
    tree: list[Classes.Node | None] = Functions.read_file(file)

    # Устанавливаем связи между вершинами в соответствии со структурой файла
    Functions.appropriate_descendants(tree)

    # Генерируем изображение бинарного дерева
    Functions.draw_tree(tree)

    # Поиск длиннейших путей, вдоль которых вершины упорядочены по возрастанию
    longest_paths = Functions.find_longest_path(tree)

    # Если пути не были найдены, то информируем об этом
    if not longest_paths:
        print("\nВ данном дереве нет возрастающих путей.")
    else:
        # Если пути были найдены, то выводим их
        print(f"\nНайдено {len(longest_paths)} длиннейших возрастающих путей:")

        for i, path in enumerate(longest_paths, 1):
            path_str = " -> ".join(str(node.number) for node in path)
            print(f"Путь {i}: {path_str}")

            # Генерируем изображение найденного пути
            Functions.draw_path(tree, path, output_png=f"./Images/path{i}.png")


if __name__ == "__main__":
    # Очищаем каталог "Images"
    Functions.clear_images_folder()

    # Вывод информации и меню
    print(
        "Данная программа выполняет поиск длиннейших путей в бинарном дереве,\n"
        "вдоль которых вершины расположены в порядке возрастания.\n\n"
        "Меню:\n"
        "1 - чтение бинарного дерева из существующего файла.\n"
        "2 - генерация файла бинарного дерева и его чтение.\n\n"
    )

    # mode - режим работы программы
    # file_name - имя файла для чтения/генерации
    mode: int = int(input("Выберете режим работы программы: "))
    file_name: str = "./Cases/" + input("Введите имя файла: ")

    if mode == 1:
        # Работа программы в режиме 1
        main(mode, file_name)
    else:
        n: int = int(input("Введите количество вершин в бинарном дереве: "))
        # Работа программы в режиме 2
        main(mode, file_name, n)
