import types


def run_all_test(args):
    for key, value in args.items():
        if key.startswith("test") and type(value) is types.FunctionType:
            args[key]()


def log(args):
    for key, value in args.items():
        if key.startswith("_") and key.endswith("_"):
            continue
        if key.startswith(("data", "result", "item")):
            print(f"{key:>10} {value}")
