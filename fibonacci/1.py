# storing the results of function calls
# returning the cached result when the same inputs occur again
dic = {1: 1, 2: 2}


def f(n):
    if n not in dic:
        dic[n] = f(n - 1) + f(n - 2)
    return dic[n]


if __name__ == '__main__':
    result = f(8)
    print(result)
