# 篡改俱乐部的体重名单


def get_weight(body):
    cnt=0
    for item in list(body):
        cnt += int(item)
    return cnt


def order_weight(body_str):
    bodys=[item for item in body_str.split(' ')]
    print(bodys)

    info_dirs =[]
    for body in bodys:
        info_dirs.append([body,get_weight(body)])



    info_dirs=sorted(info_dirs,key=lambda x:(x[1],x[0]),reverse=False)


    # print(info_dirs)
    out_info=[]
    for item in info_dirs:
        out_info.append(item[0])
    return ' '.join(out_info)


order_weight("103 123 4444 99 2000")#, "2000 103 123 4444 99")
order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")#, "11 11 2000 10003 22 123 1234000 44444444 9999")