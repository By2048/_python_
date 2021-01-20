import types


def run_all_test(args):
    for key, value in args.items():
        if key.startswith("test") and type(value) is types.FunctionType:
            args[key]()
