# coding=utf-8

async def async_function():
    return 'hello'


if __name__ == '__main__':
    try:
        async_function().send(None)
    except StopIteration as e:
        print(e.value)
