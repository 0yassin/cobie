from pathlib import Path


def read_file(path):
    file_path = Path(path)

    if not file_path.exists():
        return "File does not exists"
    return file_path.read_text()


def write_file(path, content):
    file_path = Path(path)
    file_path.write_text(content)
    return "File written successfully."


def list_directory(path):
    directory = Path(path)
    lists = []
    if not directory.exists():
        return "The directory doesn't exists"
    if not directory.is_dir():
        return "Given path is not directory"
    for list in directory.iterdir():
        lists.append(list.name)

    return lists


if __name__ == "__main__":
    print(list_directory("."))
