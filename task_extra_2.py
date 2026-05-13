def digital_root(num):
    while num > 9:
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num