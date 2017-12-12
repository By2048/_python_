def square_digits(num):
    out_str=''
    for item in str(num):
        out_str+=str(int(item)*int(item))
    return int(out_str)



print(square_digits(9119))