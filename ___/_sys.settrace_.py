import inspect
import sys
import functools


def log(function):
    def printer(frame, event, arg):
        print(f"-> {event} {arg}")
        code = frame.f_code
        module = inspect.getmodule(code)
        module_name = ""
        module_path = ""
        if module:
            module_path = module.__file__
            module_name = module.__name__
        print(event, module_path, module_name, code.co_name, frame.f_lineno, frame.f_locals, arg)
        return printer

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print("-->", function.__name__, *args, **kwargs)

        sys.settrace(printer)
        result = function(*args, **kwargs)
        sys.settrace(None)

        return result

    return wrapper


@log
def add(a, b):
    c = 3
    d = 4
    e = c + d
    result = a + b + e
    return result


if __name__ == "__main__":
    print(add(1, 2))
