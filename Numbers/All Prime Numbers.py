def get_all_primes(n):
    arr = [True for _ in range(n+1)]  # 0-n inclusively
    num = 2

    while num*num <= n:
        if arr[num]:  # no need to check Falses
            # update all multiples of p
            for i in range(num*num, n+1, num):
                arr[i] = False

        num = num + 1

    # return all primes by removing 'Falses'
    primes = []
    for i in range(2, n+1):
        if arr[i]:
            primes.append(i)

    return primes


if __name__ == "__main__":
    print(get_all_primes(n=20))
