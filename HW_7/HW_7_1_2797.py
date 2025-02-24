import math

EMPTY = "EMPTY"

size: int = 100_003
count: int
keys: list[int]
values: list[str]


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def rehash():
    global size
    size = size * 2 + 1
    while not is_prime(size):
        size += 2

    _keys = keys
    _values = values
    init()
    for i in range(len(_keys)):
        if _keys[i] is not EMPTY:
            set(_keys[i], _values[i])


def _hash(key: int):
    return key % size


def init():
    global count, keys, values
    count = 0
    keys = [EMPTY for _ in range(size)]
    values = [EMPTY for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global count
    i = _hash(key)
    while keys[i] is not EMPTY:
        if keys[i] == key:
            values[i] = value
            return
        i = (i + 1) % size

    count += 1
    keys[i] = key
    values[i] = value


if __name__ == "__main__":
    init()
    n = int(input())
    numbers = list(map(int, input().split()))
    for j in numbers:
        set(j, str(j))
    print(count)