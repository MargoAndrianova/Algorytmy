memo: dict[str, bool] = {}

def solve_game(state: str, k: int) -> bool:
    if state in memo:
        return memo[state]
    possible = False
    for i in range(len(state) - k + 1):
        if state[i:i+k] == "O" * k:
            possible = True
            new_state = state[:i] + "X" * k + state[i+k:]
            if not solve_game(new_state, k):
                memo[state] = True
                return True
    memo[state] = False if possible else False
    return memo[state]

if __name__ == "__main__":
    n, k = map(int, input().split())
    state = input().strip()
    move_possible = any(state[i:i+k] == "O" * k for i in range(n - k + 1))
    if not move_possible:
        print(0)
    else:
        result = solve_game(state, k)
        print(1 if result else 2)
