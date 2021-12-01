formatter = logging.Formatter(
        '[%(levelname)1.1s %(asctime)s.%(msecs)05d %(name)s:%(lineno)d] %(message)s',
        datefmt='%y%m%d %H:%M:%S',
    )

第一个1应该代表日志前面的空1格
第二个1代表去日志级别的第1个字母
