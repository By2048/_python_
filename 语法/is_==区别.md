## 在pycharm中运行
```py
a = "hello"
b = "hello"
print(a is b)  # 输出 True 
print(a == b)  # 输出 True
print()

a = "hello world"
b = "hello world"
print(a is b)  # 输出 True
print(a == b)  # 输出 True
print()

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # 输出 False
print(a == b)  # 输出 True
print()

a = [1, 2, 3]
b = a
print(a is b)  # 输出 True
print(a == b)  # 输出 True
```



```py
a = "hello world"
b = "hello world"
print(id(a))
print(id(b))
print(a is b)
print(a == b)

# 1828913042736
# 1828913042736
# True
# True
```

## 在命令行运行
```py
a = "a b"
b = "a b"
a == b
True
a is b
False
```

```py
a = "a b"
b = "a b"
id(a)
# 1864659208712
id(b)
# 1864659178752
a is b
# False
a == b
# True
```


is 表示的是对象标示符（object identity），而 == 表示的是相等（equality）。
is 的作用是用来检查对象的标示符是否一致，也就是比较两个对象在内存中的地址是否一样
== 是用来检查两个对象是否相等。

我们在检查 a is b 的时候，其实相当于检查 `id(a) == id(b)` 。而检查 `a == b` 的时候，实际是调用了对象 a 的 `__eq()__` 方法，`a == b` 相当于 `a.__eq__(b)`




```
1 在交互模式下，每行字符串字面量都会申请一个新字符串，但是只含大小写字母、数字和下划线的会被intern，也就是维护了一张dict来使得这些字符串全局唯一；而你把这段代码放在py文件执行，第二个也是True了，因为会常量合并

2 单个字符的字符串和空串有内建小对象池，所以测试会是全局只有唯一对象

以上只限cpy实现以及只使用cpy的情况，意思是：一，其他实现不一定保证；二，假如你自己用C扩展了一个py模块，且在C中构造了一个已经被intern的字符串或小对象，则这个字符串对象传回py环境的时候，是一个合法对象，但地址显然和你之前用的不一样，这意味着不要以为在cpy下就可以依赖这种特性

3的问题和cpy的内存管理有关，由于采用引用计数可实时销毁不需要的对象，在算完左边的id后左边list被销毁，算右边id的时候右边list实时创建，复用了左边list用过的内存，所以地址相同，但是对象的生存有先后，不代表是一个对象
```