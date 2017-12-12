# 判断过剩数


def abundant_number(num):
    out_sum=0
    for i in range(num // 2 + 1):
        if num % (i + 1)==0:
            out_sum+=i+1
    if out_sum>=num:
        return True
    else:
        return False


abundant_number(12)
