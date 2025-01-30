N = 31
M = 1000000007

def H(S):
    h = 0
    for i in range(len(S)):
        h = h * N + ord(S[i])
    return h % M

if __name__ == "__main__":
    print(H("hash"))