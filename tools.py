from pathlib import Path


def find_project_root(filename="data"):  # filename="requirements.txt"
    '''
    Find the project root by looking for file or folder
    that should be in the root.
    '''
    path = Path().resolve()
    while path != path.root:
        if (path / filename).exists():
            return path
        path = path.parent  # Move up one level
    return None  # Return None if not found


# root_path = find_project_root()
# print(root_path)
