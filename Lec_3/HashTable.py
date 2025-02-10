class HashTable:

    """Хеш-таблиця у якій колізії розв'язуються методом лінійного зондування."""

    def __init__(self):
        """ Конструктор - ініціалізує таблицю. """
        self.size = 11 # кількість слотів таблиці
        self.current_size = 0 # поточний розмір таблиці
        self.keys = [None] * self.size # список слотів
        self.data = [None] * self.size # дані пов'язані з слотом

    def hash(self, key):
        """ Повертає хеш для ключа
        :param key: ключ
        :return: хеш ключа """
        return key % self.size

    def put(self, key, value):
        """ Додає пару (ключ, значення) до таблиці
        :param key: ключ
        :param value: значення
        :return: None """

        current = self.hash(key)  # Поточний слот таблиці

        while self.keys[current] is not None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current += 1

        # якщо ключ у таблиці не знайдений
        self.keys[current] = key  # додаємо ключ
        self.values[current] = value  # додаємо значення
        self.current_size += 1

    def get(self, key):
        """ Повертає значення за ключем
        :param key: ключ
        :return: значення """

        current = self.hash(key)

        while self.keys[current] is not None:
            if self.keys[current] == key:
                return self.values[current]
            current += 1

        # якщо ключ у таблиці не знайдений
        return None

    def __setitem__(self, key, value):
        """ Перевизначення оператора [ ] для запису
        :param key: ключ
        :param value: нове значення
        """
        self.put(key, value)

    def __getitem__(self, key):
        """ Перевизначення оператора [ ] для читання
        :param key: ключ
        :return: значення, що відповідає ключу key
        """
        return self.get(key)

if __name__ == "__main__":
    M = HashTable()  # Створюємо таблицю
    M.put(55, "zz")  # додаємо пару (56, "zz")
    M.put(66, "AA")  # додаємо пару (66, "AA")
    M.put(66, "66")  # змінюємо значення за ключем 66
    M.put(77, "77")  # додаємо пару (77, "77")
    M[56] = "RR"  # M.put(56, "RR")
    M[55] = "55"  # M.put(55, "55")
    print(M[56])  # print(M.get(56))