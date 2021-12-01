使用assert断言是学习python一个非常好的习惯，python assert 断言句语格式及用法很简单。在没完善一个程序之前，我们不知道程序在哪里会出错，与其让它在运行最崩溃，不如在出现错误条件时就崩溃，这时候就需要assert断言的帮助。
```py
# assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。格式如下：
# assert expression [, arguments]
# assert 表达式 [, 参数]
assert 1==1
assert 2+2==2*2
assert 2==1,'2不等于1'
assert len(['my boy',12])<10
assert range(4)==[0,1,2,3]
```
