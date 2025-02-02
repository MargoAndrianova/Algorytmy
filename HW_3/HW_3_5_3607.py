if __name__ == '__main__':
    try:
        while True:
            cnt_of_player = int(input())
            players_high = list(map(int, input().split()))
            a, b = map(int, input().split())

            cnt = 0
            for i in range(cnt_of_player):
                if a <= players_high[i] <= b:
                    cnt += 1

            print(cnt)
    except EOFError:
        pass 