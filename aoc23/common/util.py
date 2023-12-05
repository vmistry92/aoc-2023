import os


def get_data_file_name(day: int, suffix: str = "") -> str:
    file_directory = os.path.dirname(__file__)
    return os.path.join(file_directory, f"../../data/day{day}{suffix}.txt")
