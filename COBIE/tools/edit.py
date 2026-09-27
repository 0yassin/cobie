from pathlib import Path


def edit_file(path, old_text, new_text):
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File does not exist: {path}")
    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {path}")
    content = file_path.read_text()

    if old_text not in content:
        raise ValueError("The text to replace was not found.")

    new_content = content.replace(old_text, new_text, 1)
    file_path.write_text(new_content)

    return "File edited successfully."
