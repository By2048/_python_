# def call_back(blocknum, blocksize, totalsize):
#     """下载回显
#     Args:
#        blocknum: 已经下载的数据块
#        blocksize: 数据块的大小
#        totalsize: 远程文件的大小
#     """
#     percent = 100.0 * blocknum * blocksize / totalsize
#     sys.stdout.write("\rDownloading : %.2f%%\r" % percent)
#     sys.stdout.flush()
#     if percent >= 100:
#         sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
#         logging.info('Download_Success ')
#


# import sqlite3
# sqlite_connect = sqlite3.connect(download_sql_path)
# sqlite_cursor = sqlite_connect.cursor()
