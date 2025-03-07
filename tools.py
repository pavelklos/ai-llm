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


def scientific_to_decimal(sci_str):
    '''
    Convert a scientific notation string to a decimal string.
    example: "$4.95e-05" -> "0.00005"
    example: "$1.0949999999999998e-05" -> "0.00001"
    '''
    # Remove any non-numeric characters except 'e', '-', '.'
    clean_str = ''.join(c for c in sci_str if c.isdigit() or c in 'e-.')
    # Convert to float
    num = float(clean_str)
    # Format to 5 decimal places
    return f"{num:.5f}"


result = scientific_to_decimal("$4.95e-05")
print(result)  # Output: 0.00005
result = scientific_to_decimal("$1.0949999999999998e-05")
print(result)  # Output: 0.00001
