

#b09a2
from datetime import datetime


def check_file(file: str) -> int:
    try:
        file = open(file, 'r')
        datetime.strptime(next(file), "%d.%m.%Y")
        return 0

    except FileNotFoundError:
        return 1  # print("File not found")
    except StopIteration:
        return 2  # leer
    except ValueError:
        return 3
    except Exception:
        return 4


if __name__ == "__main__":
    print(check_file("valid.txt"))  # Soll 0 ausgeben
    print(check_file("missing.txt"))  # Soll 1 ausgeben
    print(check_file("empty.txt"))  # Soll 2 ausgeben
    print(check_file("invalid.txt"))  # Soll 3 ausgeben
