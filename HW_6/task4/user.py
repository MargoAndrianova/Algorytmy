CAPACITY = 20011
table = None
cnt = 0


def init():
    """Викликається 1 раз на початку виконання програми.
       Ініціалізує хеш-таблицю з розв’язанням колізій методом ланцюжків.
    """
    global table, cnt
    table = [[] for _ in range(CAPACITY)]
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
    h = _hash(key)
    bucket = table[h]
    # Якщо книга вже існує, не додаємо її вдруге.
    for k in bucket:
        if k == key:
            return
    bucket.append(key)
    cnt += 1


def find(author, title):
    """Перевіряє, чи міститься задана книга у бібліотеці.
    :param author: Автор книги
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці, інакше False.
    """
    global table
    key = (author, title)
    h = _hash(key)
    bucket = table[h]
    for k in bucket:
        if k == key:
            return True
    return False


def delete(author, title):
    """Видаляє книгу з бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global table, cnt
    key = (author, title)
    h = _hash(key)
    bucket = table[h]
    for i, k in enumerate(bucket):
        if k == key:
            del bucket[i]
            cnt -= 1
            return


def findByAuthor(author):
    """Повертає список книг заданого автора у алфавітному порядку.
    Якщо бібліотека не містить книг цього автора, повертає порожній список.
    :param author: Автор
    :return: Список назв книг заданого автора.
    """
    global table
    result = []
    for bucket in table:
        for k in bucket:
            if k[0] == author:
                result.append(k[1])
    result.sort()
    return result
