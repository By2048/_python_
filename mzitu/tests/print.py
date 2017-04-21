import sys


pp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

cnt=1
for p in pp:
    k=str(p)
    # sys.stdout.write('\t'+k)
    if cnt%5!=0:
        sys.stdout.write(k+'\t\t')
    else:
        sys.stdout.write('\n')
    cnt+=1





# print(start_link)
# print(image_name)
# print(start_str)
# print(end_num)
# print(image_type)





# for i in range(15):
#     print(str(i).rjust(3,''))
# for i in range(15):
#     print(str(i).zfill(2))
