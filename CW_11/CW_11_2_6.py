max_income = 0

def solve(income: int, voucher: list[tuple], day) -> None:
    global max_income

    if len(voucher) == 0 and income > max_income:
        max_income = income

    for i in range(len(voucher)):
        sub_income = (voucher[i][0] - day)* voucher[i][1] + income
        sub_voucher = []
        for j in range(len(voucher)):
            if i != j and (voucher[j][0] - day > 1):
                sub_voucher.append(voucher[j])
        solve(sub_income, sub_voucher, day + 1)

if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        voucher = []
        for _ in range(n):
            voucher.append(
                tuple(map(int, f.readline().split()))
            )
        solve(0, voucher, 0)
        print(max_income)