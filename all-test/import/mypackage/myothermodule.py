if __name__=='__main__':
    from mymodule import as_int
else:
    from .mymodule import as_int

# Exported function
def add(a, b):
    return as_int(a) + as_int(b)

# Test function for module
def _test():
    assert add('1', '1') == 2

if __name__ == '__main__':
    _test()