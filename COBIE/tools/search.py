from pathlib import Path


def search_file(query, path="."):
    root = Path(path)
    result = []

    for file in root.rglob("*"):
        if not file.is_file():
            continue
        try:
            content = file.read_text()
        except Exception:
            continue

        if query in content:
            result.append(str(file))
    return result
