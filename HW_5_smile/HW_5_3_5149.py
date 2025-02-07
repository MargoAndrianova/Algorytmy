def can_place(stalls, k, distance):
    """
    Перевіряє, чи можна розмістити k корів так,
    що мінімальна відстань між ними не менша за distance.
    """
    cnt = 1  # розміщуємо першу корову в першій стійлі
    last_position = stalls[0]

    for pos in stalls[1:]:
        if pos - last_position >= distance:
            cnt += 1
            last_position = pos
        if cnt >= k:
            return True
    return False


def find_min_distance(stalls, k):
    """
    За допомогою бінарного пошуку знаходить найбільшу можливу мінімальну відстань.
    """
    low = 0
    high = stalls[-1] - stalls[0]  # максимальна відстань між першою та останньою стійлою
    best = 0

    while low <= high:
        m = low + (high - low) // 2  # поточна кандидатура на мінімальну відстань
        if can_place(stalls, k, m):
            best = m  # якщо розміщення можливе — запам'ятовуємо
            low = m + 1  # пробуємо збільшити мінімальну відстань
        else:
            high = m - 1  # інакше зменшуємо відстань
    return best


if __name__ == '__main__':
    n, k = map(int, input().split())
    stalls = list(map(int, input().split()))

    # Знаходимо відповідь
    answer = find_min_distance(stalls, k)
    print(answer)
