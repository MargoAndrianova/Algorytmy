CAPACITY = 20011
table = None
cnt = 0
DELETED = "DELETED"


def init():
    """Викликається 1 раз на початку виконання програми.
       Ініціалізує власноруч реалізовану хеш-таблицю з відкритою адресацією.
    """
    global table, cnt
    table = [None] * CAPACITY
    cnt = 0


def _hash(key):
    """Обчислює хеш для ключа, який є кортежем (author, title),
       використовуючи просту поліноміальну хеш-функцію.
    """
    s = key[0] + "$" + key[1]
    h = 0
    base = 31
    for ch in s:
        h = (h * base + ord(ch)) % CAPACITY
    return h


def addBook(author, title):
    """Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global table, cnt
    key = (author, title)
    idx = _hash(key)
    i = 0
    while True:
        pos = (idx + i) % CAPACITY
        if table[pos] is None or table[pos] == DELETED:
            table[pos] = key
            cnt += 1
            return
        elif table[pos] == key:
            # Книга вже є в каталозі, тому не додаємо вдруге.
            return
        i += 1


def find(author, title):
    """Перевіряє, чи міститься задана книга у бібліотеці.
    :param author: Автор книги
    :param title: Назва книги
    :return: True, якщо книга міститься, інакше False.
    """
    global table
    key = (author, title)
    idx = _hash(key)
    i = 0
    while True:
        pos = (idx + i) % CAPACITY
        if table[pos] is None:
            return False
        elif table[pos] == DELETED:
            i += 1
            continue
        elif table[pos] == key:
            return True
        i += 1


def delete(author, title):
    """Видаляє книгу з бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global table, cnt
    key = (author, title)
    idx = _hash(key)
    i = 0
    while True:
        pos = (idx + i) % CAPACITY
        if table[pos] is None:
            return  # Книга не знайдена
        elif table[pos] == DELETED:
            i += 1
            continue
        elif table[pos] == key:
            table[pos] = DELETED
            cnt -= 1
            return
        i += 1


def findByAuthor(author):
    """Повертає список книг заданого автора у алфавітному порядку.
    Якщо бібліотека не містить книг цього автора, повертає порожній список.
    :param author: Автор
    :return: Список назв книг заданого автора.
    """
    global table
    result = []
    for entry in table:
        if entry is not None and entry != DELETED:
            if entry[0] == author:
                result.append(entry[1])
    result.sort()
    return result
