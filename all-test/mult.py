import multiprocessing
import time

def run(num):
    print ("Num: ",num * num)

if __name__=="__main__":
    print ("Start")
    keep=range(10)
    pool=multiprocessing.Pool(9)
    for i in keep:
        pool.apply_async(run,(i,)).get()
    pool.close()

# pool_num=multiprocessing.cpu_count()*2
# print ("pool_num",pool_num)
# def keep_all_image(img_link):
#     pool_num=multiprocessing.cpu_count*2
#     my_pool = multiprocessing.Pool(pool_num)
#     for link in img_link:
#         path=get_img_keep_path()
#         my_pool.apply_async(down_img,(link,path,))