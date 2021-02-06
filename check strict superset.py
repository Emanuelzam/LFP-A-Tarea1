if __name__ == "__main__":
    A = set(map(int, input().strip().split(' ')))
    t = int(input().strip())
    ss = True
    
    for _ in range(t):
        sb = set(map(int, input().strip().split(' ')))
        if len(sb - A) != 0 or len(A - sb) == 0:
            ss = False
            break
    print(ss)