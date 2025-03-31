from pathlib import Path


def clear_images_folder(folder: str = "./Images/") -> None:
    """
    Очищает каталог с изображениями
    :param folder: Название каталога
    :return: None
    """

    path: Path = Path(folder)

    if not(path.exists()):
        return

    for file in path.glob("*.png"):
        file.unlink()
