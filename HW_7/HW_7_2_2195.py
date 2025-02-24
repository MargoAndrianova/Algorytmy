import sys, re

class HashTable:
    def __init__(self, size=1000003):
        self.size = size
        self.currentSize = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        current = self.hash(key)
        while self.keys[current] is not None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current = (current + 1) % self.size
        self.keys[current] = key
        self.values[current] = value
        self.currentSize += 1

    def get(self, key):
        current = self.hash(key)
        while self.keys[current] is not None:
            if self.keys[current] == key:
                return self.values[current]
            current = (current + 1) % self.size
        return None

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    # Перший рядок містить N і M
    N, M = map(int, data[0].split())

    vocabHT = HashTable()
    usedHT = HashTable()
    dictionary = []

    # Зчитування словника
    for i in range(1, N + 1):
        word = data[i].strip().lower()
        dictionary.append(word)
        vocabHT.put(word, True)
        usedHT.put(word, False)

    # Зчитування тексту твору
    text = "\n".join(data[N + 1:N + 1 + M])
    words_in_text = re.findall(r"[A-Za-z]+", text)
    words_in_text = [w.lower() for w in words_in_text]

    # Перевірка: чи всі слова з тексту є у словнику?
    for w in words_in_text:
        if vocabHT.get(w) is None:
            print("Some words from the text are unknown.")
            return
        else:
            usedHT.put(w, True)

    # Перевірка: чи всі слова зі словника зустрічаються у тексті?
    for word in dictionary:
        if usedHT.get(word) != True:
            print("The usage of the vocabulary is not perfect.")
            return

    print("Everything is going to be OK.")

if __name__ == "__main__":
    main()