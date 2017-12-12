# 计算数字金字塔的和

def row_sum_odd_numbers(n):
    out_sum = 0
    cnt = 0
    for i in range(1, n):
        cnt += i
    for i in range((2 * (cnt + 1) - 1), (2 * (cnt + n + 1) - 1), 2):
        out_sum+=i
    return (out_sum)



# 12345
row_sum_odd_numbers(13)