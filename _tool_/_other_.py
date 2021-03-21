import types
import time

from types import FunctionType


def run_all_test(args):
    for key, value in args.items():
        if key.startswith("test") and isinstance(value, FunctionType):
            print()
            print(f"   [{key}]   ")
            args[key]()
            print()


def print_value(args):
    for key, value in args.items():
        if key.startswith("_") or key.endswith("_"):
            continue
        if "_" in key or key.startswith(("data", "result", "item")):
            print(f"{key:>15} {value}")
