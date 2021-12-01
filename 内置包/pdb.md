# `pdb`
`python -m pdb filename.py`
`breakpoint()`

- `l` `list` 查看源代码
    - 查看当前位置前后11行源代码（多次会翻页）
    - 当前位置在代码中会用`-->`这个符号标出来

- `ll` 查看当前函数或框架的所有源代码

- `b` `break` 添加断点
    - `b lineno`
    - `b filename:lineno `
    - `b functionname`
    - 不带参数表示查看断点设置
    - 带参则在指定位置设置一个断点

- `tbreak` 添加临时断点,同`b`,执行一次后时自动删除
    - `tbreak`
    - `tbreak lineno`
    - `tbreak filename:lineno`
    - `tbreak functionname`
    
- `cl` `clear` 清除断点
    - `cl`
    - `cl filename:lineno`
    - `cl bpnumber [bpnumber ...]` `bpnumber`断点序号（多个以空格分隔）
    - 不带参数用于清除所有断点，会提示确认（包括临时断点）
    - 带参数则清除指定文件行或当前文件指定序号的断点

- `p expression` 打印变量值 `expression` Python表达式

- `s n r`
    - `s` `step` 执行下一行（能够进入函数体）
    - `n` `next`执行下一行（不会进入函数体）
    - `r` `return` 执行下一行（在函数中时会直接执行到函数返回处）

- `c` `continue` 持续执行下去，直到遇到一个断点

- `unt lineno` 持续执行直到运行到指定行（或遇到断点）

- `j lineno` 直接跳转到指定行（被跳过的代码不执行）

- `a` `args` 在函数中时打印函数的参数和参数的值

- `whatis expression` 打印变量类型

- `interact` 启动交互式解释器
    - 启动一个python的交互式解释器，使用当前代码的全局命名空间（使用ctrl+d返回pdb）

- `w`/`bt` `where`打印堆栈信息,最新的帧在最底部。箭头表示当前帧。

- `q` 退出pdb

- `up`

- `down`

- `restart`/`run`


# `ipdb`