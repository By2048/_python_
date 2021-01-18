python 文件读写时用open还是codecs.open
     当我面有数据需要保存时，第一时间一般会想到写到一个txt文件中，当然，数据量比较大的时候还是写到数据库比较方便管理，需要进行网络传输时要序列化，json化。下面主要整理一下平时用的最多的写入到文件中，一般以txt结尾，linux里不会以后缀来区分文件类型，后缀可以随便，也可以没有。

      python读写文件估计大家都用open内置函数，或者file这个工厂函数，这两个的效果基本一样。

      打开文件的方式一般为：f=open(file_name,access_mode = 'r',buffering = -1)。file_name就是文件的路径加文件名字，不加路径则文件会存放在python程序的路径下，

access_mode就是操作文件的模式，主要有r,w,rb，wb等，细节网上一大堆,buffering = -1是用于指示访问文件所采用的缓存方式。0表示不缓存；1表示只缓存一行，n代表缓存n行。如果不提供或为负数，则代表使用系统默认的缓存机制。

      打开以后就是写和读的操作。但是用open方法打开会有一些问题。open打开文件只能写入str类型,不管字符串是什么编码方式。例如
```py
>>> fr = open('test.txt','a')
>>> line1 = "我爱祖国"
>>> fr.write(line1)
```
这样是完全可以的。但是有时候我们爬虫或者其他方式得到一些数据写入文件时会有编码不统一的问题，所以就一般都统一转换为unicode。此时写入open方式打开的文件就有问题了。例如
```py
>>> line2 = u'我爱祖国'
>>> fr.write(line2)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fr.write(line2)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-11: ordinal not in range(128)
>>>
```

怎么办，我们可以将上面的line2编码成str类型，但是太麻烦。我们要把得到的东西先decode为unicode再encode为str。。。

input文件(gbk, utf-8...)   ----decode----->   unicode  -------encode------> output文件(gbk, utf-8...)

代替这繁琐的操作就是codecs.open，例如
```py
>>> import codecs
>>> fw = codecs.open('test1.txt','a','utf-8')
>>> fw.write(line2)
```

不会报错，说明写入成功。这种方法可以指定一个编码打开文件，使用这个方法打开的文件读取返回的将是unicode。写入时，如果参数 是unicode，则使用open()时指定的编码进行编码后写入；如果是str，则先根据源代码文件声明的字符编码，解码成unicode后再进行前述 操作。相对内置的open()来说，这个方法比较不容易在编码上出现问题。
