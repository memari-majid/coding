def bitwise_add(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    while y != 0:
        answer = x ^ y
        carry = (x & y) << 1
        x = answer
        y = carry
    return bin(x)[2:]


print(bitwise_add('1111','0010'))